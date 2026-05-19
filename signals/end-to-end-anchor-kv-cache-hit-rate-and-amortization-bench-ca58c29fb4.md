# End-to-End Anchor KV Cache Hit-Rate and Amortization Benchmark

Status: `useful_signal`
Project ID: `end-to-end-anchor-kv-cache-hit-rate-and-amortization-bench-ca58c29fb4`
Run ID: `end-to-end-anchor-kv-cache-hit-rate-and-amortization-bench-ca58c29fb4-20260518T063422884903+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: End-to-End Anchor KV Cache Hit-Rate and Amortization Benchmark: internal_generated:end-to-end-anchor-kv-cache-hit-rate-and-amortization-bench-ca58c29fb4

## What looked useful

High anchor KV hit-rate can amortize prefill when reused anchors dominate per-request work; the benefit is workload-dependent and disappears or reverses when anchors are unique or decode/suffix work dominates.

## Boundaries and scale limits

Single model, synthetic prompts, sequential request loop, Hugging Face cache API, no production paged-KV allocator, no batching/concurrency, no real traffic trace, no eviction/memory-pressure study, and only next-token equivalence was checked.

## Claim scope

On a local GB10 using Qwen/Qwen3-0.6B with synthetic repeated-anchor prompts and sequential Hugging Face/PyTorch inference, real past_key_values anchor reuse achieved 96.875% anchor-token hit-rate and 2.10x-2.29x end-to-end speedup for long anchors with 1-token decode; the same method was only 1.03x for shorter anchors with 8-token decode and slower than baseline for unique-anchor controls.

## Why it stopped

Bounded local validation produced a useful mechanism signal but not direct publication-grade evidence for production serving workloads.

## Recommended next action

Run one final depth-4 deepen test in a real serving stack or paged-KV simulator using a public request trace, concurrency, batching, eviction pressure, and matched no-cache/prefix-cache controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Driven Paged-KV Anchor Cache Serving Benchmark
- Success threshold: At least 90% anchor-token hit-rate and at least 1.5x improvement in both p50 and p95 end-to-end latency versus no-cache at comparable throughput, with unique-anchor control speedup no greater than 1.05x.
- Stop condition: Stop as negative if repeated-anchor p95 speedup is below 1.2x, unique-anchor control shows similar speedup, or eviction/memory overhead eliminates the latency gain at the tested concurrency.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-anchor-kv-cache-hit-rate-and-amortization-bench-ca58c29fb4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
