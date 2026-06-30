# Aggressive n-gram deduplication for tiny pretraining data at matched budget

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `aggressive-n-gram-deduplication-for-tiny-pretraining-data-at-matched-budget-58348438343f`
Run ID: `aggressive-n-gram-deduplication-for-tiny-pretraining-data-at-matched-budget-58348438343f-20260619T175503819353+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3dedabb33ff9

## What looked useful

Dedup with n=64 removed 45% of documents and improved held-out loss in 3/3 seeds by mean -0.01575 nats. A sweep showed aggressive thresholds can fail: n=8 kept only 2/420 documents and worsened validation loss by +3.09541 nats; n=16 removed 83.1% and worsened by +0.03718 nats.

## Boundaries and scale limits

This run used a small GRU character model, one public text source, controlled duplicate injection, and about 1M consumed characters per condition. It does not validate tokenizer-level deduplication, transformer pretraining, natural web-scale duplicate distributions, downstream transfer, or long training budgets.

## Claim scope

In a tiny character-level language-model probe on Tiny Shakespeare with controlled exact and near duplicates, moderate document-level character n-gram deduplication at matched consumed-token budget slightly improved held-out validation loss across three seeds, while very short n-gram thresholds over-removed data and degraded validation.

## Why it stopped

Bounded local evidence is mixed and useful but not paper-ready: moderate dedup helped slightly, while aggressive short n-gram dedup caused clear over-removal failures.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up with a small transformer, tokenizer-level n-gram dedup, naturally duplicated tiny corpora, and retained-token-fraction controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-level retained-fraction dedup for tiny transformer pretraining
- Success threshold: A retained-fraction-controlled dedup condition improves held-out perplexity versus raw duplicate data in both corpora with non-overlapping or clearly separated seed confidence intervals, while preserving at least 40% of unique training tokens.
- Stop condition: Stop if no dedup threshold beats raw in either corpus, or if every apparent win requires retaining less than 40% of unique tokens or fails across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/aggressive-n-gram-deduplication-for-tiny-pretraining-data-at-matched-budget-58348438343f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
