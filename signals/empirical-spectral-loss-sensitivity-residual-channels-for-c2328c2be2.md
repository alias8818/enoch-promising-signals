# Empirical Spectral Loss-Sensitivity Residual Channels for Low-Bit Transformer Quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `empirical-spectral-loss-sensitivity-residual-channels-for-c2328c2be2`
Run ID: `empirical-spectral-loss-sensitivity-residual-channels-for-c2328c2be2-20260520T190522758659+0000`

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

- Parent run decision: Spectral-Sensitivity-Guided Residual Channels for 1-2bit Quantization: enoch://control-plane/projects/spectral-sensitivity-guided-residual-channels-for-1-2bit-quantization-6f96410446d8/runs/spectral-sensitivity-guided-residual-channels-for-1-2bit-quantization-6f96410446d8-20260520T185531192316+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/32934b6f2703

## What looked useful

Residual full-precision channels materially reduced 3-bit quantization loss, but the spectral loss-sensitivity selector did not meet the predeclared threshold and was weaker than gradient-only loss-sensitivity at 1%, 2%, and 5% budgets. At the primary 3% budget it recovered 22.79% of quantization-induced loss versus 21.54% for loss-sensitivity, below the required 15% relative improvement.

## Boundaries and scale limits

Small pretrained transformer only; short validation slice; no 7B+ model, no full benchmark suite, no activation quantization, no production quantization kernels, and no multi-seed corpus resampling.

## Claim scope

Tier 1 controlled small direct test on distilgpt2 with WikiText-2 calibration/evaluation slices, 3-bit weight-only quantization of GPT-2 Conv1D projection matrices, and 1%-5% per-layer residual output-channel budgets.

## Why it stopped

Direct small transformer quantization evidence missed the stated threshold and showed the spectral component is not a stable improvement over the loss-sensitivity control.

## Recommended next action

Stop this spectral-loss-sensitivity claim as unsupported at Tier 1; if continuing, run a bounded branch that treats gradient-only loss-sensitivity residual channels as the primary method and tests whether it remains robust across 2-bit and 4-bit quantization.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Gradient-Only Loss-Sensitivity Residual Channels for Low-Bit Transformer Quantization
- Success threshold: Gradient/loss-sensitivity residual channels recover at least 15% more quantization-induced loss than magnitude and spectral-loss selectors in at least two bitwidths and two residual budgets, without increasing residual-channel budget.
- Stop condition: Stop if gradient/loss-sensitivity fails to beat magnitude by at least 10% relative recovery in the first two bitwidth-budget pairs or if results reverse across calibration slices.

## Evidence references

- Artifact root: `<local-path>/projects/empirical-spectral-loss-sensitivity-residual-channels-for-c2328c2be2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
