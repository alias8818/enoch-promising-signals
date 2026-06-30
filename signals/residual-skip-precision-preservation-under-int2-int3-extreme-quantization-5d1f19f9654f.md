# Residual Skip-Precision Preservation Under INT2/INT3 Extreme Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-skip-precision-preservation-under-int2-int3-extreme-quantization-5d1f19f9654f`
Run ID: `residual-skip-precision-preservation-under-int2-int3-extreme-quantization-5d1f19f9654f-20260602T150114184416+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b3657682c7fa

## What looked useful

Across 384 trials, fp32 residual preservation reduced NMSE by about 84-99% depending on bit-width, depth, and branch scale, with about 8-19 dB SQNR gain versus requantizing the residual stream every layer.

## Boundaries and scale limits

No trained transformer, language-model perplexity, downstream task accuracy, GPT-2-small-class baseline, hardware-native INT2/INT3 packing, latency, or memory-bandwidth validation was run. Evidence is a CPU-only NumPy fake-quant mechanism probe.

## Claim scope

In synthetic random-weight residual MLP stacks with LayerNorm/GELU branches, INT2/INT3 quantized branch weights and activations, and depths 4-32, preserving the residual stream/addition path in fp32 consistently reduces output error versus quantizing the residual stream after every layer.

## Why it stopped

No-paper closure: the local result is a synthetic mechanism signal, not direct publication-grade model-quality or hardware evidence.

## Recommended next action

Run a bounded direct follow-up on a trained tiny transformer or GPT-2-small-class checkpoint comparing perplexity for all-low-bit residual quantization versus fp32 residual preservation with all other quantization choices fixed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained Transformer Perplexity Test for Residual Precision Preservation
- Success threshold: Residual preservation should improve held-out perplexity by at least 10% relative to quantized residual at the same bit-width, or prevent catastrophic perplexity blow-up in a setting where quantized residual fails.
- Stop condition: Stop if residual preservation does not improve perplexity or layerwise error at INT2/INT3 under matched quantization, or if installation/runtime cannot produce a valid trained-transformer evaluation within the bounded local budget.

## Evidence references

- Artifact root: `<local-path>/projects/residual-skip-precision-preservation-under-int2-int3-extreme-quantization-5d1f19f9654f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
