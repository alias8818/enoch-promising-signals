# Anchor-Pinned Adaptive KV Quantization by Distance

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-pinned-adaptive-kv-quantization-by-distance-f2d75d1970fc`
Run ID: `anchor-pinned-adaptive-kv-quantization-by-distance-f2d75d1970fc-20260531T124910969551+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/66bf5b7704cf

## What looked useful

Sparse FP16 anchors can protect long-range attention if they cover important KV entries, but fixed periodic anchors are brittle. In the aligned synthetic case anchor_pinned_adaptive reached rel_mse 0.00131 at 0.183 FP16 storage versus uniform_int3 rel_mse 0.04984 at 0.188 storage; in unaligned salience it degraded to rel_mse 0.27227, effectively the same as distance_no_anchor and far worse than uniform_int3 rel_mse 0.04954.

## Boundaries and scale limits

No trained language model perplexity or downstream quality run; synthetic Q/K/V only; 4 seeds; no packed fused quantized attention kernel; idealized storage ratios exclude metadata, scale, packing, and memory-bandwidth overhead.

## Claim scope

4096-token synthetic GPU attention-output probe: fixed periodic anchor-pinned adaptive KV quantization preserves outputs very well only when salient far-context tokens coincide with pinned anchors; it fails when salience is unaligned and underperforms uniform int3/int4 baselines on random attention at similar storage.

## Why it stopped

Proxy mechanism test found a clear brittleness: fixed periodic anchors help only under aligned salience and fail the unaligned-salience control, so this is useful no-paper evidence rather than full validation.

## Recommended next action

Stop the fixed-periodic-anchor paper path; run a bounded real-model trace follow-up comparing fixed anchors against attention/content-selected anchors on GPT-2-small-class KV traces before investing in packed kernels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Trace Test for Content-Selected KV Anchors
- Success threshold: At <=0.20 FP16-equivalent KV storage, content-selected anchors reduce attention-output relative MSE by at least 2x versus uniform int3 and keep perplexity delta within 1% on the bounded corpus.
- Stop condition: Stop if selected anchors do not cover substantially more high-attention historical mass than fixed periodic anchors or if perplexity/attention error is not better than uniform int3 at comparable storage.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-pinned-adaptive-kv-quantization-by-distance-f2d75d1970fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
