# Dynamic Quantization Granularity for CPU Inference Latency Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-quantization-granularity-for-cpu-inference-latency-reduction-bbab1ef86846`
Run ID: `dynamic-quantization-granularity-for-cpu-inference-latency-reduction-bbab1ef86846-20260611T163250751709+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4ab3cbe94cf3

## What looked useful

Dynamic top-5% fine rows beat uniform group-64 on 3/4 synthetic layers with median 1.155x speedup versus group-64 and median relative RMSE 0.0120, close to group-64 at 0.0111 and better than row-wise at 0.0160. It beat row-wise int8 on only 1/4 layers and FP32 on 0/4 layers.

## Boundaries and scale limits

No real transformer model, no end-to-end generation, no optimized production int8 GEMM backend, and no downstream task-quality metric. NumPy int32 matmul made every int8 path slower than FP32, so this does not support a real serving latency claim.

## Claim scope

Synthetic NumPy CPU linear-inference benchmark with prepacked int8 weights: dynamic row selection for group-64 quantization can reduce latency versus uniformly fine group-64 quantization on most tested batch-style layers while keeping relative RMSE near the group-64 result.

## Why it stopped

Early bounded synthetic test produced a mixed mechanism signal but failed to establish CPU inference latency reduction versus strong baselines; this is not full validation and not paper-ready.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded test should implement the same dynamic policy inside an optimized CPU int8 backend and compare against row-wise int8, dynamic quantization, and FP32 on real transformer linear layers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized CPU int8 backend test for dynamic quantization granularity
- Success threshold: At least 1.10x median latency improvement versus the best non-dynamic int8 baseline on a majority of real transformer layer shapes, no regression versus FP32 where int8 is expected to win, and less than 2% relative model-quality degradation versus the best fixed-granularity quantized baseline.
- Stop condition: Stop if dynamic packing fails to beat per-row int8 by at least 5% on two representative real transformer layer families or if model-level quality is worse than uniform group-wise quantization without a latency advantage.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-quantization-granularity-for-cpu-inference-latency-reduction-bbab1ef86846`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
