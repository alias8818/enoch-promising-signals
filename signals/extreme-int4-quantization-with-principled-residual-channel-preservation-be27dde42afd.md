# Extreme INT4 Quantization with Principled Residual Channel Preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-be27dde42afd`
Run ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-be27dde42afd-20260605T225147946211+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/98b36175dbbe

## What looked useful

The mechanism is useful when activation-weighted quantization error is concentrated: the principled selector beat random and row-norm baselines in all 20 case/fraction comparisons, with aggregate MSE reduction versus naive INT4 rising from 6.42% at 0.39% residual to 24.77% at 6.25% residual. Gains were small in Gaussian and weight-only outlier regimes.

## Boundaries and scale limits

No real transformer weights, real calibration traces, downstream perplexity/accuracy, kernel latency, or deployment memory accounting were tested. Evidence is synthetic linear-layer output MSE only and should not be treated as full validation of extreme INT4 quantization.

## Claim scope

Synthetic 512x512 linear layers show that preserving 0.39%-6.25% of input-channel weight rows exactly and selecting them by activation-energy-weighted INT4 quantization error reduces output MSE more than random, row-norm, or activation-only residual selection, especially in activation-outlier and mixed-heavy-tail regimes.

## Why it stopped

No-paper closure: this is a synthetic/proxy useful signal, not direct publication-grade evidence for model quantization.

## Recommended next action

Run a bounded real-layer follow-up on a small open transformer: collect calibration activations, apply the same residual-channel selector to attention and MLP linear layers, and measure perplexity at matched residual fractions against random, row-norm, activation-only, and naive INT4 baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-layer residual channel preservation for small-transformer INT4 quantization
- Success threshold: At 1%-6.25% residual channels, the principled selector should recover at least 25% of naive INT4 perplexity degradation and beat the best non-oracle baseline by at least 10% relative degradation reduction on the same evaluation set.
- Stop condition: Stop if real-layer calibration scores are diffuse or if the principled selector does not beat the best non-oracle baseline at two or more residual fractions.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int4-quantization-with-principled-residual-channel-preservation-be27dde42afd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
