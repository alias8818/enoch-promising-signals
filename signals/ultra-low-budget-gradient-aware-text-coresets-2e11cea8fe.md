# Ultra-Low-Budget Gradient-Aware Text Coresets

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `28`
Project ID: `ultra-low-budget-gradient-aware-text-coresets-2e11cea8fe`
Run ID: `ultra-low-budget-gradient-aware-text-coresets-2e11cea8fe-20260516T043108743168+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `28`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Ultra-Low-Budget Gradient-Aware Text Coresets: internal_generated:ultra-low-budget-gradient-aware-text-coresets-2e11cea8fe

## What looked useful

Gradient-space diversity can beat stratified random at some small budgets, but the gain vanishes against a simple TF-IDF/SVD diversity coreset and reverses at larger low-budget settings. The high-loss proxy ablation performs poorly, indicating that coverage/diversity is more important than raw proxy gradient magnitude in this setup.

## Boundaries and scale limits

Validation used TF-IDF/SVD features, linear downstream classifiers, 20 Newsgroups 4-class and full 20-class variants, 5-10 seeds, and budgets up to 640 examples for 4-class and 1600 examples for 20-class. It did not test transformer fine-tuning, language-model pretraining, active learning loops, or a broad multi-dataset benchmark.

## Claim scope

The tested ultra-low-budget gradient-aware selector, using proxy logistic gradients and gradient-space k-means for supervised text classification coresets, is not paper-positive because it does not robustly outperform a cheap non-gradient TF-IDF/SVD k-means diversity baseline on 20 Newsgroups variants.

## Why it stopped

Direct downstream experiments on two real 20 Newsgroups variants showed no robust advantage over a strong cheap non-gradient diversity baseline; follow-up depth is already 4, so no further deepen/retry follow-up is recommended.

## Recommended next action

Stop this depth-4 follow-up chain; the direct bounded validation produced useful no-paper evidence but failed the Tier 4 publication-readiness gate.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/ultra-low-budget-gradient-aware-text-coresets-2e11cea8fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
