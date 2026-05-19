# Validate hybrid snapshot plus evidence-ledger rollback in a networked Raft KV harness

Status: `useful_signal`
Project ID: `validate-hybrid-snapshot-plus-evidence-ledger-rollback-in-e4cbdfb07e`
Run ID: `validate-hybrid-snapshot-plus-evidence-ledger-rollback-in-e4cbdfb07e-20260516T015723336383+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Validate hybrid snapshot plus evidence-ledger rollback in a networked Raft KV harness: internal_generated:validate-hybrid-snapshot-plus-evidence-ledger-rollback-in-e4cbdfb07e

## What looked useful

Primary run: 100 seeds, 10,000 ops/seed, 4 followers, 35% corrupt snapshot probability. Baseline had 140 recovery failures from 140 injected corruptions; hybrid detected all 140 corruptions and had 0 recovery failures. No-corruption control had 0 failures for both modes. High-corruption stress had 92 baseline failures and 0 hybrid failures.

## Boundaries and scale limits

The harness models a stable leader and follower recovery in memory; it does not use an independent production Raft implementation, real TCP multi-process networking, leader election, persistent fsync/crash recovery, concurrent clients, membership changes, or Jepsen-style linearizability checking.

## Claim scope

In a deterministic local Raft-style KV recovery harness with seeded snapshot corruption after compaction, snapshot plus evidence-ledger rollback eliminated follower state divergence observed in the snapshot-only baseline across the tested seeds.

## Why it stopped

The mechanism was supported in a scoped harness, but the Tier 4 publication-readiness threshold was not met because the validation is not a real multi-process networked Raft KV replication study.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful mechanism evidence; paper readiness would require a separate real networked Raft KV implementation with persistent crash/fault injection and linearizability checking, but the controller depth cap prevents recommending another follow-up here.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/validate-hybrid-snapshot-plus-evidence-ledger-rollback-in-e4cbdfb07e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
