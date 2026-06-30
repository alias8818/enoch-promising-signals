# Bounded KV Cache: Learned Eviction vs LRU Baseline

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-kv-cache-learned-eviction-vs-lru-baseline-d623efb415b3`
Run ID: `bounded-kv-cache-learned-eviction-vs-lru-baseline-d623efb415b3-20260613T041402048126+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/3aa1f9434937

## What looked useful

Main capacity-32 run improved mean hit rate from 0.3520 for LRU to 0.3956 for learned eviction, closing 43.3% of the LRU-to-Belady gap. A shorter capacity sweep also favored learned eviction with hit-rate deltas of +0.0545, +0.0413, and +0.0527 at capacities 16, 32, and 64.

## Boundaries and scale limits

Trace-level CPU simulation only; no real transformer runtime, no GPU serving stack, no latency or model-quality measurement, and synthetic block-class metadata stands in for runtime-observable features.

## Claim scope

On deterministic synthetic KV-block request traces with local, topic, anchor, and distractor reuse classes, a small learned eviction score improves mean cache hit rate over LRU at capacities 16, 32, and 64, while remaining below Belady oracle.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but does not validate real transformer serving behavior or publication-grade latency/quality claims.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded direct-evidence follow-up on real small-model KV-cache traces using only runtime-observable features.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-model KV trace learned eviction vs LRU
- Success threshold: At least 3% absolute hit-rate improvement over LRU and non-worse output-quality metric across two cache capacities, with latency not degraded by learned scoring overhead.
- Stop condition: Stop if learned eviction fails to beat LRU by 1% absolute hit rate on two real-trace seeds or if scoring overhead eliminates latency gains.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-kv-cache-learned-eviction-vs-lru-baseline-d623efb415b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
