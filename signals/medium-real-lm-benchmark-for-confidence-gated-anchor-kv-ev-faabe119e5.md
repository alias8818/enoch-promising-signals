# Medium real-LM benchmark for confidence-gated anchor KV eviction

Status: `useful_signal`
Project ID: `medium-real-lm-benchmark-for-confidence-gated-anchor-kv-ev-faabe119e5`
Run ID: `medium-real-lm-benchmark-for-confidence-gated-anchor-kv-ev-faabe119e5-20260515T063122587585+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Medium real-LM benchmark for confidence-gated anchor KV eviction: internal_generated:medium-real-lm-benchmark-for-confidence-gated-anchor-kv-ev-faabe119e5

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct GPT-2-small/WikiText-2 fixed-seed evidence shows confidence anchors beat sliding and random anchors, but a matched low-confidence-anchor control is far closer to full-cache perplexity, so the stated confidence-gated mechanism is not supported for publication.

## Recommended next action

Stop the confidence-gated anchor KV eviction claim as not paper-worthy; branch only to a bounded uncertainty-gated anchor benchmark if the controller wants to pursue the stronger low-confidence control result.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Uncertainty-gated anchor KV eviction across real LMs and cache budgets
- Success threshold: Uncertainty-gated anchors must beat sliding, random, and confidence anchors in mean NLL delta on every model/dataset/budget family and retain at least 95% of the full-cache perplexity advantage over sliding.
- Stop condition: Stop if uncertainty-gated anchors fail to beat confidence anchors on any model/dataset/budget family or if gains disappear when anchor fraction is varied.

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-lm-benchmark-for-confidence-gated-anchor-kv-ev-faabe119e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
