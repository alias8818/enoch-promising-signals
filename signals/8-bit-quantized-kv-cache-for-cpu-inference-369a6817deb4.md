# 8-bit Quantized KV Cache for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-quantized-kv-cache-for-cpu-inference-369a6817deb4`
Run ID: `8-bit-quantized-kv-cache-for-cpu-inference-369a6817deb4-20260629T095542171206+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4a5ef7e4f0eb

## What looked useful

Int8 KV cache storage reduced cache bytes by 73.44%. Materialized NumPy dequantization was 4.25x to 14.69x slower than float32, but a fused scalar C++ dequant path was faster at sequence lengths 512 through 16384, with best observed median throughput ratio 3.13x at sequence length 2048 and relative L2 output error around 0.8% to 1.0% on synthetic tensors.

## Boundaries and scale limits

No full transformer integration, no real activation distribution, no perplexity or downstream quality metric, no SIMD-optimized production kernel, no allocator/multi-layer cache pressure, and no batched decode measurement.

## Claim scope

Synthetic CPU single-token decode attention over random normal K/V tensors, comparing float32 KV cache against int8 K/V with per-token per-head float32 scales for heads=8, head_dim=64, sequence lengths 128 through 16384.

## Why it stopped

No-paper closure: this run provides a useful synthetic mechanism signal and an early negative result for materialized dequantization, but it is not direct full-inference evidence.

## Recommended next action

Run a bounded real-model CPU decode follow-up that integrates int8 KV cache storage into a small transformer and measures tokens/second, peak memory, and perplexity/logit drift against float32 or fp16 KV-cache baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU decode validation for fused int8 KV cache
- Success threshold: At least 1.15x decode tokens/second at context length >=2048, at least 60% KV-cache memory reduction, and <=1% relative perplexity degradation or a documented comparable logit-drift threshold.
- Stop condition: Stop as negative if real-model int8 KV cache is slower than baseline at context length >=2048, exceeds 1% relative perplexity degradation, or requires unfused materialized dequantization.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-quantized-kv-cache-for-cpu-inference-369a6817deb4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
