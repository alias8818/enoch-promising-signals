# Nonlinear residual predictor optimized for direct cache-substitution fidelity

Status: `useful_signal`
Project ID: `nonlinear-residual-predictor-optimized-for-direct-cache-su-dd938b3461`
Run ID: `nonlinear-residual-predictor-optimized-for-direct-cache-su-dd938b3461-20260514T185251701431+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Nonlinear residual predictor optimized for direct cache-substitution fidelity: internal_generated:nonlinear-residual-predictor-optimized-for-direct-cache-su-dd938b3461

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct target validation with real GPT-2-small/WikiText-2 substitution, controls, three fixed full seeds, and a direct-objective ablation missed the strict KL threshold; mechanism support is not publication readiness.

## Recommended next action

Stop this run as no-paper: bounded direct GPT-2-small validation found a real nonlinear-vs-linear gain, but KL drift stayed around 0.067 nats/token versus the 0.02 direct-fidelity threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layerwise and multi-layer direct-fidelity residual substitutes
- Success threshold: At least one substitution setting must achieve KL <= 0.02 nats/token and CE delta <= 0.02 across at least three fixed seeds while materially outperforming the linear predictor and trivial controls.
- Stop condition: Stop if all tested layers remain above KL 0.02 or if direct-KL optimization fails to improve held-out KL by at least 25% over the MSE-trained nonlinear predictor.

## Evidence references

- Artifact root: `<local-path>/projects/nonlinear-residual-predictor-optimized-for-direct-cache-su-dd938b3461`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
