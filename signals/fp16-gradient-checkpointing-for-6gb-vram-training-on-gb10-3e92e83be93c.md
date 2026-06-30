# FP16 Gradient Checkpointing for 6GB VRAM Training on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `fp16-gradient-checkpointing-for-6gb-vram-training-on-gb10-3e92e83be93c`
Run ID: `fp16-gradient-checkpointing-for-6gb-vram-training-on-gb10-3e92e83be93c-20260605T142008715595+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4368a712410f

## What looked useful

Checkpointing reduced peak allocation from 2.31 GB to 1.18 GB at batch 4 sequence 1024, and turned batch 8 sequence 2048 from baseline OOM at about 5.92 GB allocated into a successful run at 2.86 GB max allocated. Batch 16 sequence 2048 also completed with checkpointing near the 6 GiB reserved-memory boundary.

## Boundaries and scale limits

Evidence is synthetic, short-run, and uses an artificial allocator cap on a GB10 UMA system rather than a physical 6 GB discrete GPU. It does not validate real data training, long-run convergence, production optimizer settings, or larger models.

## Claim scope

On GB10 with PyTorch 2.12/CUDA 13, a synthetic GPT-like 12-layer 768-hidden FP16 transformer training step under a 6 GiB CUDA allocator cap was feasible with per-block activation checkpointing at shapes where the non-checkpointed baseline OOMed.

## Why it stopped

The result is useful but proxy-limited: it demonstrates the memory mechanism in a synthetic short run under an artificial 6 GiB allocator cap, not a full validation on a real 6 GB training workload.

## Recommended next action

Stop this run as bounded no-paper evidence; deepen with a real GPT-2-small-class model/data pipeline and include optimizer/microbatching controls before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real GPT-2-small FP16 checkpointing under a 6 GiB cap
- Success threshold: Checkpointed FP16 training completes at least one shape that the non-checkpointed baseline OOMs under the 6 GiB cap, with finite loss for 100 steps and no increasing peak-memory trend after warmup.
- Stop condition: Stop if the real model cannot reproduce a checkpointing-enabled OOM-to-success transition under the cap, or if finite-loss training requires changes that dominate the memory effect being tested.

## Evidence references

- Artifact root: `<local-path>/projects/fp16-gradient-checkpointing-for-6gb-vram-training-on-gb10-3e92e83be93c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
