# Heuristic quality filter ablation on tiny pretraining corpora

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `heuristic-quality-filter-ablation-on-tiny-pretraining-corpora-f022793db3b2`
Run ID: `heuristic-quality-filter-ablation-on-tiny-pretraining-corpora-f022793db3b2-20260628T124804934625+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6a792cdac89d

## What looked useful

Blanket heuristic quality filters are not uniformly beneficial for tiny pretraining corpora. In this proxy, deduplication can remove near-clean redundant signal that helps validation perplexity, so duplicate filtering should be ablated under the actual token budget.

## Boundaries and scale limits

Synthetic corpus, word trigram LM, 5 seeds, 3k/6k/12k token budgets, clean held-out perplexity only. No neural transformer training, no real web corpus, no downstream task evaluation, and no large-scale pretraining evidence.

## Claim scope

In a controlled synthetic tiny-corpus proxy using an add-k word trigram LM, strict heuristic quality filtering improved held-out clean perplexity at a 3k-token budget, was marginal at 6k tokens, and hurt at 12k tokens; duplicate-overlap filtering was the clearest harmful heuristic at the main 12k-token budget.

## Why it stopped

This run produced useful bounded proxy evidence, but the result is mixed and not a full validation of heuristic filtering for neural pretraining.

## Recommended next action

Run a bounded direct follow-up with a small neural LM on a real tiny text corpus, preserving the same fixed-token budget and ablations, especially with and without duplicate-overlap filtering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small neural LM validation of duplicate-filter harm in tiny pretraining corpora
- Success threshold: The duplicate-filter-off configuration improves validation perplexity by at least 5% over all_filters in at least one budget without increasing obvious junk-token share enough to degrade a held-out clean slice.
- Stop condition: Stop if neural validation loss shows no repeatable duplicate-filter harm across budgets/seeds or if real-corpus filtering removes too little data to create a meaningful ablation.

## Evidence references

- Artifact root: `<local-path>/projects/heuristic-quality-filter-ablation-on-tiny-pretraining-corpora-f022793db3b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
