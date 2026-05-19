# Production-baseline crash campaign for incremental Merkle WAL KV

Status: `useful_signal`
Project ID: `production-baseline-crash-campaign-for-incremental-merkle-46d4f04fc4`
Run ID: `production-baseline-crash-campaign-for-incremental-merkle-46d4f04fc4-20260518T012604885972+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Production-baseline crash campaign for incremental Merkle WAL KV: internal_generated:production-baseline-crash-campaign-for-incremental-merkle-46d4f04fc4

## What looked useful

Zero recovery mismatches were observed in 6,000 internal torn-WAL/corruption trials and 750 external kill trials across incremental, full-rebuild, and SQLite controls. Incremental Merkle maintenance achieved 165,730.79 ops/s without per-operation fsync versus 726.78 ops/s for full rebuild, and 2,361.61 ops/s with fsync versus 657.64 ops/s for full rebuild.

## Boundaries and scale limits

Evidence is bounded to a local synthetic harness: no production database integration, hardware power-fail rig, concurrent writers/readers, compaction, snapshots, long-duration soak, or real application traces. SQLite WAL was used as a production crash/throughput control, not as a Merkle-equivalent implementation.

## Claim scope

A self-contained deterministic WAL key-value implementation with incremental Merkle maintenance recovered the correct WAL prefix and Merkle root across 6,000 torn/corrupt WAL trials and 250 external SIGKILL trials, and outperformed a full-rebuild Merkle control on local synthetic write workloads.

## Why it stopped

Bounded direct crash campaign supports the mechanism but remains a local synthetic harness rather than publication-grade production replication and robustness evidence.

## Recommended next action

Stop this follow-up as no-paper useful-signal evidence: the Tier 4 paper-readiness bar was not met, and the controller follow-up depth is already 4 so no further chained follow-up is recommended.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/production-baseline-crash-campaign-for-incremental-merkle-46d4f04fc4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
