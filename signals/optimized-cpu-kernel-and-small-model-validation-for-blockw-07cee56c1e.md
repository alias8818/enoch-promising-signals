# Optimized CPU kernel and small-model validation for blockwise int8 weight-only inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `optimized-cpu-kernel-and-small-model-validation-for-blockw-07cee56c1e`
Run ID: `optimized-cpu-kernel-and-small-model-validation-for-blockw-07cee56c1e-20260604T090416404511+0000`

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

- Parent run decision: Blockwise Int8 Weight Quantization for CPU Inference: enoch://control-plane/projects/blockwise-int8-weight-quantization-for-cpu-inference-43a9e14255e0/runs/blockwise-int8-weight-quantization-for-cpu-inference-43a9e14255e0-20260604T040904314754+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d1eff6718125

## What looked useful

Blockwise int8 weight-only GEMV preserved relative RMS output error below 0.41% and accelerated MLP/large projection shapes by 2.53x-4.48x while reducing weight storage by about 3.56x for block size 32, but the 768x768 attention projection reached only 1.20x with block size 32 and 1.00x with block size 64, below the stated 1.25x latency threshold for uniform small-model benefit.

## Boundaries and scale limits

No end-to-end decoder model, no real-token perplexity/logit validation, no multi-thread serving test, and no validation on modern VNNI/AMX-class CPUs. Results cover batch-1 GEMV-shaped linear layers only.

## Claim scope

Single-thread CPU Tier 1 direct GEMV benchmark for deterministic blockwise int8 weight-only linear layers on GPT-2-small-class and medium-like dimensions on an AVX-512BW Xeon Silver 4114 without AVX-512 VNNI.

## Why it stopped

Controlled direct kernel evidence is mixed: numerical accuracy and MLP speedups support the mechanism, but a core 768x768 projection case misses the latency threshold and end-to-end model validation was not performed.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up that integrates the kernel into a tiny or GPT-2-small-class decoder block and measures real-token logit drift plus batch-1 decode latency against an optimized FP32 baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small decoder validation for blockwise int8 CPU weight-only inference
- Success threshold: Relative logit RMS drift below 1% or perplexity increase below 2%, plus at least 1.25x end-to-end batch-1 decode speedup over FP32 with no individual core projection layer slower than 0.9x.
- Stop condition: Stop if end-to-end decode speedup is below 1.1x, quality drift exceeds the tolerance, or layer timing shows projection overhead dominates MLP gains.

## Evidence references

- Artifact root: `<local-path>/projects/optimized-cpu-kernel-and-small-model-validation-for-blockw-07cee56c1e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
