# Multi-Anchor Exactness Under Restricted Retrieval Queries

Status: `useful_signal`
Project ID: `multi-anchor-exactness-under-restricted-retrieval-queries-487403b40e`
Run ID: `multi-anchor-exactness-under-restricted-retrieval-queries-487403b40e-20260515T141123104837+0000`

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

Tier 1 controlled direct test found mechanism support under anchor coverage and binary TF-IDF, but the stated exact@1 threshold was not robust across rankers: BM25 passed only 3/5 seeds and raw TF-IDF cosine passed 0/5 seeds.

## Recommended next action

Stop this run as a proxy/early falsification for paper readiness; the next concrete step, if the controller chooses to deepen, is a bounded natural-corpus benchmark with anchor-coverage reranking versus BM25, dense, hybrid, and TF-IDF baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-Corpus Multi-Anchor Exactness With Coverage Reranking
- Success threshold: Anchor-coverage reranking must reach at least 95% exact@1 on three-anchor restricted queries, improve by at least 30 percentage points over single-anchor queries, and outperform the strongest non-coverage baseline by at least 10 percentage points across at least three corpus/collision settings.
- Stop condition: Stop if anchor-coverage reranking falls below 90% exact@1 in any primary setting, fails to beat the strongest baseline by 10 percentage points, or if manual inspection shows target identity is not recoverable from the restricted anchors.

## Evidence references

- Artifact root: `<local-path>/projects/multi-anchor-exactness-under-restricted-retrieval-queries-487403b40e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
