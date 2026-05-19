# GPT-2 Scale Token-Superposition Pretraining Reproduction

Status: `compute_scale_blocked`
Project ID: `gpt-2-scale-token-superposition-pretraining-reproduction-ce453cf42b1f`
Run ID: `gpt-2-scale-token-superposition-pretraining-reproduction-ce453cf42b1f-20260514T105827219356+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Efficient Pre-Training with Token Superposition: https://arxiv.org/abs/2605.06546
- Token Superposition for Long-Context Anchor Compression: https://arxiv.org/abs/2605.06546

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy evidence supports the TST mechanism at tiny character-LM scale but does not directly reproduce the GPT-2-scale pretraining claim or provide publication-grade validation.

## Recommended next action

Stop this worker run as a proxy-only non-paper result; run a bounded GPT-2-small-class deepen follow-up with BPE data and profiler-backed compute accounting if more evidence is desired.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class Token-Superposition Training reproduction with BPE corpus and compute profiling
- Success threshold: TST must match or beat baseline validation CE by at least 0.01 at matched wall time or measured compute while preserving a throughput advantage of at least 1.3x during the superposition phase.
- Stop condition: Stop if TST remains worse than baseline by more than 0.03 validation CE after a recovery budget equal to the measured time saved by the superposition phase, or if profiler data shows no material compute advantage.

## Evidence references

- Artifact root: `<control-plane-state>/projects/gpt-2-scale-token-superposition-pretraining-reproduction-ce453cf42b1f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
