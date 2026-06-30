# Gradient-guided INT8 calibration for CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-guided-int8-calibration-for-cpu-inference-56c1ce59032d`
Run ID: `gradient-guided-int8-calibration-for-cpu-inference-56c1ce59032d-20260609T021905410864+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9e27228b3cd6

## What looked useful

Naive high-gradient calibration sample selection worsened KL divergence and logit MSE versus random, while low activation-gradient, low-confidence, and gradient-times-activation policies reduced distributional/logit distortion but slightly reduced FP32 argmax agreement.

## Boundaries and scale limits

Synthetic data, small MLP, simulated per-tensor symmetric quantization, no real CPU INT8 runtime, no pretrained model, and no production latency measurements.

## Claim scope

Small synthetic MLP teacher with NumPy simulated post-training INT8 quantize/dequantize inference; gradient-aware calibration policies compared against random calibration over 5 seeds, 4 budgets, and 3 clipping percentiles.

## Why it stopped

Proxy/local evidence is mixed and not paper-ready: it falsifies the simple high-gradient heuristic but only supports narrower gradient-diagnostic calibration ideas under synthetic simulated conditions.

## Recommended next action

Run a bounded real-runtime follow-up using ONNX Runtime or oneDNN INT8 on one pretrained CPU model and compare random, percentile, low-gradient, low-confidence, and gradient-times-activation calibration at matched calibration budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU INT8 runtime test of low-gradient and gradient-times-activation calibration
- Success threshold: At least one gradient-diagnostic policy improves quantization error or task accuracy versus random by a practically meaningful margin at small calibration budgets, with no more than 0.5 percentage-point task accuracy loss and no added inference-time cost.
- Stop condition: Stop if gradient-diagnostic policies fail to beat random/representative calibration on both task accuracy and quantization error for the pretrained runtime test.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-guided-int8-calibration-for-cpu-inference-56c1ce59032d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
