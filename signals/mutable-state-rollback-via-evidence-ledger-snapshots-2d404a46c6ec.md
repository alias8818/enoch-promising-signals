# Mutable State Rollback via Evidence Ledger Snapshots

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mutable-state-rollback-via-evidence-ledger-snapshots-2d404a46c6ec`
Run ID: `mutable-state-rollback-via-evidence-ledger-snapshots-2d404a46c6ec-20260516T012955496832+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/40feb6f09d0c

## What looked useful

The mechanism works as a rollback/correctness/tamper-evidence prototype and exposes the main engineering tradeoff: sparse snapshots buy storage savings but increase replay latency, while small states may not amortize ledger metadata.

## Boundaries and scale limits

The evidence is synthetic and in-memory only. It does not test production storage engines, filesystem sync cost, crash recovery, concurrent writers, compaction, application object graphs, or multi-seed robustness. Tiny-state smoke tests showed ledger metadata can exceed full checkpoint storage.

## Claim scope

In a deterministic in-memory key/value simulator, hash-chained evidence-ledger snapshots reconstructed sampled checkpoint states with zero mismatches and reduced independently serialized storage by 12.1% to 82.4% on medium synthetic workloads, at the cost of 2.49x to 32.87x higher p95 rollback latency versus copying a full checkpoint.

## Why it stopped

No-paper useful signal: the result is direct for a synthetic prototype but lacks production baselines, crash recovery, concurrent mutation, and disk-backed storage evidence.

## Recommended next action

Do not write a paper from this run; run a bounded disk-backed comparison against SQLite WAL snapshots, RocksDB checkpoints, or LMDB/copy-on-write snapshots before investing further.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Disk-backed evidence-ledger rollback versus practical snapshot baselines
- Success threshold: Across at least three seeds, achieve zero rollback mismatches, detect all deliberate tampering, reduce stored bytes by at least 30% versus the best tested practical baseline, and keep p95 rollback latency below 50 ms.
- Stop condition: Stop if any implementation has rollback mismatches or undetected tampering, or if storage savings stay below 15% while p95 rollback latency exceeds 100 ms on two or more seeds.

## Evidence references

- Artifact root: `<local-path>/projects/mutable-state-rollback-via-evidence-ledger-snapshots-2d404a46c6ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
