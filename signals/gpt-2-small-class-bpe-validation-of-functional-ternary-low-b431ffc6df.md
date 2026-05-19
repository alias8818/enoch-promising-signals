# GPT-2-small-class BPE validation of functional ternary low-rank residual repair

Status: `useful_signal`
Project ID: `gpt-2-small-class-bpe-validation-of-functional-ternary-low-b431ffc6df`
Run ID: `gpt-2-small-class-bpe-validation-of-functional-ternary-low-b431ffc6df-20260519T151746419909+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: GPT-2-small-class BPE validation of functional ternary low-rank residual repair: internal_generated:gpt-2-small-class-bpe-validation-of-functional-ternary-low-b431ffc6df

## What looked useful

Dense SVD residuals recovered about 44-47% of the ternary loss gap but still left validation PPL in the 3.6k-5.1k range versus dense PPL 30.18; ternary-factor low-rank residuals recovered only about 1.6% at rank 16 and worsened at rank 32.

## Boundaries and scale limits

Single pretrained GPT-2-small model, WikiText-2 validation only, inference-time deterministic SVD residuals rather than learned calibration-trained repair, no WikiText-103/test/downstream validation, no larger GPT-2 variants, and no fused efficient ternary/low-rank kernel implementation.

## Claim scope

On GPT-2-small (`gpt2`) with GPT-2 BPE tokens and the full WikiText-2 validation split, deterministic ternary quantization of transformer 2D weights plus local low-rank SVD residual repair did not recover usable language-model perplexity; dense low-rank residuals partially reduced loss, while ternary-factor residuals were near ineffective.

## Why it stopped

Direct full WikiText-2 GPT-2 BPE validation falsified the practical success threshold for deterministic functional ternary low-rank residual repair: best SVD repair remained over 100x dense perplexity and ternary-factor repair barely improved over ternary-only.

## Recommended next action

Stop this deterministic SVD-repair claim as no-paper evidence; only pursue a bounded learned residual repair follow-up if it explicitly targets full WikiText-2 validation PPL recovery with ternary-factor and dense-low-rank controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibration-trained ternary low-rank residual repair for GPT-2-small BPE validation
- Success threshold: On full WikiText-2 validation, ternary base plus learned low-rank residual reaches PPL <= 60, or at minimum recovers >= 90% of the ternary-to-dense loss gap, while the ternary-factor implementation remains within 20% relative PPL of the dense low-rank residual control.
- Stop condition: Stop as negative if after a bounded calibration run of <= 6 GPU-hours the best learned ternary-factor residual remains above PPL 120 or recovers less than 75% of the ternary-to-dense loss gap on full validation.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-bpe-validation-of-functional-ternary-low-b431ffc6df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
