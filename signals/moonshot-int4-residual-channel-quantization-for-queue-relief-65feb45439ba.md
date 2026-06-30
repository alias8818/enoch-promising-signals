# Moonshot: INT4 Residual-Channel Quantization for Queue Relief

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `moonshot-int4-residual-channel-quantization-for-queue-relief-65feb45439ba`
Run ID: `moonshot-int4-residual-channel-quantization-for-queue-relief-65feb45439ba-20260610T150337716494+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a766a379b386

## What looked useful

The isolated queue-relief mechanism exists because prepacked INT4 copies fewer bytes, but conversion overhead dominates the saved copy time by roughly 10x to 16x in the tested implementation, making the practical hypothesis unsupported without a much faster fused kernel.

## Boundaries and scale limits

Synthetic tensor proxy only; no full model-serving queue, no transformer loss/accuracy measurement, no fused CUDA/Triton INT4 kernel, and no datacenter-scale workload.

## Claim scope

On NVIDIA GB10 with PyTorch eager CUDA kernels and synthetic residual tensors up to 8192x4096, prepacked INT4 reduces queue payload copy latency, but end-to-end per-channel INT4 quantize-copy-dequantize is 9.28x to 12.24x slower than a simple FP16 queue copy and introduces about 15% to 16% relative RMSE.

## Why it stopped

Proxy early falsification: the direct queue payload copy improved, but end-to-end INT4 residual-channel conversion overhead was 9.28x to 12.24x slower than FP16 copy at the tested shapes, so this is not a paper-ready validation.

## Recommended next action

Stop this run as a proxy early falsification of the straightforward implementation; only revisit with a fused CUDA/Triton pack-dequant path integrated at a real queue boundary and a model-quality metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused INT4 Residual Queue Kernel at a Real Consumer Boundary
- Success threshold: Static or dynamic fused INT4 end-to-end queue path is at least 1.25x faster than FP16/BF16 queue baseline at 4096x4096 and 8192x4096 while keeping downstream loss or perplexity regression at or below 1%.
- Stop condition: Stop if fused conversion remains more than 2x slower than the FP16/BF16 queue baseline or if model-quality regression exceeds 1% at the smallest tested model/block scale.

## Evidence references

- Artifact root: `<local-path>/projects/moonshot-int4-residual-channel-quantization-for-queue-relief-65feb45439ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
