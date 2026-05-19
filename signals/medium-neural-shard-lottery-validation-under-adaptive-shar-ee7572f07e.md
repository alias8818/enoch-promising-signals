# Medium neural shard-lottery validation under adaptive shard corruptions

Status: `useful_signal`
Project ID: `medium-neural-shard-lottery-validation-under-adaptive-shar-ee7572f07e`
Run ID: `medium-neural-shard-lottery-validation-under-adaptive-shar-ee7572f07e-20260518T220833579058+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Medium neural shard-lottery validation under adaptive shard corruptions: internal_generated:medium-neural-shard-lottery-validation-under-adaptive-shar-ee7572f07e

## What looked useful

All-shard aggregation was brittle when an adaptive attacker could drive a few high-margin shard outputs toward the same wrong class; subset aggregation preserved nonzero accuracy at higher corruption budgets. The lottery-specific mechanism was not isolated because deterministic fixed-subset aggregation matched lottery accuracy within about 0-2 percentage points.

## Boundaries and scale limits

Small real dataset, small MLP shards, output-level corruption only, no large-model training, no parameter-level shard compromise, and no routing-knowledge ablation beyond fixed subset versus random lottery.

## Claim scope

On sklearn digits with 9 small neural shards, 5 fixed seeds, and adaptive per-example shard-output corruptions, random 3-shard lottery aggregation outperformed all-shard aggregation at corruption budgets 2-4 but did not meaningfully outperform a deterministic fixed 3-shard subset.

## Why it stopped

Tier 2 evidence is mixed: the shard subset idea has useful robustness signal versus all-shard aggregation, but lottery randomness itself is not separated from a fixed-subset control and clean accuracy trails the dense neural baseline.

## Recommended next action

Stop this run as no-paper evidence; if deepening, run a routing-knowledge ablation comparing hidden lottery, revealed lottery, fixed subset, and all-shard aggregation with matched clean accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Routing-knowledge ablation for neural shard lottery robustness
- Success threshold: Hidden lottery beats both fixed-subset and revealed-routing controls by at least 5 absolute percentage points at budgets 1-3 while losing no more than 2 absolute percentage points clean accuracy versus the best matched shard control.
- Stop condition: Stop if hidden lottery is within 2 percentage points of fixed-subset/revealed controls or if clean-accuracy matching cannot be achieved without making the shard pool much larger than the dense baseline.

## Evidence references

- Artifact root: `<local-path>/projects/medium-neural-shard-lottery-validation-under-adaptive-shar-ee7572f07e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
