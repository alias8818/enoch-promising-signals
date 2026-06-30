# KV-Cache Eviction Prioritized by Queue Wait Time

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-eviction-prioritized-by-queue-wait-time-c9f07a135d2a`
Run ID: `kv-cache-eviction-prioritized-by-queue-wait-time-c9f07a135d2a-20260530T065423904410+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d04a9c2427be

## What looked useful

Wait-aware eviction consistently beat the best non-wait baseline by 47.3-95.2% p95 TTFT in the tested proxy and beat demand-only queue-aware eviction by 3.9-40.6%, indicating that accumulated queue wait can add value beyond queued-prefix demand alone.

## Boundaries and scale limits

No real model, GPU KV allocator, continuous batching runtime, production trace, multi-tenant scheduler, or serving-stack implementation was tested. Heavy-load cases are intentionally queue-stressed and should not be interpreted as production latency magnitudes.

## Claim scope

In a synthetic discrete-event LLM serving proxy with shared prompt prefixes, bounded prefix/KV cache capacity, FIFO service, Zipf prefix popularity, 12 seeds, 3 cache capacities, and 2 arrival rates, wait-aware eviction reduced p95 TTFT and recompute work relative to LRU, random, size-aware LRU, and demand-only queue-aware eviction.

## Why it stopped

No-paper closure: this run produced synthetic proxy evidence supporting the mechanism, but direct serving-stack evidence is required before making a paper or production claim.

## Recommended next action

Implement the policy as a bounded direct experiment in vLLM or another serving stack and replay realistic traces under GPU KV pressure, comparing against LRU, size-aware, and demand-only queue-aware eviction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct vLLM replay of wait-aware KV eviction under GPU cache pressure
- Success threshold: At least 10% p95 TTFT reduction versus both size-aware LRU and demand-only queue-aware eviction at two or more cache pressure levels, with throughput loss no greater than 3%.
- Stop condition: Stop if wait-aware eviction fails to beat demand-only queue-aware eviction by 5% p95 TTFT in two controlled serving-stack workloads or causes more than 3% throughput loss.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-eviction-prioritized-by-queue-wait-time-c9f07a135d2a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
