# Bounded full-scale commit-reveal replay auditing on a realistic large-model optimizer trace

Status: `compute_scale_blocked`
Project ID: `bounded-full-scale-commit-reveal-replay-auditing-on-a-real-3eddb3740f`
Run ID: `bounded-full-scale-commit-reveal-replay-auditing-on-a-real-3eddb3740f-20260515T005536794583+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Bounded full-scale commit-reveal replay auditing on a realistic large-model optimizer trace: internal_generated:bounded-full-scale-commit-reveal-replay-auditing-on-a-real-3eddb3740f

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded full-scale simulator evidence was produced, including full replay and clean controls, but the validation did not use a real training optimizer trace or distributed commitment/reveal integration.

## Recommended next action

Stop this run as no-paper: the mechanism is supported on a bounded 1B-parameter synthetic AdamW optimizer trace, but paper-grade closure requires an integrated audit on a real model-training trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated commit-reveal audit on a real GPT-2-small training optimizer trace
- Success threshold: On at least one real GPT-2-small-class training trace with fixed seeds, sampled replay at 12.5% must achieve approximately 8x auditor replay speedup versus full replay, zero clean-control false positives, and observed tamper detection consistent with at least 95% analytic detection probability for the declared attack density.
- Stop condition: Stop if trainer integration cannot persist deterministic commitments, if clean controls produce any unexplained mismatch, or if sampled replay overhead fails to scale within 20% of the requested sample fraction.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-full-scale-commit-reveal-replay-auditing-on-a-real-3eddb3740f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
