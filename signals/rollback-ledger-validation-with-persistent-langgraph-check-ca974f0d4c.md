# Rollback ledger validation with persistent LangGraph checkpointing and database/API tool adapters

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `rollback-ledger-validation-with-persistent-langgraph-check-ca974f0d4c`
Run ID: `rollback-ledger-validation-with-persistent-langgraph-check-ca974f0d4c-20260528T033417375472+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Process-kill rollback ledger validation for concurrent LangGraph tool agents: enoch://control-plane/projects/process-kill-rollback-ledger-validation-for-concurrent-lan-1f6772560b/runs/process-kill-rollback-ledger-validation-for-concurrent-lan-1f6772560b-20260528T003853173266+0000
- Parent run decision: Durable checkpointed rollback ledger for interrupted LangGraph tool agents: enoch://control-plane/projects/durable-checkpointed-rollback-ledger-for-interrupted-langg-fe31290b22/runs/durable-checkpointed-rollback-ledger-for-interrupted-langg-fe31290b22-20260527T203043312150+0000

## What looked useful

Across five fixed seeds and 5000 trials per mode, persistent checkpointing with rollback ledger preserved exact database balances and exact net API effects under 3308 injected crashes, while persistent checkpointing without a ledger duplicated database transfers and produced 6667 committed API calls for 5000 intended operations. A volatile-checkpoint ledger ablation also passed, showing adapter-local rollback carried most of the measured correctness.

## Boundaries and scale limits

Synthetic local adapters only; no real remote API, no production database schema, no concurrent multi-worker runs, no OS-level kill at arbitrary instruction boundaries, and no comparison against idempotency-key or transactional-outbox production baselines.

## Claim scope

In a local deterministic LangGraph StateGraph benchmark using SQLite checkpointing and SQLite-backed database/API adapter simulations, a persistent rollback ledger repaired injected post-side-effect crash windows that checkpoint-only replay failed.

## Why it stopped

The result supports the rollback-ledger mechanism in a bounded local benchmark but falls short of Tier 4 paper-readiness because the API/database adapters are synthetic and the volatile-checkpoint ablation shows persistent LangGraph checkpointing was not uniquely responsible for correctness.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful-signal evidence; do not chain another follow-up from this controller lineage without a new external mandate.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/rollback-ledger-validation-with-persistent-langgraph-check-ca974f0d4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
