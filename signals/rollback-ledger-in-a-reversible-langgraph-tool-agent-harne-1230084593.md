# Rollback ledger in a reversible LangGraph tool-agent harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `rollback-ledger-in-a-reversible-langgraph-tool-agent-harne-1230084593`
Run ID: `rollback-ledger-in-a-reversible-langgraph-tool-agent-harne-1230084593-20260527T173313898339+0000`

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

- Parent run decision: Rollback ledger for multi-step agent error recovery: enoch://control-plane/projects/rollback-ledger-for-multi-step-agent-error-recovery-d01821746136/runs/rollback-ledger-for-multi-step-agent-error-recovery-d01821746136-20260527T144554888264+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d359c38564ef

## What looked useful

The rollback-ledger mechanism worked in the controlled direct harness: ledger mode restored initial external-state hash in 11/11 injected failures while the no-rollback baseline restored 0/11. This supports a bounded mechanism claim but is not publication-grade validation.

## Boundaries and scale limits

Small CPU-only Tier 1 test: 3 deterministic plans, 11 injected failure points, no LLM planner nondeterminism, no concurrent branches, no durable process-restart recovery, no irreversible external APIs, and no production trace workload.

## Claim scope

In a deterministic local LangGraph StateGraph harness with reversible key/value and account-transfer tools, a LIFO inverse-operation rollback ledger restored external mutable tool state after every injected post-side-effect failure in 11 matched failure runs.

## Why it stopped

Tier 1 direct mechanism threshold satisfied, but evidence remains small-harness and no-paper; stop after useful signal rather than overclaiming publication readiness.

## Recommended next action

Run a bounded durability follow-up that persists the rollback ledger through LangGraph checkpointing and verifies rollback after process restart/crash on randomized reversible tool plans.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Durable checkpointed rollback ledger for interrupted LangGraph tool agents
- Success threshold: At least 95% restoration over 50 or more crash/restart runs with randomized reversible tool plans, with zero unexplained ledger invariant violations and a matched baseline below 50% restoration.
- Stop condition: Stop if any persisted-ledger run loses ledger entries, replays inverses out of order, or fails to restore a reversible local tool world in two independently reproduced crash/restart cases.

## Evidence references

- Artifact root: `<local-path>/projects/rollback-ledger-in-a-reversible-langgraph-tool-agent-harne-1230084593`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
