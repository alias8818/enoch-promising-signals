# Spectral Residual Decomposition for Sub-2bit Weight Quantization

Status: `useful_signal`
Project ID: `spectral-residual-decomposition-for-sub-2bit-weight-quantization-5547c307a409`
Run ID: `spectral-residual-decomposition-for-sub-2bit-weight-quantization-5547c307a409-20260516T154717366306+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9f35e150e0c8

## What looked useful

SRD reduced sampled layer-output relative MSE by 49-55% versus 1-bit binary across 1.4, 1.6, 1.8, and 1.95 bpw, but at 1.8 bpw its all-block model-loss delta was +3.2567 versus fp32, worse than same-budget spectral-only at +1.7228.

## Boundaries and scale limits

Evidence is limited to DistilGPT-2, Wikitext-2 test samples, CPU execution, 12-module per-layer MSE probes, and a 32-sample sequence-length-128 loss check over 24 quantized block matrices. It does not include full-test perplexity, GPT-2-small/large models, learned calibration, GPTQ/AWQ baselines, or hardware throughput.

## Claim scope

On DistilGPT-2 block matrices, low-rank spectral plus 1-bit residual decomposition under 1.4-1.95 bits/weight consistently improves isolated layer-output and weight reconstruction error versus binary quantization, but the tested uncalibrated formulation does not beat same-budget spectral-only on a small end-to-end Wikitext loss check.

## Why it stopped

Bounded local evidence supports the per-layer mechanism but the direct small end-to-end loss proxy fails against the same-budget spectral-only control, so this is not paper-ready and not a broad validation.

## Recommended next action

Stop this exact unscaled SRD formulation as no-paper mixed evidence; run one bounded residual-scaling/gating follow-up only if pursuing the mechanism further.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Residual Scaling for Sub-2bit Spectral Residual Quantization
- Success threshold: Calibrated SRD must beat same-budget spectral-only in held-out mean loss while retaining at least a 25% layer-output relative-MSE reduction versus binary at 1.8 bpw.
- Stop condition: Stop if calibrated SRD still has higher held-out loss than same-budget spectral-only at 1.8 bpw or if the gain appears only on calibration samples.

## Evidence references

- Artifact root: `<local-path>/projects/spectral-residual-decomposition-for-sub-2bit-weight-quantization-5547c307a409`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
