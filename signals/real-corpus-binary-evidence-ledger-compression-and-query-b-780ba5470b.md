# Real-corpus binary evidence ledger compression and query benchmark

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `real-corpus-binary-evidence-ledger-compression-and-query-b-780ba5470b`
Run ID: `real-corpus-binary-evidence-ledger-compression-and-query-b-780ba5470b-20260523T033642865226+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-trace compressed evidence ledger audit benchmark: enoch://control-plane/projects/real-trace-compressed-evidence-ledger-audit-benchmark-4a02c5f08f/runs/real-trace-compressed-evidence-ledger-audit-benchmark-4a02c5f08f-20260523T030724663942+0000
- Parent run decision: Binary evidence ledger corpus benchmark against gzip and zstd controls: enoch://control-plane/projects/binary-evidence-ledger-corpus-benchmark-against-gzip-and-z-6a60939fbb/runs/binary-evidence-ledger-corpus-benchmark-against-gzip-and-z-6a60939fbb-20260523T032824454293+0000

## What looked useful

Binary ledger artifacts were consistently about 0.25x SQLite+FTS5 size and far faster than compressed-JSONL scans, but they were 1.33x larger than JSONL+gzip and 28x slower than SQLite+FTS5 term queries on the broad corpus. Smaller chunks improved lookup latency but worsened compression and still did not beat SQLite.

## Boundaries and scale limits

The run used local documentation corpora, Python implementation, zlib compression, read-only exact and term queries, and one worker host. It did not test zstd dictionaries, memory-mapped native implementations, update workloads, external web-scale corpora, or concurrent serving.

## Claim scope

A standard-library binary evidence ledger with zlib-compressed chunks and a varint term-posting index was benchmarked on local real documentation corpora up to 37,587 records / 7.149 MB UTF-8 text against JSONL+gzip and SQLite+FTS5.

## Why it stopped

Bounded real-corpus validation directly tested the compression/query threshold and found a mixed mechanism signal rather than a paper-ready result: compact versus SQLite, but worse than gzip for size and worse than SQLite for query latency.

## Recommended next action

Stop this branch as no-paper evidence; use SQLite+FTS5 when query latency matters, JSONL+gzip when compression-only archival matters, and this binary design only when a compact portable bundle smaller than SQLite is the primary requirement.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-binary-evidence-ledger-compression-and-query-b-780ba5470b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
