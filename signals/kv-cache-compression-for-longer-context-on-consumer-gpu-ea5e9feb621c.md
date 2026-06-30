# KV Cache Compression for Longer Context on Consumer GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-for-longer-context-on-consumer-gpu-ea5e9feb621c`
Run ID: `kv-cache-compression-for-longer-context-on-consumer-gpu-ea5e9feb621c-20260613T064630187951+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/62aab312ff43

## What looked useful

KV quantization has a real memory-extension mechanism and low synthetic attention error, but implementation strategy dominates usefulness: unfused full-cache dequantization makes the simple path impractical for latency-sensitive decode.

## Boundaries and scale limits

Synthetic single-layer attention only; no real LLM perplexity, task accuracy, fused quantized-attention kernel, paged cache integration, or discrete 8-24 GiB consumer GPU pressure test. The result should not be read as full validation of practical long-context serving.

## Claim scope

On synthetic single-token decode attention on NVIDIA GB10, groupwise int8 KV cache with fp16 scales provides 1.939x KV-only memory reduction and very low attention-output error versus fp16, but a naive dequantize-then-attend implementation is 1.9x to 13.2x slower than fp16 attention across 512 to 16,384 tokens.

## Why it stopped

Closed as no-paper useful signal because the local proxy supports the memory/error mechanism but early-falsifies the naive implementation for practical serving latency; this is not a full validation.

## Recommended next action

Run a bounded deepen test using an existing transformers/Hugging Face quantized-cache path or a small fused quantized-attention kernel on a small real LLM, measuring perplexity and tokens/sec against fp16 KV.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model KV Quantized Cache Decode Test
- Success threshold: At least 1.8x KV memory reduction, perplexity degradation no worse than 1%, and decode tokens/sec at least 67% of fp16 baseline on two tested context lengths.
- Stop condition: Stop if integrated quantized KV is slower than 2x fp16 or degrades perplexity by more than 3% on the small evaluation sample.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-for-longer-context-on-consumer-gpu-ea5e9feb621c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
