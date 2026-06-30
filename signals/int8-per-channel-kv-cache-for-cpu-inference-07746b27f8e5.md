# INT8 per-channel KV cache for CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-per-channel-kv-cache-for-cpu-inference-07746b27f8e5`
Run ID: `int8-per-channel-kv-cache-for-cpu-inference-07746b27f8e5-20260523T072003624646+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4041ebcdf4b0

## What looked useful

INT8 per-channel KV cache appears useful when CPU decode is memory-traffic dominated at long contexts, but dequantization overhead can erase gains at short contexts. Output drift versus FP32 attention was about 0.6% to 1.1% relative L2 with cosine above 0.99994 in this proxy.

## Boundaries and scale limits

Synthetic single-head attention only; no real transformer model, no end-to-end tokens/sec, no perplexity/logit-quality validation, no production int8 CPU kernels, no batching, and no multi-layer scheduling effects.

## Claim scope

In a single-threaded synthetic CPU decode-attention microbenchmark, per-channel INT8 K/V cache reduced KV cache footprint to about 25% of FP32 and improved long-context attention latency by 1.86x to 4.54x at tested large sequence lengths, while short-context cases were neutral or slower.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a synthetic microbenchmark, not full validation of real CPU inference.

## Recommended next action

Run a bounded deepen experiment by integrating per-channel INT8 KV cache into llama.cpp or ggml CPU decode and measuring tokens/sec, RSS, p50/p95 latency, and logit/perplexity drift on a small open model across short and long contexts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU decode validation for per-channel INT8 KV cache
- Success threshold: At contexts of at least 8192 tokens, achieve at least 1.25x decode tokens/sec improvement and at least 2.5x KV memory reduction with logit cosine at least 0.999 or perplexity degradation no more than 2% on the selected small open model.
- Stop condition: Stop if end-to-end decode speedup is below 1.10x at long context, if quality degradation exceeds the threshold, or if integration shows dequantization overhead dominates real CPU kernels.

## Evidence references

- Artifact root: `<local-path>/projects/int8-per-channel-kv-cache-for-cpu-inference-07746b27f8e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
