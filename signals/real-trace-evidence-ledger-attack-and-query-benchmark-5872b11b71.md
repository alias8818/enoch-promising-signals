# Real Trace Evidence Ledger Attack and Query Benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-trace-evidence-ledger-attack-and-query-benchmark-5872b11b71`
Run ID: `real-trace-evidence-ledger-attack-and-query-benchmark-5872b11b71-20260527T111650899596+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: CPU Agent Evidence Ledger: enoch://control-plane/projects/cpu-agent-evidence-ledger-f3b03da62bd0/runs/cpu-agent-evidence-ledger-f3b03da62bd0-20260525T051940964757+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fa784b59fdfb

## What looked useful

Mechanism support is positive for anchored hash-chain tamper detection under the tested post-hoc attack model. Practicality is mixed: verification reached about 71.8k events/s and rare indexed queries were about 22x faster than baseline scan, but ledger build was 3.84x slower and storage was 2.59x larger than baseline, with common exact-match and keyword queries slower than baseline scans.

## Boundaries and scale limits

Single CPU worker, one readable local trace source, 8,050 events, local JSON tip anchor, no remote timestamping/signing, no concurrent ingestion, no multi-source correlation, no million-event retention test, and no adversary with control over both ledger and anchor.

## Claim scope

Tier 1 controlled small direct test: a Python/SQLite hash-chained evidence ledger over 8,050 real /var/log/dpkg.log trace events detected raw modification, row deletion, and suffix-recompute-without-anchor-update attacks; query performance was favorable for rare indexed exact matches but unfavorable for common exact matches and scan-bound keyword queries.

## Why it stopped

No-paper useful signal: the small direct test supports the mechanism but does not provide publication-grade operational evidence.

## Recommended next action

Run a bounded deepen test on multi-source readable logs with remote or signed anchors, FTS keyword indexing, and at least 100k events before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-source signed-anchor evidence ledger benchmark
- Success threshold: All tested tampering attacks are detected; full verification throughput is at least 50k events/s; rare exact-match median query latency is below 1 ms; FTS keyword median query latency improves over raw scan; storage overhead stays below 3.5x baseline.
- Stop condition: Stop if any tampering attack passes verification under the stated anchor model, if verification throughput falls below 25k events/s at 100k events, or if storage overhead exceeds 5x baseline without a compensating query benefit.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evidence-ledger-attack-and-query-benchmark-5872b11b71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
