# Direct Small/Large LM Entropy Cascade Evaluation

Status: `compute_scale_blocked`
Project ID: `direct-small-large-lm-entropy-cascade-evaluation-12393790f2`
Run ID: `direct-small-large-lm-entropy-cascade-evaluation-12393790f2-20260514T153246768084+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/406d9f2e6535

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 direct token-level evidence supports the entropy-cascade mechanism, but this is not publication-grade validation and does not measure task accuracy, robustness, or end-to-end serving cost.

## Recommended next action

Run a medium confirmation with multiple datasets, at least two small/large model pairs, repeated random-routing controls, held-out threshold calibration, and measured cascade latency before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Confirmation of Small/Large LM Entropy Cascade Routing
- Success threshold: Entropy routing beats random routing by at least 0.05 NLL at 20%, 40%, and 60% large-call budgets on at least two datasets and preserves at least half of the large-only NLL improvement over small-only while reducing measured large-model calls.
- Stop condition: Stop if entropy routing fails to beat random by 0.05 NLL at two or more tested large-call budgets on the first two datasets or if measured cascade overhead erases the intended serving-cost reduction.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-large-lm-entropy-cascade-evaluation-12393790f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
