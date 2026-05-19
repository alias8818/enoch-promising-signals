# Natural-Corpus Multi-Anchor Exactness With Coverage Reranking

Status: `useful_signal`
Project ID: `natural-corpus-multi-anchor-exactness-with-coverage-rerank-01615747c2`
Run ID: `natural-corpus-multi-anchor-exactness-with-coverage-rerank-01615747c2-20260515T141622811260+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Natural-Corpus Multi-Anchor Exactness With Coverage Reranking: internal_generated:natural-corpus-multi-anchor-exactness-with-coverage-rerank-01615747c2

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 direct natural-corpus validation found a clear gain over BM25 but only a marginal coverage-rerank gain over multi-anchor exact scoring without coverage.

## Recommended next action

Stop this paper path: the medium natural-corpus run supports multi-anchor exact matching but coverage reranking only added 0.28 top-1 percentage points over the no-coverage ablation, so the named mechanism is not paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Collision-Rich Natural Query Coverage Reranking
- Success threshold: Coverage rerank must beat multi-anchor exact without coverage by at least 2 absolute top-1 percentage points with a 95% paired confidence interval excluding zero, while also matching or beating BM25.
- Stop condition: Stop if shared-anchor collisions occur in less than 10% of evaluable queries or if coverage rerank improves top-1 over no-coverage by less than 1 percentage point after at least 1,000 queries.

## Evidence references

- Artifact root: `<local-path>/projects/natural-corpus-multi-anchor-exactness-with-coverage-rerank-01615747c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
