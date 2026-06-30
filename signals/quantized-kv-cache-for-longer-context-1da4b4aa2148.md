# Quantized KV cache for longer context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-kv-cache-for-longer-context-1da4b4aa2148`
Run ID: `quantized-kv-cache-for-longer-context-1da4b4aa2148-20260605T145815140141+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0eb48d708acf

## What looked useful

8-bit affine KV quantization reduced theoretical packed KV memory to 51.6% of fp16 with about 0.8% relative output L2 error and very small attention KL in this benchmark, but naive full-cache dequantization was about 11x slower than fp16 at 4096 tokens. 4-bit reduced memory to 26.6% of fp16 but consistently changed top attention positions and produced about 13% relative output L2 error at 4096 tokens.

## Boundaries and scale limits

No trained model perplexity, task accuracy, multi-layer compounding, production packed-cache kernel, paged attention integration, or serving throughput was measured. Latency uses a naive PyTorch full-cache dequantization path; memory is theoretical packed KV plus fp16 scale/zero metadata.

## Claim scope

Synthetic single-step GPU decode-attention microbenchmark on NVIDIA GB10 comparing fp16 KV cache with per-token/per-head affine 8-bit and 4-bit quantized K/V caches at sequence lengths 1024, 4096, and 8192.

## Why it stopped

Synthetic microbenchmark supports the 8-bit memory/error mechanism but also finds naive dequantization latency is not viable and 4-bit affine KV is unstable; this is not full validation.

## Recommended next action

Stop this worker run as useful no-paper evidence; next bounded action is an end-to-end small-transformer decode/perplexity test with 8-bit KV cache and a fused or streaming dequantized attention path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end 8-bit KV cache evaluation on a small transformer
- Success threshold: At least 45% KV-cache memory reduction versus fp16, less than 1% perplexity degradation or next-token KL below a predefined tolerance, and decode latency no worse than 1.25x fp16 at a matched context length.
- Stop condition: Stop if 8-bit KV causes more than 1% perplexity degradation, persistent top-token distribution drift, or fused/streaming dequantization remains above 1.25x fp16 latency on the small-model workload.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-kv-cache-for-longer-context-1da4b4aa2148`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
