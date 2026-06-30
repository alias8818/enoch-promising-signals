# Prefix KV reuse router for CPU local serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prefix-kv-reuse-router-for-cpu-local-serving-25f824ddff05`
Run ID: `prefix-kv-reuse-router-for-cpu-local-serving-25f824ddff05-20260604T192532772861+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/cc28ee7c2dd8

## What looked useful

Prefix-aware routing cut uncached prompt tokens by 39.1%, 22.3%, and 9.6% on high, moderate, and low sharing steady-load traces, respectively, with p95 TTFT improving 6.2%, 6.1%, and 1.3%. Saturated-load throughput gains were only 0.2-0.3%, and no-reuse traffic was unchanged.

## Boundaries and scale limits

No real transformer, tokenizer, KV allocator, batching engine, HTTP/RPC server, or measured CPU model inference was run. Results use 4 simulated workers, 12,000 synthetic requests per scenario, fixed token costs, and a per-worker LRU prefix cache.

## Claim scope

Synthetic multi-worker CPU-local serving simulation with transparent token-cost model: a completion-time-aware prefix router reduces uncached prompt-prefill tokens and modestly improves TTFT on shared-prefix traces while matching least-ready behavior on no-reuse traces.

## Why it stopped

Closed as a no-paper useful signal because the mechanism is supported only by synthetic/proxy evidence and the end-to-end latency/throughput improvements are modest.

## Recommended next action

Run one bounded direct-serving follow-up with a small CPU LLM server and real prefix cache enabled, comparing least-ready versus prefix-aware routing on repeated system-prompt traffic.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM prefix-router validation
- Success threshold: At least 5% p95 TTFT improvement on repeated-prefix traffic, no more than 1% p95 latency regression on no-reuse traffic, and reproducible cache-hit telemetry explaining the gain.
- Stop condition: Stop if a smoke run cannot produce real prefix-cache hits, if no-reuse traffic regresses by more than 5%, or if repeated-prefix p95 TTFT improvement is below 2% after controlling for cache capacity and request ordering.

## Evidence references

- Artifact root: `<local-path>/projects/prefix-kv-reuse-router-for-cpu-local-serving-25f824ddff05`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
