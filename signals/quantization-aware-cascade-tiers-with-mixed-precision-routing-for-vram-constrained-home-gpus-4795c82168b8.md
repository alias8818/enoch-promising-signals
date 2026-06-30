# Quantization-Aware Cascade Tiers with Mixed-Precision Routing for VRAM-Constrained Home GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantization-aware-cascade-tiers-with-mixed-precision-routing-for-vram-constrained-home-gpus-4795c82168b8`
Run ID: `quantization-aware-cascade-tiers-with-mixed-precision-routing-for-vram-constrained-home-gpus-4795c82168b8-20260607T104641194976+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2fe9114ac6a6

## What looked useful

Routing preserved fp16-level accuracy across three seeds while routing a mean 98.68% of examples to int4, but a resident same-model int4+int8+fp16 cascade requires 1.75x fp16 weight memory, so it is not a VRAM-saving design unless the high-precision tier is offloaded or on-demand.

## Boundaries and scale limits

Three small synthetic seeds only; no native low-bit kernels, no transformer/KV-cache measurement, no offload/load latency, and no real home-GPU VRAM pressure beyond analytical weight accounting.

## Claim scope

Synthetic CUDA MLP benchmark with simulated int4/int8/fp16 weight tiers and confidence-margin routing; evaluates router accuracy preservation and weight-memory accounting, not real LLM serving.

## Why it stopped

Proxy evidence supports the router mechanism but early-falsifies the resident same-model VRAM-saving claim; this is not a full validation of LLM serving.

## Recommended next action

Stop this run as a proxy useful signal; a follow-up should test a small real transformer with native quantization and measured resident versus offloaded tier memory/latency under a fixed VRAM cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Native transformer cascade with resident-low and offloaded-high precision tiers
- Success threshold: Cascade improves quality by at least 50% of the gap between int4-only and fp16 while staying under the VRAM cap and adding less than 25% p95 latency versus int4-only.
- Stop condition: Stop if resident memory exceeds the cap, fp16 fallback is required for more than 10% of requests, or p95 latency exceeds int4-only by more than 50% without a commensurate quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-aware-cascade-tiers-with-mixed-precision-routing-for-vram-constrained-home-gpus-479`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
