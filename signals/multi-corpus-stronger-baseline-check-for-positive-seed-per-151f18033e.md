# Multi-corpus stronger-baseline check for positive-seed perplexity filtering

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `multi-corpus-stronger-baseline-check-for-positive-seed-per-151f18033e`
Run ID: `multi-corpus-stronger-baseline-check-for-positive-seed-per-151f18033e-20260622T003805072848+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-corpus bounded comparison of small-LM perplexity filtering against keyword filtering: enoch://control-plane/projects/real-corpus-bounded-comparison-of-small-lm-perplexity-filt-93433d88d6/runs/real-corpus-bounded-comparison-of-small-lm-perplexity-filt-93433d88d6-20260622T001631022344+0000
- Parent run decision: Small-LM perplexity filter vs heuristic keyword filter for tiny pretraining: enoch://control-plane/projects/small-lm-perplexity-filter-vs-heuristic-keyword-filter-for-tiny-pretraining-64ef6248ecee/runs/small-lm-perplexity-filter-vs-heuristic-keyword-filter-for-tiny-pretraining-64ef6248ecee-20260621T235856481026+0000

## What looked useful

Positive-seed perplexity beat random and negative-seed controls on mean AP and ROC-AUC, but lost to BM25 on every corpus. Mean AP was 0.267655 for positive-seed perplexity, 0.355793 for BM25, 0.115724 for random, and 0.109480 for negative-seed perplexity. Paired AP difference versus BM25 was -0.088139 with bootstrap 95% CI [-0.109855, -0.067299], and positive-seed perplexity won only 55 of 195 paired tasks.

## Boundaries and scale limits

This run used public text classification corpora, 8 positive seeds per task, 30 positives plus 270 negatives per candidate pool, and a raw unigram seed language model. It did not test neural LM perplexity, likelihood-ratio calibration, downstream fine-tuning, private corpora, or web-scale filtering.

## Claim scope

In a five-corpus, fixed-seed, few-positive-seed retrieval setup with 39 labels and 195 paired tasks, raw unigram positive-seed perplexity filtering contains useful topic signal but does not beat BM25 seed-centroid retrieval.

## Why it stopped

Medium direct validation with fixed seeds, controls, and a real BM25 baseline failed the pre-registered success threshold: observed mean AP difference was -0.088139 instead of at least +0.03, and paired win rate was 28.21% instead of at least 60%.

## Recommended next action

Stop treating raw positive-seed perplexity filtering as stronger than a real lexical baseline; only run a bounded deepen test if it evaluates calibrated likelihood-ratio perplexity against the same BM25 threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Likelihood-ratio positive-seed perplexity filter versus BM25
- Success threshold: Mean AP at least +0.03 over BM25 with at least 60% paired wins across the same 195 task structure, and no corpus-level collapse below random-control behavior.
- Stop condition: Stop as negative if likelihood-ratio perplexity fails to beat BM25 by +0.03 mean AP or wins fewer than 60% of paired tasks.

## Evidence references

- Artifact root: `<local-path>/projects/multi-corpus-stronger-baseline-check-for-positive-seed-per-151f18033e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
