# AdaptiveKV: Sliding Window KV Compression with Disk Offload for CPU Long-Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptivekv-sliding-window-kv-compression-with-disk-offload-for-cpu-long-context-cb8f48e52669`
Run ID: `adaptivekv-sliding-window-kv-compression-with-disk-offload-for-cpu-long-context-cb8f48e52669-20260620T030752969115+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e5d886975975

## What looked useful

The mechanism is conditionally viable for memory reduction but not robust or latency-competitive in this proxy. Page locality made AdaptiveKV match full-cache retrieval at 32k with 93.6% lower resident KV; IID keys exposed centroid routing failure, with only 0.1927 to 0.2667 top-1 match versus full-cache.

## Boundaries and scale limits

Tested only synthetic 16k/32k single-head dot-product retrieval with NumPy and compressed NPZ page files. No real transformer inference, model quality benchmark, optimized mmap/direct-I/O offload, batching, memory-pressure study, or 7B+ model validation was run.

## Claim scope

In a deterministic CPU retrieval proxy, AdaptiveKV-style recent exact KV plus int8 compressed disk pages reduced resident KV by about 93.6% at 32k tokens and recovered full-cache top-1 retrieval only when old KV pages had query-aligned page locality. Simple centroid routing was weak on IID keys, and the Python disk path was much slower than full-cache scanning.

## Why it stopped

Bounded proxy evidence is mixed: it supports the page-locality mechanism but early-falsifies a broad AdaptiveKV claim with centroid-only routing and unoptimized disk reloads. This is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; next, implement a direct transformer inference prototype with mmap binary pages and a stronger offloaded-page index before considering larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: AdaptiveKV mmap-page transformer prototype with stronger offload routing
- Success threshold: At 32k or longer context, achieve at least 90% of full-cache retrieval/task accuracy, at least 70% resident KV reduction, and less than 2x median decode latency versus full-cache on the tested CPU setup.
- Stop condition: Stop if the stronger index remains below 70% of full-cache accuracy on old-context queries or if optimized page loading remains above 5x median decode latency versus full-cache.

## Evidence references

- Artifact root: `<local-path>/projects/adaptivekv-sliding-window-kv-compression-with-disk-offload-for-cpu-long-context-cb8f48e52669`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
