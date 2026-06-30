# CPU Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-agent-evidence-ledger-f3b03da62bd0`
Run ID: `cpu-agent-evidence-ledger-f3b03da62bd0-20260525T051940964757+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fa784b59fdfb

## What looked useful

A minimal hash-chain evidence ledger appears practical for local CPU-agent provenance: in the 100k-event confirmation run, hash-chain JSONL wrote 59,067 events/s at 2.71x plain-JSONL time and 1.71x size, while SQLite hash-chain wrote 34,393 events/s at 4.65x time and 1.60x size. Both tamper-evident variants verified intact ledgers and detected a modified middle row.

## Boundaries and scale limits

Synthetic traces only; no production agent replay, cryptographic signatures, trusted timestamping, multi-writer concurrency, rollback resistance, deletion/reordering attack suite, or human audit study.

## Claim scope

On one CPU worker with synthetic single-writer agent evidence events, hash-chained JSONL and SQLite ledgers provide deterministic detection of a modified middle record while sustaining tens of thousands of events per second.

## Why it stopped

Useful no-paper signal from a synthetic local benchmark; evidence is not production-grade or broad enough for finalize_positive.

## Recommended next action

Run a bounded deepen follow-up using real CPU-agent traces and an explicit deletion/reordering/rollback attack suite before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Evidence Ledger Attack and Query Benchmark
- Success threshold: Hash-chain or checkpointed ledger detects all non-rollback attacks in the suite, has write slowdown under 5x plain JSONL, and answers predefined audit queries under 1 second at 100k records.
- Stop condition: Stop if real trace replay cannot be obtained locally, if deletion/reordering attacks are not detected without adding external checkpoints, or if overhead exceeds 10x plain JSONL on 100k records.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-agent-evidence-ledger-f3b03da62bd0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
