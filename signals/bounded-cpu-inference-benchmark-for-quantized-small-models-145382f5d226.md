# Bounded CPU Inference Benchmark for Quantized Small Models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-cpu-inference-benchmark-for-quantized-small-models-145382f5d226`
Run ID: `bounded-cpu-inference-benchmark-for-quantized-small-models-145382f5d226-20260609T055413792099+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/25069159f620

## What looked useful

TinyLlama-1.1B Q4_K_M used about 1.15 GiB peak RSS. Prompt processing rose from 18.79 tok/s at 1 thread to 114.60 tok/s at 8 threads. Generation improved through 7 threads, with 21.38 tok/s in the broad sweep and 24.36 tok/s under strict affinity, while 8 strict pinned threads dropped to 12.44 tok/s.

## Boundaries and scale limits

One host, one model family, one Q4 quantization, llama-bench only, short prompt/generation lengths, no serving-stack latency, no quality measurement, no multi-model or multi-quant robustness.

## Claim scope

On this 8-visible-logical-CPU Xeon Silver 4114 worker, TinyLlama-1.1B-Chat Q4_K_M GGUF runs comfortably in memory under llama.cpp and generation throughput is materially sensitive to thread count; 7 pinned threads outperformed 8 pinned threads in the bounded benchmark.

## Why it stopped

Closed as no-paper useful signal: direct bounded evidence exists, but it covers only one quantized model and benchmark harness, so it is not broad or robust enough for a paper.

## Recommended next action

Run a bounded deepen follow-up comparing Q4_K_M, Q5_K_M, and Q8_0 for the same model with pinned thread sweeps and one simple serving latency test.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization and thread-affinity sweep for TinyLlama CPU inference
- Success threshold: At least two quantizations reproduce a best pinned thread count below 8 with >=15% generation throughput or p95 latency advantage over 8 threads.
- Stop condition: Stop if Q5/Q8 downloads or benchmarks exceed the bounded CPU budget, or if repeated pinned runs show less than 5% difference between best thread count and 8 threads.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-cpu-inference-benchmark-for-quantized-small-models-145382f5d226`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
