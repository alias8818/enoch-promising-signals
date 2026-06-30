# Bounded-Error Residual Channels for Mixed-Precision CPU Kernels

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-error-residual-channels-for-mixed-precision-cpu-kernels-abae73109dc4`
Run ID: `bounded-error-residual-channels-for-mixed-precision-cpu-kernels-abae73109dc4-20260529T134632711686+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/396d993366fb

## What looked useful

Residual side channels provide a reproducible accuracy mechanism for mixed-precision CPU kernels, but the current evidence is not paper-ready because performance competitiveness was only measured in a prototype implementation.

## Boundaries and scale limits

Prototype scalar C++ kernels only; synthetic uniform/cancellation/heavy-tail data; no production SIMD/cache-blocked implementation, real workload traces, hardware-counter profiling, or optimized library baseline.

## Claim scope

In deterministic synthetic GEMV-like CPU dot products, an int8 primary channel plus first-order int8 residual channels reduced RMSE by 41.8x to 236.4x across the main single-thread matrix, with zero observed violations of the computed omitted second-order error bound.

## Why it stopped

Closed as useful no-paper evidence: local synthetic tests support the numerical mechanism, but production-kernel evidence is required before a paper claim.

## Recommended next action

Run a bounded deepen follow-up implementing AVX2/AVX-512 cache-blocked residual-channel GEMV with per-block scales and fair optimized int8/fp32 baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SIMD Cache-Blocked Residual-Channel GEMV
- Success threshold: Median first-order RMSE improvement >= 40x over int8-only and median runtime overhead <= 1.5x versus optimized int8 on at least three medium workloads, with zero omitted-bound violations.
- Stop condition: Stop if SIMD/cache-blocked residual overhead exceeds 2x on two workloads or if omitted-bound violations appear under the implemented decomposition.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-error-residual-channels-for-mixed-precision-cpu-kernels-abae73109dc4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
