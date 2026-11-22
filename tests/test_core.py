from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from bloxd_ad_monitor.core import (
    MonitorError,
    build_filter_rules,
    compare_occurrences,
    detector_matches,
    load_detectors,
    run_scan,
)

ROOT = Path(__file__).resolve().parents[1]


class DetectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.detectors, cls.fingerprint = load_detectors(ROOT / "config/detectors.json")

    def test_nitro_countdown_requires_full_signature(self) -> None:
        source = "NitroSdkAdaptor NitroVideoSkip Skip ad in adStartSoPause"
        matches = detector_matches(source, self.detectors)
        self.assertEqual([item["id"] for item in matches], ["nitro-video-skip-overlay"])

    def test_partial_nitro_name_does_not_match(self) -> None:
        self.assertEqual(detector_matches("NitroSdkAdaptor", self.detectors), [])

    def test_aditude_is_tracked_but_not_published(self) -> None:
        source = "AditudeSdkAdaptor requestInstreamPlayer GenericVideoWrapper"
        matches = detector_matches(source, self.detectors)
        self.assertEqual(len(matches), 1)
        self.assertFalse(matches[0]["publish_filter"])


class FilterTests(unittest.TestCase):
    def test_filter_is_generated_for_isolated_chunk(self) -> None:
        occurrences = [{
            "environment": "bloxd.io",
            "detector_id": "nitro-video-skip-overlay",
            "chunk_id": "149",
            "filterable": True,
            "publish_filter": True,
            "path": "bundles/bloxd.io/chunks/js/149.js",
        }]
        rules = build_filter_rules(occurrences)
        self.assertEqual(rules[0]["rule"], "||bloxd.io/static/js/*.149.*.chunk.js$script")

    def test_main_bundle_is_never_filterable(self) -> None:
        occurrences = [{
            "environment": "bloxd.io",
            "detector_id": "nitro-video-skip-overlay",
            "chunk_id": None,
            "filterable": False,
            "publish_filter": False,
            "path": "bundles/bloxd.io/main.js",
        }]
        self.assertEqual(build_filter_rules(occurrences), [])

    def test_compare_reports_chunk_id_move(self) -> None:
        old = [{"environment": "bloxd.io", "detector_id": "nitro", "chunk_id": "149", "path": "old.js", "sha256": "a"}]
        new = [{"environment": "bloxd.io", "detector_id": "nitro", "chunk_id": "151", "path": "new.js", "sha256": "b"}]
        changes = compare_occurrences(old, new)
        self.assertEqual(changes["moved"][0]["from"], ["149"])
        self.assertEqual(changes["moved"][0]["to"], ["151"])


class ScanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.detectors, cls.fingerprint = load_detectors(ROOT / "config/detectors.json")

    def test_offline_scan_verifies_hash_and_publishes_chunk_rule(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            bundle = root / "bundles/bloxd.io/chunks/js/149.js"
            bundle.parent.mkdir(parents=True)
            content = b"NitroSdkAdaptor NitroVideoSkip NitroOutstreamVideo Skip ad in adStartSoPause"
            bundle.write_bytes(content)
            sha = hashlib.sha256(content).hexdigest()
            manifest = {
                "bloxd.io": {
                    "build": "test.12345678",
                    "checked_at": "2026-01-01T00:00:00Z",
                    "files": [{
                        "path": "bundles/bloxd.io/chunks/js/149.js",
                        "sha256": sha,
                        "identity": "chunk.js:149",
                        "source_filename": "test.149.abcdef01.chunk.js",
                    }],
                }
            }
            report, state = run_scan(manifest, {"content_cache": {}, "latest": {}}, self.detectors, self.fingerprint, source_root=root)
            self.assertEqual(report["summary"]["filter_rules"], 1)
            self.assertEqual(report["filter_rules"][0]["chunk_id"], "149")
            self.assertIn(sha, state["content_cache"])

    def test_hash_mismatch_aborts_scan(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            bundle = root / "bundles/bloxd.io/chunks/js/149.js"
            bundle.parent.mkdir(parents=True)
            bundle.write_text("NitroSdkAdaptor NitroVideoSkip Skip ad in adStartSoPause", encoding="utf-8")
            manifest = {
                "bloxd.io": {
                    "build": "test.12345678",
                    "files": [{"path": "bundles/bloxd.io/chunks/js/149.js", "sha256": "0" * 64, "identity": "chunk.js:149"}],
                }
            }
            with self.assertRaises(MonitorError):
                run_scan(manifest, {"content_cache": {}, "latest": {}}, self.detectors, self.fingerprint, source_root=root)

    def test_cached_hash_is_reused_and_stale_entries_are_pruned(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            content = b"NitroSdkAdaptor NitroVideoSkip NitroOutstreamVideo Skip ad in adStartSoPause"
            sha = hashlib.sha256(content).hexdigest()
            # The cached match is intentionally sufficient; this path is not present locally.
            manifest = {"bloxd.io": {"build": "test.12345678", "files": [{"path": "bundles/bloxd.io/chunks/js/149.js", "sha256": sha, "identity": "chunk.js:149"}]}}
            matches = detector_matches(content.decode(), self.detectors)
            state = {"content_cache": {
                sha: {"detector_fingerprint": self.fingerprint, "matches": matches},
                "f" * 64: {"detector_fingerprint": self.fingerprint, "matches": []},
            }, "latest": {}}
            report, next_state = run_scan(manifest, state, self.detectors, self.fingerprint, source_root=root)
            self.assertEqual(report["summary"]["new_hashes_scanned"], 0)
            self.assertEqual(report["summary"]["filter_rules"], 1)
            self.assertEqual(set(next_state["content_cache"]), {sha})

    def test_malformed_manifest_entries_abort_scan(self) -> None:
        manifest = {"bloxd.io": {"build": "test.12345678", "files": [None]}}
        with self.assertRaises(MonitorError):
            run_scan(manifest, {"content_cache": {}, "latest": {}}, self.detectors, self.fingerprint)


if __name__ == "__main__":
    unittest.main()
