# Memory-Bounded KV Cache Compression for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-bounded-kv-cache-compression-for-cpu-inference-1dfd7a58f290`
Run ID: `memory-bounded-kv-cache-compression-for-cpu-inference-1dfd7a58f290-20260607T160009524328+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/3a7b700e2be0

## What looked useful

Memory-bounded KV compression has a narrow mechanism signal on redundant/topic-like attention, including int8 compressed old chunks, but broad content-agnostic compression is not supported because retrieval-heavy traces failed with very low p05 cosine.

## Boundaries and scale limits

No real transformer was run; no perplexity, task accuracy, or production CPU serving benchmark was measured. Chunk-mean timing includes recomputation overhead and should be treated as a prototype upper bound, not optimized serving latency.

## Claim scope

On synthetic CPU attention traces up to seq_len 2048 and dim 64, naive recent-window and contiguous chunk-mean KV compression can preserve full-attention outputs on redundant topic-like traces at 16x-32x nominal cache byte reduction, but not on random or long-range needle traces.

## Why it stopped

No-paper useful signal: proxy evidence is mixed and early-falsifies the broad naive compression claim, though topic-like traces show a reproducible mechanism worth a bounded direct follow-up.

## Recommended next action

Run one bounded deepen follow-up in a small real CPU transformer with retrieval-aware retention and incremental compression; stop paper work for the current naive-policy result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Retrieval-Aware Bounded KV Compression in a Small CPU Transformer
- Success threshold: At least 8x measured KV memory reduction, no more than 2% relative perplexity or loss degradation on real text, at least parity decode throughput versus full KV, and retrieval task accuracy within 5 percentage points of full KV.
- Stop condition: Stop if retrieval-aware compression cannot beat recent-only on both retrieval quality and memory at seq_len 1024-2048, or if incremental compression makes CPU decode throughput worse than full KV by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/memory-bounded-kv-cache-compression-for-cpu-inference-1dfd7a58f290`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
