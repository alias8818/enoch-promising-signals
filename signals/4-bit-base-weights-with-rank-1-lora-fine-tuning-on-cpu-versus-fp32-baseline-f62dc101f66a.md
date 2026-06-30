# 4-bit base weights with rank-1 LoRA fine-tuning on CPU versus fp32 baseline

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-base-weights-with-rank-1-lora-fine-tuning-on-cpu-versus-fp32-baseline-f62dc101f66a`
Run ID: `4-bit-base-weights-with-rank-1-lora-fine-tuning-on-cpu-versus-fp32-baseline-f62dc101f66a-20260523T203854810575+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9716dd2a98f5

## What looked useful

In a best-case true rank-1 target update, fp32 rank-1 LoRA reached 7.48e-13 mean test MSE, while q4 base plus rank-1 LoRA remained at 1.36e-2 despite improving frozen q4 by 76.3%. On full-rank target updates, both rank-1 methods barely improved frozen baselines. This suggests rank-1 capacity is consumed by or insufficient for full-rank int4 quantization residuals.

## Boundaries and scale limits

Synthetic linear maps only; no transformer, language modeling, GPT-2-small-class run, real dataset, production int4 kernel, or rank sweep. Three fully trained seeds for the main 2000-step result; five under-trained seeds used only for calibration.

## Claim scope

Bounded CPU linear-adaptation probe: frozen row-wise symmetric int4 base weights plus rank-1 LoRA did not match fp32 full fine-tuning or fp32 rank-1 LoRA on d=128 synthetic matrix adaptation. The result supports a mechanism-level caution, not a transformer-scale claim.

## Why it stopped

Proxy mechanism result, not full validation: the tested q4 rank-1 LoRA configuration failed to match fp32 baselines even when the target update was exactly rank 1, because quantization residual remained after adaptation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should sweep LoRA ranks 1/2/4/8 with group-wise or NF4-style quantization on the same linear probe before attempting a GPT-2-small-class validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rank and quantizer sweep for int4-base LoRA residual correction
- Success threshold: At least one int4 configuration reaches within 10% relative test MSE of the fp32 same-rank LoRA control on low-rank target updates while using at most 25% of fp32 full-finetune weight storage.
- Stop condition: Stop if rank 8 with the best tested quantizer still leaves more than 2x the fp32 same-rank LoRA test MSE or if gains are only from using storage comparable to fp32.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-base-weights-with-rank-1-lora-fine-tuning-on-cpu-versus-fp32-baseline-f62dc101f66a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
