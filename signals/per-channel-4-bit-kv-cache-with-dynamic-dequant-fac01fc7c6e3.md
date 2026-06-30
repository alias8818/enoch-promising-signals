# Per-Channel 4-Bit KV Cache with Dynamic Dequant

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-channel-4-bit-kv-cache-with-dynamic-dequant-fac01fc7c6e3`
Run ID: `per-channel-4-bit-kv-cache-with-dynamic-dequant-fac01fc7c6e3-20260604T133841820809+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6d9b13293951

## What looked useful

Packed per-channel INT4 KV cache achieved the expected roughly 4x storage reduction, but dynamic dequantization that materializes FP16 K/V dominated runtime and erased the memory-bandwidth benefit. The simple implementation is not a practical replacement for FP16 KV decode on this host; a fused packed-KV attention kernel is the bounded next test if the idea is pursued.

## Boundaries and scale limits

Direct evidence is limited to a single-token CUDA/PyTorch microbenchmark, random tensors, batch 1, 16 heads, head dim 128, context lengths up to 8192, and an unfused dequantize-then-attend implementation. It does not test a fused attention kernel, full transformer serving, paged KV cache layout, grouped query attention, or task/perplexity quality.

## Claim scope

On NVIDIA GB10, a straightforward PyTorch decode path that dynamically dequantizes packed per-channel signed INT4 K/V into FP16 before attention reduces KV storage to about 25% of FP16 but is 4.16x to 9.63x slower than FP16 decode attention for batch 1, 16 heads, head dim 128, and sequence lengths 256 to 8192, with relative L2 output error from 0.1778 to 0.2400.

## Why it stopped

Proxy/direct microbenchmark early falsification of the simple dynamic-dequant path: storage savings were real, but decode latency was 4.16x to 9.63x slower than FP16 and output error was non-trivial. This is not a full validation or a full rejection of fused INT4 KV cache designs.

## Recommended next action

Stop this unfused path as no-paper evidence; only pursue a bounded fused CUDA/Triton packed-KV attention follow-up that avoids materializing dequantized K/V.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused packed-INT4 KV decode attention without materialized dequantized K/V
- Success threshold: At sequence length 8192 or longer, fused INT4 packed-KV decode is at least 1.25x faster than FP16 baseline while using no more than 30% of FP16 KV storage and keeping relative L2 output error below 0.20 on the benchmark output.
- Stop condition: Stop if the fused implementation remains slower than FP16 by 10% or more at 8192 tokens, or if relative L2 output error is at least 0.25 after reasonable scale-granularity tuning.

## Evidence references

- Artifact root: `<local-path>/projects/per-channel-4-bit-kv-cache-with-dynamic-dequant-fac01fc7c6e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
