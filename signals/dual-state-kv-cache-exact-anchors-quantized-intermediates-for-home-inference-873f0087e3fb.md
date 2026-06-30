# Dual-State KV Cache: Exact Anchors + Quantized Intermediates for Home Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dual-state-kv-cache-exact-anchors-quantized-intermediates-for-home-inference-873f0087e3fb`
Run ID: `dual-state-kv-cache-exact-anchors-quantized-intermediates-for-home-inference-873f0087e3fb-20260522T001604521055+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e1a8b95f3655

## What looked useful

Exact anchors sharply reduce output error when attention mass lands on anchor tokens, but provide almost no benefit over all-quantized KV when attention targets non-anchor, diffuse, or random positions. This suggests the idea needs explicit anchor-aware routing/summarization to be useful; periodic exact anchors alone are not a robust drop-in fix for quantized KV cache error.

## Boundaries and scale limits

No real LLM layers, no multi-head/multi-layer cache interaction, no perplexity or task-quality measurement, no optimized fused serving kernel, and no long-context production trace. The result supports only a mechanism-level conclusion about attention output error under controlled traces.

## Claim scope

Synthetic single-head attention probe over sequence lengths 1024, 4096, and 8192 with dim 128, per-token symmetric 8-bit or 4-bit quantized intermediate KV states, and exact fp16 anchors every 16 or 64 tokens.

## Why it stopped

Closed as no-paper useful signal: the synthetic probe supports the anchor-benefit mechanism in favorable traces but early-falsifies the broad drop-in claim because non-anchor and diffuse attention errors match ordinary all-quantized KV.

## Recommended next action

Run a bounded real-model follow-up on a small decoder with forced anchor summaries or sink-token-style anchors, comparing perplexity and decode quality against all-int8/all-int4 KV baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Anchor-Aware KV Compression Probe
- Success threshold: At 4-bit or mixed 4/8-bit intermediate KV, anchor-aware dual-state cache reduces perplexity degradation by at least 30% relative to all-quantized KV while preserving at least 3x KV memory compression versus fp16 on the tested small model.
- Stop condition: Stop if periodic and anchor-aware variants both match all-quantized perplexity degradation within 5% relative improvement or if memory compression drops below 2.5x versus fp16.

## Evidence references

- Artifact root: `<local-path>/projects/dual-state-kv-cache-exact-anchors-quantized-intermediates-for-home-inference-873f0087e3fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
