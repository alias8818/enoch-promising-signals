# Entropy-Weighted Deduplication for Tiny Data

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-weighted-deduplication-for-tiny-data-c1116e661fa1`
Run ID: `entropy-weighted-deduplication-for-tiny-data-c1116e661fa1-20260531T192752907570+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/074b42fbf6bb

## What looked useful

Across duplicate-contaminated synthetic cells, entropy-weighted dedup beat raw/count-preserving duplicate pressure by +0.139 macro-F1 in the n=4 probe and +0.196 in the n=2 stress probe, showing deduplication matters. Against ordinary keep-one exact dedup, the added entropy weighting was small: +0.0004 mean macro-F1 in the main probe and +0.0067 in the stress probe, with many ties and some losses.

## Boundaries and scale limits

Synthetic data only; exact duplicates only; no real tiny datasets, semantic near-duplicate clustering, transformer fine-tuning, or production curation workflow was tested. CPU-only bounded runs completed in seconds and do not substitute for real-corpus validation.

## Claim scope

Controlled synthetic tiny text classification with exact duplicate contamination and a from-scratch multinomial Naive Bayes learner. Exact deduplication strongly reduces duplicate-count distortion; entropy weighting over keep-one dedup provides only marginal and brittle additional gains.

## Why it stopped

Proxy/early bounded evidence supports exact deduplication but does not support entropy weighting as a robust paper-worthy improvement over plain keep-one dedup.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test entropy weighting on real tiny text datasets with exact and semantic dedup baselines before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tiny-Text Validation of Entropy-Weighted Deduplication
- Success threshold: Mean macro-F1 delta of at least +0.02 over keep-one dedup, positive median delta, and losses in fewer than 20% of dataset-seed cells.
- Stop condition: Stop if entropy weighting does not beat keep-one dedup by +0.01 mean macro-F1 on the first two real datasets or if losses exceed 30% of cells.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-weighted-deduplication-for-tiny-data-c1116e661fa1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
