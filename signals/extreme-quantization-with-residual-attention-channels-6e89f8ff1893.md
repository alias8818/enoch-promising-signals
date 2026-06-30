# Extreme Quantization with Residual Attention Channels

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `extreme-quantization-with-residual-attention-channels-6e89f8ff1893`
Run ID: `extreme-quantization-with-residual-attention-channels-6e89f8ff1893-20260604T150141569922+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/52d33b61574f

## What looked useful

Binary attention projections with no residual full-precision channels reached perfect or near-perfect copy-region accuracy at 6.25% of the fp16 dense attention bit budget. Adding 2 or 4 residual full-precision channels per head increased attention bit budget to 17.97% and 29.69% without measurable benefit in the bounded tests.

## Boundaries and scale limits

Synthetic copy task only; tiny 2-layer 64-dim Transformer; attention projection weights only were quantized; no real text corpus, GPT-2-small-class model, full-network quantization, optimized quantized kernels, or downstream tasks were tested.

## Claim scope

On a tiny causal Transformer synthetic copy language-modeling task, preserving 2 or 4 full-precision residual output channels per attention head did not improve validation loss or copy-region accuracy over zero-residual binary attention projections.

## Why it stopped

Proxy-scale direct mechanism test did not support the residual-channel hypothesis; this is an early falsification, not a full large-model validation.

## Recommended next action

Stop this paper path as an early bounded negative for residual attention channels; if continuing, run a GPT-2-small-class real-corpus ablation comparing dense, zero-residual binary attention, and fixed-bit residual-channel variants.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus ablation for zero-residual versus residual binary attention
- Success threshold: Residual-channel variants must improve validation perplexity by at least 3% over zero-residual binary attention at comparable or explicitly justified attention bit budget, without worse stability across seeds.
- Stop condition: Stop if zero-residual binary attention matches or beats residual-channel variants on validation perplexity across the planned seeds, or if training instability prevents a fair matched-budget comparison.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-quantization-with-residual-attention-channels-6e89f8ff1893`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
