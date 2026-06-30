# Extreme Quantization with Principled Residual Channels: Quality Preservation in Sub-4-bit Regimes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-quantization-with-principled-residual-channels-quality-preservation-in-sub-4-bit-regimes-da9781796da7`
Run ID: `extreme-quantization-with-principled-residual-channels-quality-preservation-in-sub-4-bit-regimes-da9781796da7-20260528T015413242984+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/93bf42d03423

## What looked useful

Across outlier-channel distributions, calibrated residual channels reduced baseline quantization relative MSE by 54.3% on average versus 4.6% for random residual channels; in iid Gaussian cases the calibrated advantage was small. 2-bit plus 10% residual rows did not match plain 3-bit reconstruction error.

## Boundaries and scale limits

No real transformer, pretrained model, perplexity, downstream task, packed-kernel latency, or full storage-budget-matched deployment validation was run. The evidence is limited to synthetic dense linear maps with held-out synthetic activations.

## Claim scope

Synthetic linear-layer probe: calibrated high-precision residual input channels substantially reduce held-out output reconstruction error for 2-bit and 3-bit quantization when quantization error is concentrated in outlier activation or weight channels.

## Why it stopped

Closed as no-paper useful signal because this was a synthetic/proxy mechanism test with mixed support, not direct full-model evidence for sub-4-bit quality preservation.

## Recommended next action

Run a bounded GPT-2-small-class perplexity test with real calibration activations, storage-matched 2-bit/3-bit baselines, calibrated residual channels, and random residual controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small residual-channel quantization perplexity probe
- Success threshold: At matched effective storage below 4 bits/weight, calibrated residual channels improve held-out perplexity by at least 10% relative to random residual selection and close at least half of the perplexity gap between plain 2-bit and plain 3-bit quantization.
- Stop condition: Stop if calibrated residual selection is not better than random residual selection in perplexity or if matched-budget residual storage fails to close at least 25% of the 2-bit to 3-bit perplexity gap.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-quantization-with-principled-residual-channels-quality-preservation-in-sub-4-bit-regimes`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
