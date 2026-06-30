# KV-Cache Compression for Low-VRAM Volunteer Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-for-low-vram-volunteer-workers-d809aa2628ff`
Run ID: `kv-cache-compression-for-low-vram-volunteer-workers-d809aa2628ff-20260613T213521203794+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b55635fe84fe

## What looked useful

Memory compression is real, int8 is much safer than int4 in the synthetic attention-output probe, and naive full dequantization before every decode step likely erases much of the serving benefit through latency overhead.

## Boundaries and scale limits

Evidence is limited to synthetic K/V tensors plus a tiny GPT-2 Transformers QuantizedCache sanity check. It does not validate real 7B-class model quality, packed int4 kernels, fused quantized attention, low-VRAM allocator behavior, batching, or production volunteer-worker scheduling.

## Claim scope

On GB10 synthetic single-token decode attention, per-token int8 KV quantization nearly halves effective KV-cache bytes with about 0.9-1.0% relative L2 attention-output error, but a dequantize-before-attention implementation is materially slower than fp16 at long contexts. Per-token int4 gives larger memory savings but much higher synthetic attention-output error.

## Why it stopped

Closed as no-paper useful signal: bounded local evidence supports the memory/error mechanism and identifies naive dequantization overhead, but it is not direct end-to-end low-VRAM volunteer-serving validation.

## Recommended next action

Implement or select a fused/blockwise int8 KV attention path and compare fp16, naive dequantize-before-attention, and fused quantized attention on a small real decoder model under an explicit memory cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused int8 KV-cache attention under a real low-VRAM serving cap
- Success threshold: At least 1.7x measured KV-cache memory reduction versus fp16, less than 20% median decode-latency overhead versus fp16, and no more than 1% perplexity regression or an agreed logit-divergence bound on the tested small model.
- Stop condition: Stop if fused/blockwise int8 remains more than 50% slower than fp16 at 8k or longer context, exceeds the memory cap, or shows quality/perplexity degradation beyond the threshold.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-for-low-vram-volunteer-workers-d809aa2628ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
