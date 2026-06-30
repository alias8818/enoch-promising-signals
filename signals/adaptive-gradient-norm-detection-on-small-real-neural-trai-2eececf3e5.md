# Adaptive Gradient-Norm Detection on Small Real Neural Training Runs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-gradient-norm-detection-on-small-real-neural-trai-2eececf3e5`
Run ID: `adaptive-gradient-norm-detection-on-small-real-neural-trai-2eececf3e5-20260602T220010987655+0000`

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

- Parent run decision: Gradient Norm Anomaly Detection with Adaptive Thresholds: enoch://control-plane/projects/gradient-norm-anomaly-detection-with-adaptive-thresholds-6ca5fe164911/runs/gradient-norm-anomaly-detection-with-adaptive-thresholds-6ca5fe164911-20260602T133543710473+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6ddf27822c98

## What looked useful

The Tier 1 direct test met its threshold: lr_spike and label_flip conditions both had 100% gradient-norm detection within the injection window plus grace period, controls had zero gradient false flags across full 360-step runs, and gradient detection tied or slightly led matched loss detection.

## Boundaries and scale limits

Evidence is limited to MNIST, a 784-64-10 MLP, 360-step CPU training runs, 5 seeds per condition, and abrupt synthetic interventions in otherwise real neural training. It does not cover larger models, transformers, long horizons, subtle drift, naturally occurring failures, GPU/distributed overhead, or production training regimes.

## Claim scope

On a small real MNIST NumPy MLP training setup, an adaptive rolling median/MAD detector on per-step backpropagation gradient norms detected abrupt injected learning-rate spike and label-flip instabilities across 5 seeds each with zero observed false positives and latency no worse than a matched adaptive loss detector.

## Why it stopped

Tier 1 controlled direct evidence supports the mechanism but remains too small and intervention-specific for publication readiness.

## Recommended next action

Run one bounded deepen test on a harder small real model/dataset with subtler injected anomaly magnitudes before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Subtle Gradient-Norm Detection on Harder Small Real Training
- Success threshold: Gradient detector achieves at least 80% detection within the anomaly window plus 20 steps, mean full-control false flags below 1 per run, and mean latency no worse than matched loss detection on at least one subtle anomaly setting.
- Stop condition: Stop as unsupported if full-control false flags average at least 1 per run, or if gradient detection misses more than 20% of subtle anomaly runs while loss detection succeeds.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-gradient-norm-detection-on-small-real-neural-trai-2eececf3e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
