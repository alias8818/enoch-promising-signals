# Medium GPT-2-small-class activation-aware LoRA scaling test

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `medium-gpt-2-small-class-activation-aware-lora-scaling-tes-9fd6c18d27`
Run ID: `medium-gpt-2-small-class-activation-aware-lora-scaling-tes-9fd6c18d27-20260523T022104722964+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Quantized LoRA with Activation-Aware Scaling: enoch://control-plane/projects/quantized-lora-with-activation-aware-scaling-c79b3fc238f5/runs/quantized-lora-with-activation-aware-scaling-c79b3fc238f5-20260522T182128468090+0000
- Parent run decision: Real-transformer activation-aware scaling for quantized LoRA modules: enoch://control-plane/projects/real-transformer-activation-aware-scaling-for-quantized-lo-f136647a5b/runs/real-transformer-activation-aware-scaling-for-quantized-lo-f136647a5b-20260522T213802385703+0000

## What looked useful

In the stronger Tier 2 matrix, standard LoRA reached 0.8811 mean SST-2 validation accuracy across three seeds, activation-aware scaling reached 0.8735, and random scaling reached 0.8781. Activation-aware scaling was worse than standard LoRA on all paired seeds with mean paired delta -0.0076 accuracy, despite using the same 222,722 trainable parameters.

## Boundaries and scale limits

Single task, single GPT-2-small-class model, frozen backbone, rank 4 adapters, one activation-RMS scaling formula, one learning-rate schedule, and local GB10 validation. Results do not rule out learned/adaptive scaling rules, language-modeling targets, higher ranks, other modules, or larger models.

## Claim scope

Frozen GPT-2-small SST-2 classification fine-tuning with rank-4 LoRA adapters on attention c_attn and c_proj, 8192 training examples, 872-example validation, 1000 optimizer steps, seeds 11/17/23. The tested activation-aware rule was a pre-training per-module multiplier (median input RMS / module input RMS) ** 0.5 clipped to [0.5, 2.0].

## Why it stopped

Tier 2 direct fixed-seed evidence with a real standard-LoRA baseline and random-scale ablation does not support the tested activation-aware scaling hypothesis.

## Recommended next action

Stop this branch as no-paper useful negative evidence for this specific activation-RMS LoRA scaling rule; do not escalate without a materially different scaling mechanism or target task.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/medium-gpt-2-small-class-activation-aware-lora-scaling-tes-9fd6c18d27`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
