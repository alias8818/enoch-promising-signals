# Quantized KV-cache with mixed-precision for long-context inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-kv-cache-with-mixed-precision-for-long-context-inference-bac6c331baa8`
Run ID: `quantized-kv-cache-with-mixed-precision-for-long-context-inference-bac6c331baa8-20260605T162738408520+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/7be7d2f361d0

## What looked useful

Quantized old KV cache produced expected storage savings: int8 used about 52-53% of fp16 KV storage with low synthetic output error, and int4 used about 27-29% storage but higher random-query error. A 256-token fp16 recent window sharply reduced error in recent-salient probes, including int4 at 32k context from 0.116 to 0.00745 relative L2. The naive implementation was 9-18x slower than fp16 at 32k context, so practical serving viability requires a fused or otherwise optimized quantized-attention path.

## Boundaries and scale limits

No end-to-end LLM perplexity/task evaluation, no real KV traces, no batching/scheduler measurements, no RoPE/layer/head distribution study, and no fused quantized-attention kernel; latency reflects a naive PyTorch dequantize-then-attend implementation.

## Claim scope

Synthetic single-token GPU decode-attention probe on GB10 for batch=1, heads=8, head_dim=64, contexts up to 32768, comparing fp16 KV attention to grouped int8 or packed int4 old-cache quantization with optional fp16 residual windows.

## Why it stopped

Local synthetic evidence supports the accuracy mechanism but proxy latency early-falsifies the naive dequantize-then-attend implementation as a practical inference method; this is not a full validation or full rejection of optimized quantized-KV inference.

## Recommended next action

Run a bounded follow-up using a fused dequantize-attend kernel or optimized quantized-KV backend on real model KV traces, with success requiring memory reduction without more than 1.25x decode-latency regression and no material perplexity/task degradation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused quantized-KV decode attention on real model traces
- Success threshold: At least 2x KV-cache memory reduction, relative L2 attention-output error below 0.01 or model-quality delta within a predeclared tolerance, and mean per-token decode latency no worse than 1.25x fp16 baseline at 16k-32k context.
- Stop condition: Stop if optimized/fused quantized attention remains above 1.25x fp16 decode latency at 16k context or if int4/int8 mixed precision causes model-quality degradation outside the predeclared tolerance despite residual-window tuning.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-kv-cache-with-mixed-precision-for-long-context-inference-bac6c331baa8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
