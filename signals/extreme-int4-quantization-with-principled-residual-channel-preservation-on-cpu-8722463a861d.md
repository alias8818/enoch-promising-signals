# Extreme INT4 Quantization with Principled Residual Channel Preservation on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-on-cpu-8722463a861d`
Run ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-on-cpu-8722463a861d-20260607T233251985998+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/3b3ec81cde58

## What looked useful

Across 9 medium synthetic cases, preserving 0.5% to 8% of input channels reduced median relative MSE from 0.083962 to 0.081946-0.071113 while retaining estimated 7.82x-6.41x compression versus FP32. Small-budget principled selectors recovered planted outlier channels with median hit rate 1.0, but residual computation cost about 1.4x-1.6x FP32/dequantized-proxy latency.

## Boundaries and scale limits

No real transformer weights, calibration traces, perplexity/task metrics, packed INT4 CPU kernel, or end-to-end serving benchmark were tested. Timings use NumPy BLAS with dequantized weights and a separate residual GEMM, so they are a proxy for CPU implementation cost, not production INT4 throughput.

## Claim scope

Bounded synthetic CPU proxy: INT4 per-output-channel linear-layer quantization with residual input-channel preservation on heavy-tailed 1024 x 1024 layers. Principled contribution/quant-error selection improves reconstruction error versus all-INT4 and random residual selection at matched residual budgets, but the naive CPU residual implementation is slower than the dequantized INT4 proxy.

## Why it stopped

Proxy evidence supports the selection mechanism but not a practical CPU inference claim; the result is not publication-grade without real-model quality metrics and a packed or fused CPU INT4 implementation.

## Recommended next action

Stop this run as no-paper useful signal; next concrete test is a bounded fused CPU INT4 kernel prototype on real model layer traces to see whether the residual-channel mechanism can keep the error gains without the separate-GEMM latency penalty.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU INT4 Residual-Channel Kernel on Real Layer Traces
- Success threshold: At 1%-4% residual channels, reduce layer relative MSE by at least 10% versus all-INT4, keep compression at least 6.5x versus FP32, and keep fused residual-kernel latency within 1.10x of all-INT4 and below FP32 on the tested CPU.
- Stop condition: Stop if the fused residual path remains more than 1.10x slower than all-INT4 at every tested residual budget or if real-model perplexity/task metrics do not improve over all-INT4 at matched storage.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int4-quantization-with-principled-residual-channel-preservation-on-cpu-8722463a861d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
