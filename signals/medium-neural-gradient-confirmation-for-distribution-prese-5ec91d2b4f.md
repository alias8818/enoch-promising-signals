# Medium Neural Gradient Confirmation for Distribution-Preserving Text Coresets

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `medium-neural-gradient-confirmation-for-distribution-prese-5ec91d2b4f`
Run ID: `medium-neural-gradient-confirmation-for-distribution-prese-5ec91d2b4f-20260516T040702994682+0000`

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

- Internal Enoch project: Medium Neural Gradient Confirmation for Distribution-Preserving Text Coresets: internal_generated:medium-neural-gradient-confirmation-for-distribution-prese-5ec91d2b4f

## What looked useful

Neural-gradient selection preserved gradient centroids somewhat at 5% but failed the downstream target: macro-F1 was 0.0227 below stratified random and 0.0770 below TF-IDF SVD KMeans at 5%, and 0.0162 below stratified random and 0.0450 below TF-IDF SVD KMeans at 10%.

## Boundaries and scale limits

This run did not test LLM pretraining, generative perplexity, billion-token corpora, transformer gradient embeddings, or long training schedules. It is a medium local confirmation on real text classification data.

## Claim scope

On an 8-class 20 Newsgroups text classification benchmark with 4,590 training documents, 3,057 held-out test documents, five fixed seeds, 5% and 10% coresets, and downstream logistic-regression evaluation, plain label-stratified neural-gradient KMeans coreset selection did not outperform stratified random or TF-IDF SVD KMeans baselines.

## Why it stopped

Medium direct validation failed the pre-set success threshold and showed consistent downstream underperformance versus real baselines.

## Recommended next action

Stop plain gradient-only coreset selection as a paper path; if continuing, run a bounded hybrid semantic-plus-gradient selector against the same TF-IDF SVD KMeans baseline.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Hybrid Semantic-Gradient Text Coresets Against Strong Semantic KMeans
- Success threshold: Hybrid selection must beat TF-IDF SVD KMeans by at least 0.01 mean macro-F1 or match it within 0.005 while reducing gradient-centroid relative error by at least 20% at both 5% and 10%.
- Stop condition: Stop if the hybrid selector is worse than TF-IDF SVD KMeans by more than 0.005 macro-F1 at either coreset size or fails to reduce gradient-centroid error at both sizes.

## Evidence references

- Artifact root: `<local-path>/projects/medium-neural-gradient-confirmation-for-distribution-prese-5ec91d2b4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
