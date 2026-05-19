# Hybrid Semantic-Gradient Text Coresets Against Strong Semantic KMeans

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `88`
Project ID: `hybrid-semantic-gradient-text-coresets-against-strong-sema-9e9439faf7`
Run ID: `hybrid-semantic-gradient-text-coresets-against-strong-sema-9e9439faf7-20260516T041632420091+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `88`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Hybrid Semantic-Gradient Text Coresets Against Strong Semantic KMeans: internal_generated:hybrid-semantic-gradient-text-coresets-against-strong-sema-9e9439faf7

## What looked useful

The strong semantic KMeans baseline beats random at every budget, while gradient/hybrid selection has a narrow low-budget signal but loses or ties semantic KMeans at practical 5-10% budgets.

## Boundaries and scale limits

Single dataset family, classical TF-IDF/SVD semantic features, logistic-regression probe gradients, and classical downstream classifier; not a neural sentence-transformer or LLM finetuning validation.

## Claim scope

On 20 Newsgroups text classification with TF-IDF/SVD semantic features, class-balanced per-class KMeans medoid selection, and logistic-regression downstream evaluation, hybrid semantic-gradient coresets show small low-budget gains over semantic KMeans at 0.5% and 2% budgets but do not consistently outperform semantic KMeans across 1%, 5%, and 10% budgets.

## Why it stopped

Bounded direct validation found mixed and budget-dependent effects, not a consistent improvement over strong semantic KMeans; this is not paper-positive.

## Recommended next action

Stop this paper track; only pursue a final depth-4 bounded follow-up if specifically interested in the ultra-low-budget regime rather than broad coreset superiority.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ultra-Low-Budget Gradient-Aware Text Coresets
- Success threshold: Hybrid or gradient-aware selection must improve macro-F1 over semantic KMeans by at least 1.0 percentage point on average at <=2% budgets with paired wins on at least two of three datasets, while not losing by more than 0.5 points at 5%.
- Stop condition: Stop if the <=2% macro-F1 lift is below 0.5 percentage points on two datasets or if semantic KMeans wins at 5% by more than 1 point on two datasets.

## Evidence references

- Artifact root: `<local-path>/projects/hybrid-semantic-gradient-text-coresets-against-strong-sema-9e9439faf7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
