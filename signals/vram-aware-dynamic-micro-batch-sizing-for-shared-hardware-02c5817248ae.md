# VRAM-Aware Dynamic Micro-Batch Sizing for Shared Hardware

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `vram-aware-dynamic-micro-batch-sizing-for-shared-hardware-02c5817248ae`
Run ID: `vram-aware-dynamic-micro-batch-sizing-for-shared-hardware-02c5817248ae-20260521T221825863972+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/712b6525b03c

## What looked useful

Across 30 deterministic synthetic traces of 2000 steps each, the dynamic policy achieved 94.29 mean samples/s with 0.0 mean OOMs, versus 24.26 samples/s and 1660.23 OOMs for fixed micro-batch 16 and 18.96 samples/s and 1854.47 OOMs for fixed micro-batch 32.

## Boundaries and scale limits

No direct CUDA allocator telemetry, no real GPU, no model training, no convergence measurement, no distributed workload, and no datacenter-scale shared-hardware validation. Throughput ratios are simulator-specific.

## Claim scope

CPU-only synthetic shared-VRAM trace simulation shows a VRAM-aware dynamic micro-batch policy can avoid synthetic OOMs and improve simulated throughput versus fixed micro-batch baselines under volatile co-tenant memory pressure.

## Why it stopped

No-paper closure: this run provides a useful synthetic proxy signal but not direct GPU evidence or publication-grade validation.

## Recommended next action

Run a bounded direct-GPU validation on a single shared CUDA host using live memory telemetry, fixed and retry-on-OOM baselines, and a small real transformer workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Single-GPU Live Telemetry Validation of VRAM-Aware Micro-Batching
- Success threshold: Dynamic policy has at least 80% fewer OOM events than the best fixed baseline and no more than 5% lower tokens/s than the fastest non-crashing baseline over at least 30 minutes of real GPU workload.
- Stop condition: Stop if dynamic policy either still OOMs frequently under telemetry control or loses more than 15% tokens/s versus a stable fixed baseline after tuning one safety-margin parameter.

## Evidence references

- Artifact root: `<local-path>/projects/vram-aware-dynamic-micro-batch-sizing-for-shared-hardware-02c5817248ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
