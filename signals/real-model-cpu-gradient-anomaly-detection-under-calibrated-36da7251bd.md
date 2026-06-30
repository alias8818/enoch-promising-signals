# Real-model CPU gradient anomaly detection under calibrated false-positive budgets

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-cpu-gradient-anomaly-detection-under-calibrated-36da7251bd`
Run ID: `real-model-cpu-gradient-anomaly-detection-under-calibrated-36da7251bd-20260522T001722731804+0000`

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

- Parent run decision: CPU Gradient Anomaly Detection for Volunteer Training: enoch://control-plane/projects/cpu-gradient-anomaly-detection-for-volunteer-training-6bf09d433ed0/runs/cpu-gradient-anomaly-detection-for-volunteer-training-6bf09d433ed0-20260521T224353142942+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ba50c91d1226

## What looked useful

Static empirical calibration controls false positives in a stationary frozen-model gradient regime, but fails during continuing training because clean gradient score drift causes severe false-positive budget overruns. Large 5x gradient scale anomalies remain easy to detect.

## Boundaries and scale limits

Single small MLP, one real benchmark dataset, CPU-only, injected gradient anomalies, no transformers/CNNs/distributed training/production telemetry/adaptive thresholding.

## Claim scope

Small direct CPU test on exact gradients from a one-hidden-layer ReLU MLP trained on sklearn handwritten digits, with empirical threshold calibration at 10%, 5%, and 1% false-positive budgets.

## Why it stopped

No-paper useful signal: the direct continuing-training test did not satisfy calibrated false-positive budgets, although the stationary control supports the calibration mechanism under narrower conditions.

## Recommended next action

Run a bounded drift-aware calibration follow-up on the same harness before scaling to larger model families.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Drift-aware CPU gradient anomaly calibration during continuing training
- Success threshold: Across five seeds, mean clean FP <= 1.5x each nominal budget and 5x scale detection >= 95% at the 1% budget, with at least one non-scale anomaly class detected at >= 50% at the 5% budget.
- Stop condition: Stop if drift-aware calibration still exceeds 1.5x nominal false-positive budgets in at least three of five seeds or reduces 5x scale detection below 95% at the 1% budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-cpu-gradient-anomaly-detection-under-calibrated-36da7251bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
