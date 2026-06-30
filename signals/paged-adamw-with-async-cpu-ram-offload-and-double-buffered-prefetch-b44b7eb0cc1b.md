# Paged AdamW with async CPU-RAM offload and double-buffered prefetch

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `paged-adamw-with-async-cpu-ram-offload-and-double-buffered-prefetch-b44b7eb0cc1b`
Run ID: `paged-adamw-with-async-cpu-ram-offload-and-double-buffered-prefetch-b44b7eb0cc1b-20260614T095313460719+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8e64d1d89fb2

## What looked useful

Double-buffered offload was consistently faster than synchronous offload in the 64M page sweep and reached 94.57 ms steady-state at 256M/1M pages versus 121.70 ms for synchronous offload and 96.98 ms for this script's GPU-full flat update.

## Boundaries and scale limits

Synthetic optimizer-step only; no real model, backward pass, convergence, mixed precision, parameter groups, checkpointing, dataloader, or memory-near-capacity training run. Largest direct test was 256M float32 flattened parameters for 5 optimizer steps.

## Claim scope

On GB10 with PyTorch 2.12/CUDA 13, a synthetic flattened AdamW optimizer-step benchmark showed that CPU-RAM-resident moments can be paged through CUDA staging buffers with double-buffered prefetch, matching bounded update checksums and improving over synchronous offload across tested page sizes.

## Why it stopped

Evidence is a bounded synthetic optimizer-step validation, not direct end-to-end model training validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the optimizer into a small real training loop and require matched throughput, memory, and loss-curve evidence before paper consideration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real training-loop validation for double-buffered CPU-offloaded AdamW
- Success threshold: Double-buffered offload matches loss within 2% of GPU-resident AdamW over the probe and stays within 20% tokens/sec overhead while reducing CUDA-resident optimizer-state memory by at least 50%.
- Stop condition: Stop as negative if integration overhead exceeds 40% tokens/sec, loss diverges under matched hyperparameters, or memory telemetry does not show optimizer-state offload.

## Evidence references

- Artifact root: `<local-path>/projects/paged-adamw-with-async-cpu-ram-offload-and-double-buffered-prefetch-b44b7eb0cc1b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
