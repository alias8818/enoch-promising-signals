# CPU-Optimized Ternary Residual Transformer: Direct Inference Benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-optimized-ternary-residual-transformer-direct-inference-benchmark-f3f3e7fcb252`
Run ID: `cpu-optimized-ternary-residual-transformer-direct-inference-benchmark-f3f3e7fcb252-20260531T161410921826+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/290050cb2943

## What looked useful

Sparse ternary CPU inference is promising only when sparsity is real enough to skip work; ternary weights without zeros are not a reliable CPU speed mechanism. The benchmark provides reproducible small/medium projection evidence but is not publication-grade.

## Boundaries and scale limits

This is a local direct-kernel benchmark only. It does not validate full transformer decode latency, model quality, trained ternary residual architectures, production BLAS baselines, custom AVX512 bit-packed kernels, core pinning, NUMA tuning, or larger model serving.

## Claim scope

On this CPU worker, a hand-written sparse ternary per-row index-sum GEMV accelerates batch-1 transformer-like projection layers when the ternary matrix has substantial zeros, with stable single-thread median speedups of 3.26x at 50% nonzero, 6.34x at 25% nonzero, and 15.10x at 12.5% nonzero across tested 768 and 2048 hidden-size projections. At 100% nonzero density the speedup is mixed and not robust.

## Why it stopped

The result is a bounded local inference-kernel signal rather than full validation of a CPU-optimized ternary residual transformer; quality and end-to-end serving evidence are missing.

## Recommended next action

Stop this run as a no-paper useful signal; next, run a bounded deepen test with pinned-core repetitions comparing OpenBLAS dense GEMV against an AVX512 or bit-packed ternary kernel inside a full single-layer decode microbenchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pinned-core AVX512 ternary decode microbenchmark against BLAS
- Success threshold: Median end-to-end one-layer decode latency improves by at least 2x versus dense BLAS at <=50% nonzero in two hidden-size regimes, with no worse than 10% regression in overhead-dominated small projections.
- Stop condition: Stop if BLAS plus full-layer overhead reduces ternary speedup below 1.25x at 50% nonzero or if timing variance remains too high after pinning and repeated trials.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-optimized-ternary-residual-transformer-direct-inference-benchmark-f3f3e7fcb252`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
