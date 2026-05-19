# Nonlinear shared-gradient proxy verifier confirmation

Status: `useful_signal`
Project ID: `nonlinear-shared-gradient-proxy-verifier-confirmation-15238b296a`
Run ID: `nonlinear-shared-gradient-proxy-verifier-confirmation-15238b296a-20260517T191643277215+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Nonlinear shared-gradient proxy verifier confirmation: internal_generated:nonlinear-shared-gradient-proxy-verifier-confirmation-15238b296a

## What looked useful

Shared-gradient proxy features contain real verifier signal for candidate update selection, but the nonlinear verifier claim is not confirmed because linear/logistic shared-gradient baselines match or outperform it on rank, AUROC, and top-k selection metrics.

## Boundaries and scale limits

Evidence is limited to sklearn digits, a small MLP, one-step SGD candidate selection, 5 fixed seeds, and 6,720 candidate-step evaluations. It is not a language-model, long-horizon curriculum, or large-scale training validation.

## Claim scope

On a local digits MLP candidate-step verifier task, shared-gradient features predict direct one-step validation-loss improvement better than loss-only, random, shuffled-target, and no-gradient controls, but nonlinear shared-gradient verifiers do not beat simpler linear/logistic shared-gradient baselines.

## Why it stopped

Tier 2 local confirmation produced mixed mechanism support but negative evidence for nonlinear superiority over real shared-gradient baselines.

## Recommended next action

Stop this nonlinear confirmation as no-paper evidence; branch to a harder direct training-efficiency test of linear/logistic shared-gradient verifiers against exact-gradient and loss-only selectors.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Linear shared-gradient verifier downstream training-efficiency test
- Success threshold: Across at least 5 fixed seeds, the linear/logistic shared-gradient selector improves final validation loss or area-under-learning-curve by at least 5% over loss-only and random controls, while reaching at least 80% of exact-gradient selector gain at lower measured compute cost.
- Stop condition: Stop if the shared-gradient selector fails to beat loss-only/random controls on downstream validation trajectory in 3 or more of 5 seeds, or if exact-gradient cost savings disappear after measuring feature extraction overhead.

## Evidence references

- Artifact root: `<local-path>/projects/nonlinear-shared-gradient-proxy-verifier-confirmation-15238b296a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
