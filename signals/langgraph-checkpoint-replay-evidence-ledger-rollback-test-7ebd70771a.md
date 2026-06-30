# LangGraph checkpoint/replay evidence-ledger rollback test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `langgraph-checkpoint-replay-evidence-ledger-rollback-test-7ebd70771a`
Run ID: `langgraph-checkpoint-replay-evidence-ledger-rollback-test-7ebd70771a-20260529T154831031585+0000`

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

- Parent run decision: Evidence-ledger rollback in a real small-agent tool-trace harness: enoch://control-plane/projects/evidence-ledger-rollback-in-a-real-small-agent-tool-trace-69838f339b/runs/evidence-ledger-rollback-in-a-real-small-agent-tool-trace-69838f339b-20260529T101322478201+0000
- Parent run decision: Evidence-ledger rollback for tool-use small agents: enoch://control-plane/projects/evidence-ledger-rollback-for-tool-use-small-agents-d0951e0665b3/runs/evidence-ledger-rollback-for-tool-use-small-agents-d0951e0665b3-20260529T065032674876+0000

## What looked useful

Checkpoint/replay restored graph state but did not clean up external effects. Evidence recording alone did not help. Compensating rollback after the replay checkpoint reduced abandoned-branch charge and notification leak rates from 1.00 to 0.00 while preserving active branch consistency.

## Boundaries and scale limits

CPU-only local experiment; in-memory checkpointer; deterministic in-process simulated payment/notification effects; no persistent database ledger, process crash recovery, async/concurrent workers, real external APIs, or irreversible side effects.

## Claim scope

For LangGraph 1.2.2 in-memory checkpoint time-travel/fork workflows with deterministic reversible simulated external effects, a compensating evidence ledger eliminated abandoned-branch charge and notification leaks across 1,000 fixed-seed trials, while checkpoint-only and record-only baselines leaked in every trial.

## Why it stopped

Medium local validation supports the mechanism but remains simulated and lacks persistence, crash recovery, concurrency, and real external side-effect evidence needed for a bounded paper claim.

## Recommended next action

Stop this run as no-paper useful signal; next, deepen with persistent checkpointer plus persistent ledger and kill/restart fault injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent LangGraph rollback ledger under crash-recovery replay
- Success threshold: Across at least 10 fixed seeds and 1,000 crash-injected trials, rollback ledger leak rate is below 1%, active consistency is at least 99%, and both checkpoint-only and record-only baselines have at least 25 percentage points higher leak rate.
- Stop condition: Stop if persistent rollback cannot recover cleanly after process restart, if active branch consistency drops below 99%, or if rollback fails to improve leak rate by at least 25 percentage points versus checkpoint-only.

## Evidence references

- Artifact root: `<local-path>/projects/langgraph-checkpoint-replay-evidence-ledger-rollback-test-7ebd70771a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
