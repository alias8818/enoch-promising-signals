# Per-Head KV Cache Quantization with Outlier Channels on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-kv-cache-quantization-with-outlier-channels-on-cpu-315448700485`
Run ID: `per-head-kv-cache-quantization-with-outlier-channels-on-cpu-315448700485-20260607T100500591471+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/536a305805e4

## What looked useful

The mechanism appears numerically useful under controlled outlier channels, but the naive CPU outlier path is about 4.8-4.9x slower at dequantization than plain per-head int8, so it is not paper-ready or production-ready without a fused/gather-aware kernel and real-model validation.

## Boundaries and scale limits

Synthetic tensors only; no real LLM KV cache traces, perplexity, generation quality, or integrated decode-latency measurements. The outlier implementation is a naive dense dequantization path, not an optimized CPU kernel.

## Claim scope

On synthetic CPU attention tensors with controlled persistent KV outlier channels, retaining the top 2% KV dimensions in fp16 while quantizing the rest per head reduces attention-output relative MSE by about 44-47% versus per-head int8 and about 41-59% versus per-tensor int8 in outlier cases, while preserving about 3.91x fp32 cache compression.

## Why it stopped

Scoped synthetic evidence supports the numerical mechanism but also exposes a CPU implementation cost; this is insufficient for a paper and is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the scheme into a small real CPU decoding benchmark and measure perplexity plus end-to-end decode latency with an optimized outlier-channel layout.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU KV outlier quantization with fused outlier layout
- Success threshold: At least 3.5x KV memory reduction versus fp32, quality degradation no worse than plain per-head int8 and preferably at least 25% lower error/perplexity delta in outlier-heavy cases, with decode latency overhead no more than 15% versus plain per-head int8.
- Stop condition: Stop if real-model quality is not better than plain per-head int8 or if optimized outlier handling remains more than 25% slower than plain per-head int8 decoding.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-kv-cache-quantization-with-outlier-channels-on-cpu-315448700485`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
