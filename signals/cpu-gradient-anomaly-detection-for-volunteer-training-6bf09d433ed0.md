# CPU Gradient Anomaly Detection for Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-gradient-anomaly-detection-for-volunteer-training-6bf09d433ed0`
Run ID: `cpu-gradient-anomaly-detection-for-volunteer-training-6bf09d433ed0-20260521T224353142942+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ba50c91d1226

## What looked useful

Main run scored 560,000 synthetic updates in 42.22 seconds on the CPU worker. Best ROC-AUC was ensemble_robust at 0.9852 +/- 0.0016; best aggregation effect was maha_diag_mad with 0.4396 +/- 0.2083 relative MSE improvement across nonzero attack rates.

## Boundaries and scale limits

Synthetic/proxy only: no real model training, no real volunteer data, no non-IID dataset partitions, no adaptive attacker, and filtering used the known anomaly budget rather than a deployed threshold policy.

## Claim scope

In a bounded synthetic volunteer-gradient benchmark with drifting true gradients, heavy-tailed benign noise, and injected sign-flip, random-direction, and sparse-bias anomalies, CPU-side robust-statistic detectors ranked anomalous updates well and top-budget filtering improved aggregate gradient MSE.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic/proxy benchmark rather than direct validation on real volunteer training.

## Recommended next action

Run a bounded real-model federated training follow-up that compares these CPU detectors against robust aggregation baselines under calibrated false-positive budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU gradient anomaly detection under calibrated false-positive budgets
- Success threshold: At <=5% benign false-positive rate, the detector-based filter improves attacked-run validation metric or aggregate-gradient error by at least 10% relative to the best simple baseline on at least 3 random seeds without degrading the benign-only run by more than 1%.
- Stop condition: Stop if calibrated detectors fail to beat simple norm filtering on both downstream quality and attack mitigation across 3 seeds, or if CPU overhead exceeds 10% of training wall-clock for the small workload.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-gradient-anomaly-detection-for-volunteer-training-6bf09d433ed0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
