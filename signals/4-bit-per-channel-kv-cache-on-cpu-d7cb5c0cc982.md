# 4-Bit Per-Channel KV Cache on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-per-channel-kv-cache-on-cpu-d7cb5c0cc982`
Run ID: `4-bit-per-channel-kv-cache-on-cpu-d7cb5c0cc982-20260607T054408832394+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4d064f2d90ca

## What looked useful

Memory compression is mechanically supported, but materializing fp32 K,V after unpacking erases CPU latency benefits and dequantization dominates runtime. Symmetric per-channel int4 also produced 0.19-0.41 relative-L2 output drift on synthetic decode cases.

## Boundaries and scale limits

No real LLM KV traces, perplexity, generation quality, batching, fp16/bf16 CPU latency baseline, or fused AVX2/AVX-512 int4 attention kernel was tested.

## Claim scope

Synthetic single-token decode attention on an Intel Xeon Silver 4114 CPU: packed signed int4 per-channel KV cache reduces KV memory by about 4x versus fp16-sized storage, but naive unpack/dequantize-to-fp32 execution is 2.5x-5.0x slower than fp32 attention and shows nontrivial output drift.

## Why it stopped

Bounded synthetic evidence is useful but not paper-ready: the memory mechanism works, while naive CPU dequantization is slower than fp32 and accuracy drift is too high for a broad claim.

## Recommended next action

Stop this naive implementation path; if continuing, implement a fused packed-int4 CPU attention kernel and validate against real model KV traces with perplexity or generation-quality controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU Packed-Int4 KV Attention on Real KV Traces
- Success threshold: At 4096-token or longer contexts, fused int4 decode is at least 1.2x faster than the best CPU baseline while using at least 3x less KV memory than fp16-sized storage and keeping quality degradation within a predeclared small threshold.
- Stop condition: Stop if the fused kernel remains slower than the baseline at 4096-token context or real-trace quality degradation exceeds the threshold.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-per-channel-kv-cache-on-cpu-d7cb5c0cc982`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
