# Prefix KV Deduplication for Batch Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prefix-kv-deduplication-for-batch-long-context-f182f8f1f1f0`
Run ID: `prefix-kv-deduplication-for-batch-long-context-f182f8f1f1f0-20260605T015001070281+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/47a251bb1026

## What looked useful

Across 32 shared-prefix cases, all outputs matched the duplicated-cache baseline; KV memory savings ranged from 60.0% to 96.50% with median 86.49%, and dedup was faster in 30/32 cases. A B=1 no-sharing control had 0% memory savings and median 1.412x latency overhead, indicating the benefit depends on actual duplicate prefixes.

## Boundaries and scale limits

Tested only a hand-written PyTorch microbenchmark on one GB10 with bfloat16, 16 heads, head dimension 64, batch sizes up to 32, prefix lengths up to 16384, and suffix lengths up to 256. Not tested in a production paged-attention kernel, full transformer serving loop, multi-token decode scheduler, or real request trace.

## Claim scope

Synthetic one-token CUDA decode attention for batches whose requests share an identical long prefix shows exact-output prefix KV deduplication can greatly reduce theoretical KV-cache memory and often reduce latency versus materializing duplicate prefix KV.

## Why it stopped

No-paper useful signal: this is direct synthetic attention evidence, not end-to-end serving validation or publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up that integrates prefix KV aliasing into a paged-attention or serving-cache prototype and replays mixed exact-prefix workloads before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paged-attention prefix KV aliasing under mixed shared-prefix traces
- Success threshold: At >=50% exact-prefix reuse and prefix length >=4096, reduce peak KV memory by >=50% while keeping decode tokens/sec within 95% of baseline or improving it; no-sharing workloads must not regress by more than 10%.
- Stop condition: Stop if paged-cache indirection causes >10% decode throughput regression at target reuse rates or if exact-prefix hit rates required for benefit are unrealistic under replayed traces.

## Evidence references

- Artifact root: `<local-path>/projects/prefix-kv-deduplication-for-batch-long-context-f182f8f1f1f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
