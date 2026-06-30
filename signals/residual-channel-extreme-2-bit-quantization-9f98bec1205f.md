# Residual-Channel Extreme 2-bit Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-extreme-2-bit-quantization-9f98bec1205f`
Run ID: `residual-channel-extreme-2-bit-quantization-9f98bec1205f-20260528T023133918586+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d16359ce1dba

## What looked useful

Contribution-aware residual channels produced a 43.0% relative-MSE reduction versus plain 2-bit in the activation-outlier proxy at 2.3125 average bits/weight, but only about 2% reduction in gaussian, correlated, and weight-outlier proxies. At 3.0 and 4.0 average bits/weight, residual-channel repair remained worse than ordinary 3-bit and 4-bit quantization in all tested cases.

## Boundaries and scale limits

No transformer perplexity, real activation traces, downstream task accuracy, hardware kernel speed, or multi-model validation was run. Results are CPU-only NumPy simulations on synthetic activation and weight distributions.

## Claim scope

Synthetic 1024x1024 dense linear-layer proxy tests show residual-channel repair can reduce plain 2-bit output error when activation outliers concentrate error in a few input channels, but it is not competitive with ordinary 3-bit or 4-bit quantization at matched effective storage budgets.

## Why it stopped

Proxy evidence does not support residual-channel extreme 2-bit quantization as storage-competitive with standard 3-bit/4-bit quantization; this is an early bounded falsification, not a full LLM validation.

## Recommended next action

Stop this run as a no-paper useful signal; only pursue a bounded follow-up if real transformer activation traces can test whether the activation-outlier mechanism appears in actual layers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real transformer activation-trace test for residual-channel 2-bit repair
- Success threshold: At matched effective storage no greater than 3.0 bits per weight, residual-channel 2-bit repair must beat ordinary 3-bit quantization on held-out layer output relative MSE in a majority of tested layers and show no worse model-level loss/perplexity than 3-bit.
- Stop condition: Stop if residual-channel repair fails to beat ordinary 3-bit on held-out output MSE in at least half of traced transformer layers or if calibration-selected channels do not transfer to held-out traces.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-extreme-2-bit-quantization-9f98bec1205f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
