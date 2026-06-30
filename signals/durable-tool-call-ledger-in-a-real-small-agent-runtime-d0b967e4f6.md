# Durable Tool-Call Ledger in a Real Small-Agent Runtime

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `durable-tool-call-ledger-in-a-real-small-agent-runtime-d0b967e4f6`
Run ID: `durable-tool-call-ledger-in-a-real-small-agent-runtime-d0b967e4f6-20260527T041403310159+0000`

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

- Parent run decision: Tool-Call Ledger for Small Agent Rollback: enoch://control-plane/projects/tool-call-ledger-for-small-agent-rollback-6fe3e063c81e/runs/tool-call-ledger-for-small-agent-rollback-6fe3e063c81e-20260524T165917428701+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/43764c537a02

## What looked useful

Ledger plus idempotent tool achieved 100% exactly-once side-effect rate in the Tier 1 crash/restart matrix. Ledger without tool idempotency duplicated side effects in 100/100 trials at the crash-after-side-effect point, matching the volatile baseline and falsifying any ledger-alone exactly-once claim.

## Boundaries and scale limits

Tested 2,000 local trials across deterministic crash points; not tested on production LangGraph, concurrent workers, real LLM nondeterminism, real external APIs, filesystem corruption, or long-running deployments.

## Claim scope

In a controlled single-process restartable small-agent runtime with SQLite persistence, a durable tool-call ledger preserves intent and completed-result replay across injected crashes, but exactly-once external side effects across the post-side-effect/pre-completion crash window require stable tool idempotency keys.

## Why it stopped

Tier 1 direct controlled test found mixed mechanism support and a clear limitation: durable ledger alone does not prevent duplicate side effects after a committed external side effect and before ledger completion.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should add concurrent duplicate executors in a real LangGraph or equivalent small-agent runtime with the same ledger and idempotency controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent Durable Tool Ledger in an Existing Agent Runtime
- Success threshold: Across at least 1,000 controlled concurrent crash/restart trials, ledger-with-idempotency has zero duplicate side effects, zero stuck pending calls, completed-result replay after ledger completion, and lower duplicate invocation rate than the no-ledger idempotent baseline.
- Stop condition: Stop as negative if any duplicate side effect occurs in ledger-with-idempotency, if pending calls remain unrecovered after bounded retry, or if the existing runtime cannot expose stable tool-call IDs without invasive changes.

## Evidence references

- Artifact root: `<local-path>/projects/durable-tool-call-ledger-in-a-real-small-agent-runtime-d0b967e4f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
