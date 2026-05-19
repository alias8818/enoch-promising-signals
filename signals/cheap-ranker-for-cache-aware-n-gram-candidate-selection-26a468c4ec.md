# Cheap ranker for cache-aware n-gram candidate selection

Status: `useful_signal`
Project ID: `cheap-ranker-for-cache-aware-n-gram-candidate-selection-26a468c4ec`
Run ID: `cheap-ranker-for-cache-aware-n-gram-candidate-selection-26a468c4ec-20260514T040536641125+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Cheap ranker for cache-aware n-gram candidate selection: internal_generated:cheap-ranker-for-cache-aware-n-gram-candidate-selection-26a468c4ec

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct replicated n-gram candidate-selection metrics across three corpora, fixed seeds, ablation, and budget sensitivity show only tiny metric-dependent cache-aware gains and a consistent hit@4 loss versus the count-only cheap ranker.

## Recommended next action

Stop this depth-4 follow-up: the cheap count transform is useful, but the cache-aware term does not beat the count-only ablation robustly enough for a paper-ready claim.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/cheap-ranker-for-cache-aware-n-gram-candidate-selection-26a468c4ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
