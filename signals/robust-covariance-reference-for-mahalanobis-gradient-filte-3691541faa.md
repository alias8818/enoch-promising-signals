# Robust covariance reference for Mahalanobis gradient filtering

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `robust-covariance-reference-for-mahalanobis-gradient-filte-3691541faa`
Run ID: `robust-covariance-reference-for-mahalanobis-gradient-filte-3691541faa-20260522T215442856379+0000`

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

- Parent run decision: Gradient-norm bounding with Mahalanobis outlier rejection: enoch://control-plane/projects/gradient-norm-bounding-with-mahalanobis-outlier-rejection-f2d8a71fe19d/runs/gradient-norm-bounding-with-mahalanobis-outlier-rejection-f2d8a71fe19d-20260522T213509397388+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/61fb35a2c0a6

## What looked useful

MCD robust Mahalanobis passed 0/4 MSE scenarios and 0/4 rejection-diagnostic scenarios; MAD-pretrimmed robust Mahalanobis passed 1/4 MSE scenarios and 0/4 diagnostics. Compact malicious clusters were ranked as central, producing AUC near 0.0 and rejection of benign high-variance points.

## Boundaries and scale limits

Evidence is synthetic and small-scale; it does not test real model-training gradients, temporal covariance references, per-layer structure, or large client populations.

## Claim scope

In a controlled 80-client, 32-dimensional synthetic gradient-filtering task with 20% compact or shifted adversarial clients and exact keep-count thresholding, current-batch robust covariance references did not improve Mahalanobis filtering over contaminated sample covariance across the predeclared scenarios.

## Why it stopped

The controlled direct test failed the predeclared threshold: neither robust covariance method achieved the required 3/4 MSE wins or 3/4 attack-rejection diagnostic successes.

## Recommended next action

Stop this run as a no-paper useful negative; if continuing the line, test whether a prior-round or clean-warmup covariance reference avoids compact-cluster masking on the same direct metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prior-round covariance reference for compact-cluster Mahalanobis filtering
- Success threshold: Prior-reference Mahalanobis must reduce aggregate MSE by at least 20% versus current-batch sample Mahalanobis in at least 3 of 4 scenarios and achieve attack rejection >=0.80 with benign rejection <=0.10 in at least 3 of 4 scenarios.
- Stop condition: Stop if compact-cluster or low-variance attacks still produce AUC below 0.5 or fail the attack-rejection threshold in more than one scenario.

## Evidence references

- Artifact root: `<local-path>/projects/robust-covariance-reference-for-mahalanobis-gradient-filte-3691541faa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
