# Activation-Aware Residual Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-aware-residual-quantization-28d0fb6aefd5`
Run ID: `activation-aware-residual-quantization-28d0fb6aefd5-20260604T190714145550+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a91f0529d9f4

## What looked useful

Activation-aware residual quantization is conditionally useful: main 2-bit run improved output NMSE by 52.10% on correlated activations and 17.36% on outlier activations, while degrading isotropic by 2.54% and diagonal anisotropic by 22.23%. A 3-bit sensitivity run preserved the correlated/outlier wins but showed larger diagonal degradation.

## Boundaries and scale limits

Small controlled linear-layer benchmark only: 128x256 weights, four synthetic activation distributions, 8 seeds for the main 2-bit run, 4 seeds for a 3-bit sensitivity run. No real transformer traces, no perplexity, no generation-quality evaluation, no optimized kernels.

## Claim scope

On synthetic dense linear layers with grouped residual quantization, calibration activation-aware residual scale fitting lowers held-out output NMSE for correlated and sparse-outlier activation distributions, but does not dominate plain weight-MSE scale fitting on isotropic or diagonal anisotropic activations.

## Why it stopped

No-paper useful signal: local synthetic evidence is mixed and proxy-scoped, so it supports a targeted follow-up rather than a paper-positive positive claim.

## Recommended next action

Run a bounded real-transformer follow-up on GPT-2-small-class MLP and attention projection layers using saved calibration activations, comparing per-layer output NMSE and end-to-end perplexity against weight-MSE residual quantization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transformer Trace Test for Activation-Aware Residual Quantization
- Success threshold: At least 75% of tested projection layers improve held-out output NMSE with no more than 0.1 perplexity regression versus the matched residual quantization baseline, with benefits concentrated in layers diagnosed as correlated or outlier-heavy.
- Stop condition: Stop if activation-aware fitting fails to improve at least half of target layers or causes more than 0.1 perplexity regression at matched quantization settings.

## Evidence references

- Artifact root: `<local-path>/projects/activation-aware-residual-quantization-28d0fb6aefd5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
