# Multi-corpus validation of intrinsic quality filtering for small text subsets

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `multi-corpus-validation-of-intrinsic-quality-filtering-for-972889cdc2`
Run ID: `multi-corpus-validation-of-intrinsic-quality-filtering-for-972889cdc2-20260628T222600671119+0000`

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

- Parent run decision: Quality-Filtered Small Corpus vs Matched Random Subset: enoch://control-plane/projects/quality-filtered-small-corpus-vs-matched-random-subset-8990bbbeb6ac/runs/quality-filtered-small-corpus-vs-matched-random-subset-8990bbbeb6ac-20260628T220002415631+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4581481eb0d4

## What looked useful

Naive top-k intrinsic quality filtering was harmful in this bounded test: quality-top beat random on 0/9 accuracy and 0/9 macro-F1 comparisons, with mean top-minus-random deltas of -0.096369 accuracy and -0.079151 macro-F1. A middle-quantile diagnostic beat random in 6/9 accuracy comparisons, suggesting band-pass or rejection-style quality filtering is more plausible than top-k quality selection.

## Boundaries and scale limits

CPU-only bounded run; not transformer fine-tuning, not large-corpus validation, not multilingual, and only one hand-designed intrinsic quality score. Runtime was under 10 seconds after downloads, with capped AG News train/test examples.

## Claim scope

For three public English text classification corpora, a transparent label-free intrinsic quality score used as top-k small-subset selection underperformed 10-seed random balanced selection with a pure-Python bag-of-words Naive Bayes classifier at k=10,25,50 examples per class.

## Why it stopped

Bounded direct evidence falsified the tested top-k intrinsic quality filtering hypothesis; this is not a full validation of all intrinsic filtering methods.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded follow-up that pre-registers a band-pass intrinsic filter and compares it against random and diversity baselines on held-out corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Band-pass intrinsic quality filtering for small text subsets
- Success threshold: Band-pass filter improves mean accuracy or macro-F1 over random by at least 2 percentage points and wins at least 70% of corpus/size/model comparisons without a large failure on any corpus.
- Stop condition: Stop if band-pass filtering fails to beat random on most comparisons or if gains disappear when diversity-only controls are included.

## Evidence references

- Artifact root: `<local-path>/projects/multi-corpus-validation-of-intrinsic-quality-filtering-for-972889cdc2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
