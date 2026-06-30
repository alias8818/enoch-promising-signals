# LLM-Driven Sparse Residual Memory on Noisy Tool-Loop Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-driven-sparse-residual-memory-on-noisy-tool-loop-tasks-ec6be77e46`
Run ID: `llm-driven-sparse-residual-memory-on-noisy-tool-loop-tasks-ec6be77e46-20260522T092514426449+0000`

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

- Parent run decision: Mixed-Precision Residual Slots for Tool-Loop Agents: enoch://control-plane/projects/mixed-precision-residual-slots-for-tool-loop-agents-bad0e4b8b6f5/runs/mixed-precision-residual-slots-for-tool-loop-agents-bad0e4b8b6f5-20260522T004203814167+0000
- Parent run decision: Real Tool-Loop Task Test for Sparse Residual Agent Memory: enoch://control-plane/projects/real-tool-loop-task-test-for-sparse-residual-agent-memory-6eca7c53d4/runs/real-tool-loop-task-test-for-sparse-residual-agent-memory-6eca7c53d4-20260522T080904558414+0000

## What looked useful

Sparse confidence-filtered key memory can help over recency when capacity covers enough of the hot working set, but the residual component produced no independent gain. Main Tier 2 accuracy was lexical retrieval 0.8108, sparse residual 0.2756, no-residual ablation 0.2756, recency 0.1953, dense oracle 0.9981. Capacity sweep at 20% noise showed sparse residual reaches 0.8650 at budget 384 but remains identical to the no-residual ablation.

## Boundaries and scale limits

Synthetic traces only; no live LLM, no learned salience scorer, and no real external tool outputs. The lexical retrieval baseline uses a full external trace store, while sparse residual uses a strict retained-item budget. The residual path collapsed to zero retained residual records under this implementation's budget enforcement, so the result falsifies this concrete mechanism rather than every possible residual memory design.

## Claim scope

On a synthetic noisy tool-loop memory benchmark with 2,400-step traces, 10 fixed seeds, three corruption levels, fixed memory budget 96, ablations, recency/reservoir baselines, full-trace lexical retrieval baseline, and dense oracle control, the tested sparse residual memory implementation does not support the residual-memory hypothesis. It improves over simple bounded recency/reservoir memory but fails far below full-trace lexical retrieval, and the no-residual ablation is identical to the residual policy.

## Why it stopped

Tier 2 fixed-seed synthetic validation produced a no-paper useful signal: the concrete sparse residual memory did not beat a real retrieval baseline at the main budget and the residual ablation showed zero mechanism contribution.

## Recommended next action

Stop paper escalation for this mechanism; run one bounded deepen test of residual-protected allocation or query-conditioned residual retrieval before any larger LLM-agent validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-Protected Sparse Memory on Noisy Tool Traces
- Success threshold: At budget 96 or a pre-registered comparable constrained budget, residual-protected memory improves accuracy by at least 10 percentage points over the no-residual ablation with 95% paired CI excluding zero, while staying within 5 percentage points of full-trace lexical retrieval on at least one medium-noise setting.
- Stop condition: Stop if residual records remain unused/nonzero without accuracy gain, or if the residual policy fails to beat the no-residual ablation by at least 5 percentage points in the synthetic fixed-seed Tier 2 sweep.

## Evidence references

- Artifact root: `<local-path>/projects/llm-driven-sparse-residual-memory-on-noisy-tool-loop-tasks-ec6be77e46`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
