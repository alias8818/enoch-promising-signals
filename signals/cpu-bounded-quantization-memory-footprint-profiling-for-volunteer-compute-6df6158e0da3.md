# CPU-Bounded Quantization Memory Footprint Profiling for Volunteer Compute

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-bounded-quantization-memory-footprint-profiling-for-volunteer-compute-6df6158e0da3`
Run ID: `cpu-bounded-quantization-memory-footprint-profiling-for-volunteer-compute-6df6158e0da3-20260609T133210115640+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1ef4e8652a3f

## What looked useful

For an 8192x8192 layer, fp32 direct peaked at 301.8 MiB and 29.6 effective GFLOP/s; int8 full dequant stored 64.0 MiB but peaked at 621.4 MiB and 3.55 GFLOP/s; int8 tiled peaked at 136.7 MiB and 1.85 GFLOP/s; packed int4 tiled peaked at 119.0 MiB and 1.03 GFLOP/s.

## Boundaries and scale limits

Synthetic Gaussian weights and activations only; no real model checkpoint, no optimized GGUF/llama.cpp quantized kernel, no end-to-end generation, no accuracy or perplexity validation, and only one CPU host.

## Claim scope

On this CPU-only worker, synthetic linear-layer profiling showed that int8 and packed int4 storage reduce resident weight footprint, full int8 dequantization can exceed fp32 peak RSS, and tiled dequantization preserves peak-memory savings at substantial CPU throughput cost.

## Why it stopped

Bounded synthetic profiling is sufficient to expose the memory-versus-CPU mechanism, but it is proxy evidence rather than full validation on real models or optimized kernels.

## Recommended next action

Stop this run as no-paper useful signal; next run should profile real optimized CPU quantized inference kernels with identical RSS telemetry before making any broader volunteer-compute claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Peak-RSS and throughput profiling for real CPU GGUF quantized inference kernels
- Success threshold: A real quantized kernel should reduce peak RSS by at least 2x versus fp32/fp16 while retaining at least 25% of baseline token throughput, or demonstrate that fp32/fp16 cannot fit where quantized inference can run.
- Stop condition: Stop if optimized quantized kernels still require full dequantization peak memory comparable to fp32/fp16, or if throughput falls below 10% of baseline on both tested model sizes.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-bounded-quantization-memory-footprint-profiling-for-volunteer-compute-6df6158e0da3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
