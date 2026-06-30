# Mixed-Precision Residual Slots for Tool-Loop Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mixed-precision-residual-slots-for-tool-loop-agents-bad0e4b8b6f5`
Run ID: `mixed-precision-residual-slots-for-tool-loop-agents-bad0e4b8b6f5-20260522T004203814167+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71b83696c4f4

## What looked useful

Sparse residuals at 6.25%, 12.5%, and 25% residual density reduced MSE versus plain int8 by 18.1%, 33.2%, and 56.7% respectively; however, the 25% residual variant used about fp16 memory and still had 332x fp16 MSE. Dense residuals nearly eliminated quantization error but cost 3.02 bytes/value.

## Boundaries and scale limits

Synthetic proxy only; no real LLM agent, no real tool-call trajectories, retrieval metric saturated, sparse residual storage was measured as logical bytes rather than a production kernel, and near-fp16 memory residual variants remained far worse than fp16 reconstruction error.

## Claim scope

In a synthetic CUDA benchmark of mutable tool-loop-like memory slots with repeated sparse additive updates, int8 slots augmented with sparse fp16 residual corrections reduce reconstruction error and slightly improve fixed-readout sign agreement versus plain int8 at logical memory budgets below fp16.

## Why it stopped

Proxy evidence is useful but not paper-ready: it supports an int8-error-compensation mechanism while failing to show fp16-competitive quality at similar memory or real agent-task gains.

## Recommended next action

Run a bounded real tool-loop memory benchmark with a small local model or scripted agent, comparing int8, fp16, and int8 plus sparse residual slots on non-saturated task success and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tool-Loop Task Test for Sparse Residual Agent Memory
- Success threshold: At less than 1.6 logical bytes/value, residual int8 slots improve task success or answer fidelity by at least 2 percentage points over plain int8 with no more than 20% latency overhead, while preserving at least half of fp16's gain over int8 if fp16 is better.
- Stop condition: Stop if the task metric is saturated for all memory methods, if residual int8 improves only reconstruction but not task success, or if measured overhead erases the memory benefit versus fp16.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-residual-slots-for-tool-loop-agents-bad0e4b8b6f5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
