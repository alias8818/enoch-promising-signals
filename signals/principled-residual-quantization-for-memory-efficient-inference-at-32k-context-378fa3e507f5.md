# Principled Residual Quantization for Memory-Efficient Inference at 32K Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `principled-residual-quantization-for-memory-efficient-inference-at-32k-context-378fa3e507f5`
Run ID: `principled-residual-quantization-for-memory-efficient-inference-at-32k-context-378fa3e507f5-20260608T204255225222+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/91e7721ea839

## What looked useful

At 32K context, residual_2plus2 had 0.1563 attention-output relative L2 versus 0.0925 for direct_int4 while using 1.111x more estimated memory; residual_4plus2 had 0.0308 versus 0.0216 for direct_int6 while using 1.077x more memory. The same negative pattern held at 4K and 16K.

## Boundaries and scale limits

Synthetic KV distributions only; no real model KV traces, real prompts, task-level generation quality, optimized serving kernels, or learned/vector residual codebooks were tested. The result should not be generalized to all residual quantization methods.

## Claim scope

For synthetic 32K-context KV-cache tensors with 8 heads, dim 64, and groupwise affine scalar quantization, two-stage residual scalar quantization did not improve memory-efficient inference quality over direct scalar quantization at matched code-bit budgets.

## Why it stopped

Bounded proxy experiment produced an early negative result for simple affine scalar residual quantization; it is not a full validation of all residual, learned, or vector quantization approaches.

## Recommended next action

Stop this scalar residual quantization line as no-paper evidence; a separate bounded test should use real model KV traces and compare learned or product-code residual quantizers against direct quantization at matched total memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-KV Learned Residual Quantization at Matched Total Memory
- Success threshold: At 32K context, residual design reduces attention-output relative L2 by at least 20% versus the best direct scalar baseline at equal total memory, with no task-quality regression and no more than 10% decode throughput penalty.
- Stop condition: Stop if learned/product-code residual quantization fails to beat direct scalar quantization on real KV traces at equal total memory or if codebook/kernel overhead erases the memory-quality advantage.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residual-quantization-for-memory-efficient-inference-at-32k-context-378fa3e507f5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
