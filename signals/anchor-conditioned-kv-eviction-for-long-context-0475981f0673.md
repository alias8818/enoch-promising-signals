# Anchor-Conditioned KV Eviction for Long Context

Status: `useful_signal`
Project ID: `anchor-conditioned-kv-eviction-for-long-context-0475981f0673`
Run ID: `anchor-conditioned-kv-eviction-for-long-context-0475981f0673-20260515T061149147323+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f7310c1b4b69

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic proxy evidence supports the mechanism when anchors are reliable, but adversarial anchors underperform recency and no trained-model or real benchmark validation was produced.

## Recommended next action

Stop this run as a proxy-only mixed result; next run should implement confidence-gated anchor-conditioned KV eviction in a real small LM and test needle-in-haystack under matched KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM Confidence-Gated Anchor KV Eviction
- Success threshold: At two or more KV budgets, anchor-conditioned eviction improves retrieval accuracy by at least 10 percentage points over recency without more than 2 percentage points degradation versus recency on low-confidence or misleading-anchor cases, and uses no more KV memory than the matched budget.
- Stop condition: Stop if the real LM cannot expose an anchor confidence signal that predicts target section relevance, or if anchor-conditioned eviction fails to beat recency by at least 5 percentage points on the primary needle-in-haystack setting.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-conditioned-kv-eviction-for-long-context-0475981f0673`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
