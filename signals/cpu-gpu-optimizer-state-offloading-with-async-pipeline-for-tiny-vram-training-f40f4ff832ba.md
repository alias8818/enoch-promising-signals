# CPU-GPU optimizer state offloading with async pipeline for tiny-VRAM training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-gpu-optimizer-state-offloading-with-async-pipeline-for-tiny-vram-training-f40f4ff832ba`
Run ID: `cpu-gpu-optimizer-state-offloading-with-async-pipeline-for-tiny-vram-training-f40f4ff832ba-20260608T010109923628+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/87067f92a14c

## What looked useful

CPU-offloaded AdamW moments with async chunk pipelining reduced peak CUDA allocation from 640.0 MiB to 263.5 MiB at 67.1M parameters using 4 MiB of staging, while increasing isolated optimizer-step median time from 12.40 ms to 23.46 ms. Async pipelining was consistently faster than synchronous offload at matched chunk sizes.

## Boundaries and scale limits

No end-to-end training, no real transformer/loss/convergence measurement, no enforced VRAM cap, no comparison against production offload systems, and no fused custom kernel implementation.

## Claim scope

Single-GB10 optimizer-step microbenchmark with one flat fp16 parameter tensor up to 67.1M parameters and synthetic gradients; AdamW moments are stored in pinned CPU memory and streamed through GPU staging buffers.

## Why it stopped

No-paper closure: this run produced useful mechanism evidence but only from a synthetic optimizer-step microbenchmark, not direct model-training validation.

## Recommended next action

Run a bounded transformer training follow-up under an enforced low CUDA-memory budget, using the 256K-1M async chunk range and comparing against GPU AdamW plus a strong existing offload baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Async CPU-offloaded AdamW in low-memory small-transformer training
- Success threshold: Offloaded training completes at a memory point where GPU AdamW cannot fit or must reduce batch/sequence size, with peak CUDA memory at least 35% lower than GPU AdamW and end-to-end throughput no worse than 2.5x for a stable short loss curve.
- Stop condition: Stop if the offloaded run is more than 3x slower end-to-end than GPU AdamW at the same feasible configuration, diverges while the baseline is stable, or fails to reduce peak CUDA memory by at least 25%.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-gpu-optimizer-state-offloading-with-async-pipeline-for-tiny-vram-training-f40f4ff832ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
