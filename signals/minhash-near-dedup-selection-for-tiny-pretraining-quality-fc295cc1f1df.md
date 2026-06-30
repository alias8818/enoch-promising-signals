# MinHash near-dedup selection for tiny pretraining quality

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `minhash-near-dedup-selection-for-tiny-pretraining-quality-fc295cc1f1df`
Run ID: `minhash-near-dedup-selection-for-tiny-pretraining-quality-fc295cc1f1df-20260605T004014929895+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e4701a56048d

## What looked useful

True near-duplicate family removal improved proxy perplexity by 8.5% versus random, but MinHash LSH at the best tested threshold improved only 0.23% and had about 1.5% duplicate-pair recall despite perfect precision. Exact dedup was not useful because redundancy was mostly mutated near duplication.

## Boundaries and scale limits

No real web corpus, tokenizer, neural pretraining, downstream tasks, or large-scale validation. CPU-only synthetic runs: 10 seeds, about 12k selected tokens per strategy, under 1 minute per final run.

## Claim scope

Synthetic fixed-token selection benchmark with generated near-duplicate document families and add-smoothed trigram held-out perplexity. Oracle family dedup improved the tiny-LM proxy, but the tested MinHash LSH near-dedup recipe did not produce a reliable practical gain.

## Why it stopped

Bounded proxy result is mixed and not paper-ready: oracle near-dedup supports the mechanism, but the tested MinHash implementation failed to capture enough near duplicates for a reliable quality improvement.

## Recommended next action

Stop this run as no-paper evidence; a bounded follow-up should test recall-oriented MinHash/SimHash clustering plus fixed-token tiny transformer pretraining on a real small corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Recall-oriented near-dedup selection on a real tiny-pretraining corpus
- Success threshold: At least 2% held-out perplexity improvement over random and exact-dedup controls with no large loss of topical/source diversity, plus near-duplicate recall materially above this run's 1.5% pair recall.
- Stop condition: Stop if audited detector recall remains below 20% at usable precision or if fixed-token neural pretraining shows less than 1% perplexity improvement over both controls.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-near-dedup-selection-for-tiny-pretraining-quality-fc295cc1f1df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
