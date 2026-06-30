# MinHash Deduplication for Tiny CPU Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `minhash-deduplication-for-tiny-cpu-pretraining-4d412066a5fe`
Run ID: `minhash-deduplication-for-tiny-cpu-pretraining-4d412066a5fe-20260524T011756700683+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d24ceda12ad

## What looked useful

MinHash removed 77.36% of known duplicate documents versus 35.98% for exact dedup, lost zero source groups, reduced tokens by 41.16%, and improved clean perplexity by 8.24% relative to a raw equal-token prefix, but was 8.17% worse than raw-all perplexity because raw-all used many more duplicate tokens.

## Boundaries and scale limits

Three Project Gutenberg books, 1301 unique training paragraphs expanded to about 2.7k crawl documents, three random seeds, injected duplicates, word-level interpolated trigram LM, no neural transformer pretraining, no naturally duplicated web corpus, and no downstream task evaluation.

## Claim scope

On a bounded public-domain paragraph corpus with injected crawl-like exact and near duplicates, MinHash+LSH deduplication reduced tiny word-level LM training tokens by about 41% versus raw while outperforming a raw equal-token prefix on held-out perplexity; it did not beat training on all duplicated tokens.

## Why it stopped

Closed as no-paper useful signal: the local evidence supports the deduplication mechanism in a proxy setting, but not publication-grade tiny neural CPU pretraining.

## Recommended next action

Run a bounded neural LM follow-up on naturally duplicated text, comparing raw, exact-dedup, and MinHash under equal-token and equal-wall-clock budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural tiny-LM validation of MinHash dedup under fixed CPU budgets
- Success threshold: MinHash must improve validation perplexity by at least 3% over raw equal-budget and exact-dedup controls while reducing duplicate memorization, without losing unique source coverage.
- Stop condition: Stop if MinHash fails to beat both raw equal-budget and exact-dedup controls on validation perplexity or causes unique-source loss above 0.5%.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-deduplication-for-tiny-cpu-pretraining-4d412066a5fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
