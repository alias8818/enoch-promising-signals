# Pretrained GPT-2-small real-corpus checkpointing stability under a 6 GiB cap

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pretrained-gpt-2-small-real-corpus-checkpointing-stability-de271b6148`
Run ID: `pretrained-gpt-2-small-real-corpus-checkpointing-stability-de271b6148-20260605T204237815896+0000`

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

- Parent run decision: Real GPT-2-small FP16 checkpointing under a 6 GiB cap: enoch://control-plane/projects/real-gpt-2-small-fp16-checkpointing-under-a-6-gib-cap-8d4e50a996/runs/real-gpt-2-small-fp16-checkpointing-under-a-6-gib-cap-8d4e50a996-20260605T181709489490+0000
- Parent run decision: FP16 Gradient Checkpointing for 6GB VRAM Training on GB10: enoch://control-plane/projects/fp16-gradient-checkpointing-for-6gb-vram-training-on-gb10-3e92e83be93c/runs/fp16-gradient-checkpointing-for-6gb-vram-training-on-gb10-3e92e83be93c-20260605T142008715595+0000

## What looked useful

Medium local confirmation supports exact checkpoint/resume stability for a bounded GPT-2-small/WikiText-2 regime under 6 GiB, while a longer-context stress probe suggests memory savings from non-reentrant checkpointing and warns that bitwise identity can become context-sensitive.

## Boundaries and scale limits

Local single-GPU GB10 evidence only; no long-horizon training, no near-OOM batch sweep, no mixed precision, no scheduler/dataloader randomness, no distributed training, and only one seed for the 1024-token stress probe.

## Claim scope

Pretrained GPT-2-small fine-tuning on WikiText-2 under a 6 GiB CUDA process cap was checkpoint/resume stable for 18-step, 128-token, batch-1 runs across seeds 11, 22, and 33, matching a no-gradient-checkpointing baseline and two activation-checkpointing ablations exactly at the final state. A one-seed 1024-token stress probe stayed within cap and showed lower CUDA allocation for non-reentrant checkpointing, but exact bitwise resume identity did not hold at that longer context despite negligible loss drift.

## Why it stopped

No-paper useful signal: Tier 2 direct evidence is reproducible but too scoped for publication-grade claims, and the 1024-token stress probe makes exact stability context-sensitive.

## Recommended next action

Run a bounded deepen follow-up that sweeps sequence length and batch size toward the 6 GiB cap across the same three seeds, recording memory headroom and resume drift thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small checkpoint/resume stability near the 6 GiB memory boundary
- Success threshold: For at least one configuration with baseline peak CUDA allocation >= 5.5 GiB or baseline OOM under the 6 GiB cap, checkpointed training must complete with >= 10% lower peak CUDA allocation and resumed/uninterrupted eval-loss delta <= 1e-5 across all three seeds.
- Stop condition: Stop if checkpointed modes fail to reduce peak CUDA allocation by at least 10% near the cap, if resume drift exceeds the predefined tolerance on two or more seeds, or if no configuration can be driven above 5.5 GiB without changing the model class.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-gpt-2-small-real-corpus-checkpointing-stability-de271b6148`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
