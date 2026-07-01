# Quality filter comparison: fastText vs KenLM vs length for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-filter-comparison-fasttext-vs-kenlm-vs-length-for-tiny-pretraining-00a63255e5e3`
Run ID: `quality-filter-comparison-fasttext-vs-kenlm-vs-length-for-tiny-pretraining-00a63255e5e3-20260610T045831644398+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/000b52be0247

## What looked useful

fasttext_hash won 4/4 main seeds with mean held-out char cross entropy 2.1613 nats and mean selected clean fraction 0.9773; kenlm_char was second at 2.3385 nats and 0.7761 clean fraction; length was weak at 2.9763 nats and 0.4989 clean fraction.

## Boundaries and scale limits

The run used local fastText/KenLM-style analogues, synthetic noise, Project Gutenberg source text, and a character n-gram LM as the pretraining proxy. It did not evaluate actual fastText/KenLM packages, real web-crawl shards, tokenizers, or neural Transformer/RNN pretraining.

## Claim scope

In a bounded public-domain English plus synthetic-noise tiny-pretraining proxy, a supervised fastText-style hashed n-gram quality classifier selected cleaner text and yielded lower held-out clean-English character-LM loss than KenLM-style character n-gram scoring, length filtering, or random selection across four seeds.

## Why it stopped

Closed as a no-paper useful proxy result: evidence is consistent and reproducible locally, but it is not direct full-scale neural pretraining evidence.

## Recommended next action

Run a bounded neural follow-up using actual fastText and KenLM filters on a small real web-crawl shard, then train the same tiny decoder LM for matched sequence-item budgets from each selected corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual fastText/KenLM filters on real crawl shard with tiny neural LM validation
- Success threshold: fastText selection beats KenLM and length by at least 3% relative held-out validation loss or by a statistically consistent margin across at least three seeds, while selecting a higher clean fraction than both baselines.
- Stop condition: Stop if actual package installation or crawl acquisition fails, or if fastText does not beat KenLM on both clean fraction and held-out neural LM loss in at least two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/quality-filter-comparison-fasttext-vs-kenlm-vs-length-for-tiny-pretraining-00a63255e5e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
