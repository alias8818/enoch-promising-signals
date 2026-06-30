# Crash-window rollback coverage inside a real LangGraph-style tool executor

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `crash-window-rollback-coverage-inside-a-real-langgraph-sty-d67fb0d5d0`
Run ID: `crash-window-rollback-coverage-inside-a-real-langgraph-sty-d67fb0d5d0-20260527T020743806560+0000`

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

- Parent run decision: Durable evidence-ledger rollback in a real tool-agent harness: enoch://control-plane/projects/durable-evidence-ledger-rollback-in-a-real-tool-agent-harn-cce396b529/runs/durable-evidence-ledger-rollback-in-a-real-tool-agent-harn-cce396b529-20260526T193511381023+0000
- Parent run decision: Evidence-ledger tool agent with local rollback: enoch://control-plane/projects/evidence-ledger-tool-agent-with-local-rollback-0348276a0352/runs/evidence-ledger-tool-agent-with-local-rollback-0348276a0352-20260525T111521496628+0000

## What looked useful

Across two 2400-trial medium runs, the plain baseline duplicated effects in 200/200 trials for the after_effect_before_return crash window and had 0 duplicates in the post_tool_checkpoint control. Idempotent and journaled controls had 0 duplicate/lost effects in all tested cells.

## Boundaries and scale limits

Tested 5 fixed seeds, 3 policies, 4 crash phases, 40 trials per cell, with SQLite external effects and both in-memory and SQLite LangGraph checkpointers. Not tested: arbitrary OS SIGKILL timing, production external APIs, concurrent tool fanout, multi-effect sagas, distributed workers, or long-running agent workloads.

## Claim scope

In a deterministic LangGraph StateGraph using the prebuilt ToolNode, checkpoint replay alone does not cover the crash window after a durable external side effect commits but before the tool node returns/checkpoints; idempotency-key and journal-plus-idempotency controls covered that single-effect window in fixed-seed SQLite experiments.

## Why it stopped

Tier 2 local evidence supports the mechanism but remains bounded to controlled SQLite and injected-exception crash windows, so it is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Do not write a paper from this run; deepen only with subprocess-level hard-kill injection and concurrent multi-tool graphs if the controller wants stronger direct evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Subprocess hard-kill and concurrent multi-tool rollback coverage for LangGraph ToolNode
- Success threshold: Journaled/idempotent policies maintain >=99.5% exactly-once effect correctness with zero unresolved prepared journals, while the non-idempotent baseline shows a statistically clear duplicate-effect failure in after-effect/pre-checkpoint windows.
- Stop condition: Stop if subprocess hard-kill cannot reproduce the baseline duplicate window or if idempotent/journaled policies fail to improve correctness over baseline under the same seeds.

## Evidence references

- Artifact root: `<local-path>/projects/crash-window-rollback-coverage-inside-a-real-langgraph-sty-d67fb0d5d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
