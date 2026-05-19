# Medium Confirmation of Activation-Selected Residual Channels for Whole-Model Sub-2bit Quantization

Status: `useful_signal`
Project ID: `medium-confirmation-of-activation-selected-residual-channe-8da773aa9f`
Run ID: `medium-confirmation-of-activation-selected-residual-channe-8da773aa9f-20260516T084002935679+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Medium Confirmation of Activation-Selected Residual Channels for Whole-Model Sub-2bit Quantization: internal_generated:medium-confirmation-of-activation-selected-residual-channe-8da773aa9f

## What looked useful

Activation-selected residual channels had the best equal-bit loss at both 5% and 10% residual budgets: 9.6498 loss at 1.416 bpp and 9.7708 loss at 1.808 bpp, versus fp16 loss 4.0256 and no-residual binary loss 10.5436.

## Boundaries and scale limits

Single 82M-parameter distilgpt2-class model, Wikitext-2 only, simple row-wise binary quantization with fp16 residuals/scales, no GPTQ/AWQ-class quantizer, no larger LLMs, no packed-kernel runtime validation.

## Claim scope

On pretrained distilgpt2 evaluated on 65,408 Wikitext-2 tokens, activation-selected residual projection channels improve sub-2-bit binary whole-model quantization relative to equal-bit random and weight-magnitude residual controls, but the resulting perplexity remains unusably far from fp16.

## Why it stopped

Medium direct validation supports the channel-selection mechanism but falsifies practical paper readiness under a simple whole-model sub-2-bit binary quantizer because perplexity remains above 15000 versus 56 for fp16.

## Recommended next action

Stop this branch as no-paper evidence; run one bounded follow-up combining activation-selected residual channels with a GPTQ/AWQ-style error-aware 2-bit baseline and an embedding-aware policy on GPT-2-small-class models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-selected residual channels with error-aware 2-bit quantization
- Success threshold: At sub-2.0 estimated bits per parameter, activation-selected residuals improve validation loss by at least 0.2 versus the best equal-bit control and keep perplexity within 2x of the error-aware no-residual 2-bit baseline on at least two fixed seeds.
- Stop condition: Stop if activation-selected residuals fail to beat the best equal-bit control by 0.1 loss or if all sub-2-bit conditions remain catastrophically degraded relative to the error-aware 2-bit baseline.

## Evidence references

- Artifact root: `<local-path>/projects/medium-confirmation-of-activation-selected-residual-channe-8da773aa9f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
