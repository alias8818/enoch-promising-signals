# Pseudo-4-bit QAT During GPT-2-Small Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pseudo-4-bit-qat-during-gpt-2-small-pretraining-b191be90eedf`
Run ID: `pseudo-4-bit-qat-during-gpt-2-small-pretraining-b191be90eedf-20260531T201830932980+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8d9c62e110b1

## What looked useful

Weight-only pseudo-4-bit QAT was close to the floating-point control (+0.00665 paired validation loss, about +0.10% relative) but 5.4% slower. W4A4 pseudo-QAT from step 1 had a larger paired validation-loss penalty (+0.07658, about +1.18% relative) and was 10.0% slower. All variants were numerically stable.

## Boundaries and scale limits

Not full GPT-2-small scale, not long pretraining, not a broad corpus, and not packed int4 deployment. The tested model used 6 layers, width 384, 6 heads, sequence length 128, 409,600 training tokens per run, and three seeds.

## Claim scope

In a 30M-parameter GPT-style decoder trained from scratch for 400 steps on Wikitext-2, immediate pseudo-4-bit weight-only fake-quantization of linear layers remained trainable with a small validation-loss penalty versus a floating-point control, while immediate pseudo-4-bit weight-plus-activation fake-quantization consistently worsened early validation loss.

## Why it stopped

The result is a bounded small-model early-pretraining signal, not a full GPT-2-small validation or a paper-ready result.

## Recommended next action

Stop this run as a no-paper useful signal; if another bounded budget is assigned, test delayed activation quantization plus groupwise or per-channel scaling against the same floating-point and W4 controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Delayed and Groupwise W4A4 QAT for Early GPT-Style Pretraining
- Success threshold: Delayed/groupwise W4A4 mean paired validation-loss delta versus floating point is <= 0.02 with no divergence and less than 15% throughput overhead in the bounded run.
- Stop condition: Stop if delayed/groupwise W4A4 remains worse than floating point by >0.05 validation loss after the planned token budget or shows repeated instability in any seed.

## Evidence references

- Artifact root: `<local-path>/projects/pseudo-4-bit-qat-during-gpt-2-small-pretraining-b191be90eedf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
