# Int4 KV Cache CPU Inference with Per-Channel Scaling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-kv-cache-cpu-inference-with-per-channel-scaling-dd6cacc7f5dc`
Run ID: `int4-kv-cache-cpu-inference-with-per-channel-scaling-dd6cacc7f5dc-20260531T134000930934+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/17ab5397eb0f

## What looked useful

Per-channel int4 KV gives about 7.8x-8.0x cache compression versus FP32, but scalar unpack/dequant overhead makes it slower through 4096 tokens for dim=128 and all tested lengths for dim=64. Long-context speedups appeared only at larger dim=256 from 4096 tokens onward and were mixed at dim=128/8192. Synthetic relative L2 output error was about 0.18-0.25.

## Boundaries and scale limits

Synthetic tensors only; no real transformer runtime, no real model activations, no quality benchmark, no SIMD-optimized int4 kernel, and no end-to-end decode measurement.

## Claim scope

Local CPU microbenchmark of one-head single-token attention over synthetic KV caches, comparing scalar FP32 KV with scalar packed signed int4 KV using per-channel scales.

## Why it stopped

This run produced a useful CPU microbenchmark signal, but the evidence is proxy/synthetic and mixed: compression is supported, broad latency benefit is not.

## Recommended next action

Run a bounded deepen test with AVX-512/SIMD int4 unpack-dequant kernels and real transformer KV activation traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SIMD and real-activation validation for int4 KV cache CPU decode
- Success threshold: At sequence length >=4096 and head dimension 128 or 256, int4 KV attention is at least 1.25x faster than the strongest optimized non-int4 CPU baseline with >=7.5x KV memory reduction and no material quality degradation on the chosen proxy.
- Stop condition: Stop if optimized int4 remains slower than baseline at 4096 and 8192 tokens, or if real-activation/model-quality error is too large to preserve generation quality.

## Evidence references

- Artifact root: `<local-path>/projects/int4-kv-cache-cpu-inference-with-per-channel-scaling-dd6cacc7f5dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
