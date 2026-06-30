# GPT-2-small LoRA validation for 8-bit SGDM momentum

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-small-lora-validation-for-8-bit-sgdm-momentum-4c41f1bec2`
Run ID: `gpt-2-small-lora-validation-for-8-bit-sgdm-momentum-4c41f1bec2-20260526T015841048628+0000`

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
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/51320b64bd65

## What looked useful

8-bit SGDM momentum preserved GPT-2-small LoRA training quality in this bounded direct test: mean final validation loss was 5.5193 for 8-bit momentum versus 5.5210 for FP32 momentum, and all three paired seed differences stayed within the 0.05 Tier-1 equivalence threshold. Quantization error remained small, with max absolute final logged momentum error 6.46e-4.

## Boundaries and scale limits

Small dataset, 240-step runs, one LoRA rank, one learning-rate/momentum setting, per-tensor quantization, non-fused Python optimizer, and no demonstrated wall-clock or end-to-end memory advantage. The result does not validate long-horizon persistence, broader corpora, production implementation speed, or larger model classes.

## Claim scope

In a Tier-1 controlled direct test, GPT-2-small with frozen base weights and 1.18M LoRA trainable parameters trained on Tiny Shakespeare for 240 steps across three paired seeds. A per-tensor int8 SGDM momentum implementation matched FP32 SGDM momentum on final validation loss within 0.0113 max absolute paired loss difference.

## Why it stopped

No-paper useful signal: the small direct test supports the mechanism but is not robust enough for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with a longer GPT-2-small LoRA schedule on a second language-modeling dataset and explicit optimizer-state memory accounting before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer GPT-2-small LoRA persistence test for 8-bit SGDM momentum
- Success threshold: 8-bit momentum final validation loss is within 0.05 of FP32 SGDM for every paired seed, mean validation-loss improvement is not worse by more than 0.05 loss, no persistent validation-loss spikes occur after checkpoints, and measured optimizer momentum state memory is at least 3x smaller than FP32 momentum.
- Stop condition: Stop as negative if any paired seed diverges, if final validation loss is worse than FP32 by more than 0.05, if loss spikes persist for two consecutive validation checkpoints, or if optimizer-state memory accounting fails to show a meaningful momentum-buffer reduction.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-lora-validation-for-8-bit-sgdm-momentum-4c41f1bec2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
