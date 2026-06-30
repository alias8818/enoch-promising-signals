# 2-bit+FP16 residual weight quantization for CPU inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `2-bit-fp16-residual-weight-quantization-for-cpu-inference-af553de5c7de`
Run ID: `2-bit-fp16-residual-weight-quantization-for-cpu-inference-af553de5c7de-20260629T085442149500+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/85c96a57ff49

## What looked useful

Packed 2-bit weights can beat a scalar FP16-load matvec baseline in this microbenchmark, but residual densities up to 12.5% leave high output error and reduce or remove the speed advantage. Best speed was 1.60x at output NRMSE 0.397; best output error was NRMSE 0.329 with only 1.13x speedup on normal weights, while heavy-tailed weights remained much worse.

## Boundaries and scale limits

No real model weights, no perplexity/task metric, no batched GEMM, no production inference runtime, and no SIMD-optimized decode kernel were tested.

## Claim scope

Bounded CPU microbenchmark of a simple per-group symmetric 2-bit weight quantizer with sparse top-error FP16 residuals on synthetic 2048x2048 matvecs, group sizes 16 and 64, residual fractions up to 12.5%.

## Why it stopped

Early bounded proxy falsification: the tested 2-bit plus sparse FP16 residual design does not provide an acceptable accuracy-speed tradeoff for CPU inference, though it does not rule out substantially different optimized residual quantization schemes.

## Recommended next action

Stop this simple formulation as no-paper evidence; only revisit with a different quantizer plus an optimized SIMD CPU kernel and direct real-model quality metrics.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Real-model AVX512 2-bit residual quantization with outlier-aware scaling
- Success threshold: On a real model or representative transformer layers, output/task degradation is within a predeclared bound while throughput is at least 1.2x over FP16 and storage is below 8 effective bits per weight including metadata.
- Stop condition: Stop if real-model error remains high at residual densities that preserve at least 1.2x throughput, or if residual metadata/decode overhead eliminates the speed advantage.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-fp16-residual-weight-quantization-for-cpu-inference-af553de5c7de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
