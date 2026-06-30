# KV Cache Compression for CPU-Bounded Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-compression-for-cpu-bounded-inference-2170028bcd69`
Run ID: `kv-cache-compression-for-cpu-bounded-inference-2170028bcd69-20260609T155214900888+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/11df40c64e18

## What looked useful

KV cache compression appears worthwhile for CPU-bounded long-context decode attention once KV memory traffic dominates: int8 KV plus float32 scales was 3.879x smaller than float32 KV and showed repeatable long-context speedups, especially in the single-thread control. This supports a bounded follow-up in a real CPU LLM runtime but is not paper-ready.

## Boundaries and scale limits

Synthetic kernel only; no full LLM inference runtime, no model perplexity or task-quality measurement, no batching sweep, no production CPU kernel integration, and no comparison against fp16/bf16 or specialized int8 dot-product implementations.

## Claim scope

In a local CPU decode-attention microbenchmark with 8 heads, head dimension 128, and contexts from 512 to 16384 tokens, symmetric per-token int8 KV cache compression reduced KV cache footprint by 3.879x versus float32 and improved single-thread decode-attention latency by about 2.0x-2.3x at 2048-16384 context with about 0.64%-0.70% relative L2 attention-output error.

## Why it stopped

The result is a useful bounded microbenchmark signal, but it is not full validation of CPU LLM inference and therefore should close as no-paper evidence.

## Recommended next action

Run a bounded real-runtime follow-up by integrating or emulating int8 KV cache in a CPU LLM inference stack and measuring tokens/sec, latency, memory, perplexity, and generation quality against float32/fp16/bf16 baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM Runtime Validation of Int8 KV Cache Compression
- Success threshold: At 8192-token or longer context, show at least 1.25x end-to-end decode tokens/sec improvement and at least 2.5x KV memory reduction with perplexity or task-quality degradation small enough to be operationally acceptable for the evaluated model.
- Stop condition: Stop if end-to-end decode speedup is below 1.10x at 8192-token context, or if quality/perplexity degradation is large enough that the compressed cache would not be usable.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-for-cpu-bounded-inference-2170028bcd69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
