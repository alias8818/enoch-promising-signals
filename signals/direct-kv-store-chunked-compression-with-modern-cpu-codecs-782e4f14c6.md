# Direct KV-store chunked compression with modern CPU codecs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-kv-store-chunked-compression-with-modern-cpu-codecs-782e4f14c6`
Run ID: `direct-kv-store-chunked-compression-with-modern-cpu-codecs-782e4f14c6-20260605T191608715977+0000`

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

- Parent run decision: CPU-only KV compression for bounded evidence ledger storage: enoch://control-plane/projects/cpu-only-kv-compression-for-bounded-evidence-ledger-storage-200ef81d187f/runs/cpu-only-kv-compression-for-bounded-evidence-ledger-storage-200ef81d187f-20260605T142527054453+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/205a2aa29d04

## What looked useful

The direct Tier 1 test supports the mechanism that chunked compression can preserve large storage savings while avoiding whole-value decompression cost for partial KV reads, but only for compressible or semi-compressible values and only under local single-process conditions.

## Boundaries and scale limits

Synthetic deterministic values, LMDB only, one process, warm/local filesystem effects, no production traces, no concurrent mixed read/write workload, no cold-cache or network serving validation; incompressible values failed the space-saving condition.

## Claim scope

In a single-process LMDB KV-style store with deterministic semi-compressible 256 KiB values and random 4 KiB partial reads, independently compressed 16 KiB chunks using LZ4 or Zstandard saved about 75% disk versus raw storage and reduced p95 partial-read latency versus whole-value compression by 2.45x to 4.53x.

## Why it stopped

No-paper closure: the Tier 1 direct test produced a useful mechanism signal, but the evidence is too narrow and synthetic for publication readiness.

## Recommended next action

Run a bounded deepen follow-up with real or trace-derived KV values, a 4 KiB/16 KiB/64 KiB chunk-size sweep, and concurrent mixed read/write traffic; stop if chunked compression fails to save at least 30% disk while keeping p95 partial-read latency within 2x raw under concurrency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent trace-derived KV chunked compression validation
- Success threshold: At least one chunked codec/chunk-size setting saves >=30% disk versus raw, has p95 partial-read latency <=2x raw, and has p95 partial-read latency at least 2x faster than whole-value compression during concurrent traffic.
- Stop condition: Stop if no chunked setting meets the disk-saving threshold or if all chunked settings exceed 2x raw p95 partial-read latency under concurrency.

## Evidence references

- Artifact root: `<local-path>/projects/direct-kv-store-chunked-compression-with-modern-cpu-codecs-782e4f14c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
