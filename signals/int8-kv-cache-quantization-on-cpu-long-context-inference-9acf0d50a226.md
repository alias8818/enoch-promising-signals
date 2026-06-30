# Int8 KV-Cache Quantization on CPU Long-Context Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-kv-cache-quantization-on-cpu-long-context-inference-9acf0d50a226`
Run ID: `int8-kv-cache-quantization-on-cpu-long-context-inference-9acf0d50a226-20260630T020841956912+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65a9515b260a

## What looked useful

The memory mechanism is promising but latency is negative for a naive CPU implementation. Int8 KV-cache quantization should not be evaluated further via full-cache dequantization per decode token; the next useful test is a fused or tiled int8 attention path that avoids materializing full float32 K/V every step.

## Boundaries and scale limits

Synthetic random attention tensors only; no real LLM quality, perplexity, fused int8 kernel, production serving loop, fp16/bf16 baseline, or 128k+ full-model validation. CPU-only run completed in 24.22 seconds on an 8-online-logical-CPU Xeon Silver 4114 host.

## Claim scope

On this CPU NumPy one-token decode attention microbenchmark, int8 KV-cache storage with per-token/per-head scales reduced cache bytes by 3.76x and kept synthetic attention output relative L2 error below 0.009, but a dequantize-then-attend decode path was 4.0x to 21.8x slower than fp32 across 1k-65k context lengths.

## Why it stopped

No-paper useful signal: bounded direct microbenchmark supports memory reduction and low synthetic error, but early implementation-level evidence falsifies latency benefit for the naive dequantize-then-attend CPU path.

## Recommended next action

Run one bounded follow-up implementing a fused or tiled CPU int8 attention decode kernel and compare time/token, memory, and error against fp32 at 32k-128k context; stop if it does not beat fp32 latency while preserving sub-1% relative attention-output error.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused tiled int8 KV-cache CPU decode attention
- Success threshold: At 65k context, fused/tiled int8 decode median time/token is at least 1.2x faster than fp32 while using at least 3x less KV-cache storage and keeping relative L2 attention-output error below 0.01.
- Stop condition: Stop as negative if fused/tiled int8 remains slower than fp32 at 65k context, exceeds 0.01 relative L2 error, or requires full-cache float32 materialization per decode token.

## Evidence references

- Artifact root: `<local-path>/projects/int8-kv-cache-quantization-on-cpu-long-context-inference-9acf0d50a226`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
