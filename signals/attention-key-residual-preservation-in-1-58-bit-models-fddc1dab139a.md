# Attention-Key Residual Preservation in 1.58-bit Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `attention-key-residual-preservation-in-1-58-bit-models-fddc1dab139a`
Run ID: `attention-key-residual-preservation-in-1-58-bit-models-fddc1dab139a-20260521T224320231799+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/130c0d3912f4

## What looked useful

Key residuals reduced GPT-2 attention-map MSE versus fully ternary from 0.002383 to 0.001577 and recovered 26.9% of the loss gap with 7.08M residual weights. Equal-size V residuals slightly beat K on perplexity/loss, while K was clearly better than Q/O for both attention MSE and loss recovery.

## Boundaries and scale limits

No quantization-aware training, no native 1.58-bit training, one pretrained GPT-2 model, one fixed local corpus, one seed, and short evaluation only. The synthetic training task failed to produce a strong dense associative-recall model, so it was not used as positive evidence.

## Claim scope

Bounded post-training proxy: on pretrained GPT-2 with Conv1D weights ternarized to a 1.58-bit-style {-1,0,1} codebook, restoring only attention-key residuals best preserved dense attention maps among equal-size Q/K/V/O residual controls, but did not uniquely optimize language-model loss.

## Why it stopped

Evidence is proxy-only post-training quantization plus an inconclusive toy-training probe; it supports a mechanism signal but not a publication-grade or native 1.58-bit-model claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should directly train or fine-tune a small 1.58-bit GPT-2-class model with matched K/Q/V residual budgets on a public corpus and require both loss and attention-preservation wins before paper consideration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched-budget K/Q/V residuals during 1.58-bit GPT-2-small training
- Success threshold: K residuals must beat fully ternary by at least 10% relative loss-gap recovery and beat every equal-budget Q/V/O residual control on attention-map MSE, while matching or beating them on validation loss in at least two of three seeds.
- Stop condition: Stop if the dense/quantized training baseline cannot reach a usable validation loss, or if K residuals do not outperform equal-budget V/Q/O controls on attention drift and validation loss after the planned small-model budget.

## Evidence references

- Artifact root: `<local-path>/projects/attention-key-residual-preservation-in-1-58-bit-models-fddc1dab139a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
