# Selective FFN-Only Gradient Checkpointing for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `selective-ffn-only-gradient-checkpointing-for-tiny-vram-training-bd4ed53c98d5`
Run ID: `selective-ffn-only-gradient-checkpointing-for-tiny-vram-training-bd4ed53c98d5-20260521T222325445256+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/712b6525b03c

## What looked useful

Primary run: FFN-only retained 57.5% of baseline saved-tensor bytes at 1.096x step time; full-block retained 30.0% at 1.139x step time. FFN-mult-8 ablation: FFN-only retained 41.1% at 1.057x step time; full-block retained 21.4% at 1.122x step time. CPU RSS was flat or worse for checkpointing.

## Boundaries and scale limits

No direct GPU VRAM, tiny-VRAM OOM boundary, mixed precision, real dataset, or GPT-2-small-class training run was tested. Results are short synthetic CPU runs with 2-6 layer toy models.

## Claim scope

CPU-local PyTorch proxy on toy GPT-style transformers: FFN-only activation checkpointing reduced autograd saved-tensor retention versus no checkpointing and had lower step-time overhead than full-block checkpointing, but did not reduce sampled CPU RSS.

## Why it stopped

Closed as no-paper useful signal because the local evidence supports the saved-activation mechanism but only proxies the tiny-VRAM claim and CPU RSS did not show practical memory relief.

## Recommended next action

Run a bounded direct CUDA/UMA follow-up that measures maximum batch/sequence before OOM and tokens/s for none, FFN-only, and full-block checkpointing on a GPT-2-small-class model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tiny-VRAM OOM-boundary test for FFN-only checkpointing
- Success threshold: FFN-only must raise the no-checkpoint maximum batch or sequence capacity by at least 25% while retaining at least 90% of full-block checkpointing throughput, or it must match full-block capacity with at least 10% better throughput.
- Stop condition: Stop if FFN-only fails to improve the no-checkpoint OOM boundary by at least 10% on two constrained-memory configurations or if its throughput is no better than full-block checkpointing.

## Evidence references

- Artifact root: `<local-path>/projects/selective-ffn-only-gradient-checkpointing-for-tiny-vram-training-bd4ed53c98d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
