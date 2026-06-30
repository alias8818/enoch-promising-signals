# Blockwise KV cache quantization on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blockwise-kv-cache-quantization-on-cpu-c139cf6a281f`
Run ID: `blockwise-kv-cache-quantization-on-cpu-c139cf6a281f-20260609T022915268796+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9e27228b3cd6

## What looked useful

The memory/accuracy mechanism looks viable in a bounded synthetic probe: stored KV bytes drop almost 4x with low one-step attention drift. CPU performance depends strongly on implementation: full-cache dequantization is a clear negative path, while block-streaming reduces overhead and can approach fp32 in at least one medium-context case.

## Boundaries and scale limits

No real LLM, perplexity, task quality, production fused kernel, batching, p95 serving latency, framework integration, or real KV activation traces were tested. Python/NumPy streaming is a mechanism proxy and not an optimized CPU kernel. Results should not be generalized to 7B+ serving or publication-grade CPU inference claims.

## Claim scope

Synthetic CPU single-token decode attention with 8 heads, head dimension 64, sequence lengths 256-16384 for full-dequantization and 1024-8192 for streaming subset. Blockwise symmetric int8 K/V storage gives about 4x lower stored KV bytes and about 1.1%-1.4% relative L2 output drift versus fp32 K/V on normalized synthetic activations. Naive full-cache dequantization is consistently slower than fp32; block-streaming is more promising but only reached parity in one tested medium-context configuration.

## Why it stopped

No-paper useful signal: synthetic evidence supports memory reduction and low output drift, but direct real-model and optimized-kernel evidence is missing and the naive CPU full-dequantization path is too slow.

## Recommended next action

Stop paper progression for this run; next concrete step is a bounded fused C++/SIMD blockwise int8 attention implementation tested on real model KV traces for latency, memory, and quality drift.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU blockwise int8 KV attention on real model traces
- Success threshold: At 4k and 8k contexts, achieve at least 3.5x stored KV-cache reduction, no more than 1% perplexity degradation or an agreed task-quality drift bound, and decode latency no worse than 1.10x the fp32/fp16 KV baseline.
- Stop condition: Stop if the fused path remains more than 1.5x slower than baseline at both 4k and 8k contexts or if real-model quality drift exceeds 2% perplexity degradation under reasonable block sizes.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-kv-cache-quantization-on-cpu-c139cf6a281f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
