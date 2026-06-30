# FP16-specific residual channel sensitivity with matched FP32 and perturbation controls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fp16-specific-residual-channel-sensitivity-with-matched-fp-b61f10a5f2`
Run ID: `fp16-specific-residual-channel-sensitivity-with-matched-fp-b61f10a5f2-20260528T164914054452+0000`

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

- Parent run decision: Outlier-Channel Residual: FP16 for High-Variance Activation Channels at 2-bit: enoch://control-plane/projects/outlier-channel-residual-fp16-for-high-variance-activation-channels-at-2-bit-023d78bcac1a/runs/outlier-channel-residual-fp16-for-high-variance-activation-channels-at-2-bit-023d78bcac1a-20260528T102153376612+0000
- Parent run decision: Layerwise perplexity validation for high-variance FP16 residual activation channels: enoch://control-plane/projects/layerwise-perplexity-validation-for-high-variance-fp16-res-417d82248b/runs/layerwise-perplexity-validation-for-high-variance-fp16-res-417d82248b-20260528T141243989736+0000

## What looked useful

The FP16 numerical pathway is measurably more perturbation-sensitive than matched FP32 in this bounded setup, but the proposed discrepancy-ranked residual channel mechanism fails against random-channel controls.

## Boundaries and scale limits

Single pretrained GPT-2-small baseline, one dataset split, inference-only perturbations at transformer block outputs, 3 fixed random-control seeds, 2 perturbation magnitudes; no training dynamics, model-family sweep, long-context test, or 7B-class validation.

## Claim scope

On GPT-2-small inference over 96 WikiText-2 test windows, residual-channel perturbations produce larger loss effects in FP16 than FP32, but channels selected by normalized FP16-vs-FP32 residual activation discrepancy do not show greater FP16-specific loss excess than same-layer random channels.

## Why it stopped

Medium fixed-seed direct perturbation evidence with a real GPT-2-small baseline and FP32, random-channel, zero-hook, and perturbation-magnitude controls did not support the channel-specific hypothesis.

## Recommended next action

Stop this branch as no-paper evidence; if continuing, test whether the observed FP16 excess is a global precision/quantization effect rather than a channel-specific residual-discrepancy mechanism.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Global FP16 residual perturbation sensitivity versus activation quantization controls
- Success threshold: A precision-format or quantization condition explains at least 75% of the FP16-specific excess variance across seed-layer-magnitude aggregates and beats discrepancy-ranking by a paired effect size of at least 2x.
- Stop condition: Stop if BF16/activation-quantized controls do not reproduce the FP16 excess or if precision-format effects are not larger than random-channel variability across fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/fp16-specific-residual-channel-sensitivity-with-matched-fp-b61f10a5f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
