# Structured residual channels: block-sparse corrections for 2-bit MLP layers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `structured-residual-channels-block-sparse-corrections-for-2-bit-mlp-layers-c181363001e0`
Run ID: `structured-residual-channels-block-sparse-corrections-for-2-bit-mlp-layers-c181363001e0-20260526T000701103683+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8514db946c1d

## What looked useful

At 8% residual block density and 3.53 estimated bits/weight, structured row residuals improved normalized output MSE by 20.32% on low-rank MLP-like weights and 12.62% on outlier-channel weights, versus 8.09% and 8.36% for random residual blocks. On Gaussian weights, structured rows only improved 8.49% versus 7.98% for random, indicating the mechanism depends on structured residual energy.

## Boundaries and scale limits

No real pretrained transformer weights, real calibration activations, perplexity, downstream task accuracy, kernel implementation, latency, or full-model memory-traffic validation were tested. Matrix sizes were 768 x 768 with 512 synthetic activation samples and 6-8 seeds.

## Claim scope

Synthetic single-layer MLP-like matrix reconstruction: 2-bit groupwise quantized weights plus fp16 block residuals reduce layer-output MSE when quantization residual energy is concentrated in structured output channels/blocks, but provide little advantage over random residual blocks on iid Gaussian weights.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only and mixed: the mechanism appears useful under structured residuals but is not validated on real transformer MLP layers or model quality.

## Recommended next action

Run a bounded deepen test on real pretrained GPT-2-small-class MLP layers with captured calibration activations and perplexity or layer-output metrics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real transformer MLP validation for structured 2-bit residual blocks
- Success threshold: At equal estimated bits/weight, structured residual blocks must reduce quantization-induced perplexity or normalized layer-output MSE by at least 10% relative to random residual blocks on most tested MLP layers and remain within 20% of top-block residual performance.
- Stop condition: Stop if structured residual blocks fail to beat random residual blocks by at least 5% on median real-layer output MSE or if same-bit dense/low-rank residual baselines dominate structured blocks.

## Evidence references

- Artifact root: `<local-path>/projects/structured-residual-channels-block-sparse-corrections-for-2-bit-mlp-layers-c181363001e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
