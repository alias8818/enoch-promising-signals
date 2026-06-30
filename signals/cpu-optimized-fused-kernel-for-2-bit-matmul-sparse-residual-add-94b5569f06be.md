# CPU-Optimized Fused Kernel for 2-bit Matmul + Sparse Residual Add

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-optimized-fused-kernel-for-2-bit-matmul-sparse-residual-add-94b5569f06be`
Run ID: `cpu-optimized-fused-kernel-for-2-bit-matmul-sparse-residual-add-94b5569f06be-20260525T202341047364+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5c1de356f2ba

## What looked useful

Fusion of sparse residual add into a scalar packed 2-bit CPU matmul averaged 1.0028x versus packed-separate across 11 cases, ranging from 0.9584x to 1.0535x. The fused packed path averaged only 0.8724x of the unpacked int8-weight separate baseline, indicating bit extraction/decode cost dominates before sparse residual fusion can matter.

## Boundaries and scale limits

Synthetic matrices only; no vectorized 2-bit microkernel, no multi-threading, no real model tensors, no quantization scales, and no mature library baselines. Results should not be treated as a full rejection of highly optimized 2-bit CPU inference.

## Claim scope

On this AVX-512-capable Xeon worker, a portable scalar fused packed-2-bit matmul plus CSR sparse residual add is correctness-valid but provides only neutral performance versus packed matmul followed by sparse add across small/medium synthetic CPU benchmarks; it remains slower than an unpacked int8-weight matmul baseline.

## Why it stopped

Moderate synthetic evidence does not support the fused kernel as a standalone CPU performance win; the result is a bounded proxy/early falsification of the naive scalar version, not a full validation or full rejection of all optimized 2-bit CPU kernels.

## Recommended next action

Stop this as a no-paper useful signal; only reopen with a vectorized AVX-512/AVX2 2-bit decode/multiply microkernel and compare it against packed-separate plus strong int8 library baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Vectorized 2-bit CPU microkernel before sparse residual fusion
- Success threshold: Across at least three medium transformer-like shapes, fused vectorized packed 2-bit matmul plus sparse residual add is at least 1.10x faster than packed-separate and no slower than 0.95x of the selected strong int8 CPU baseline.
- Stop condition: Stop if the vectorized packed matmul remains below 0.95x of the int8 baseline or if fusion remains within +/-5% of packed-separate after decode overhead is reduced.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-optimized-fused-kernel-for-2-bit-matmul-sparse-residual-add-94b5569f06be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
