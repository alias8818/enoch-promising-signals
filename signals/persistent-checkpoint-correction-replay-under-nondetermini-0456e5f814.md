# Persistent Checkpoint Correction Replay Under Nondeterministic Agent Planning

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `persistent-checkpoint-correction-replay-under-nondetermini-0456e5f814`
Run ID: `persistent-checkpoint-correction-replay-under-nondetermini-0456e5f814-20260528T225743340185+0000`

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

- Parent run decision: Replay Realistic Agent Traces Through Rollback and Recompute Ledgers: enoch://control-plane/projects/replay-realistic-agent-traces-through-rollback-and-recompu-cb8d48abe7/runs/replay-realistic-agent-traces-through-rollback-and-recompu-cb8d48abe7-20260528T015541065369+0000
- Parent run decision: Live Tool Correction Replay Through LangGraph Checkpoints: enoch://control-plane/projects/live-tool-correction-replay-through-langgraph-checkpoints-7e2e53c33f/runs/live-tool-correction-replay-through-langgraph-checkpoints-7e2e53c33f-20260528T160311016500+0000

## What looked useful

Across 512000 main policy-task rows, checkpoint_persistent_replay achieved 1.0000 success and 0.0000 repeated violations versus 0.0839 success and 2.7832 repeated violations for no/volatile memory and 0.2246 success, 2.2949 repeated violations, and 19.1430 overcorrections for global memory. A 128000-row robustness run with different seeds and weaker bias reproduced the ordering.

## Boundaries and scale limits

Evidence is simulator-only: symbolic action labels, generated tasks, synthetic corrections, no real LLM, no real tool-calling environment, no production LangGraph checkpoint store, and no human correction text. The result supports the mechanism but not publication readiness for deployed agents.

## Claim scope

In a fixed-seed synthetic checkpointed planning simulator with context-specific invalid actions, checkpoint-scoped persistent correction replay eliminated repeated violations and achieved 100% bounded task success, outperforming no-memory, volatile-memory, and global-memory controls.

## Why it stopped

The mechanism is supported in a bounded synthetic simulator with direct replay metrics and controls, but the evidence is not real-agent or real-checkpoint evidence and is therefore insufficient for a paper-positive decision.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next, implement the same checkpoint-scoped, volatile, no-memory, and global policies in a real checkpointed agent harness and evaluate replay traces with model/tool failures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Checkpointed Agent Replay Harness for Persistent Corrections
- Success threshold: Checkpoint-scoped replay improves success by >=20 percentage points over no/volatile baselines and reduces repeated violations by >=50% without increasing unrelated-context failures by more than 5 percentage points versus no-memory baseline.
- Stop condition: Stop as negative if checkpoint-scoped replay fails to beat no/volatile baselines by 10 percentage points on success or if it causes more than a 5 percentage point unrelated-context failure increase.

## Evidence references

- Artifact root: `<local-path>/projects/persistent-checkpoint-correction-replay-under-nondetermini-0456e5f814`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
