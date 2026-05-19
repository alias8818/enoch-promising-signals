# Behavior-aware learned KV residual prediction for exact-anchor cache substitution

Status: `compute_scale_blocked`
Project ID: `behavior-aware-learned-kv-residual-prediction-for-exact-an-b76f7664e0`
Run ID: `behavior-aware-learned-kv-residual-prediction-for-exact-an-b76f7664e0-20260514T184136929523+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Behavior-aware learned KV residual prediction for exact-anchor cache substitution: internal_generated:behavior-aware-learned-kv-residual-prediction-for-exact-an-b76f7664e0

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 direct cache-substitution tests on distilgpt2/WikiText-2 showed consistent mechanism support but large remaining behavior drift: stride 4 behavior-aware delta CE 1.2308 and KL 1.3632; stride 2 delta CE 0.9371 and KL 1.0874 versus exact cache.

## Recommended next action

Stop this linear behavior-aware residual predictor as not paper-ready; only deepen with a nonlinear predictor if it can target direct cache-substitution KL and CE thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Nonlinear residual predictor optimized for direct cache-substitution fidelity
- Success threshold: At anchor stride 2 or 4, behavior-aware nonlinear predictor must achieve mean delta CE <= 0.2, mean KL <= 0.2, top-1 agreement >= 0.8 versus exact cache, and a clear improvement over the linear behavior-aware baseline across at least three fixed seeds.
- Stop condition: Stop if a smoke plus one medium fixed-seed run cannot beat delta CE 0.5 and KL 0.5, or if predictor overhead eliminates the cache/throughput benefit.

## Evidence references

- Artifact root: `<local-path>/projects/behavior-aware-learned-kv-residual-prediction-for-exact-an-b76f7664e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
