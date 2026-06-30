# 1.58-bit Residual Channel Quantization for CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-58-bit-residual-channel-quantization-for-cpu-e223e2c461de`
Run ID: `1-58-bit-residual-channel-quantization-for-cpu-e223e2c461de-20260602T155814396442+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/96eff9dcdbc4

## What looked useful

Residual dense channels reduce ternary error most on outlier-channel weights, but the effective bit budget rises quickly and accuracy remains far worse than INT8; packed 2-bit ternary decoding was slower than FP32 while INT8 was both faster and much more accurate.

## Boundaries and scale limits

No real model perplexity or task metric was measured; no quantization-aware training, learned residual codebook, optimized AVX512 ternary kernel, or end-to-end serving benchmark was run.

## Claim scope

Post-training per-channel ternary 1.58-bit quantization with explicit dense residual output-channel escapes on synthetic weight matrices, plus CPU matvec microbenchmarks on a 4096 x 4096 matrix.

## Why it stopped

Proxy and microbenchmark evidence does not support the practical 1.58-bit CPU claim: ternary/residual accuracy remains high-error and packed ternary is not faster than FP32 or INT8 in the tested CPU kernel.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded deepen follow-up should test actual transformer layer weights and activations against an optimized INT8 CPU baseline before any larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-layer residual-channel ternary quantization probe
- Success threshold: At no more than 3 effective bits per weight, residual-channel ternary must achieve layer output relative RMSE below 0.05 on at least most tested projection layers and show a CPU throughput advantage over INT8 for the same layer shapes.
- Stop condition: Stop if layer output relative RMSE remains above 0.10 at 3 effective bits/weight or if an optimized packed ternary kernel cannot beat the INT8 CPU baseline on representative layer shapes.

## Evidence references

- Artifact root: `<local-path>/projects/1-58-bit-residual-channel-quantization-for-cpu-e223e2c461de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
