# Gradient Norm Distribution Outlier Rejection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-norm-distribution-outlier-rejection-9855a3786887`
Run ID: `gradient-norm-distribution-outlier-rejection-9855a3786887-20260629T125656246325+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4aed25db8fa9

## What looked useful

Gradient norm matched the oracle on feature-label outliers at a 20% rejection budget: 0.9610 mean test accuracy vs 0.8998 no rejection and 0.9596 oracle, with 0.9717 corruption precision/recall. On plain label noise at the same budget, full gradient norm was slightly below no rejection while normalized-gradient and loss were modestly positive.

## Boundaries and scale limits

Synthetic data only; 4,000 training examples, 4,000 test examples, 64 features, 10 classes, 8 seeds, linear classifier only. No real datasets, deep networks, iterative filtering, or calibrated threshold selection were tested.

## Claim scope

On synthetic 10-class Gaussian classification with a softmax linear classifier, exact per-example gradient-norm rejection can identify and remove feature-plus-label outliers and improve clean test accuracy, but it is not consistently superior to loss or normalized-gradient rejection for plain label noise.

## Why it stopped

Bounded synthetic evidence is mixed: useful mechanism signal for feature-label outliers, but insufficient breadth and novelty for a paper and not a broad validation.

## Recommended next action

Stop this run as no-paper useful evidence; run a bounded follow-up on one real dataset with injected feature and label corruptions plus a non-oracle rejection-fraction calibration rule.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-dataset gradient-norm filtering with calibrated rejection budgets
- Success threshold: Gradient-norm rejection improves clean test accuracy by at least 1 absolute point over loss rejection and random rejection while maintaining corruption precision at least 0.70 under a non-oracle threshold.
- Stop condition: Stop if gradient-norm rejection is not better than loss rejection on mean clean test accuracy or requires oracle knowledge of the corruption fraction.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-distribution-outlier-rejection-9855a3786887`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
