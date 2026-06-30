# Longer GPT-2-small LoRA persistence test for 8-bit SGDM momentum

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `longer-gpt-2-small-lora-persistence-test-for-8-bit-sgdm-mo-5c80a550a7`
Run ID: `longer-gpt-2-small-lora-persistence-test-for-8-bit-sgdm-mo-5c80a550a7-20260526T145031375379+0000`

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

- Parent run decision: 8-bit SGDM for LoRA Fine-tuning: enoch://control-plane/projects/8-bit-sgdm-for-lora-fine-tuning-dd0c0d2cd7ae/runs/8-bit-sgdm-for-lora-fine-tuning-dd0c0d2cd7ae-20260525T142810930123+0000
- Parent run decision: GPT-2-small LoRA validation for 8-bit SGDM momentum: enoch://control-plane/projects/gpt-2-small-lora-validation-for-8-bit-sgdm-momentum-4c41f1bec2/runs/gpt-2-small-lora-validation-for-8-bit-sgdm-momentum-4c41f1bec2-20260526T015841048628+0000

## What looked useful

Persisting quantized 8-bit SGDM momentum across resume appears mechanically useful for LoRA training: checkpoint reload was exact for LoRA weights, int8 momentum used 442,752 bytes vs 1,769,472 fp32 bytes, and the reset ablation was worse on every seed.

## Boundaries and scale limits

Single small real-text corpus, GPT-2-small only, 160 training steps, one LoRA rank, one learning rate/momentum setting, no AdamW baseline, no larger or instruction-tuning datasets, and no long-horizon stability or hyperparameter robustness sweep.

## Claim scope

On GPT-2-small LoRA rank-8 attention fine-tuning over tiny Shakespeare for 160 steps and three fixed seeds, per-tensor int8 SGDM momentum persisted across checkpoint/resume preserved a 4x momentum-state memory reduction, stayed within +0.0026 mean validation loss of fp32 SGDM, and outperformed a momentum-reset ablation by 0.0117 mean validation loss.

## Why it stopped

Medium local validation supports the mechanism but is too narrow and short for publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded deepen follow-up should run longer multi-dataset GPT-2-small LoRA experiments with AdamW/SGDM baselines before any paper gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer multi-dataset GPT-2-small LoRA validation for persisted 8-bit SGDM momentum
- Success threshold: Persisted int8 SGDM mean validation loss within +0.01 of fp32 SGDM, better than reset ablation on at least 80% of seed/dataset pairs, and at least 3.5x lower momentum-state memory.
- Stop condition: Stop if persisted int8 SGDM is worse than fp32 SGDM by more than 0.03 mean validation loss on either dataset or fails to beat reset on a majority of seed/dataset pairs.

## Evidence references

- Artifact root: `<local-path>/projects/longer-gpt-2-small-lora-persistence-test-for-8-bit-sgdm-mo-5c80a550a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
