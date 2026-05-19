# Adaptive exact anchors with learned cross-layer KV residual prediction

Status: `useful_signal`
Project ID: `adaptive-exact-anchors-with-learned-cross-layer-kv-residua-ebc41d5055`
Run ID: `adaptive-exact-anchors-with-learned-cross-layer-kv-residua-ebc41d5055-20260514T183126697393+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b94336eb2cb6

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct small GPT-2 and DistilGPT2 cache-substitution tests failed the success threshold: learned residuals improved cache NMSE but recovered only about 15-17% of the zero-fill loss penalty under uniform anchors, and adaptive anchors were worse than uniform at the same exact-layer budget.

## Recommended next action

Stop this run as a direct Tier 1 threshold failure; if continuing, run one bounded deepen test with behavior-aware residual predictors optimized for continuation KL/loss rather than cache MSE.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Behavior-aware learned KV residual prediction for exact-anchor cache substitution
- Success threshold: Adaptive behavior-aware learned residual prediction has loss_delta_vs_exact <= uniform learned and recovery_vs_zero_excess >= 0.50, with first-step KL no worse than zero-fill, on GPT-2-small-class held-out continuations.
- Stop condition: Stop if behavior-aware training still recovers <50% of the zero-fill loss penalty or if adaptive anchors remain worse than uniform under the same exact-anchor budget.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-exact-anchors-with-learned-cross-layer-kv-residua-ebc41d5055`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
