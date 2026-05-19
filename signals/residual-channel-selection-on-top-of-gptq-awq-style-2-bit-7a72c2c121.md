# Residual-channel selection on top of GPTQ/AWQ-style 2-bit quantization

Status: `useful_signal`
Project ID: `residual-channel-selection-on-top-of-gptq-awq-style-2-bit-7a72c2c121`
Run ID: `residual-channel-selection-on-top-of-gptq-awq-style-2-bit-7a72c2c121-20260516T090102951376+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Residual-channel selection on top of GPTQ/AWQ-style 2-bit quantization: internal_generated:residual-channel-selection-on-top-of-gptq-awq-style-2-bit-7a72c2c121

## What looked useful

AWQ-style residual selection was the best tested method, reducing mean PPL from 15320.6 for plain 2-bit to 4360.1 at 3.125% residual channels, but dense GPT-2 was 35.7 PPL; even 25% residual channels had 1277.5 PPL.

## Boundaries and scale limits

Tested one pretrained 124M-parameter GPT-2 model, WikiText-2 validation, 245280 evaluated tokens, 64 calibration windows, and a GPTQ/AWQ-style local implementation rather than a mature production GPTQ or AWQ stack on 7B+ models.

## Claim scope

On GPT-2 small with WikiText-2 validation, groupwise 2-bit quantization plus selected residual input channels shows a measurable mechanism benefit over plain 2-bit and random residual controls, but does not recover usable language-model perplexity at residual budgets from 1.5625% to 25%.

## Why it stopped

Direct GPT-2/WikiText-2 target metrics with fixed seeds, real baselines, and residual controls show a mechanism signal but decisively miss paper-readiness quality thresholds.

## Recommended next action

Stop this depth-4 follow-up as no-paper evidence; do not chain another follow-up unless a separate project starts from a mature GPTQ/AWQ implementation and predefines a memory-adjusted success threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-selection-on-top-of-gptq-awq-style-2-bit-7a72c2c121`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
