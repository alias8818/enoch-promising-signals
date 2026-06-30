# Bounded-memory trie with LRU eviction: speed/memory Pareto

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-memory-trie-with-lru-eviction-speed-memory-pareto-baedc5287d94`
Run ID: `bounded-memory-trie-with-lru-eviction-speed-memory-pareto-baedc5287d94-20260619T041158567624+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6dad8e1c9970

## What looked useful

Prefix lookup speed improved with capacity, but the tested trie used 8.73x to 15.29x more traced peak memory, had 0.024x to 0.047x dictionary insert throughput, and had much slower exact lookups.

## Boundaries and scale limits

Single-process CPU-only Python microbenchmark; synthetic keys only; no production replay traces, compressed radix trie, native implementation, concurrent workload, or end-to-end agent memory quality measurement.

## Claim scope

On a deterministic Python synthetic prefix-heavy memory benchmark, an object-per-character bounded LRU trie improved prefix p95 latency by 1.07x to 2.65x versus a bounded LRU dictionary scan baseline as capacity increased from 2000 to 16000, but did not improve the overall speed/memory Pareto frontier.

## Why it stopped

Early bounded falsification of the broad speed/memory Pareto claim for the tested implementation; useful prefix-speed signal remains but is not a full validation.

## Recommended next action

Stop this object-per-character trie path for paper claims; if continuing, test a compressed radix or array-backed bounded LRU trie against the same benchmark plus a replay trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed bounded LRU radix trie Pareto check
- Success threshold: At capacity 16000 or larger, compressed trie prefix p95 latency at least 2x faster than bounded LRU dictionary, peak memory no more than 2x dictionary, insert throughput at least 0.5x dictionary, and exact p95 no worse than 2x dictionary on both synthetic and replay-trace workloads.
- Stop condition: Stop if compressed trie peak memory remains above 4x dictionary or insert throughput remains below 0.25x dictionary after one bounded implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-memory-trie-with-lru-eviction-speed-memory-pareto-baedc5287d94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
