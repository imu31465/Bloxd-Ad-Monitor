from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HOST_RE = re.compile(r"^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)(?:\.(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?))*$", re.I)
CHUNK_RE = re.compile(r"^[A-Za-z0-9_-]{1,100}$")
DEFAULT_RAW_BASE = "https://raw.githubusercontent.com/imu31465/Bloxd-Build-Monitor/main/"
DEFAULT_MANIFEST_URL = DEFAULT_RAW_BASE + ".monitor-state.json"
STATE_VERSION = 1
USER_AGENT = "Bloxd-Ad-Monitor/0.1 (+https://github.com/imu31465/Bloxd-Ad-Monitor)"


class MonitorError(RuntimeError):
    """Raised when source data cannot be trusted or processed safely."""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise MonitorError(f"Cannot read JSON file {path}: {exc}") from exc


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


def stable_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def load_detectors(config_path: Path) -> tuple[list[dict[str, Any]], str]:
    config = load_json(config_path, None)
    if not isinstance(config, dict) or config.get("schema_version") != 1:
        raise MonitorError("Detector configuration must be a schema_version 1 JSON object")
    detectors = config.get("detectors")
    if not isinstance(detectors, list) or not detectors:
        raise MonitorError("Detector configuration contains no detectors")
    seen: set[str] = set()
    for detector in detectors:
        if not isinstance(detector, dict):
            raise MonitorError("Each detector must be an object")
        detector_id = detector.get("id")
        groups = detector.get("required_groups")
        if not isinstance(detector_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,63}", detector_id):
            raise MonitorError(f"Invalid detector id: {detector_id!r}")
        if detector_id in seen:
            raise MonitorError(f"Duplicate detector id: {detector_id}")
        seen.add(detector_id)
        if not isinstance(groups, list) or not groups or any(not isinstance(g, list) or not g or any(not isinstance(m, str) or not m for m in g) for g in groups):
            raise MonitorError(f"Detector {detector_id} has invalid required_groups")
    fingerprint = hashlib.sha256(stable_json(config).encode("utf-8")).hexdigest()
    return detectors, fingerprint


def validate_manifest(manifest: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(manifest, dict) or not manifest:
        raise MonitorError("Manifest must be a non-empty object keyed by environment hostname")
    result: dict[str, dict[str, Any]] = {}
    for host, env in manifest.items():
        if not isinstance(host, str) or not HOST_RE.fullmatch(host):
            raise MonitorError(f"Invalid environment hostname: {host!r}")
        if not isinstance(env, dict):
            raise MonitorError(f"Environment entry for {host} must be an object")
        files = env.get("files")
        if not isinstance(files, list):
            raise MonitorError(f"Environment {host} does not contain a files array")
        build = env.get("build")
        if not isinstance(build, str) or not build:
            raise MonitorError(f"Environment {host} is missing build id")
        clean_files: list[dict[str, Any]] = []
        for index, item in enumerate(files):
            if not isinstance(item, dict):
                raise MonitorError(f"Environment {host} contains a non-object file entry at index {index}")
            path = item.get("path")
            if not isinstance(path, str) or not path:
                raise MonitorError(f"Environment {host} contains a file entry without a valid path at index {index}")
            normalized = Path(path)
            if normalized.is_absolute() or ".." in normalized.parts or "\\" in path:
                raise MonitorError(f"Unsafe bundle path in manifest: {path!r}")
            expected_prefix = f"bundles/{host}/"
            if not path.startswith(expected_prefix):
                raise MonitorError(f"Bundle path is outside its environment directory: {path}")
            if not path.endswith(".js"):
                continue
            sha = item.get("sha256")
            if not isinstance(sha, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", sha):
                raise MonitorError(f"Missing or invalid SHA-256 for {path}")
            clean_files.append(item)
        result[host] = {**env, "files": clean_files}
    return result


def fetch_text(url: str, timeout: int = 30) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json,text/plain,*/*"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise MonitorError(f"Download failed for {url}: {exc}") from exc
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise MonitorError(f"Downloaded content is not UTF-8: {url}") from exc


def source_url(raw_base_url: str, relative_path: str) -> str:
    base = raw_base_url.rstrip("/") + "/"
    quoted = urllib.parse.quote(relative_path, safe="/._-~")
    return urllib.parse.urljoin(base, quoted)


def read_bundle(path: str, raw_base_url: str, source_root: Path | None, timeout: int) -> bytes:
    if source_root is not None:
        root = source_root.resolve()
        candidate = (root / path).resolve()
        if candidate != root and root not in candidate.parents:
            raise MonitorError(f"Bundle path escapes source root: {path}")
        try:
            return candidate.read_bytes()
        except OSError as exc:
            raise MonitorError(f"Cannot read fixture bundle {candidate}: {exc}") from exc
    request = urllib.request.Request(source_url(raw_base_url, path), headers={"User-Agent": USER_AGENT, "Accept": "text/plain,*/*"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.read()
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise MonitorError(f"Cannot download bundle {path}: {exc}") from exc


def detector_matches(text: str, detectors: list[dict[str, Any]]) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    for detector in detectors:
        matched_groups: list[str] = []
        marker_hits: list[str] = []
        passed = True
        for group in detector["required_groups"]:
            hits = [marker for marker in group if marker in text]
            if not hits:
                passed = False
                break
            matched_groups.append(" | ".join(hits))
            marker_hits.extend(hits)
        if passed:
            found.append({
                "id": detector["id"],
                "name": detector.get("name", detector["id"]),
                "confidence": detector.get("confidence", "high"),
                "evidence": marker_hits,
                "matched_groups": matched_groups,
                "publish_filter": bool(detector.get("publish_filter", False)),
                "filter_note": detector.get("filter_note", ""),
            })
    return found


def logical_chunk_id(file_entry: dict[str, Any]) -> str | None:
    identity = file_entry.get("identity")
    if isinstance(identity, str) and identity.startswith("chunk.js:"):
        candidate = identity.split(":", 1)[1]
    else:
        path = str(file_entry.get("path", ""))
        if "/chunks/js/" not in path:
            return None
        candidate = Path(path).stem
    if candidate in {"main", ""} or not CHUNK_RE.fullmatch(candidate):
        return None
    return candidate


def _download_uncached(
    sha: str,
    entry: dict[str, Any],
    raw_base_url: str,
    source_root: Path | None,
    timeout: int,
    detectors: list[dict[str, Any]],
) -> tuple[str, list[dict[str, Any]]]:
    raw = read_bundle(entry["path"], raw_base_url, source_root, timeout)
    actual = hashlib.sha256(raw).hexdigest()
    expected = entry["sha256"].lower()
    if actual != expected:
        raise MonitorError(f"SHA-256 mismatch for {entry['path']}: expected {expected}, got {actual}")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise MonitorError(f"Bundle is not UTF-8 text: {entry['path']}") from exc
    return sha, detector_matches(text, detectors)


def _make_occurrence(host: str, env: dict[str, Any], entry: dict[str, Any], match: dict[str, Any]) -> dict[str, Any]:
    chunk_id = logical_chunk_id(entry)
    is_chunk = chunk_id is not None
    return {
        "environment": host,
        "build": env["build"],
        "checked_at": env.get("checked_at"),
        "detector_id": match["id"],
        "detector_name": match["name"],
        "confidence": match["confidence"],
        "evidence": match["evidence"],
        "matched_groups": match["matched_groups"],
        "path": entry["path"],
        "identity": entry.get("identity"),
        "chunk_id": chunk_id,
        "source_filename": entry.get("source_filename"),
        "source_url": entry.get("source_url"),
        "sha256": entry["sha256"].lower(),
        "filterable": match["publish_filter"] and is_chunk,
        "publish_filter": match["publish_filter"] and is_chunk,
        "filter_note": match["filter_note"],
    }


def build_filter_rules(occurrences: list[dict[str, Any]]) -> list[dict[str, str]]:
    rules: dict[tuple[str, str], dict[str, str]] = {}
    for occurrence in occurrences:
        if not occurrence.get("publish_filter") or not occurrence.get("filterable"):
            continue
        host = occurrence["environment"]
        chunk_id = occurrence["chunk_id"]
        if not HOST_RE.fullmatch(host) or not CHUNK_RE.fullmatch(chunk_id):
            continue
        rule = f"||{host}/static/js/*.{chunk_id}.*.chunk.js$script"
        rules[(host, chunk_id)] = {
            "rule": rule,
            "environment": host,
            "chunk_id": chunk_id,
            "detector_id": occurrence["detector_id"],
            "source_path": occurrence["path"],
        }
    return [rules[key] for key in sorted(rules)]


def compare_occurrences(previous: list[dict[str, Any]], current: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    def grouped(items: list[dict[str, Any]]) -> dict[tuple[str, str], list[dict[str, Any]]]:
        result: dict[tuple[str, str], list[dict[str, Any]]] = {}
        for item in items:
            result.setdefault((item["environment"], item["detector_id"]), []).append(item)
        return result

    old, new = grouped(previous), grouped(current)
    changes: dict[str, list[dict[str, Any]]] = {"new": [], "disappeared": [], "moved": [], "changed": []}
    for key in sorted(set(old) | set(new)):
        before = old.get(key, [])
        after = new.get(key, [])
        if not before:
            for item in after:
                changes["new"].append({"environment": key[0], "detector_id": key[1], "path": item["path"], "chunk_id": item.get("chunk_id")})
            continue
        if not after:
            for item in before:
                changes["disappeared"].append({"environment": key[0], "detector_id": key[1], "path": item["path"], "chunk_id": item.get("chunk_id"), "note": "Detector no longer matched; generated block rule removed."})
            continue
        old_by_id = {str(x.get("chunk_id") or x.get("path")): x for x in before}
        new_by_id = {str(x.get("chunk_id") or x.get("path")): x for x in after}
        old_ids, new_ids = set(old_by_id), set(new_by_id)
        if old_ids != new_ids:
            changes["moved"].append({"environment": key[0], "detector_id": key[1], "from": sorted(old_ids), "to": sorted(new_ids)})
        for item_id in sorted(old_ids & new_ids):
            old_item, new_item = old_by_id[item_id], new_by_id[item_id]
            if old_item.get("sha256") != new_item.get("sha256"):
                changes["changed"].append({"environment": key[0], "detector_id": key[1], "chunk_id": new_item.get("chunk_id"), "path": new_item["path"], "from_sha256": old_item.get("sha256"), "to_sha256": new_item.get("sha256")})
    return changes


def load_static_filters(path: Path) -> list[str]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise MonitorError(f"Cannot read static filter file {path}: {exc}") from exc
    rules = [line.strip() for line in lines if line.strip() and not line.lstrip().startswith("!")]
    for rule in rules:
        if not rule.startswith(("||", "bloxd.io,", "preprod.bloxd.io,", "staging.bloxd.io,")):
            raise MonitorError(f"Unsupported static filter line in {path}: {rule}")
    return rules


def render_filter_list(
    rules: list[dict[str, str]],
    generated_at: str,
    source_url_value: str,
    static_filters: list[str] | None = None,
) -> str:
    static_filters = static_filters or []
    lines = [
        "! Title: Bloxd Ad Monitor — combined Bloxd filters",
        "! Description: Fixed Bloxd ad filters plus automatically tracked video-ad adapter chunks.",
        "! Homepage: https://github.com/imu31465/Bloxd-Ad-Monitor",
        "! Expires: 12 hours",
        f"! Last generated: {generated_at}",
        f"! Source manifest: {source_url_value}",
        "! Static provider, cosmetic, and supported scriptlet rules are maintained in config/static-filters.txt.",
        "! Dynamic chunk rules are emitted only for high-confidence isolated lazy-loaded adapters.",
        "! The main bundle is never blocked automatically.",
        "",
        "! Fixed Bloxd rules",
    ]
    lines.extend(static_filters or ["! No fixed Bloxd rules configured."])
    lines.append("")
    lines.append("! Automatically tracked ad-adapter chunks")
    if not rules:
        lines.append("! No currently verified chunk filters. This section is intentionally fail-open.")
    else:
        for item in rules:
            lines.append(f"! {item['environment']} — {item['detector_id']} — logical chunk {item['chunk_id']}")
            lines.append(item["rule"])
    return "\n".join(lines).rstrip() + "\n"


def render_markdown(report: dict[str, Any]) -> str:
    counts = report["summary"]
    lines = [
        "# Latest ad scan",
        "",
        f"- Generated: `{report['generated_at']}`",
        f"- Source manifest: [{report['source']['manifest_url']}]({report['source']['manifest_url']})",
        f"- Environments: **{counts['environments']}**",
        f"- JavaScript assets considered: **{counts['javascript_assets']}**",
        f"- Unique content hashes scanned or reused: **{counts['unique_hashes']}**",
        f"- High-confidence detections: **{counts['detections']}**",
        f"- Published filter rules (total): **{counts['filter_rules']}**",
        f"- Fixed filters: **{counts.get('static_filter_rules', 0)}**",
        f"- Dynamic chunk filters: **{counts.get('chunk_filter_rules', counts['filter_rules'])}**",
        "",
        "> Filter rules are emitted only for explicitly approved detector signatures in isolated lazy-loaded chunks. `main.js` is never blocked automatically. When a signature disappears, its rule is removed rather than retaining a potentially stale chunk ID.",
        "",
        "## Current detections",
        "",
    ]
    if not report["occurrences"]:
        lines.append("No configured ad-module signatures matched the latest manifest.")
    else:
        lines.extend(["| Environment | Detector | Chunk | Source file | Evidence |", "|---|---|---:|---|---|"])
        for item in report["occurrences"]:
            chunk = item.get("chunk_id") or "main / non-chunk"
            evidence = ", ".join(f"`{x}`" for x in item["evidence"])
            lines.append(f"| `{item['environment']}` | `{item['detector_id']}` | `{chunk}` | `{item['path']}` | {evidence} |")
    lines.extend(["", "## Filter rules", ""])
    if not report["filter_rules"]:
        lines.append("No rules were generated. The published list remains fail-open.")
    else:
        for item in report["filter_rules"]:
            lines.append(f"- `{item['rule']}`")
    changes = report["changes"]
    lines.extend(["", "## Changes from previous scan", ""])
    if not any(changes.values()):
        lines.append("No detector-location or implementation changes detected.")
    else:
        for label in ("new", "moved", "changed", "disappeared"):
            if changes[label]:
                lines.append(f"### {label.title()}")
                for item in changes[label]:
                    lines.append(f"- `{json.dumps(item, ensure_ascii=False, sort_keys=True)}`")
    lines.extend(["", "## Interpretation", "", "A match means the configured signature was found in the archived JavaScript source. It does not prove the provider is selected for every player, region, or session. Blocking a detected adapter can affect the related ad flow; non-ad game logic is not intentionally targeted.", ""])
    return "\n".join(lines)


def run_scan(
    manifest: dict[str, Any],
    state: dict[str, Any],
    detectors: list[dict[str, Any]],
    detector_fingerprint: str,
    *,
    raw_base_url: str = DEFAULT_RAW_BASE,
    manifest_url: str = DEFAULT_MANIFEST_URL,
    source_root: Path | None = None,
    timeout: int = 30,
    workers: int = 8,
    static_filter_count: int = 0,
) -> tuple[dict[str, Any], dict[str, Any]]:
    environments = validate_manifest(manifest)
    cache = state.get("content_cache", {}) if isinstance(state, dict) else {}
    if not isinstance(cache, dict):
        cache = {}
    # Invalidate cached detections whenever the signature database changes.
    cache = {k: v for k, v in cache.items() if isinstance(v, dict) and v.get("detector_fingerprint") == detector_fingerprint}

    entries_by_sha: dict[str, dict[str, Any]] = {}
    total_assets = 0
    for host, env in environments.items():
        for entry in env["files"]:
            total_assets += 1
            sha = entry["sha256"].lower()
            entries_by_sha.setdefault(sha, entry)

    missing = {sha: entry for sha, entry in entries_by_sha.items() if sha not in cache}
    downloaded: dict[str, list[dict[str, Any]]] = {}
    failures: list[str] = []
    if missing:
        with ThreadPoolExecutor(max_workers=max(1, min(workers, 16))) as pool:
            futures = {
                pool.submit(_download_uncached, sha, entry, raw_base_url, source_root, timeout, detectors): sha
                for sha, entry in missing.items()
            }
            for future in as_completed(futures):
                sha = futures[future]
                try:
                    key, matches = future.result()
                    downloaded[key] = matches
                except Exception as exc:  # aggregate failures so a partial scan is never published
                    failures.append(str(exc))
    if failures:
        raise MonitorError("One or more bundles could not be verified; refusing partial publication:\n- " + "\n- ".join(failures[:20]))

    for sha, matches in downloaded.items():
        cache[sha] = {"detector_fingerprint": detector_fingerprint, "matches": matches}

    # Only hashes present in the current manifest are needed for the next
    # scan. Pruning prevents the persistent cache from growing with every build.
    cache = {sha: cache[sha] for sha in entries_by_sha}

    occurrences: list[dict[str, Any]] = []
    for host, env in sorted(environments.items()):
        for entry in env["files"]:
            sha = entry["sha256"].lower()
            matches = cache[sha]["matches"]
            for match in matches:
                occurrences.append(_make_occurrence(host, env, entry, match))
    occurrences.sort(key=lambda x: (x["environment"], x["detector_id"], x.get("chunk_id") or "", x["path"]))

    previous = state.get("latest", {}) if isinstance(state, dict) else {}
    previous_occurrences = previous.get("occurrences", []) if isinstance(previous, dict) else []
    if not isinstance(previous_occurrences, list):
        previous_occurrences = []
    changes = compare_occurrences(previous_occurrences, occurrences)
    filter_rules = build_filter_rules(occurrences)
    generated_at = utc_now()
    environment_summary = {
        host: {
            "build": env["build"],
            "checked_at": env.get("checked_at"),
            "javascript_assets": len(env["files"]),
        }
        for host, env in sorted(environments.items())
    }

    # A poll can run repeatedly against the same build. Keep the last
    # meaningful detector movement/new/disappearance report visible until a
    # different build arrives; otherwise the next no-op poll erases the event.
    previous_builds = {
        host: entry.get("build")
        for host, entry in (previous.get("environments", {}) if isinstance(previous, dict) else {}).items()
        if isinstance(entry, dict)
    }
    current_builds = {host: env["build"] for host, env in environments.items()}
    same_build_snapshot = current_builds == previous_builds
    if same_build_snapshot and not any(changes.values()):
        previous_changes = previous.get("changes", {}) if isinstance(previous, dict) else {}
        if isinstance(previous_changes, dict) and any(
            isinstance(previous_changes.get(key), list) and previous_changes[key]
            for key in ("new", "disappeared", "moved", "changed")
        ):
            changes = previous_changes

    report = {
        "schema_version": 1,
        "generated_at": generated_at,
        "source": {"repository": "imu31465/Bloxd-Build-Monitor", "manifest_url": manifest_url},
        "environments": environment_summary,
        "summary": {
            "environments": len(environments),
            "javascript_assets": total_assets,
            "unique_hashes": len(entries_by_sha),
            "new_hashes_scanned": len(downloaded),
            "cached_hashes_reused": len(entries_by_sha) - len(downloaded),
            "detections": len(occurrences),
            "filter_rules": len(filter_rules) + static_filter_count,
            "chunk_filter_rules": len(filter_rules),
            "static_filter_rules": static_filter_count,
        },
        "occurrences": occurrences,
        "filter_rules": filter_rules,
        "changes": changes,
    }
    next_state = {
        "schema_version": STATE_VERSION,
        "updated_at": generated_at,
        "detector_fingerprint": detector_fingerprint,
        "content_cache": cache,
        "latest": report,
    }
    return report, next_state
