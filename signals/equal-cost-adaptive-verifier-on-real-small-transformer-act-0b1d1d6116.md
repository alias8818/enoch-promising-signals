# Equal-cost adaptive verifier on real small-transformer activation replay

Status: `useful_signal`
Project ID: `equal-cost-adaptive-verifier-on-real-small-transformer-act-0b1d1d6116`
Run ID: `equal-cost-adaptive-verifier-on-real-small-transformer-act-0b1d1d6116-20260517T182923382404+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Equal-cost adaptive verifier on real small-transformer activation replay: internal_generated:equal-cost-adaptive-verifier-on-real-small-transformer-act-0b1d1d6116

## What looked useful

Real activations add signal over random, shuffled-label, and permuted-hidden controls, but the tested adaptive activation verifier is weaker than a cheap uncertainty-only verifier at the same verification budgets.

## Boundaries and scale limits

One small transformer model, one validation corpus, 4,391 held-out token decisions, 8,000 training tokens per seed, and oracle correction potential rather than an actual larger verifier model.

## Claim scope

On GPT-2-small activation replay from Wikitext-2 validation text, a linear activation-based adaptive verifier learned a real error-detection signal but did not outperform equal-cost uncertainty-only baselines for selecting next-token errors.

## Why it stopped

Tier 2 medium confirmation found mechanism support but failed the central equal-cost baseline comparison; this is not a full validation and not paper-positive.

## Recommended next action

Stop this branch as no-paper evidence unless a bounded residual/nonlinear activation verifier is tested against uncertainty-only baselines with actual verifier-model correction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual nonlinear activation verifier with actual verifier-model correction
- Success threshold: Across fixed seeds, the residual activation verifier must beat uncertainty-only logistic by at least +0.01 AUPRC and +0.02 Precision@10%, and improve realized corrected-token accuracy under the same verification budget.
- Stop condition: Stop if the residual activation verifier fails to beat uncertainty-only logistic on Precision@10% or realized correction accuracy on either real text split.

## Evidence references

- Artifact root: `<local-path>/projects/equal-cost-adaptive-verifier-on-real-small-transformer-act-0b1d1d6116`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
