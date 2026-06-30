# Bounded Suffix-Trie Prompt Lookup on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-suffix-trie-prompt-lookup-on-gb10-be06cb6ef626`
Run ID: `bounded-suffix-trie-prompt-lookup-on-gb10-be06cb6ef626-20260620T131633270981+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8e3db9ee8b8d

## What looked useful

Bounded reversed suffix tries were correct and much faster than direct scan. They were not uniformly faster than suffix-hash indexing, but at B=64 they improved p95 lookup latency and used less peak memory in the mostly unique-suffix control; shared suffixes also reduced trie build time at larger prompt counts.

## Boundaries and scale limits

No real prompt traces, no dynamic cache eviction workload, no tokenizer study, no LLM KV-cache integration, no GPU acceleration, and no end-to-end serving latency measurement. Python implementation only.

## Claim scope

Synthetic CPU data-structure benchmark for bounded longest-suffix lookup over integer-token prompts up to 50,000 prompts and B=64 on a GB10 worker host.

## Why it stopped

No-paper useful signal: this is a synthetic CPU-only data-structure result, not direct evidence for end-to-end prompt lookup or GB10 inference acceleration.

## Recommended next action

Run a bounded direct follow-up integrating trie and suffix-hash indexes into a small LLM prompt/KV-cache simulation with real or trace-like prompts, measuring cache-hit rate, time-to-first-token, and memory under dynamic insert/evict load.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded suffix lookup in a dynamic LLM prompt-cache simulation
- Success threshold: At equal cache capacity and match quality, trie p95 lookup latency is at least 25% lower than suffix-hash and added memory is not higher on a workload of at least 100,000 cache operations.
- Stop condition: Stop if trie lookup p95 is not at least 10% better than suffix-hash or if dynamic deletion/eviction makes memory or implementation complexity materially worse than suffix-hash.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-suffix-trie-prompt-lookup-on-gb10-be06cb6ef626`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
