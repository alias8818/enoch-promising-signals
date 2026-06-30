# KV Cache INT4 Quantization for Long Context Bounded Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-int4-quantization-for-long-context-bounded-memory-92ba7c955ac8`
Run ID: `kv-cache-int4-quantization-for-long-context-bounded-memory-92ba7c955ac8-20260605T210708743428+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/87c976834bf7

## What looked useful

INT4 KV-cache quantization provides real memory compression but the naive unfused path is latency-negative and outlier-sensitive. The result justifies a focused fused-kernel/backend follow-up rather than paper writing.

## Boundaries and scale limits

Synthetic one-token decode only; no real model perplexity, no serving runtime, no fused INT4 attention kernel, no allocator pressure test beyond tensors up to sequence length 8192, batch 1, 8 heads, head dimension 128.

## Claim scope

A simple packed INT4 KV-cache with FP16 per-group scales reduces synthetic KV-cache memory by 3.2x to 3.76x on GB10 test shapes, preserves normal-activation attention outputs roughly by cosine similarity near 0.99, but an unfused PyTorch dequantize-then-attend decode path is 3x to 12x slower than FP16 and outlier activations materially degrade output error.

## Why it stopped

No-paper proxy result: the tested mechanism saves memory but the unfused implementation is much slower than FP16 and synthetic outliers expose quality fragility; full validation would require fused-kernel and real-model evidence.

## Recommended next action

Implement or use a fused INT4 KV dequantization-plus-attention kernel and compare decode tokens/sec, output error, and memory residency against FP16 and INT8 baselines on the same GB10.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused INT4 KV-cache decode benchmark on GB10
- Success threshold: INT4 resident KV cache achieves at least 3x effective memory reduction including scales, decode latency is no more than 1.2x FP16 or is faster than INT8 at the same shape, and normal-activation attention cosine remains at least 0.99 with bounded outlier degradation.
- Stop condition: Stop if the fused/backend path remains more than 2x slower than FP16 at sequence length 8192 or if real-model/perplexity proxy degradation is clearly unacceptable under the same memory settings.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-int4-quantization-for-long-context-bounded-memory-92ba7c955ac8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
