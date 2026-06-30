# Aggressive INT4 Quantization for Home GPU VRAM Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `aggressive-int4-quantization-for-home-gpu-vram-reduction-5b9927f75e8f`
Run ID: `aggressive-int4-quantization-for-home-gpu-vram-reduction-5b9927f75e8f-20260614T025611960644+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a4135adbcc7b

## What looked useful

Packed INT4 storage provides the expected weight-byte reduction, but storage-only quantization is insufficient for practical home-GPU VRAM reduction unless the serving backend uses fused kernels or otherwise avoids full FP16 dequantized weight materialization during forward.

## Boundaries and scale limits

This is a bounded GPU microbenchmark, not a full-model inference, perplexity, quality, KV-cache, or fused-kernel validation. Shapes tested were 4096x4096 and 11008x4096 linear layers with 64 tokens on one GB10 host.

## Claim scope

On GB10, synthetic Transformer-sized linear layers with packed symmetric INT4 weights and FP16 per-group scales reduce raw FP16 weight storage by 3.56x to 3.94x, but a naive PyTorch dequantize-then-matmul path is 8.98x to 11.01x slower than FP16 GEMM and materializes dequantized weights, causing high peak allocator use.

## Why it stopped

No-paper closure: bounded local evidence supports the storage mechanism but shows the naive implementation is too slow and loses practical peak-memory benefits through dequantization materialization.

## Recommended next action

Stop paper pursuit for the naive packed-storage approach; next bounded test should evaluate a fused INT4 backend on a real small language model and require lower peak memory than FP16 with less than 2x latency regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused INT4 Inference Backend Test on GB10
- Success threshold: INT4 peak inference memory is at least 2.5x lower than FP16/BF16 weight memory contribution, latency regression is less than 2x or throughput improves, and quality proxy degradation remains within a predefined acceptable bound.
- Stop condition: Stop if the backend materializes full FP16 weights during forward, fails to run on GB10, or shows more than 2x latency regression with no compensating memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/aggressive-int4-quantization-for-home-gpu-vram-reduction-5b9927f75e8f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
