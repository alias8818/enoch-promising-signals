# Hierarchical 4-Bit KV Cache for CPU Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-4-bit-kv-cache-for-cpu-long-context-8a1e00fcb45c`
Run ID: `hierarchical-4-bit-kv-cache-for-cpu-long-context-8a1e00fcb45c-20260608T044636441147+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48a4ed233ae9

## What looked useful

Across 28 non-baseline cases, packed-cache compression versus fp32 ranged from 1.77x to 7.53x with median 7.35x; relative L2 output error ranged from 0.104 to 0.182 with median 0.137; hierarchical top-attention index matched fp32 in 14/14 cases, including old-token needle cases; latency was 2.97x to 36.34x slower than fp32 with median 19.33x slowdown.

## Boundaries and scale limits

Tested synthetic K/V tensors only, sequence lengths up to 131072, head dimension 128, one CPU worker, no real LLM traces, no perplexity/task quality, no multi-layer serving stack, and no fused packed-int4 AVX2/AVX-512 kernel.

## Claim scope

Bounded synthetic CPU single-token attention benchmark: hierarchical recent-fp32/old-int4 KV cache gives substantial theoretical packed-cache memory reduction and preserves deliberate old-token retrieval, but the tested NumPy dequantize-then-attend path is much slower than fp32 attention.

## Why it stopped

No-paper useful signal: the local synthetic benchmark supports memory savings and bounded old-signal preservation, but it early-falsifies the naive CPU dequantize-then-attend path as a viable long-context speed result and lacks real-model quality evidence.

## Recommended next action

Implement and benchmark a fused packed-int4 CPU attention kernel that dequantizes inside the dot-product path, then compare tokens/s, memory, and output error against fp32/bf16 baselines on real model KV traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused Packed-Int4 CPU Attention Kernel for Hierarchical KV Cache
- Success threshold: At 128k context and dim 128, hierarchical packed-int4 cache uses at least 6x less KV memory than fp32, has less than 2x median latency slowdown versus fp32/bf16 baseline, relative L2 output error below 0.15, and preserves old-needle top attention.
- Stop condition: Stop if the fused kernel remains more than 3x slower than the fp32/bf16 baseline at 32k context or if real-trace output error exceeds 0.20 before scaling to 128k.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-4-bit-kv-cache-for-cpu-long-context-8a1e00fcb45c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
