#!/usr/bin/env python3
"""Validate generated Enoch promising-signal records without network access."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "signals.jsonl"
MANIFEST = ROOT / "data" / "manifest.json"
RANKING = ROOT / "data" / "ranking.json"
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
    "curation",
    "do_not_overclaim",
}
STATUSES = {"useful_signal", "promising_if_scaled", "compute_scale_blocked"}
PRIVATE_PATHS = ("/var/lib/enoch-control-plane", "/opt/enoch-control-plane")
RANKING_SCHEMA_VERSION = "enoch_promising_signal_ranking_v1"
RANKING_BUCKETS = {
    "top_external_researcher_candidates": "Top external-researcher candidates",
    "compute_scale_blocked": "Compute-scale blocked",
    "followup_recommended": "Follow-up recommended",
    "weak_local_only_preserved": "Weak/local-only preserved signals",
    "likely_stale_low_value_archive": "Likely stale/low-value archive",
}
RANKING_BUCKET_ORDER = [
    "top_external_researcher_candidates",
    "compute_scale_blocked",
    "followup_recommended",
    "weak_local_only_preserved",
    "likely_stale_low_value_archive",
]


def _text(value) -> str:
    return str(value or "").strip()


def _truthy(value) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    return _text(value).lower() in {"1", "true", "t", "yes", "y", "on"}


def _list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return []
        try:
            parsed = json.loads(text)
            if isinstance(parsed, list):
                return parsed
        except Exception:
            pass
        return [text]
    return [value]


def _strength_score(value) -> tuple[int, str]:
    text = _text(value).lower().replace("-", "_").replace(" ", "_")
    if text in {"strong", "high"}:
        return 35, "strong evidence_strength"
    if text in {"moderate", "medium"}:
        return 25, "moderate evidence_strength"
    if text in {"weak", "low"}:
        return 10, "weak evidence_strength"
    return 0, "missing or unclear evidence_strength"


def _hypothesis_score(value) -> tuple[int, str]:
    text = _text(value).lower().replace("-", "_").replace(" ", "_")
    if text in {"supported", "supportive", "confirmed"}:
        return 30, "supported hypothesis_status"
    if text in {"partially_supported", "partly_supported"}:
        return 20, "partially supported hypothesis_status"
    if text in {"mixed", "inconclusive_but_useful"}:
        return 15, "mixed hypothesis_status"
    if text in {"unsupported", "not_supported", "negative", "falsified"}:
        return -15, "unsupported hypothesis_status"
    return 0, "missing or unclear hypothesis_status"


def _has_external_source_url(sources: list[dict]) -> bool:
    for source in sources:
        url = _text(source.get("url")).lower()
        source_id = _text(source.get("source_id")).lower()
        if url.startswith(("http://", "https://", "arxiv:", "doi:")):
            return True
        if source_id.startswith(("arxiv:", "doi:")):
            return True
    return False


def rank_record(record: dict) -> dict:
    score_breakdown: dict[str, int] = {}
    reasons: list[str] = []
    evidence_score, evidence_reason = _strength_score(record.get("evidence_strength"))
    score_breakdown["evidence_strength"] = evidence_score
    reasons.append(evidence_reason)
    hypothesis_score, hypothesis_reason = _hypothesis_score(record.get("hypothesis_status"))
    score_breakdown["hypothesis_status"] = hypothesis_score
    reasons.append(hypothesis_reason)
    sources = record.get("sources") if isinstance(record.get("sources"), list) else []
    source_score = 0
    if sources:
        source_score += 8
        reasons.append("source lineage present")
    else:
        source_score -= 20
        reasons.append("source lineage missing")
    if _has_external_source_url(sources):
        source_score += 4
        reasons.append("external source URL present")
    score_breakdown["source_lineage"] = source_score
    followup = record.get("followup") if isinstance(record.get("followup"), dict) else {}
    followup_score = 0
    if _truthy(followup.get("recommended")):
        followup_score += 10
        reasons.append("bounded follow-up is specified")
    required_evidence = [_text(item) for item in _list(followup.get("required_evidence")) if _text(item)]
    followup_score += min(5, len(required_evidence) * 2)
    depth = int(followup.get("depth") or 0)
    if depth > 2:
        followup_score -= min(15, (depth - 2) * 5)
        reasons.append("follow-up depth is already high")
    score_breakdown["followup"] = followup_score
    evidence = record.get("evidence") if isinstance(record.get("evidence"), dict) else {}
    artifact_paths = [_text(item) for item in _list(evidence.get("artifact_paths")) if _text(item)]
    bounded_score = min(10, len(artifact_paths) * 2)
    if artifact_paths:
        reasons.append("local evidence artifact paths are present")
    joined_paths = " ".join(path.lower() for path in artifact_paths)
    if "metrics" in joined_paths:
        bounded_score += 4
        reasons.append("metrics artifact is present")
    if "project_decision" in joined_paths:
        bounded_score += 4
        reasons.append("project decision artifact is present")
    disclaimer = record.get("do_not_overclaim") if isinstance(record.get("do_not_overclaim"), dict) else {}
    if disclaimer.get("not_a_paper") is True and _text(record.get("claim_scope")) and _text(record.get("scale_limits")):
        bounded_score += 4
    score_breakdown["bounded_evidence"] = bounded_score
    score = max(0, min(100, sum(score_breakdown.values())))
    hypothesis_text = _text(record.get("hypothesis_status")).lower().replace("-", "_").replace(" ", "_")
    if record.get("status") == "compute_scale_blocked":
        bucket = "compute_scale_blocked"
    elif hypothesis_text in {"unsupported", "not_supported", "negative", "falsified"} or score < 35:
        bucket = "likely_stale_low_value_archive"
    elif score >= 85 and _text(record.get("evidence_strength")).lower() in {"strong", "high", "moderate", "medium"}:
        bucket = "top_external_researcher_candidates"
    elif _truthy(followup.get("recommended")) and score >= 45:
        bucket = "followup_recommended"
    else:
        bucket = "weak_local_only_preserved"
    return {
        "schema_version": RANKING_SCHEMA_VERSION,
        "score": score,
        "bucket": bucket,
        "bucket_label": RANKING_BUCKETS[bucket],
        "score_breakdown": score_breakdown,
        "reasons": reasons,
    }


def ranked_records(records: list[dict]) -> list[dict]:
    return sorted(
        records,
        key=lambda record: (
            -int((record.get("curation") or {}).get("score") or 0),
            _text(record.get("title")).lower(),
            _text(record.get("project_id")),
        ),
    )


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
    curation = record.get("curation") if isinstance(record.get("curation"), dict) else {}
    expected_curation = rank_record(record)
    if curation.get("schema_version") != RANKING_SCHEMA_VERSION:
        issues.append("curation.schema_version:invalid")
    if curation.get("bucket") not in RANKING_BUCKETS:
        issues.append("curation.bucket:invalid")
    for key in ("score", "bucket", "score_breakdown", "reasons"):
        if curation.get(key) != expected_curation.get(key):
            issues.append(f"curation.{key}:drift")
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
    if not MANIFEST.exists():
        print(f"missing {MANIFEST.relative_to(ROOT)}", file=sys.stderr)
        return 1
    if not RANKING.exists():
        print(f"missing {RANKING.relative_to(ROOT)}", file=sys.stderr)
        return 1
    failures = []
    ids = set()
    status_counts: dict[str, int] = {}
    records: list[dict] = []
    for line_no, line in enumerate(DATA.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        record = json.loads(line)
        records.append(record)
        project_id = record.get("project_id") or f"line:{line_no}"
        if project_id in ids:
            failures.append({"project_id": project_id, "issues": ["project_id:duplicate"]})
        ids.add(project_id)
        status = str(record.get("status") or "")
        status_counts[status] = status_counts.get(status, 0) + 1
        issues = issues_for(record)
        if issues:
            failures.append({"project_id": project_id, "issues": issues})
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ranking = json.loads(RANKING.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != "enoch_promising_signal_manifest_v1":
        failures.append({"project_id": "manifest", "issues": ["schema_version:invalid"]})
    if manifest.get("record_count") != len(ids):
        failures.append({"project_id": "manifest", "issues": [f"record_count:{manifest.get('record_count')} != {len(ids)}"]})
    if manifest.get("status_counts") != {key: status_counts[key] for key in sorted(status_counts)}:
        failures.append({"project_id": "manifest", "issues": ["status_counts:drift"]})
    if manifest.get("project_ids") != sorted(ids):
        failures.append({"project_id": "manifest", "issues": ["project_ids:drift"]})
    ranking_counts: dict[str, int] = {}
    for record in records:
        bucket = str((record.get("curation") or {}).get("bucket") or "")
        ranking_counts[bucket] = ranking_counts.get(bucket, 0) + 1
    expected_ranking_summary = {bucket: ranking_counts[bucket] for bucket in RANKING_BUCKET_ORDER if ranking_counts.get(bucket, 0)}
    if manifest.get("ranking_summary") != expected_ranking_summary:
        failures.append({"project_id": "manifest", "issues": ["ranking_summary:drift"]})
    if manifest.get("public_evidence_copied") is not False:
        failures.append({"project_id": "manifest", "issues": ["public_evidence_copied:must_be_false"]})
    if ranking.get("schema_version") != RANKING_SCHEMA_VERSION:
        failures.append({"project_id": "ranking", "issues": ["schema_version:invalid"]})
    if ranking.get("bucket_counts") != expected_ranking_summary:
        failures.append({"project_id": "ranking", "issues": ["bucket_counts:drift"]})
    expected_ranked_ids = [record.get("project_id") for record in ranked_records(records)]
    actual_ranked_ids = [item.get("project_id") for item in ranking.get("items", []) if isinstance(item, dict)]
    if actual_ranked_ids != expected_ranked_ids:
        failures.append({"project_id": "ranking", "issues": ["items:order_drift"]})
    expected_items = [
        {
            "project_id": record.get("project_id"),
            "score": (record.get("curation") or {}).get("score"),
            "bucket": (record.get("curation") or {}).get("bucket"),
            "reasons": (record.get("curation") or {}).get("reasons"),
        }
        for record in ranked_records(records)
    ]
    actual_items = [
        {
            "project_id": item.get("project_id"),
            "score": item.get("score"),
            "bucket": item.get("bucket"),
            "reasons": item.get("reasons"),
        }
        for item in ranking.get("items", [])
        if isinstance(item, dict)
    ]
    if actual_items != expected_items:
        failures.append({"project_id": "ranking", "issues": ["items:drift"]})
    if failures:
        print(json.dumps({"error": "validation_failed", "failures": failures}, indent=2), file=sys.stderr)
        return 1
    print(json.dumps({"ok": True, "count": len(ids)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
