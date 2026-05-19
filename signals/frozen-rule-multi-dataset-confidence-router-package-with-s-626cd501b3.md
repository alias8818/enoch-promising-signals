# Frozen-rule multi-dataset confidence-router package with shared-feature latency accounting

Status: `useful_signal`
Project ID: `frozen-rule-multi-dataset-confidence-router-package-with-s-626cd501b3`
Run ID: `frozen-rule-multi-dataset-confidence-router-package-with-s-626cd501b3-20260519T001335777766+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Frozen-rule multi-dataset confidence-router package with shared-feature latency accounting: internal_generated:frozen-rule-multi-dataset-confidence-router-package-with-s-626cd501b3

## What looked useful

At threshold 0.90 the router achieved mean accuracy retention 1.0162 and mean shared-feature latency reduction 0.4234 versus expensive-only, with minimum accuracy retention 0.9936. However breast_cancer had mean shared-feature latency regression -0.4925 and worst regression -0.8853, showing a plain frozen confidence rule needs a cost-aware guard.

## Boundaries and scale limits

CPU-only scikit-learn classifiers; no production model serving, no GPU/LLM routing, no online latency percentiles, and only one medium synthetic dataset beyond built-in sklearn datasets.

## Claim scope

In a bounded local scikit-learn validation over five datasets, five fixed seeds, and three frozen thresholds, a frozen confidence router can meet aggregate accuracy-retention and shared-feature latency-reduction targets, but it fails on at least one low-cost dataset where router overhead exceeds expensive-only inference.

## Why it stopped

No-paper useful signal: direct bounded validation supports the mechanism in cost-asymmetric regimes but falsifies robustness of a plain frozen confidence threshold under shared-feature accounting.

## Recommended next action

Run one bounded depth-4 follow-up that adds a frozen cost-aware guard based on calibration-set expensive-only latency and only enables routing when predicted savings exceed router overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cost-aware frozen confidence router with measured-overhead guard
- Success threshold: At threshold 0.90, mean shared-feature latency reduction >= 25%, minimum accuracy retention >= 99%, and no dataset has negative mean shared-feature latency reduction versus expensive-only.
- Stop condition: Stop negative if any dataset still has negative mean shared-feature latency reduction or if minimum accuracy retention falls below 99%.

## Evidence references

- Artifact root: `<local-path>/projects/frozen-rule-multi-dataset-confidence-router-package-with-s-626cd501b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
