# Outlier-Residual Sub-4bit GPT-2 Quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `outlier-residual-sub-4bit-gpt-2-quantization-8bea1aa589d3`
Run ID: `outlier-residual-sub-4bit-gpt-2-quantization-8bea1aa589d3-20260621T024634246345+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c4961ff9efce

## What looked useful

Best tested sub-4-bit scheme was 3b_error_residual_3.00pct at 3.972 effective bits/weight, but it still had 3.462x dense-4b weighted relative MSE and 3.466x dense-4b random matmul-output relative MSE across 21,233,664 GPT-2 projection weights.

## Boundaries and scale limits

Weight-level and random-activation matmul-output proxy only; no end-to-end perplexity, no packed sparse kernel latency, no Hessian/AWQ/GPTQ-style calibration, and no larger-model validation.

## Claim scope

For 12 representative GPT-2 small projection matrices from openai-community/gpt2, a simple dense 3-bit per-row symmetric quantizer plus sparse exact residual/outlier correction up to 3% density did not match dense 4-bit quantization under a sub-4 effective bits-per-weight storage budget.

## Why it stopped

Proxy but direct GPT-2 weight evidence early-falsified the simple sub-4-bit residual/outlier mechanism against dense 4-bit; this is not a full model validation.

## Recommended next action

Stop this simple residual/outlier scheme as no-paper evidence; only revisit with a changed quantizer design that includes calibrated/grouped scaling and an end-to-end GPT-2 perplexity threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated GPT-2 Sub-4-bit Quantization With Residual Repair
- Success threshold: Below 4.0 effective bits/weight with validation perplexity no worse than dense 4-bit by more than 2% relative and with storage accounting including all residual metadata.
- Stop condition: Stop if calibrated residual variants remain more than 10% worse than dense 4-bit perplexity or require 4.0 or more effective bits/weight after metadata accounting.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-residual-sub-4bit-gpt-2-quantization-8bea1aa589d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
