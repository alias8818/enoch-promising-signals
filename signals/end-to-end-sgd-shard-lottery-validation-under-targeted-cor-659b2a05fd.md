# End-to-end SGD shard-lottery validation under targeted corruptions

Status: `useful_signal`
Project ID: `end-to-end-sgd-shard-lottery-validation-under-targeted-cor-659b2a05fd`
Run ID: `end-to-end-sgd-shard-lottery-validation-under-targeted-cor-659b2a05fd-20260518T220305782978+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9941cbfc3334

## What looked useful

At 40% targeted corrupted shards, shard_lottery_val improved test accuracy over random_shard_sgd by 18.35 percentage points on average across 12 paired seeds, won all 12 pairs, selected corrupted shards only 0.84% of steps, and matched its clean-control accuracy within 0.05 percentage points. At 20% targeted corruption it improved accuracy by 2.25 points and selected corrupted shards 0.23% of steps.

## Boundaries and scale limits

Tested only on synthetic binary classification with a linear model, 12 paired seeds, 5,000 train examples, 1,000 SGD steps, 20 shards, and up to 40% corrupted shards; not tested on deep networks, real datasets, adaptive validation-aware attacks, distributed systems overhead, or GPT-2-small-class training.

## Claim scope

In a controlled synthetic logistic-regression SGD task with 20 training shards, full-shard label-flip corruptions, and a trusted clean validation set, a validation-scored shard-lottery update rule rejected most corrupted shards and preserved clean-test accuracy relative to uniform random-shard SGD.

## Why it stopped

Useful Tier 1 mechanism support, but not paper-positive because the evidence is limited to a small synthetic logistic-regression setting with a trusted validation set assumption.

## Recommended next action

Run a medium direct confirmation on a real dataset and small neural model with matched update budgets, wall-clock overhead accounting, clean-validation ablations, and an adaptive corruption that tries to pass the validation scorer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium neural shard-lottery validation under adaptive shard corruptions
- Success threshold: Across at least 10 paired seeds at 40% corrupted shards, lottery accuracy exceeds random-shard SGD by at least 10 percentage points, corrupted-shard selections are below 20% of steps, clean-control degradation is below 3 percentage points, and overhead-adjusted accuracy remains positive versus a time-matched random-shard baseline.
- Stop condition: Stop as negative if lottery loses the 10 percentage point advantage at 40% corruption, selects corrupted shards at or above half their population fraction, or its clean-control/overhead cost erases the robustness benefit.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-sgd-shard-lottery-validation-under-targeted-cor-659b2a05fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
