# Memory-Efficient Attention with KV Cache Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-efficient-attention-with-kv-cache-quantization-d4c8dad24f69`
Run ID: `memory-efficient-attention-with-kv-cache-quantization-d4c8dad24f69-20260612T214038337938+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/8016a2027f8b

## What looked useful

Int8 KV-cache quantization is the most promising next target: it gives a clear memory reduction with low attention-output drift in this bounded test. Int4 is risky without better scaling or error controls. Naive dequantization is too slow, so practical viability depends on fused quantized decode attention and real model activation tests.

## Boundaries and scale limits

No end-to-end language-model quality, perplexity, generation throughput, or fused quantized-kernel validation was run. Latency measurements use a naive dequantize/unpack-then-attend implementation and should not be interpreted as optimized serving performance.

## Claim scope

Single-token decode attention on NVIDIA GB10 with synthetic Gaussian and outlier-stressed KV tensors shows symmetric per-token/per-head int8 KV-cache quantization can reduce stored cache size by about 1.94x with relative L2 attention-output error below 0.009, while packed int4 reduces memory by about 3.76x but has much larger output error.

## Why it stopped

Closed as a no-paper useful signal: this worker produced direct attention-level memory/error/latency evidence, but model-quality and optimized-kernel evidence are still missing.

## Recommended next action

Run a bounded deepen follow-up using real KV activations from a small cached causal LM plus a fused or semi-fused int8 decode-attention path, measuring logit drift, perplexity, peak memory, and tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model int8 KV-cache quantization with optimized decode attention
- Success threshold: At 8192 or longer context, int8 KV cache reduces peak KV memory by at least 1.8x, keeps next-token KL/logit drift within a predeclared small threshold, and keeps decode tokens/sec at least 80% of FP16.
- Stop condition: Stop if real-model int8 logit drift is large enough to change top-token predictions frequently, or if optimized decode throughput remains below 80% of FP16 despite avoiding full K/V materialization.

## Evidence references

- Artifact root: `<local-path>/projects/memory-efficient-attention-with-kv-cache-quantization-d4c8dad24f69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
