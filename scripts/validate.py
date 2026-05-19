#!/usr/bin/env python3
"""Validate generated Enoch promising-signal records without network access."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "signals.jsonl"
SCHEMA = ROOT / "schemas" / "promising-signal.schema.json"
REQUIRED = {
    "schema_version",
    "project_id",
    "run_id",
    "title",
    "status",
    "decision_summary",
    "hypothesis_status",
    "evidence_strength",
    "claim_scope",
    "scale_limits",
    "useful_signal_summary",
    "stop_reason",
    "recommended_next_action",
    "sources",
    "followup",
    "evidence",
    "do_not_overclaim",
}
STATUSES = {"useful_signal", "promising_if_scaled", "compute_scale_blocked"}
PRIVATE_PATHS = ("/var/lib/enoch-control-plane", "/opt/enoch-control-plane")


def issues_for(record: dict) -> list[str]:
    issues: list[str] = []
    missing = sorted(field for field in REQUIRED if record.get(field) in (None, "", [], {}))
    issues.extend(f"{field}:required" for field in missing)
    if record.get("status") not in STATUSES:
        issues.append("status:invalid")
    disclaimer = record.get("do_not_overclaim") if isinstance(record.get("do_not_overclaim"), dict) else {}
    for key in ("not_a_paper", "not_peer_reviewed", "not_publication_validated", "not_in_main_corpus"):
        if disclaimer.get(key) is not True:
            issues.append(f"do_not_overclaim.{key}:required_true")
    if "not validated papers" not in str(disclaimer.get("disclaimer") or ""):
        issues.append("do_not_overclaim.disclaimer:missing_not_validated_papers")
    evidence = record.get("evidence") if isinstance(record.get("evidence"), dict) else {}
    if evidence.get("public_evidence_copied") is not False:
        issues.append("evidence.public_evidence_copied:must_be_false")
    serialized = json.dumps(record, sort_keys=True)
    for private_path in PRIVATE_PATHS:
        if private_path in serialized:
            issues.append(f"private_path_leak:{private_path}")
    return sorted(set(issues))


def main() -> int:
    if not DATA.exists():
        print(f"missing {DATA.relative_to(ROOT)}", file=sys.stderr)
        return 1
    if not SCHEMA.exists():
        print(f"missing {SCHEMA.relative_to(ROOT)}", file=sys.stderr)
        return 1
    failures = []
    ids = set()
    for line_no, line in enumerate(DATA.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        record = json.loads(line)
        project_id = record.get("project_id") or f"line:{line_no}"
        if project_id in ids:
            failures.append({"project_id": project_id, "issues": ["project_id:duplicate"]})
        ids.add(project_id)
        issues = issues_for(record)
        if issues:
            failures.append({"project_id": project_id, "issues": issues})
    if failures:
        print(json.dumps({"error": "validation_failed", "failures": failures}, indent=2), file=sys.stderr)
        return 1
    print(json.dumps({"ok": True, "count": len(ids)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
