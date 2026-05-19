# Small Transformer Confirmation for Hybrid Spectral Adam

Status: `useful_signal`
Project ID: `small-transformer-confirmation-for-hybrid-spectral-adam-a484f816b0`
Run ID: `small-transformer-confirmation-for-hybrid-spectral-adam-a484f816b0-20260518T090346439865+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Small Transformer Confirmation for Hybrid Spectral Adam: internal_generated:small-transformer-confirmation-for-hybrid-spectral-adam-a484f816b0

## What looked useful

Direct small-Transformer evidence supports second-moment-only spectral compression with row/column residuals: rank 8 reached median val-loss ratio 1.0335 at 56.7% state, rank 16 reached 1.0264 at 62.5% state, and the spectral-only residual ablation diverged on all seeds. The exact SVD prototype was about 14x slower than AdamW, so the result is mechanism support rather than a practical optimizer claim.

## Boundaries and scale limits

One small character-level Transformer, one corpus, short 700-step training horizon, exact per-step SVD prototype, no GPT-2-small-class model, no mixed precision, no distributed/sharded state, and no practical randomized or fused SVD implementation.

## Claim scope

On a 234k-parameter Tiny Shakespeare character Transformer trained for 700 steps across seeds 0, 1, and 2, Hybrid Spectral AdamW with dense first moments and rank-8 or rank-16 spectral plus row/column residual second moments preserved validation loss within 1.05x AdamW while using 56.7% to 62.5% of dense AdamW optimizer-state elements.

## Why it stopped

Tier 2 direct evidence supports the bounded mechanism, but exact per-step SVD is far too slow and the validation is too narrow for a paper-ready claim.

## Recommended next action

Implement a randomized or periodic SVD Hybrid AdamW variant and rerun the same fixed-seed Transformer benchmark, requiring <=65% state, <=1.05x AdamW validation loss, and <=2x AdamW step-time overhead before considering larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Practical Randomized-SVD Hybrid Spectral AdamW on Small Transformers
- Success threshold: Median validation loss <=1.05x AdamW, stored optimizer-state elements <=65% of AdamW, no divergent seeds, and mean steps/sec at least 50% of AdamW on the same benchmark.
- Stop condition: Stop if the practical SVD variant exceeds 1.05x AdamW median validation loss, diverges on any seed, exceeds 65% optimizer-state elements, or remains slower than 0.5x AdamW after bounded implementation effort.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-confirmation-for-hybrid-spectral-adam-a484f816b0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
