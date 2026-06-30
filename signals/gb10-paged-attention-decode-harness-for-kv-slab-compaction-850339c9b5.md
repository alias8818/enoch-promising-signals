# GB10 paged-attention decode harness for KV slab compaction triggers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gb10-paged-attention-decode-harness-for-kv-slab-compaction-850339c9b5`
Run ID: `gb10-paged-attention-decode-harness-for-kv-slab-compaction-850339c9b5-20260630T085822114994+0000`

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

- Parent run decision: KV-Cache Slab Compaction for Long-Context Inference on GB10: enoch://control-plane/projects/kv-cache-slab-compaction-for-long-context-inference-on-gb10-e09fede454f1/runs/kv-cache-slab-compaction-for-long-context-inference-on-gb10-e09fede454f1-20260630T081604516527+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/745fc4966091

## What looked useful

The interval-1 control showed compaction itself is not faster when paid every step, but reusing a compacted dense live-KV layout across future decode steps substantially reduced measured runtime in this bounded CUDA harness with exact output agreement.

## Boundaries and scale limits

Synthetic fixed-page KV slabs only; no real paged-attention backend, request scheduler, allocator fragmentation, page-table kernel, or end-to-end model serving trace was tested. The baseline intentionally models repeated sparse live-page gathers and may be weaker than an optimized backend-native implementation.

## Claim scope

On GB10, in a synthetic PyTorch CUDA SDPA decode harness where a baseline gathers live KV pages from a sparse slab on every decode step, trigger-based compaction is useful only when the compaction cost is amortized across later decode steps. Interval 1 gave no material speedup; intervals 4, 16, and 64 averaged 2.67x, 4.90x, and 6.23x over repeated per-step gathers for the tested 512-page shapes.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only despite a clear mechanism and correctness-preserving speedup in the local harness.

## Recommended next action

Run a bounded deepen follow-up inside a real paged-attention backend or trace replay and compare a trigger policy against the backend-native page-table baseline for per-token latency, throughput, memory pressure, and compaction overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Backend-native KV slab compaction trigger replay for paged attention
- Success threshold: At least 10% median per-token latency reduction or throughput increase on churned decode traces with no correctness regression and compaction overhead under 5% of decode wall time.
- Stop condition: Stop if the backend-native baseline already avoids repeated sparse gathers or if trigger overhead erases the latency/throughput gain across two representative churn traces.

## Evidence references

- Artifact root: `<local-path>/projects/gb10-paged-attention-decode-harness-for-kv-slab-compaction-850339c9b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
