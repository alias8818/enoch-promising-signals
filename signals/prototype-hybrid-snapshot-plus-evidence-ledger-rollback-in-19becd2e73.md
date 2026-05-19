# Prototype hybrid snapshot plus evidence-ledger rollback in a real replicated key-value store

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `prototype-hybrid-snapshot-plus-evidence-ledger-rollback-in-19becd2e73`
Run ID: `prototype-hybrid-snapshot-plus-evidence-ledger-rollback-in-19becd2e73-20260516T014723324548+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Prototype hybrid snapshot plus evidence-ledger rollback in a real replicated key-value store: internal_generated:prototype-hybrid-snapshot-plus-evidence-ledger-rollback-in-19becd2e73

## What looked useful

The bounded prototype supports the mechanism: snapshots alone are not exact for arbitrary revisions, WAL replay is exact but reads much more history, and adding a small evidence ledger allows exact rollback from a snapshot plus verified delta while detecting tampering.

## Boundaries and scale limits

Validation used synthetic fixed-seed workloads, JSON persistence, local synchronous replicas, 500k operations, and no networked consensus, partitions, leader failover, concurrent clients, production storage engine, or multi-hour endurance run.

## Claim scope

In a deterministic single-process three-replica persisted KV prototype with synchronous replication, full snapshots every 50k revisions, and hash-chain WAL segment evidence, hybrid snapshot-plus-ledger rollback produced exact rollback, detected injected WAL tampering, read about 32% of the WAL-replay baseline bytes, and improved median rollback latency by 1.19x at 500k operations across three fixed seeds.

## Why it stopped

No-paper useful signal: direct prototype evidence supports the scoped mechanism, but the implementation is not a production or networked consensus KV store and the latency gain is modest.

## Recommended next action

Run one depth-4 deepen follow-up in a networked Raft KV harness with crash/restart and leader-failover cases; stop if hybrid rollback does not remain exact, tamper-detecting, and at least 1.2x faster than full WAL replay at 500k+ operations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validate hybrid snapshot plus evidence-ledger rollback in a networked Raft KV harness
- Success threshold: Hybrid rollback must be 100% correct, detect all injected WAL tampering, and achieve at least 1.2x median rollback speedup with lower p95 latency than full WAL replay across all fixed-seed networked Raft runs.
- Stop condition: Stop if any exactness or tamper-detection failure occurs, or if median hybrid speedup remains below 1.2x after 500k+ operations in the networked harness.

## Evidence references

- Artifact root: `<local-path>/projects/prototype-hybrid-snapshot-plus-evidence-ledger-rollback-in-19becd2e73`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
