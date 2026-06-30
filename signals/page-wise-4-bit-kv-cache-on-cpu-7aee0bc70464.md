# Page-wise 4-bit KV cache on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `page-wise-4-bit-kv-cache-on-cpu-7aee0bc70464`
Run ID: `page-wise-4-bit-kv-cache-on-cpu-7aee0bc70464-20260524T080842923440+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e35c100a1357

## What looked useful

Page-wise 4-bit KV on CPU can win in a direct attention microbenchmark once the float32 K/V working set is large enough and head dimensions are at least 128, but it loses for short contexts and small heads with scalar unpacking. The mechanism is plausible but requires runtime integration and optimized kernels before paper claims.

## Boundaries and scale limits

No full transformer runtime, real model activation distribution, perplexity/quality evaluation, fp16/bf16/int8 baseline, multi-layer paging allocator, or optimized SIMD int4 kernel was tested. Results are single-thread, single-process, synthetic float32 K/V on one Xeon Silver 4114 host.

## Claim scope

Local CPU microbenchmark of single-token attention over cached K/V using page-wise signed int4 quantization with one scale per page per tensor. At dim=128 and contexts of 16k to 65k tokens, the quantized path was 1.17x to 1.35x faster than float32 while compressing KV storage by about 8x; at 1k to 4k contexts it was slower. At dim=256 long-context speedup was about 1.27x; at dim=64 it was neutral to slower.

## Why it stopped

Evidence is a bounded synthetic microbenchmark with mixed outcomes, not publication-grade end-to-end model validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement an AVX2/AVX512 int4 dequant/dot kernel or integrate the cache into a CPU inference runtime and compare end-to-end against fp16/bf16/int8 KV baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SIMD and runtime validation for page-wise int4 CPU KV cache
- Success threshold: At contexts >=16k and head dimensions >=128, show at least 1.25x end-to-end decode speedup versus the strongest non-int4 CPU KV baseline with no material quality regression, while avoiding regressions for short contexts through gating.
- Stop condition: Stop if optimized/runtime int4 remains slower than int8 or fp16/bf16 baselines at long contexts, or if quality/perplexity degradation is material at 4-bit page scales.

## Evidence references

- Artifact root: `<local-path>/projects/page-wise-4-bit-kv-cache-on-cpu-7aee0bc70464`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
