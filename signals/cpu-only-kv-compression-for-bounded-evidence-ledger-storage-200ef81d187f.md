# CPU-only KV compression for bounded evidence ledger storage

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-only-kv-compression-for-bounded-evidence-ledger-storage-200ef81d187f`
Run ID: `cpu-only-kv-compression-for-bounded-evidence-ledger-storage-200ef81d187f-20260605T142527054453+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/205a2aa29d04

## What looked useful

Chunked zlib-6 at 128 records per chunk compressed the medium ledger proxy 3.537x with 47.7 MiB/s encode, 338.3 MiB/s full decode, and 0.777 ms random-read p95. Per-record zlib-6 reached only 1.833x, showing cross-record redundancy is the main mechanism. Low-entropy sensitivity reached 6.373-7.034x with zlib-6; high-entropy sensitivity still reached 2.208-2.274x. Bz2/lzma sometimes saved more bytes but imposed much worse CPU or random-read latency.

## Boundaries and scale limits

Tested up to 50,000 synthetic records and 67.690 MiB raw JSONL on a CPU worker; no production ledger corpus, embedded KV-store integration, concurrent append/read workload, compaction, retention aging, crash recovery, or multi-GB/full-retention validation was tested.

## Claim scope

On deterministic synthetic evidence-ledger KV records with repeated JSON schemas, run metadata, artifact hashes, commands, and mixed-entropy payloads, CPU-only chunked compression materially reduces bounded ledger storage versus raw JSONL and per-record compression while preserving millisecond-scale random reads.

## Why it stopped

The mechanism is supported by bounded synthetic/proxy evidence, but paper-grade claims require direct KV-store and real-trace validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the same chunked sparse-index design into a real embedded KV store and compare zstd/lz4/zlib on either production ledger traces or a trace-derived public surrogate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct KV-store chunked compression with modern CPU codecs
- Success threshold: At least 3x storage reduction versus raw ledger storage, p95 random-key read latency below 5 ms, and append throughput no worse than 25% below raw/uncompressed baseline on a direct KV-store workload.
- Stop condition: Stop as negative if real or trace-derived records compress below 2x at p95 random reads under 5 ms, or if append throughput drops more than 50% versus raw storage for all tested modern codecs and chunk sizes.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-only-kv-compression-for-bounded-evidence-ledger-storage-200ef81d187f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
