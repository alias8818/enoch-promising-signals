# Persistent LangGraph rollback ledger under crash-recovery replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `persistent-langgraph-rollback-ledger-under-crash-recovery-12f7f39ed6`
Run ID: `persistent-langgraph-rollback-ledger-under-crash-recovery-12f7f39ed6-20260529T192341926880+0000`

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

- Parent run decision: Evidence-ledger rollback in a real small-agent tool-trace harness: enoch://control-plane/projects/evidence-ledger-rollback-in-a-real-small-agent-tool-trace-69838f339b/runs/evidence-ledger-rollback-in-a-real-small-agent-tool-trace-69838f339b-20260529T101322478201+0000
- Parent run decision: LangGraph checkpoint/replay evidence-ledger rollback test: enoch://control-plane/projects/langgraph-checkpoint-replay-evidence-ledger-rollback-test-7ebd70771a/runs/langgraph-checkpoint-replay-evidence-ledger-rollback-test-7ebd70771a-20260529T154831031585+0000

## What looked useful

Across 400 forced crash/replay trials per mode, no-ledger replay duplicated external effects in 100% of trials, idempotency avoided duplicate final active effects but compensated 0% of crash-window orphans, and the rollback ledger achieved exactly one active effect while compensating the orphan in 100% of trials.

## Boundaries and scale limits

SQLite modeled the external system; only one crash point was injected, after the side effect but before node return; no distributed checkpointer, real external API, concurrent workers, multi-operation super-step, compensation failure, or commit-node crash was tested.

## Claim scope

In a local single-process LangGraph 1.2.2 StateGraph using SqliteSaver with durability='sync', a persistent rollback ledger compensated crash-window external effects and replayed to exactly one active committed effect after a hard process exit inside the side-effect node.

## Why it stopped

Bounded local validation supports the mechanism but is too synthetic and narrow for publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful mechanism evidence; the next bounded action is a depth-4 crash matrix using a separate non-transactional external service and additional crash points.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rollback ledger crash matrix against a non-transactional external service
- Success threshold: Rollback ledger has zero duplicate active committed effects, zero uncompensated recoverable orphans, and at least 99% replay success across the tested crash matrix, while no-ledger or idempotency-only baselines fail at least one direct target metric.
- Stop condition: Stop if any recoverable crash point leaves duplicate active effects or uncompensated orphans in the rollback-ledger arm, or if the separate service cannot be run locally with durable crash injection.

## Evidence references

- Artifact root: `<local-path>/projects/persistent-langgraph-rollback-ledger-under-crash-recovery-12f7f39ed6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
