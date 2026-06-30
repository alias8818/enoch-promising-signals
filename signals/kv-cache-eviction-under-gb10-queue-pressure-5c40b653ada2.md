# KV-cache eviction under GB10 queue pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-eviction-under-gb10-queue-pressure-5c40b653ada2`
Run ID: `kv-cache-eviction-under-gb10-queue-pressure-5c40b653ada2-20260605T145139376639+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0eb48d708acf

## What looked useful

Across smoke, pressure, calibrated, and mild-control runs, active-aware eviction had zero active KV evictions. In the calibrated overloaded run it completed 128/128 requests while naive LRU completed 22/128 with 408127 active evictions and FIFO completed 0/128 with 409279 active evictions. In the milder control, LRU completed with lower simulated latency but still incurred 97 active evictions, while active-aware avoided recompute at the cost of admission backpressure and higher p95 latency.

## Boundaries and scale limits

No real LLM serving stack, no production paged-attention implementation, no multi-tenant traffic, and no real token/sec or user-visible latency measurement; CUDA page writes and recompute kernels are proxies for KV memory pressure and recompute cost.

## Claim scope

Synthetic GB10 CUDA-resident KV-page benchmark: active-aware admission plus completed-page-first eviction prevents active KV recompute under queue pressure, while naive active-page eviction can cause severe recompute amplification and queue non-completion in overloaded traces.

## Why it stopped

Closed as no-paper useful signal: the mechanism is supported in a synthetic/proxy benchmark, but direct real-serving evidence is required before any paper claim.

## Recommended next action

Run a bounded direct GB10 serving-stack follow-up using vLLM or an equivalent paged-KV implementation with the same traces, measuring real token/sec, TTFT, latency, active-page eviction/preemption behavior, and MemAvailable telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GB10 paged-KV eviction test in a real serving stack
- Success threshold: Active-aware/default-active-protected behavior reduces active KV eviction or recompute/preemption events by at least 90% versus an active-evicting baseline while preserving completion and keeping p95 latency increase under 25% on the mild-load control.
- Stop condition: Stop if the serving stack already forbids active KV eviction and exposes no configurable active-evicting baseline, or if real-kernel measurements show no measurable recompute/preemption difference across policies under cache pressure.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-eviction-under-gb10-queue-pressure-5c40b653ada2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
