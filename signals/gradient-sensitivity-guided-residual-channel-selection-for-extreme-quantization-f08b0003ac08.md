# Gradient-Sensitivity-Guided Residual Channel Selection for Extreme Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-sensitivity-guided-residual-channel-selection-for-extreme-quantization-f08b0003ac08`
Run ID: `gradient-sensitivity-guided-residual-channel-selection-for-extreme-quantization-f08b0003ac08-20260524T163021302166+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5c558e37ba4a

## What looked useful

Gradient scoring won 5 of 6 aggregate bit/budget settings and beat random mean in 12 of 18 seed-by-setting comparisons, with mean accuracy improvements of +0.0188 over random, +0.0358 over magnitude, and +0.1042 over activation. The result is mixed because magnitude slightly beat gradient at the 2-bit/25% aggregate and in 8 of 18 seed-by-setting comparisons.

## Boundaries and scale limits

Evidence is limited to a tiny CNN, MNIST, weight-only per-output-channel quantization, three training seeds, and short local CUDA runs. It does not validate transformer/LLM layers, activation quantization, production kernels, latency, storage overhead, or large-scale calibration behavior.

## Claim scope

In a small MNIST CNN post-training quantization probe, restoring gradient-sensitivity-selected output-channel residuals usually preserved more accuracy than random or activation-selected residuals under 1-bit and 2-bit weight quantization, but did not uniformly beat quantization-error magnitude selection.

## Why it stopped

Closed as no-paper useful signal: the direct small-CNN evidence supports a mechanism but is mixed against a simple magnitude baseline and does not validate the intended extreme-quantization setting for transformers or large models.

## Recommended next action

Run a bounded transformer language-model deepen test with identical residual budgets, gradient versus magnitude/random controls, validation loss/perplexity as the target metric, and at least three seeds before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer residual-channel selection under extreme post-training quantization
- Success threshold: Gradient selection must beat random mean and magnitude selection on validation loss/perplexity in at least 5 of 6 aggregate bit/budget settings, with a mean relative loss reduction of at least 3% versus the best cheap non-gradient control.
- Stop condition: Stop if gradient selection fails to beat the best cheap control in at least half of the seed-by-setting comparisons or if the unquantized/quantized baselines are unstable enough to make residual-selection differences uninterpretable.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-sensitivity-guided-residual-channel-selection-for-extreme-quantization-f08b0003ac08`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
