# Live Tool Correction Replay Through LangGraph Checkpoints

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-tool-correction-replay-through-langgraph-checkpoints-7e2e53c33f`
Run ID: `live-tool-correction-replay-through-langgraph-checkpoints-7e2e53c33f-20260528T160311016500+0000`

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

- Parent run decision: Replay Realistic Agent Traces Through Rollback and Recompute Ledgers: enoch://control-plane/projects/replay-realistic-agent-traces-through-rollback-and-recompu-cb8d48abe7/runs/replay-realistic-agent-traces-through-rollback-and-recompu-cb8d48abe7-20260528T015541065369+0000
- Parent run decision: Tiny Agent Evidence Ledger with Rollback: enoch://control-plane/projects/tiny-agent-evidence-ledger-with-rollback-f5c19585376b/runs/tiny-agent-evidence-ledger-with-rollback-f5c19585376b-20260527T225836456869+0000

## What looked useful

Checkpoint-backed after-tool correction replay directly worked in LangGraph and reduced redundant repair execution: 0.0 mean expensive-tool calls during repair versus 1.0 for full rerun and 1.0 for replay-before-tool ablation, with all strategies reaching 100% final correctness over 100 fixed-seed cases.

## Boundaries and scale limits

Synthetic local CPU-only harness; deterministic tools; in-memory checkpointer; no LLM sampling, external APIs, side effects, persistent checkpoint backend, concurrency, LangGraph server deployment, or human-in-the-loop latency.

## Claim scope

On 100 seeded deterministic LangGraph 1.2.2 StateGraph tool workflows using InMemorySaver checkpoints, correcting a bad tool result by forking from the checkpoint immediately after the tool and replaying downstream preserved 100% final correctness while avoiding one expensive upstream tool execution per repair versus full rerun and before-tool replay controls.

## Why it stopped

Tier 2 direct mechanism evidence supports the scoped hypothesis but remains synthetic and local, so it is not publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next useful bounded test would add persistent checkpoint stores and nondeterministic/mock LLM planning while preserving the same correction and ablation metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent Checkpoint Correction Replay Under Nondeterministic Agent Planning
- Success threshold: At least 99% final correctness, zero repeated side-effect/upstream tool executions in the after-tool correction path, and at least 0.8 fewer upstream tool calls per repair versus both controls.
- Stop condition: Stop as negative if persistent-checkpoint replay cannot reliably fork from the intended post-tool checkpoint, if correction accuracy drops below 99%, or if upstream tools are re-executed in more than 1% of after-tool correction repairs.

## Evidence references

- Artifact root: `<local-path>/projects/live-tool-correction-replay-through-langgraph-checkpoints-7e2e53c33f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
