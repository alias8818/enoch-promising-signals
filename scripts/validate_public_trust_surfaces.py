#!/usr/bin/env python3
"""Validate public-facing Enoch promising-signal surfaces."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_EXTENSIONS = {".md", ".json", ".jsonl", ".txt"}
SECRET_LIKE_TOKEN = re.compile(
    r"("
    r"sk-proj-[A-Za-z0-9_-]{20,}"
    r"|sk-ant-api03-[A-Za-z0-9_-]{40,}"
    r"|sk-[A-Za-z0-9]{24,}"
    r"|syn_[A-Za-z0-9]{20,}"
    r"|hf_[A-Za-z0-9]{20,}"
    r"|gh[pousr]_[A-Za-z0-9_]{20,}"
    r"|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}"
    r"|Authorization:\s*Bearer\s*[A-Za-z0-9._~+/=-]{24,}"
    r"|(?:OPENAI|ANTHROPIC|SYNTHETIC|GITHUB|HF|HUGGINGFACE|SUPABASE|ENOCH|CONTROL|CALLBACK|DATABASE|POSTGRES)[_-]?(?:API[_-]?KEY|TOKEN|SECRET|PASSWORD|BEARER|DATABASE[_-]?URL)\s*[=:]\s*[A-Za-z0-9._~:/?#[\]@!$&'()*+,;=%-]{12,}"
    r")"
)
PRIVATE_PATH = re.compile(r"/(?:var/lib/enoch-control-plane|opt/enoch-control-plane|home/jeremy|root)(?:/|\b)")
PRIVATE_IP = re.compile(r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b")
OVERCLAIM = re.compile(r"\b(peer[- ]reviewed|validated paper|publication[- ]ready|scientifically proven|proves that|accepted paper)\b", re.I)
REQUIRED_COPY = [
    "not validated papers",
    "not peer reviewed",
    "not publication-positive",
    "not the paper corpus",
]


def line_for(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def public_files() -> list[Path]:
    ignored = {".git"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in ignored for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in PUBLIC_EXTENSIONS:
            files.append(path)
    return sorted(files)


def load_records() -> list[dict]:
    data = ROOT / "data" / "signals.jsonl"
    return [json.loads(line) for line in data.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    failures: list[str] = []
    combined_parts: list[str] = []
    for path in public_files():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8", errors="replace")
        combined_parts.append(text)
        for regex, label in ((SECRET_LIKE_TOKEN, "secret-like token"), (PRIVATE_PATH, "private path"), (PRIVATE_IP, "private IP")):
            for match in regex.finditer(text):
                failures.append(f"{rel}:{line_for(text, match.start())} {label}: {match.group(0)!r}")
        if rel.parts and rel.parts[0] == "signals" and rel.name != "index.md":
            for match in OVERCLAIM.finditer(text):
                window = text[max(0, match.start() - 120) : match.end() + 160].lower()
                if "not " not in window and "not a " not in window:
                    failures.append(f"{rel}:{line_for(text, match.start())} possible overclaim: {match.group(0)!r}")

    combined = "\n".join(combined_parts).lower()
    for phrase in REQUIRED_COPY:
        if phrase not in combined:
            failures.append(f"missing required public framing: {phrase}")

    records = load_records()
    manifest = json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))
    index_text = (ROOT / "signals" / "index.md").read_text(encoding="utf-8", errors="replace")
    ranked_index_path = ROOT / "signals" / "ranked-index.md"
    if not ranked_index_path.exists():
        failures.append("missing signals/ranked-index.md")
        ranked_index_text = ""
    else:
        ranked_index_text = ranked_index_path.read_text(encoding="utf-8", errors="replace")
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace")
    if f"contains {manifest.get('record_count')} deterministic" not in readme_text:
        failures.append("README.md current export count does not match manifest")
    for required_link in ("signals/ranked-index.md", "data/ranking.json", "data/manifest.json"):
        if required_link not in readme_text:
            failures.append(f"README.md missing generated surface link: {required_link}")
    for record in records:
        project_id = str(record.get("project_id") or "")
        title = str(record.get("title") or "")
        if project_id and project_id not in index_text:
            failures.append(f"signals/index.md missing project_id {project_id}")
        if title and title not in index_text:
            failures.append(f"signals/index.md missing title {title}")
        if project_id and project_id not in ranked_index_text:
            failures.append(f"signals/ranked-index.md missing project_id {project_id}")
        curation = record.get("curation") if isinstance(record.get("curation"), dict) else {}
        bucket = str(curation.get("bucket") or "")
        if bucket:
            bucket_path = ROOT / "signals" / "buckets" / f"{bucket.replace('_', '-')}.md"
            if not bucket_path.exists():
                failures.append(f"missing bucket index {bucket_path.relative_to(ROOT)}")
            else:
                bucket_text = bucket_path.read_text(encoding="utf-8", errors="replace")
                if project_id and project_id not in bucket_text:
                    failures.append(f"{bucket_path.relative_to(ROOT)} missing project_id {project_id}")
        evidence = record.get("evidence") if isinstance(record.get("evidence"), dict) else {}
        if evidence.get("public_evidence_copied") is not False:
            failures.append(f"{project_id}: public_evidence_copied must remain false")
        disclaimer = record.get("do_not_overclaim") if isinstance(record.get("do_not_overclaim"), dict) else {}
        for key in ("not_a_paper", "not_peer_reviewed", "not_publication_validated", "not_in_main_corpus"):
            if disclaimer.get(key) is not True:
                failures.append(f"{project_id}: {key} must be true")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1
    print("PASS promising signals public trust surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
