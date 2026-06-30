# Extreme 1.58-bit Quantization with Principled Residual Channels on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-1-58-bit-quantization-with-principled-residual-channels-on-cpu-2a64e66ea87d`
Run ID: `extreme-1-58-bit-quantization-with-principled-residual-channels-on-cpu-2a64e66ea87d-20260527T211121003668+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/98c7eafd6b81

## What looked useful

Residual channels recover most ternary quantization output error when residual error is concentrated in a few input channels: at 4% residual channels, output NMSE fell by about 93.6% on outlier-column and 93.2% on lowrank-outlier synthetic cases, while Gaussian weights improved only about 4.8%. Random residual channels failed in outlier cases, but the principled selector mostly matched simpler weight-energy selection.

## Boundaries and scale limits

No real pretrained transformer weights or activations were tested; no training/perplexity/task metric was measured; CPU timing used dense NumPy matmul and is not an optimized packed ternary kernel benchmark.

## Claim scope

Synthetic CPU NumPy probe of post-training ternary 1.58-bit linear-layer quantization with 0-8% full-precision residual input channels selected by residual-energy times activation variance.

## Why it stopped

Current evidence is synthetic/proxy-only and mixed: it supports a mechanism under channel-concentrated residual error but does not validate real model quality or optimized CPU speed.

## Recommended next action

Run a bounded deepen follow-up on real GPT-2-small-class linear weights with captured calibration activations and a packed ternary CPU kernel before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-activation residual-channel selection for packed ternary CPU linear layers
- Success threshold: At 2-4% residual channels, activation-aware selection reduces held-out layer output NMSE by at least 50% versus no residual and at least 10% versus weight-energy selection on a majority of tested real layers, while packed CPU latency is not worse than 1.25x dense fp16/fp32 for the same batch shape.
- Stop condition: Stop if real-layer activation-aware selection does not beat weight-energy by at least 10% relative NMSE on most layers, or if packed CPU latency exceeds dense baseline by more than 1.5x at residual budgets that preserve quality.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-1-58-bit-quantization-with-principled-residual-channels-on-cpu-2a64e66ea87d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
