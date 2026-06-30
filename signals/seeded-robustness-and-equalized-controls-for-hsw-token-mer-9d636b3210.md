# Seeded Robustness and Equalized Controls for HSW Token Merge Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `seeded-robustness-and-equalized-controls-for-hsw-token-mer-9d636b3210`
Run ID: `seeded-robustness-and-equalized-controls-for-hsw-token-mer-9d636b3210-20260522T155204379231+0000`

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

- Parent run decision: Tiny Trained Benchmark for Hierarchical Sliding Window Token Merge: enoch://control-plane/projects/tiny-trained-benchmark-for-hierarchical-sliding-window-tok-a37bfb88ec/runs/tiny-trained-benchmark-for-hierarchical-sliding-window-tok-a37bfb88ec-20260522T153104479417+0000
- Parent run decision: Hierarchical Sliding Window with Token Merge: enoch://control-plane/projects/hierarchical-sliding-window-with-token-merge-33405b63da40/runs/hierarchical-sliding-window-with-token-merge-33405b63da40-20260522T141244351815+0000

## What looked useful

HSW winnowing at window 5 used about 93 document features versus 283 full unigrams, matched clean Recall@10 (0.9996 vs 0.9997), retained noisy Recall@10 of 0.9791, and beat all equalized controls by at least +0.165 Recall@10 clean and +0.274 noisy in every fixed seed. Window 3 and 9 ablations preserved the same ordering.

## Boundaries and scale limits

Evidence is limited to extractive snippet queries from one corpus, lexical BM25 retrieval, local CPU-scale evaluation, and no standard natural-query retrieval benchmarks or dense retrieval baselines.

## Claim scope

On 20 Newsgroups source-snippet retrieval with BM25, seeded hash/window winnowing over adjacent-token merge features preserves retrieval under feature compression better than equalized random-hash, stride, and truncated-unigram controls across five fixed seeds and window-size ablations.

## Why it stopped

Tier 2 local evidence supports the mechanism but is too narrow for publication readiness because queries are extractive snippets from one corpus and baselines are lexical/local only.

## Recommended next action

Stop this worker run as a no-paper useful signal; next bounded deepening should repeat the equalized-budget fixed-seed comparison on standard non-extractive retrieval datasets before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard-Dataset Equalized HSW Token Merge Retrieval
- Success threshold: HSW must beat every equalized compressed control on the primary dataset metric in at least two datasets, retain at least 95% of the uncompressed BM25 metric at a substantial feature-count reduction, and show no latency/index-size regression that erases the compression benefit.
- Stop condition: Stop as unsupported if HSW fails to beat equalized controls on either dataset or if gains only appear on extractive/exact-overlap queries.

## Evidence references

- Artifact root: `<local-path>/projects/seeded-robustness-and-equalized-controls-for-hsw-token-mer-9d636b3210`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
