# Extreme 2-bit Quantization with Principled Residual Channels for gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-2-bit-quantization-with-principled-residual-channels-for-gb10-d4637417c716`
Run ID: `extreme-2-bit-quantization-with-principled-residual-channels-for-gb10-d4637417c716-20260605T061144255366+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/49d284b34bf5

## What looked useful

Residual channels are a real local error-reduction mechanism, with a median 1.86x best MSE reduction across 16 GPT-2 layer probes and up to 8.27x on one module, but five modules still had best relative MSE above 1.0 after 5% residual channels and synthetic non-aligned cases improved only about 1.06-1.07x.

## Boundaries and scale limits

No end-to-end perplexity or task accuracy was measured; GPT-2 calibration used random token IDs; the quantizer was simple rowwise affine 4-level dequantization; throughput used naive PyTorch residual matmuls, not a packed int2 GB10 kernel; only 16 GPT-2 modules were tested.

## Claim scope

Bounded layer-output probes on synthetic matrices and the first four GPT-2 blocks show that preserving a small fraction of fp16 residual input channels can reduce rowwise 2-bit quantization output MSE, especially when activation energy aligns with quantization-error energy.

## Why it stopped

Proxy/local evidence supports the residual-channel mechanism but not paper-ready viability: several real GPT-2 projection layers remain very high-error after 5% residual channels, and no end-to-end model-quality or packed-kernel speed evidence was produced.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate GPT-2-small perplexity with real-text activation calibration and a standard int4/control baseline before any kernel work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2 perplexity validation for 2-bit residual-channel quantization
- Success threshold: At 5% residual channels, perplexity degradation is within 20% of the int4 baseline while using fewer effective weight bits, and no individual projection family shows catastrophic layer-output relative MSE above 1.0.
- Stop condition: Stop if 5% residual-channel quantization remains worse than plain int4 by more than 20% perplexity degradation or if multiple projection families retain relative layer-output MSE above 1.0 after real-text calibration.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-2-bit-quantization-with-principled-residual-channels-for-gb10-d4637417c716`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
