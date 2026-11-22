from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from .core import (
    DEFAULT_MANIFEST_URL,
    DEFAULT_RAW_BASE,
    MonitorError,
    atomic_write,
    fetch_text,
    load_detectors,
    load_json,
    load_static_filters,
    render_filter_list,
    render_markdown,
    run_scan,
    stable_json,
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scan the latest Bloxd JavaScript bundles and generate uBlock filter rules.")
    parser.add_argument("--manifest-url", default=DEFAULT_MANIFEST_URL, help="Build Monitor .monitor-state.json URL")
    parser.add_argument("--raw-base-url", default=DEFAULT_RAW_BASE, help="Raw GitHub base URL for archived bundles")
    parser.add_argument("--config", type=Path, default=Path("config/detectors.json"), help="Detector signature database")
    parser.add_argument("--static-filters", type=Path, default=Path("config/static-filters.txt"), help="Fixed Bloxd filter rules included in the subscription list")
    parser.add_argument("--state", type=Path, default=Path(".state/scan-cache.json"), help="Persistent content-hash cache and previous report")
    parser.add_argument("--output-dir", type=Path, default=Path("."), help="Repository output directory")
    parser.add_argument("--source-root", type=Path, help="Read bundle paths from a local directory instead of downloading them (testing/offline)")
    parser.add_argument("--manifest-file", type=Path, help="Read a local manifest instead of downloading it")
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--workers", type=int, default=8)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.timeout < 1 or args.workers < 1:
            raise MonitorError("--timeout and --workers must be positive integers")
        if args.manifest_file:
            manifest_text = args.manifest_file.read_text(encoding="utf-8")
        else:
            manifest_text = fetch_text(args.manifest_url, timeout=args.timeout)
        try:
            manifest: Any = json.loads(manifest_text)
        except json.JSONDecodeError as exc:
            raise MonitorError(f"Manifest is not valid JSON: {exc}") from exc

        detectors, fingerprint = load_detectors(args.config)
        static_filters = load_static_filters(args.static_filters)
        state = load_json(args.state, {"schema_version": 1, "content_cache": {}, "latest": {}})
        if not isinstance(state, dict):
            raise MonitorError("State file must contain a JSON object")
        report, next_state = run_scan(
            manifest,
            state,
            detectors,
            fingerprint,
            raw_base_url=args.raw_base_url,
            manifest_url=args.manifest_url,
            source_root=args.source_root,
            timeout=args.timeout,
            workers=args.workers,
            static_filter_count=len(static_filters),
        )

        output_dir: Path = args.output_dir
        atomic_write(output_dir / "reports/latest.json", stable_json(report))
        atomic_write(output_dir / "reports/latest.md", render_markdown(report))
        atomic_write(output_dir / "filters/bloxd-video-adapters.txt", render_filter_list(report["filter_rules"], report["generated_at"], args.manifest_url, static_filters))
        atomic_write(args.state, stable_json(next_state))
        print(json.dumps(report["summary"], ensure_ascii=False, sort_keys=True))
        return 0
    except (MonitorError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
