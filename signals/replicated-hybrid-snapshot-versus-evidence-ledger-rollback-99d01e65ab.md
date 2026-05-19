# Replicated hybrid snapshot versus evidence-ledger rollback cost model

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replicated-hybrid-snapshot-versus-evidence-ledger-rollback-99d01e65ab`
Run ID: `replicated-hybrid-snapshot-versus-evidence-ledger-rollback-99d01e65ab-20260516T014212917367+0000`

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

- Internal Enoch project: Replicated hybrid snapshot versus evidence-ledger rollback cost model: internal_generated:replicated-hybrid-snapshot-versus-evidence-ledger-rollback-99d01e65ab

## What looked useful

Hybrid intervals consistently reduced p95 rollback cost versus ledger-only while using far less storage than exact per-transaction snapshots. The 2048-transaction interval gave about 19.9x to 20.3x p95 speedup over ledger-only, about 951x less storage than per-transaction snapshots, and about 1.96x to 1.97x ledger-only storage. Snapshots-only ablations failed exact arbitrary rollback except at checkpoint targets.

## Boundaries and scale limits

Synthetic cost model only; no production storage engine, disk fsync, network replication, partial replica divergence, compression, compaction, or real crash-recovery measurements. Results should not be treated as publication-grade systems evidence.

## Claim scope

In a deterministic replicated key-value rollback cost model with 3 replicas, 60,000 transactions, 20,000 keys, 3 workload regimes, and 5 fixed seeds, periodic snapshot plus evidence-ledger hybrid rollback preserves exact target reconstruction while offering a tunable latency-storage tradeoff versus ledger-only and exact per-transaction snapshots.

## Why it stopped

Tier 2 synthetic/model evidence supports the mechanism but is not publication-grade direct systems evidence.

## Recommended next action

Stop this run as no-paper useful evidence; the concrete next bounded test is a small real storage-engine prototype measuring rollback latency, write amplification, and recovery correctness under injected replica divergence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prototype hybrid snapshot plus evidence-ledger rollback in a real replicated key-value store
- Success threshold: Hybrid exact rollback passes all correctness checks, beats ledger-only p95 rollback latency by at least 5x in every workload regime, and remains below 3x ledger-only physical storage/write-amplification overhead.
- Stop condition: Stop as negative if exact rollback correctness fails, if p95 latency speedup is below 2x in any regime, or if physical storage/write-amplification overhead exceeds 5x ledger-only.

## Evidence references

- Artifact root: `<local-path>/projects/replicated-hybrid-snapshot-versus-evidence-ledger-rollback-99d01e65ab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
