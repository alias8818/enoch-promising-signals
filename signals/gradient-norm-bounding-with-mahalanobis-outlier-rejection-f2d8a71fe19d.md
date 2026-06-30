# Gradient-norm bounding with Mahalanobis outlier rejection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-norm-bounding-with-mahalanobis-outlier-rejection-f2d8a71fe19d`
Run ID: `gradient-norm-bounding-with-mahalanobis-outlier-rejection-f2d8a71fe19d-20260522T213509397388+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/61fb35a2c0a6

## What looked useful

Naive contaminated-covariance Mahalanobis rejection failed by covariance masking: outliers received lower scores than clean points and were never rejected in the main training runs. A clean-reference covariance diagnostic separated the same outliers strongly, so the useful signal is that reference/covariance robustness is the critical bottleneck before gradient clipping plus Mahalanobis rejection can be viable.

## Boundaries and scale limits

No deep network, real dataset, online training stack, or robust covariance estimator was tested. The evidence is bounded to small CPU-only synthetic experiments with 12 seeds and contamination rates up to 30%.

## Claim scope

Synthetic linear logistic regression with Gaussian binary classes and injected high-leverage mislabeled outliers. The tested naive method estimates Mahalanobis covariance on the contaminated training pool and combines that rejection with per-sample gradient norm clipping.

## Why it stopped

Moderate synthetic evidence is an early falsification of the naive contaminated-covariance method, not a full-scale validation of all Mahalanobis rejection variants.

## Recommended next action

Stop this naive variant; run a bounded follow-up using robust or warm-started covariance estimation with threshold tuning by target clean false-positive rate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust covariance reference for Mahalanobis gradient filtering
- Success threshold: At 15% contamination, robust Mahalanobis plus clipping should improve clean test accuracy by at least 5 percentage points over clipping alone and reject at least 50% of injected outliers at no more than 10% clean false rejection.
- Stop condition: Stop if robust covariance cannot achieve detector AUC above 0.80 or if robust Mahalanobis plus clipping fails to beat clipping alone by at least 2 percentage points at 15% contamination.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-bounding-with-mahalanobis-outlier-rejection-f2d8a71fe19d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
