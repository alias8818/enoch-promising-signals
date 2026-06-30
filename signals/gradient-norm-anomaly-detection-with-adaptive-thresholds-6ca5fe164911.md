# Gradient Norm Anomaly Detection with Adaptive Thresholds

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-norm-anomaly-detection-with-adaptive-thresholds-6ca5fe164911`
Run ID: `gradient-norm-anomaly-detection-with-adaptive-thresholds-6ca5fe164911-20260602T133543710473+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6ddf27822c98

## What looked useful

Adaptive gradient-norm thresholds tracked changing non-anomalous gradient baselines and recovered substantially more anomaly recall than a fixed threshold in most synthetic conditions, but the advantage was not universal and is not paper-grade evidence.

## Boundaries and scale limits

Synthetic data only; logistic regression only; no large neural-network training, no real dataset, no optimizer or gradient-clipping ablation, and no comparison against loss-based or feature-based anomaly detectors.

## Claim scope

In a synthetic streaming logistic-regression setup with injected anomalous minibatches, adaptive rolling median/MAD thresholds over scalar gradient norms outperformed a fixed warmup quantile threshold on mean F1 in 11 of 12 anomaly/drift condition groups, with near-zero false-positive rates.

## Why it stopped

The current run produced a reproducible bounded mechanism signal, but it remains synthetic logistic-regression evidence and is not sufficient for a paper claim.

## Recommended next action

Run a bounded direct-evidence follow-up on a small neural model and real dataset with injected bad batches, comparing adaptive gradient-norm detection against fixed, loss-based, and combined detectors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Gradient-Norm Detection on Small Real Neural Training Runs
- Success threshold: Adaptive gradient-norm detection improves mean F1 by at least 0.10 over fixed thresholds in most real-task conditions and keeps false-positive rate below 1%, or a combined detector clearly dominates loss-only detection.
- Stop condition: Stop if adaptive gradient-norm detection fails to beat fixed or loss-based baselines by at least 0.05 mean F1 on the first two real-task anomaly suites, or if false-positive rate exceeds 1% under clean validation streams.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-anomaly-detection-with-adaptive-thresholds-6ca5fe164911`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
