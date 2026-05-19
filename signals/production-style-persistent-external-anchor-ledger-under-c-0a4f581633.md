# Production-style persistent external-anchor ledger under crash and concurrent real-agent traces

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `production-style-persistent-external-anchor-ledger-under-c-0a4f581633`
Run ID: `production-style-persistent-external-anchor-ledger-under-c-0a4f581633-20260518T140152676539+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Production-style persistent external-anchor ledger under crash and concurrent real-agent traces: internal_generated:production-style-persistent-external-anchor-ledger-under-c-0a4f581633

## What looked useful

Across 5 fixed seeds at 500 anchors, sqlite_full had 0 acknowledged anchors lost, 0 corrupt rows, 0 duplicate rows, and valid chains; split-write JSONL baselines lost 803-834 acknowledged anchors and produced 7978-8576 corrupt rows; the no-unique SQLite ablation produced 6584 duplicate rows. At 2000 anchors over 3 seeds, sqlite_full matched the locked/fsynced JSONL control on safety while improving mean throughput from 2371 to 7544 attempts/s and mean worker latency from 59.35 ms to 7.46 ms.

## Boundaries and scale limits

Single-machine local filesystem only; one parsed Codex/Enoch trace source replayed deterministically; maximum tested scale was 2000 unique anchors per seed, 32 workers, 5 crash/recovery epochs; no power-loss, multi-host, network filesystem, external notary, or production soak validation.

## Claim scope

Bounded local evidence shows a SQLite WAL external-anchor ledger with unique anchors and a transactional hash chain preserves acknowledged real-agent trace anchors under concurrent duplicate writers and SIGKILL crash/recovery epochs, and scales better than a locked/fsynced JSONL baseline up to 2000 unique anchors per seed.

## Why it stopped

Useful mechanism/performance evidence was produced, but a conventional locked/fsynced JSONL baseline also satisfied the core safety invariants locally, so the result is not paper-positive or novel enough for finalize_positive.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful evidence; do not recommend another controller follow-up because the lineage cap is reached.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/production-style-persistent-external-anchor-ledger-under-c-0a4f581633`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
