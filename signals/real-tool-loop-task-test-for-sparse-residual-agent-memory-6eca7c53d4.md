# Real Tool-Loop Task Test for Sparse Residual Agent Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-tool-loop-task-test-for-sparse-residual-agent-memory-6eca7c53d4`
Run ID: `real-tool-loop-task-test-for-sparse-residual-agent-memory-6eca7c53d4-20260522T080904558414+0000`

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

- Parent run decision: Mixed-Precision Residual Slots for Tool-Loop Agents: enoch://control-plane/projects/mixed-precision-residual-slots-for-tool-loop-agents-bad0e4b8b6f5/runs/mixed-precision-residual-slots-for-tool-loop-agents-bad0e4b8b6f5-20260522T004203814167+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71b83696c4f4

## What looked useful

Across 50 trials with 37 tool calls per trial, sparse_residual reached 100% mean accuracy versus 0% for recent_window under a 4-line recent budget, and used 87.3% fewer retained-token proxy units than full_transcript while matching its 100% accuracy.

## Boundaries and scale limits

Single-process CPU-only synthetic benchmark; no LLM-driven extraction or reasoning; no natural production tasks; no cross-session persistence; no robustness to noisy or ambiguous memory writes; not a large-scale agent validation.

## Claim scope

In a controlled local file/search tool-loop benchmark with deterministic TARGET_* fact extraction, sparse residual memory preserved sparse task facts across distractor tool calls under a small recent-context budget, matching full transcript accuracy while retaining far less text.

## Why it stopped

Tier 1 controlled direct test produced a useful mechanism signal, but the evidence remains synthetic and deterministic rather than publication-grade.

## Recommended next action

Run a bounded LLM-driven deepen test of the same tool-loop benchmark with noisy observations and model-selected memory writes before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-Driven Sparse Residual Memory on Noisy Tool-Loop Tasks
- Success threshold: Sparse residual improves answer accuracy by at least 25 percentage points over recent-window under the constrained context budget, retains at least 50% fewer tokens than full transcript, and reaches at least 90% of full-transcript accuracy.
- Stop condition: Stop as unsupported if sparse residual improves less than 10 percentage points over recent-window, retains less than 30% fewer tokens than full transcript, or fails below 70% of full-transcript accuracy on the controlled tasks.

## Evidence references

- Artifact root: `<local-path>/projects/real-tool-loop-task-test-for-sparse-residual-agent-memory-6eca7c53d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
