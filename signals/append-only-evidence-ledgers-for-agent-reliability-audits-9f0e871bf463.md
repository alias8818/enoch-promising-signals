# Append-only evidence ledgers for agent reliability audits

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `append-only-evidence-ledgers-for-agent-reliability-audits-9f0e871bf463`
Run ID: `append-only-evidence-ledgers-for-agent-reliability-audits-9f0e871bf463-20260611T052151856187+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/603d8d89d296

## What looked useful

Append-only evidence ledgers add practical audit value when an external head hash is retained: they preserve evidence order/content and prevent later transcript rewrites from converting unsupported claims into apparently supported claims. The measured tradeoff was about 1.79x storage overhead and about 24 microseconds per ledger audit case in this toy JSON implementation.

## Boundaries and scale limits

Tested only 1000 synthetic structured episodes and 1400 attacked unreliable cases on a single CPU process. No real LLM traces, human auditors, production logging systems, distributed storage, key compromise, or free-form evidence extraction were evaluated.

## Claim scope

In a deterministic synthetic audit with structured evidence events, an anchored append-only hash-chain ledger detected all tested post-hoc edits, insertions, deletions/replacements, and reorderings that attempted to hide unsupported agent claims, while mutable transcripts false-accepted 75% of attacked unreliable cases.

## Why it stopped

Synthetic-only useful signal; not direct/full validation of real agent reliability audits and therefore not paper-ready.

## Recommended next action

Run a bounded follow-up on real or recorded agent traces by extracting claim/evidence records, anchoring ledger heads, and measuring tamper detection plus auditor workload against existing immutable-log baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace evidence ledger audit benchmark
- Success threshold: Ledger detects at least 95% of post-hoc tampering cases with no more than 5% false positives on clean reliable traces and no more than 2x storage overhead relative to the strongest baseline.
- Stop condition: Stop if claim/evidence extraction from real traces cannot reach 90% agreement with hand labels on a 30-trace calibration set or if ordinary immutable logs match ledger detection with lower overhead.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledgers-for-agent-reliability-audits-9f0e871bf463`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
