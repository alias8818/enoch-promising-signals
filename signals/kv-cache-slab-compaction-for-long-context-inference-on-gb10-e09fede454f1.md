# KV-Cache Slab Compaction for Long-Context Inference on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-slab-compaction-for-long-context-inference-on-gb10-e09fede454f1`
Run ID: `kv-cache-slab-compaction-for-long-context-inference-on-gb10-e09fede454f1-20260630T081604516527+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/745fc4966091

## What looked useful

Confirmed mechanism: compact contiguous KV attention was 2.45x to 2.81x faster than per-step indexed gather at 16K capacity with 50-75% occupancy, amortizing copy cost in about 1.08-1.41 decode steps. At 16K capacity with only 4K active tokens, indexed gather was already close to compact attention and compaction needed about 17.6-20.5 decode steps to repay. A 32K probe restored 2.30x-3.10x speedups versus indexed gather across 25-75% occupancy with about 0.94-1.48 decode-step breakeven.

## Boundaries and scale limits

This is not an end-to-end LLM serving result. It does not test real paged-attention kernels, scheduler overhead, allocator fragmentation, batching, model accuracy, multi-layer KV caches, or production decode loops. Maximum probed capacity was 32K tokens in a synthetic single-query attention workload.

## Claim scope

On GB10 with PyTorch CUDA microbenchmarks over fp16 KV tensors shaped as tokens x 8 heads x 64 dims, one-time compaction of active KV entries from fragmented slabs into contiguous storage can materially reduce repeated single-query attention-step time compared with per-step indexed gather when absolute active-token counts are at least about 8K, and it reduces dense masked slab attention time whenever occupancy is below full capacity.

## Why it stopped

Closed as no-paper useful signal: proxy microbenchmark supports the compaction mechanism but does not provide end-to-end serving evidence.

## Recommended next action

Deepen with a bounded direct paged-attention or llama.cpp/vLLM-style decode harness on GB10 that includes multi-layer KV, batch scheduling, and compaction trigger overhead; stop treating this run as paper-ready because it is a synthetic mechanism result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 paged-attention decode harness for KV slab compaction triggers
- Success threshold: At least 15% median decode throughput improvement over the strongest uncompacted baseline in two or more long-context settings, with compaction overhead amortized within 8 decode steps and no correctness regression.
- Stop condition: Stop if end-to-end decode throughput improves by less than 5% in two calibrated settings, if compaction overhead fails to amortize within 32 decode steps, or if correctness diverges from the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-slab-compaction-for-long-context-inference-on-gb10-e09fede454f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
