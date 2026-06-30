# Real-text threshold ablation for local MinHash deduplication leakage control

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-text-threshold-ablation-for-local-minhash-deduplicati-f5ebe4396c`
Run ID: `real-text-threshold-ablation-for-local-minhash-deduplicati-f5ebe4396c-20260520T081416580570+0000`

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

- Parent run decision: Tiny Transformer Validation of Local MinHash Deduplication: enoch://control-plane/projects/tiny-transformer-validation-of-local-minhash-deduplication-1444395243/runs/tiny-transformer-validation-of-local-minhash-deduplication-1444395243-20260520T080339421322+0000
- Parent run decision: Local MinHash Deduplication for Tiny Pretraining Gains: enoch://control-plane/projects/local-minhash-deduplication-for-tiny-pretraining-gains-bb1d1f6a8270/runs/local-minhash-deduplication-for-tiny-pretraining-gains-bb1d1f6a8270-20260520T075256466317+0000

## What looked useful

Best MinHash threshold 0.30 removed 90.25% of labeled leaks with 99.33% clean retention, versus exact hash removing 29.75% with 100% retention and true Jaccard at 0.30 removing 93.08% with 99.39% retention. Thresholds 0.50 and higher preserved clean data but missed most noisy leaks.

## Boundaries and scale limits

Leak variants were constructed from real held-out documents rather than mined as naturally occurring web-scale duplicate clusters; corpus scale was 3 seeds x 3,800 train candidates against 800 eval documents; only word-5 shingles, 128 permutations, and thresholds 0.30-0.95 were tested.

## Claim scope

On a constructed cross-split leakage benchmark using real 20 Newsgroups text, 128-permutation local MinHash-LSH with a low 0.30 threshold materially reduces exact/light/truncated/noisy leakage compared with exact hashing while retaining more than 99% of clean train documents.

## Why it stopped

Tier 2 real-text evidence supports the mechanism but not a paper-ready leakage-control claim: the best tested MinHash threshold left about 9.75% residual labeled leakage, and higher thresholds failed noisy near-duplicates.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run a bounded deepen test on naturally occurring duplicate clusters with thresholds around 0.20-0.40 and 256+ permutations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural duplicate cluster validation for low-threshold MinHash leakage control
- Success threshold: At least 95% labeled leakage removal with at least 99% clean retention, and MinHash within 2 percentage points of true-Jaccard leakage removal at the selected threshold.
- Stop condition: Stop if no threshold achieves 95% leakage removal at 99% clean retention or if MinHash remains more than 5 percentage points below true-Jaccard leakage removal after increasing permutations.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-threshold-ablation-for-local-minhash-deduplicati-f5ebe4396c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
