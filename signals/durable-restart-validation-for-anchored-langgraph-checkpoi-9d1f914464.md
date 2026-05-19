# Durable Restart Validation for Anchored LangGraph Checkpoints

Status: `useful_signal`
Project ID: `durable-restart-validation-for-anchored-langgraph-checkpoi-9d1f914464`
Run ID: `durable-restart-validation-for-anchored-langgraph-checkpoi-9d1f914464-20260515T213302968445+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Durable Restart Validation for Anchored LangGraph Checkpoints: internal_generated:durable-restart-validation-for-anchored-langgraph-checkpoi-9d1f914464

## What looked useful

Across 360 fixed-seed trials, anchored modes had 0 duplicate side effects across 120 hard exits per mode, while unanchored persistent and in-memory baselines each produced 60 duplicate side effects. Duplicates appeared only in the after-effect-before-return failure window.

## Boundaries and scale limits

Tested locally with deterministic SQLite side effects, LangGraph SqliteSaver and InMemorySaver, 10 fixed seeds, crash budgets 0-3, and three failure placements. Not validated for production PostgresSaver, distributed services, concurrent workers, multi-node agent workflows, or cloud deployment.

## Claim scope

In a local two-node LangGraph StateGraph with subprocess hard exits, a durable external logical-id anchor prevents duplicate SQLite-recorded side effects when the process dies after the side effect but before the node returns and LangGraph can checkpoint completion.

## Why it stopped

Tier 2 local evidence supports the anchoring mechanism but remains synthetic/local and insufficient for publication-grade durable execution claims.

## Recommended next action

Run a bounded deepen validation with PostgresSaver, a separate external side-effect database, concurrent restart workers, and a multi-node branching LangGraph workflow before considering a scoped paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent Postgres-backed anchored LangGraph restart validation
- Success threshold: Anchored mode completes at least 99% of trials with zero duplicate side effects under post-side-effect hard exits and concurrent contention, while the unanchored persistent baseline shows measurable duplicates in the same failure windows.
- Stop condition: Stop as negative if anchored mode produces any duplicate side effect caused by restart or concurrent contention, or if completion rate falls below 99% for reasons intrinsic to the anchor pattern.

## Evidence references

- Artifact root: `<local-path>/projects/durable-restart-validation-for-anchored-langgraph-checkpoi-9d1f914464`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
