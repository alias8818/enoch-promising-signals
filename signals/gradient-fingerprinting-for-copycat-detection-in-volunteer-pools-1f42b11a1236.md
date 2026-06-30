# Gradient Fingerprinting for Copycat Detection in Volunteer Pools

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-fingerprinting-for-copycat-detection-in-volunteer-pools-1f42b11a1236`
Run ID: `gradient-fingerprinting-for-copycat-detection-in-volunteer-pools-1f42b11a1236-20260602T175644919529+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9ba8f1c57f79

## What looked useful

Residual-level gradient fingerprints perfectly ranked simple replay, noisy-copy, and delayed-copy pairs in the toy setting, but IID-only threshold calibration produced a 44.6% mean false-positive rate on honest label-shifted volunteers. Calibrating the residual-level threshold on a non-IID honest control reduced label-shift FPR to 0.19% while preserving 100% mean recall for the injected copycat modes in this simulation.

## Boundaries and scale limits

No real volunteer traces, no deep networks, no secure aggregation, no client churn, no adaptive adversaries, and no production-scale heterogeneity. Results are a toy mechanistic signal, not deployment validation.

## Claim scope

Synthetic NumPy logistic-regression volunteer-pool simulation with 20 volunteers, 40 rounds, 30 seeds, residual-level and temporal-delta gradient fingerprint scores, and injected replay/noisy/delayed copycat pairs.

## Why it stopped

Closed as no-paper useful signal because the mechanism appears in a synthetic toy setup, but the naive IID-calibrated detector fails under an honest non-IID label-shift control and no real-trace/deep-network validation was produced.

## Recommended next action

Run a bounded deepen follow-up on a realistic federated benchmark with non-IID clients, known copycat injection, churn, and baseline anomaly detectors; stop treating IID-calibrated gradient fingerprints as deployable.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-IID Federated Benchmark Validation for Gradient Copycat Fingerprints
- Success threshold: At <=1% held-out honest-client pair false-positive rate, residual-level fingerprinting achieves >=90% recall on at least exact replay and noisy-copy injections and improves recall by >=20 percentage points over the strongest baseline.
- Stop condition: Stop if held-out honest non-IID false-positive rate exceeds 5% at thresholds needed for >=70% copycat recall, or if baselines match the detector within 5 percentage points recall at the same false-positive rate.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-fingerprinting-for-copycat-detection-in-volunteer-pools-1f42b11a1236`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
