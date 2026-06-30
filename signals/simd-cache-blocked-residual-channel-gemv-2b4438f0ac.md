# SIMD Cache-Blocked Residual-Channel GEMV

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `simd-cache-blocked-residual-channel-gemv-2b4438f0ac`
Run ID: `simd-cache-blocked-residual-channel-gemv-2b4438f0ac-20260529T214550903724+0000`

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

- Parent run decision: Bounded-Error Residual Channels for Mixed-Precision CPU Kernels: enoch://control-plane/projects/bounded-error-residual-channels-for-mixed-precision-cpu-kernels-abae73109dc4/runs/bounded-error-residual-channels-for-mixed-precision-cpu-kernels-abae73109dc4-20260529T134632711686+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/396d993366fb

## What looked useful

The direct benchmark supports a narrow tiny-residual mechanism but falsifies the broader cache-blocked residual-channel GEMV idea as a general speedup: blocked masked won for 2 of 9 shapes and lost badly for larger M because it rescans x and accesses packed columns inefficiently across output blocks.

## Boundaries and scale limits

Single CPU model, FP32 only, single-threaded microbenchmark, synthetic dense matrices, no quantization, no production inference runtime, no batching, no NUMA or prefetch tuning.

## Claim scope

On one Intel Xeon Silver 4114 AVX-512 CPU, a cache-blocked masked FP32 GEMV kernel helps only for tiny residual output-channel counts (M=17 and M=31) and is not a viable general residual-channel GEMV replacement for M=33 through M=513 in the tested shapes.

## Why it stopped

Tier 1 direct CPU GEMV evidence is mixed and insufficient for a paper: the proposed blocked residual-channel kernel only wins in tiny M cases and fails as M grows.

## Recommended next action

Stop this broad kernel direction as no-paper evidence; if continuing, test a hybrid tail-only residual kernel that is invoked only for the final 1-31 output channels after a stronger main GEMV baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Tail-Only Residual GEMV Kernel
- Success threshold: At least 1.15x end-to-end speedup over the best current baseline for three or more residual-tail sizes, with no more than 2% slowdown on non-tiny M shapes.
- Stop condition: Stop if the hybrid tail-only path fails to exceed 1.05x on isolated residual tails or introduces more than 2% end-to-end slowdown on two representative non-tiny M shapes.

## Evidence references

- Artifact root: `<local-path>/projects/simd-cache-blocked-residual-channel-gemv-2b4438f0ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
