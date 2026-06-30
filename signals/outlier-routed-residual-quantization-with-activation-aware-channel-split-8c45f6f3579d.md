# Outlier-routed residual quantization with activation-aware channel split

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `outlier-routed-residual-quantization-with-activation-aware-channel-split-8c45f6f3579d`
Run ID: `outlier-routed-residual-quantization-with-activation-aware-channel-split-8c45f6f3579d-20260621T165832127497+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/408262a02f5a

## What looked useful

Across 12 seeds and three outlier regimes, the proposed proxy reduced relative output MSE versus the best plain q4 baseline by 37.1% for activation-only outliers, 99.1% for activation-weight-aligned outliers, and 36.5% for weight-only outliers at approximately 4.64 effective bits per weight before index overhead.

## Boundaries and scale limits

Synthetic weight-only linear layers only; no real transformer activations, perplexity, task accuracy, GPT-2-small-class baseline, packed sparse-index overhead, dequantization latency, or GPU kernel measurement.

## Claim scope

In a deterministic NumPy synthetic linear-layer proxy with controlled activation and weight outlier channels, activation-aware input-channel splitting plus a sparse int8 residual route reduced relative output reconstruction MSE versus plain 4-bit split/global quantization and non-activation-aware residual baselines.

## Why it stopped

Bounded synthetic proxy supports the mechanism but does not provide direct transformer or end-to-end evidence required for a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should test the same method on real GPT-2-small-class projection weights with sampled calibration activations and report layer MSE plus perplexity at matched effective bits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real transformer-layer validation of activation-aware outlier residual routing
- Success threshold: At matched effective bits including index overhead, reduce layer output MSE by at least 20% versus the best q4 baseline and improve or match perplexity relative to the best non-activation-aware residual baseline on the sampled evaluation set.
- Stop condition: Stop as negative if activation-aware residual routing fails to beat the best matched-bit non-activation-aware baseline on both layer MSE and perplexity, or if sparse-route overhead eliminates the effective-bit advantage.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-routed-residual-quantization-with-activation-aware-channel-split-8c45f6f3579d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
