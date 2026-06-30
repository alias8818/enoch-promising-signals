# Int8 KV-Cache Quantization on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-kv-cache-quantization-on-cpu-a7805d3f6457`
Run ID: `int8-kv-cache-quantization-on-cpu-a7805d3f6457-20260523T062714465599+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1a2919369805

## What looked useful

Int8 KV cache reduced synthetic KV bytes to about 25.8-28.1% of float32. Output relative L2 error stayed around 0.7-1.2%. Throughput was mixed at small contexts but improved at longer contexts, including 1.57x speedup at seq=32768 dim=128 with 8 CPU threads.

## Boundaries and scale limits

No real LLM integration, no perplexity/task-quality measurement, no multi-layer accumulation test, no batching study, and no comparison against mature production CPU inference kernels.

## Claim scope

Synthetic CPU single-token decode-attention microbenchmark with per-token symmetric int8 K/V cache, int8 query-key dot products, dequantized int8 values, OpenMP parallelism, and context lengths up to seq=32768 dim=128.

## Why it stopped

No-paper closure: this run produced useful synthetic mechanism evidence, but not direct LLM-serving evidence or publication-grade validation.

## Recommended next action

Run a bounded direct integration in a small CPU LLM decoder and require lower memory/RSS plus no more than 1% perplexity degradation and at least 1.2x next-token latency improvement at long context before paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM Decoder Test for Int8 KV Cache
- Success threshold: At long context, at least 1.2x next-token latency improvement and clear KV memory reduction with no more than 1% perplexity degradation versus float KV.
- Stop condition: Stop if integrated int8 KV is slower than float KV at long context or causes more than 1% perplexity degradation after basic tuning.

## Evidence references

- Artifact root: `<local-path>/projects/int8-kv-cache-quantization-on-cpu-a7805d3f6457`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
