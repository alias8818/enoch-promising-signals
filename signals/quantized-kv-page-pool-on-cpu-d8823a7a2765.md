# Quantized KV page pool on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-kv-page-pool-on-cpu-d8823a7a2765`
Run ID: `quantized-kv-page-pool-on-cpu-d8823a7a2765-20260530T083550916581+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/241613175b74

## What looked useful

Across 18 matrix cases, int8 pages reduced KV memory by 3.984x-3.999x versus fp32, had max output RMSE 0.000197, and were faster in 12/18 cases with median speedup 1.055x. Repeated 8192-token cases showed dim=128 speedups of 1.54x-1.63x and dim=256 speedups of 3.47x-4.04x, while dim=64 remained neutral to slower.

## Boundaries and scale limits

Single-process CPU-only C++ microbenchmark on synthetic random tensors; no real LLM activations, no fp16/bf16 production baseline, no end-to-end serving runtime, no batching, no page eviction/churn, no NUMA policy study, and no GPU/CPU transfer path.

## Claim scope

Bounded synthetic CPU benchmark of decode-style attention over logical KV pages shows per-page int8 K/V storage can reduce KV bytes by about 4x versus fp32 with low output error, and can be latency-neutral or faster for larger context/head-dimension cases; small/narrow cases can be slower.

## Why it stopped

No-paper closure: this run is a synthetic direct-kernel useful signal, not a full validation of production quantized KV page pools.

## Recommended next action

Run a bounded deepen test inside a small transformer inference path using real fp16/bf16 KV tensors, measuring logit drift/perplexity, memory, and end-to-end decode latency under page pressure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-activation fp16 baseline test for CPU quantized KV pages
- Success threshold: At least 1.8x measured KV memory reduction versus fp16/bf16 with perplexity/logit drift within a predeclared small tolerance and decode latency no worse than 1.25x baseline, or faster, on medium CPU contexts.
- Stop condition: Stop if real-activation quantization exceeds the quality tolerance or if end-to-end decode latency is worse than 1.5x baseline in repeated medium-context runs despite memory savings.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-kv-page-pool-on-cpu-d8823a7a2765`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
