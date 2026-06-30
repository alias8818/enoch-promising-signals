# Spectral-Energy Residual Channel Selection for Sub-2-bit Quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `spectral-energy-residual-channel-selection-for-sub-2-bit-quantization-222653d90f66`
Run ID: `spectral-energy-residual-channel-selection-for-sub-2-bit-quantization-222653d90f66-20260529T093241064847+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ccfb7d53fa1b

## What looked useful

Across synthetic and real-layer tests, spectral-energy residual selection lost most comparisons. On distilgpt2 ternary rank16 it won 1/48 layer-budget comparisons with median MSE 1.241x the best non-spectral rule; binary rank16 won 4/48 with median 1.231x; ternary rank4 won 1/48; ternary rank64 won 0/48. Activation-aware residual norm was the consistent control winner.

## Boundaries and scale limits

Layer reconstruction only; tiny local text calibration set; distilgpt2 scale; no end-to-end perplexity, deployment kernel, storage accounting, larger models, or broad datasets.

## Claim scope

For distilgpt2 attention and MLP projection layer reconstruction with binary or ternary sub-2-bit weight quantization and 1-10% exact residual input-channel budgets, spectral-energy-only channel selection does not outperform simpler activation-aware residual selection.

## Why it stopped

Moderate bounded evidence directly falsifies the spectral-only channel-selection hypothesis for layer reconstruction, but this is not a full end-to-end quantized-model validation.

## Recommended next action

Stop this spectral-only selection line as a no-paper negative; future work should use activation-aware residual scoring as the baseline mechanism before considering spectral variants.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-Aware Residual Channel Selection for Sub-2-bit Quantization
- Success threshold: Activation-aware residual selection reduces perplexity degradation by at least 10% relative to residual-norm selection at the same effective bits per weight on at least two model/checkpoint settings.
- Stop condition: Stop if activation-aware residual selection fails to beat residual-norm selection on end-to-end perplexity in two independently calibrated runs.

## Evidence references

- Artifact root: `<local-path>/projects/spectral-energy-residual-channel-selection-for-sub-2-bit-quantization-222653d90f66`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
