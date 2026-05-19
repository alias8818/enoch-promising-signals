# Medium Real-Task Repeated vs One-Shot Hidden Volunteer Gradient Validation

Status: `useful_signal`
Project ID: `medium-real-task-repeated-vs-one-shot-hidden-volunteer-gra-0dd61c3177`
Run ID: `medium-real-task-repeated-vs-one-shot-hidden-volunteer-gra-0dd61c3177-20260518T050804155201+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Medium Real-Task Repeated vs One-Shot Hidden Volunteer Gradient Validation: internal_generated:medium-real-task-repeated-vs-one-shot-hidden-volunteer-gra-0dd61c3177

## What looked useful

Repeated hidden-volunteer gradients carry real label-aligned signal: at 20 repeats, repeated same volunteers beat one-shot same volunteers by +0.0057 accuracy across 40 seeds and beat shuffled-label reuse by +0.5211. However, repeated reuse lost to fresh one-shot equal-presentation volunteers by -0.0197 and showed overfitting as support accuracy saturated.

## Boundaries and scale limits

Single small real dataset, linear model only, no human feedback loop, no larger vision/NLP task, no nonlinear adapter, and no source-to-target distribution shift beyond the controlled train/test split.

## Claim scope

On sklearn digits with a deterministic linear classifier, 30 fixed hidden-volunteer examples reused for gradient adaptation improve held-out accuracy over one-shot use of the same volunteers, but do not beat fresh one-shot volunteers with equal gradient-example presentations or the supervised source-plus-volunteer baseline.

## Why it stopped

Medium real-task validation found a useful mechanism signal but falsified the stronger claim against a real budget-matched fresh-volunteer baseline.

## Recommended next action

Stop paper path for this run; run one bounded deepen follow-up only if testing whether nonlinear adapters and constrained fresh-volunteer availability change the repeated-vs-fresh tradeoff.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Nonlinear Adapter Hidden-Volunteer Repetition Under Fresh-Volunteer Scarcity
- Success threshold: Repeated same-volunteer adaptation must beat one-shot same volunteers by at least 1 percentage point and be statistically indistinguishable from or better than the fresh-volunteer baseline under a predeclared realistic collection budget, without a declining held-out curve as volunteer accuracy saturates.
- Stop condition: Stop if repeated reuse loses to fresh-volunteer baselines by at least 1 percentage point on average or if held-out accuracy declines after volunteer accuracy saturates across two repeat-count settings.

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-task-repeated-vs-one-shot-hidden-volunteer-gra-0dd61c3177`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
