# Real-text convergence validation for GPT-2-small factored Adam floor 128

Status: `useful_signal`
Project ID: `real-text-convergence-validation-for-gpt-2-small-factored-f2435c231e`
Run ID: `real-text-convergence-validation-for-gpt-2-small-factored-f2435c231e-20260516T074612576038+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Real-text convergence validation for GPT-2-small factored Adam floor 128: internal_generated:real-text-convergence-validation-for-gpt-2-small-factored-f2435c231e

## What looked useful

Factored AdamW with floor 128 activated on 50 GPT-2-small tensors and reduced optimizer state from 990.80 MB to 496.68 MB, but it consistently lagged AdamW by mean +0.186 best validation loss across seeds 1, 2, and 3. A floor-999999 no-factor ablation matched AdamW on seed 1, localizing the gap to second-moment factorization.

## Boundaries and scale limits

This is direct real-text early-training evidence over 1.23M tokens per run, not long-horizon convergence, larger-corpus pretraining, final perplexity at convergence, or publication-grade robustness across hyperparameter sweeps.

## Claim scope

GPT-2-small-shaped 123.85M parameter causal language model trained from scratch on Wikitext-2 raw text for 600 optimizer steps per seed with GPT-2 tokenization, batch size 8, sequence length 256, AdamW baseline, and a custom full-second-moment optimizer ablation.

## Why it stopped

Direct real-text GPT-2-small evidence showed stable memory savings but a consistent AdamW convergence deficit; the result is useful but not Tier-4 paper-ready, and the controller follow-up depth is already 4.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful signal; do not advance to paper unless a separate owner explicitly reruns a longer direct GPT-2-small real-text training study with a predefined AdamW-parity threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-text-convergence-validation-for-gpt-2-small-factored-f2435c231e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
