# Residual Channel Scaling Laws for Extreme Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-scaling-laws-for-extreme-quantization-a79a3361ca52`
Run ID: `residual-channel-scaling-laws-for-extreme-quantization-a79a3361ca52-20260531T151317469674+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/58a9b8942e46

## What looked useful

Across policies, linear R2 between normalized MSE and residual fraction was weak (0.06-0.17), while R2 versus retained channel error-energy fraction was approximately 0.99997-0.999999. Top-error residual channels can nearly eliminate error in heavy-tailed regimes; random residual channels at the same count may do almost nothing.

## Boundaries and scale limits

No transformer training, no real model activation traces, no perplexity or downstream task measurements; widths only up to 4096 input channels and 2520 synthetic CUDA trials.

## Claim scope

Synthetic linear-layer proxy with 1-bit activation and 1-bit weight per-channel quantization: residual channel count alone does not predict recovery across channel distributions, but retained channel quantization-error energy predicts remaining MSE.

## Why it stopped

Proxy evidence is sufficient for a no-paper useful signal and early falsification of count-only scaling, but not a full validation of residual channels for trained extreme-quantized transformers.

## Recommended next action

Run a bounded deepen follow-up on real GPT-2-small-class activation and weight traces to test whether channel quantization-error energy, rather than residual count, predicts perplexity-preserving residual budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual Error-Energy Scaling on Real Transformer Traces
- Success threshold: Retained channel error-energy fraction explains at least 80% of layerwise output-MSE variance and top-error residual channels improve perplexity or next-token loss versus random residual channels at the same budget.
- Stop condition: Stop if real traces show error-energy R2 below 0.5 or no consistent loss/perplexity benefit over random residual channels at matched budgets.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-scaling-laws-for-extreme-quantization-a79a3361ca52`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
