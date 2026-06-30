# CPU-offloaded sharded optimizer states for tiny-VRAM training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-offloaded-sharded-optimizer-states-for-tiny-vram-training-d61b2530f0f7`
Run ID: `cpu-offloaded-sharded-optimizer-states-for-tiny-vram-training-d61b2530f0f7-20260527T112700982904+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/959c804e3676

## What looked useful

Chunked AdamW matched unchunked AdamW exactly on a correctness check. For 32M synthetic parameters, simple mixed-precision AdamW device-memory accounting fell from 512 MB resident optimizer state to 132 MB offloaded peak device memory, while per-rank CPU update time was 0.111 s at 4 shards and 0.043 s at 8 shards versus 1.293 s unsharded on this CPU worker.

## Boundaries and scale limits

No CUDA/PyTorch stack was available, so this run did not measure real tiny-VRAM GPU training, host-device transfer, distributed collectives, overlap, dataloader effects, model convergence, checkpointing, or GPT-2-small-class workloads. Largest measured proxy was 32M synthetic parameters and 15.4 seconds of CPU-only runtime.

## Claim scope

Bounded CPU-only proxy: chunked AdamW optimizer-state update and memory accounting for 1M to 32M synthetic parameters, with 1, 4, and 8 optimizer-state shards. Supports the mechanism that CPU-offloaded sharded optimizer state can materially reduce peak device-memory accounting while keeping CPU update cost small at this scale.

## Why it stopped

The result is a bounded CPU-only proxy that supports the optimizer-state sharding/offload mechanism but lacks direct GPU/model-training evidence, so it cannot justify a paper-positive decision.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded direct GPU follow-up comparing standard AdamW/FSDP/ZeRO-Offload against this sharded CPU-offload path under an explicit tiny-VRAM memory cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tiny-VRAM GPU validation of sharded CPU-offloaded AdamW state
- Success threshold: Under the same memory cap, the proposed path completes the target training window with no worse final loss trend than the baseline, reduces peak device memory by at least 2x versus resident AdamW accounting, and keeps end-to-end step-time overhead below 25% versus the strongest existing offload baseline.
- Stop condition: Stop if host-device transfer or synchronization makes end-to-end steps more than 50% slower than the strongest existing offload baseline, if memory savings are below 2x, or if loss diverges relative to the matched baseline.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-sharded-optimizer-states-for-tiny-vram-training-d61b2530f0f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
