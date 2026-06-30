# Hierarchical KV Offload for Local Cascade Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-kv-offload-for-local-cascade-routing-0be256dd6bb3`
Run ID: `hierarchical-kv-offload-for-local-cascade-routing-0be256dd6bb3-20260601T072831469959+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5734810fcadd

## What looked useful

Across 16 synthetic locality/capacity comparisons, cascade prefetch cut demand-stall latency to 0.630-0.784x of LRU, but increased transferred bytes to 1.345-1.651x of LRU; no-overlap latency was 1.346-1.652x of LRU. The mechanism is useful only if extra KV movement can be hidden or prediction precision improves substantially.

## Boundaries and scale limits

No real model router traces, no integrated paged-attention backend, no concurrent serving scheduler, and no end-to-end decode quality or throughput measurement. The run used 8000-step synthetic traces and a PyTorch copy microbenchmark on one GB10 host.

## Claim scope

On synthetic Markov local-cascade routing traces with 256 KiB KV-like blocks, local cascade prefetch reduces modeled demand stalls versus LRU only when prefetch transfers are assumed to overlap with compute or idle bandwidth; conservative no-overlap transfer accounting is worse than LRU.

## Why it stopped

Proxy evidence is mixed: demand misses improve under optimistic overlap, but transfer work reverses the result under conservative no-overlap accounting. This is an early bounded proxy result, not full validation.

## Recommended next action

Stop paper path for this run; next bounded evidence should be an integrated paged-KV microbenchmark that measures actual overlap and decode throughput instead of synthetic stall bounds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paged-KV Offload Overlap Microbenchmark for Local Cascade Prefetch
- Success threshold: Cascade prefetch improves p95 token latency or tokens/s by at least 10% versus LRU while increasing total transferred bytes by no more than 25%, with no correctness regressions in the decode output.
- Stop condition: Stop if measured no-overlap behavior dominates and p95 latency is not at least 5% better than LRU in the smallest integrated paged-KV benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-kv-offload-for-local-cascade-routing-0be256dd6bb3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
