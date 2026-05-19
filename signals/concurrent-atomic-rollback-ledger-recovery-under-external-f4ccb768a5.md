# Concurrent atomic rollback ledger recovery under external latency and error injection

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `concurrent-atomic-rollback-ledger-recovery-under-external-f4ccb768a5`
Run ID: `concurrent-atomic-rollback-ledger-recovery-under-external-f4ccb768a5-20260515T200043461442+0000`

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

- Internal Enoch project: Concurrent atomic rollback ledger recovery under external latency and error injection: internal_generated:concurrent-atomic-rollback-ledger-recovery-under-external-f4ccb768a5

## What looked useful

The proposed rollback ledger mechanism outperformed unsafe local-first, saga compensation, and transaction-holding baselines on recovery correctness under injected external latency, errors, and crash cuts, but the evidence is not broad enough for paper readiness.

## Boundaries and scale limits

Synthetic local harness only; external service modeled by local SQLite; named crash-cut injection rather than process, OS, or power-loss fault injection; 12,500 operations per strategy; no multi-node, production storage engine, or real external API validation.

## Claim scope

In a deterministic SQLite-backed synthetic concurrent transfer harness with separate durable external side effects, an atomic rollback ledger with external-status reconciliation achieved zero account drift, zero external/local mismatches, and zero unresolved journal records across 5 fixed seeds and 12,500 operations, while preserving throughput close to unsafe and saga baselines.

## Why it stopped

Mechanism supported in bounded synthetic validation, but evidence is not publication-grade and controller lineage is already at follow-up depth 4.

## Recommended next action

Stop this follow-up chain at depth 4; preserve the bounded useful signal and do not claim paper readiness without a real service implementation and process-level fault-injection replication.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/concurrent-atomic-rollback-ledger-recovery-under-external-f4ccb768a5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
