# CPU-Optimized Asymmetric Quantization: Ternary Compute, FP16 Residual Accumulation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-optimized-asymmetric-quantization-ternary-compute-fp16-residual-accumulation-91a5fece076c`
Run ID: `cpu-optimized-asymmetric-quantization-ternary-compute-fp16-residual-accumulation-91a5fece076c-20260528T191610992492+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a4ad4d2c21be

## What looked useful

Ternary masked add/sub compute was cheap, but FP16 residual conversion dominated runtime on F16C-only hardware. Across 12 rows, ternary+FP16-residual won 3/12 cases, averaged 0.778x dense FP32 speed, reached 1.82x only at n=1048576, and was 0.41x-0.71x at n=16777216 while keeping max dot relative error below 5e-4.

## Boundaries and scale limits

Single-thread random-vector dot products only; no packed GEMM/GEMV, no transformer layers, no end-to-end model accuracy, no optimized INT8/FP16 library baseline, and no CPU with native AVX512-FP16 arithmetic.

## Claim scope

On the tested AVX512/F16C Xeon dot-product microbenchmark, asymmetric ternary weights plus FP16 residual accumulation preserves reconstruction accuracy but does not provide reliable CPU throughput improvement over dense FP32; speedups appeared only in the 1M-element cache-sensitive regime and disappeared at larger working sets.

## Why it stopped

Proxy microbenchmark produced an early mixed/negative result for the stated CPU optimization: accuracy is good, but throughput is not reliable and larger working sets are slower than dense FP32.

## Recommended next action

Stop this formulation as no-paper on F16C-only CPU dot products; a bounded follow-up should test packed multi-output GEMV/GEMM where input reuse may amortize residual conversion.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed multi-output ternary-plus-FP16-residual GEMV on CPU
- Success threshold: At least 1.2x median latency speedup over dense FP32 on both cache-resident and memory-resident GEMV/GEMM cases with dot relative error below 1e-3.
- Stop condition: Stop if packed residual conversion remains more than 60% of runtime or median speedup is below 1.0x on either cache-resident or memory-resident cases.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-optimized-asymmetric-quantization-ternary-compute-fp16-residual-accumulation-91a5fece076c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
