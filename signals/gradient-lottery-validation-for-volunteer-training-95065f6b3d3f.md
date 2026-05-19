# Gradient Lottery Validation for Volunteer Training

Status: `useful_signal`
Project ID: `gradient-lottery-validation-for-volunteer-training-95065f6b3d3f`
Run ID: `gradient-lottery-validation-for-volunteer-training-95065f6b3d3f-20260519T055734004880+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f1d01a04c256

## What looked useful

High-gradient volunteer examples often concentrated mislabeled or contradictory samples. Across 180 paired full-run comparisons, gradient lottery trailed random by 0.1711 mean accuracy with approximate 95% CI [-0.2030, -0.1391]; under clean labels it was indistinguishable from random, while under 20-40% label noise it trailed random by 0.2575 mean accuracy.

## Boundaries and scale limits

Tested only linear softmax models on sklearn digits, sklearn breast_cancer, and one synthetic imbalanced dataset with random label-noise proxies; did not test real human volunteers, correlated annotation errors, deep models, language-model training, or large-scale distributed training.

## Claim scope

Bounded local classification tests show that naive gradient-norm-proportional volunteer-example sampling does not improve over random selection on clean volunteer labels and fails badly when volunteer labels are noisy.

## Why it stopped

Proxy/local early falsification rather than full validation: the selector was directly tested under matched-budget local classification controls and failed the success criterion of beating random volunteer selection.

## Recommended next action

Stop the naive gradient-norm lottery line as no-paper evidence; if continuing, test a noise-robust gradient utility that discounts suspected mislabeled volunteer examples.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noise-robust gradient lottery for volunteer selection
- Success threshold: Noise-robust gradient lottery must beat random by at least +0.02 mean accuracy with a 95% paired CI excluding zero across the noisy-label subset, while not underperforming random on clean-label comparisons.
- Stop condition: Stop if the robust selector does not beat random on the noisy-label subset or if gains disappear on clean-label controls.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-lottery-validation-for-volunteer-training-95065f6b3d3f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
