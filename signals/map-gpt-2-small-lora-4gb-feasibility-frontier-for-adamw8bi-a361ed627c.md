# Map GPT-2-small LoRA 4GB feasibility frontier for AdamW8bit versus AdamW

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `48`
Project ID: `map-gpt-2-small-lora-4gb-feasibility-frontier-for-adamw8bi-a361ed627c`
Run ID: `map-gpt-2-small-lora-4gb-feasibility-frontier-for-adamw8bi-a361ed627c-20260621T060043082305+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `48`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Pretrained GPT-2-small LoRA+AdamW8bit under strict 4GB memory: enoch://control-plane/projects/pretrained-gpt-2-small-lora-adamw8bit-under-strict-4gb-mem-e32c64e631/runs/pretrained-gpt-2-small-lora-adamw8bit-under-strict-4gb-mem-e32c64e631-20260621T053933365747+0000
- Parent run decision: LoRA + 8-bit AdamW for Sub-4GB VRAM Fine-tuning: enoch://control-plane/projects/lora-8-bit-adamw-for-sub-4gb-vram-fine-tuning-b100bd0e32f0/runs/lora-8-bit-adamw-for-sub-4gb-vram-fine-tuning-b100bd0e32f0-20260621T052142131213+0000

## What looked useful

AdamW8bit reduced LoRA optimizer state from 3.09/12.38/24.75 MiB to 1.67/3.28/6.43 MiB at ranks 4/16/32, but every rank/sequence cell had the same max successful micro-batch and same first OOM batch as AdamW.

## Boundaries and scale limits

The run used synthetic token batches and measured memory feasibility only. It did not test downstream quality, pretrained checkpoint behavior, gradient checkpointing, quantized base weights, full fine-tuning, or a discrete 4 GiB GPU.

## Claim scope

On a GB10 host using a 4 GiB PyTorch CUDA allocator cap, GPT-2-small-class frozen-base LoRA training with ranks 4, 16, and 32 at sequence lengths 128, 256, and 512 had identical feasible micro-batch frontiers for torch.optim.AdamW and bitsandbytes AdamW8bit.

## Why it stopped

Direct medium sweep falsified a frontier gain for AdamW8bit in GPT-2-small LoRA under the tested 4 GiB cap.

## Recommended next action

Stop this no-paper branch; only open a distinct follow-up if testing full fine-tuning or another setting where optimizer state is a dominant memory term.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/map-gpt-2-small-lora-4gb-feasibility-frontier-for-adamw8bi-a361ed627c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
