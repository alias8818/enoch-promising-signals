# Binary evidence ledger corpus benchmark against gzip and zstd controls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `binary-evidence-ledger-corpus-benchmark-against-gzip-and-z-6a60939fbb`
Run ID: `binary-evidence-ledger-corpus-benchmark-against-gzip-and-z-6a60939fbb-20260523T032824454293+0000`

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

- Parent run decision: Real-trace compressed evidence ledger audit benchmark: enoch://control-plane/projects/real-trace-compressed-evidence-ledger-audit-benchmark-4a02c5f08f/runs/real-trace-compressed-evidence-ledger-audit-benchmark-4a02c5f08f-20260523T030724663942+0000
- Parent run decision: Compressed Agent Evidence Ledger: enoch://control-plane/projects/compressed-agent-evidence-ledger-29c1b399cf1c/runs/compressed-agent-evidence-ledger-29c1b399cf1c-20260523T022605364766+0000

## What looked useful

The benchmark met the predeclared <=0.90 size threshold against JSONL+zstd-6 on every fixed seed, averaging 0.709x the baseline. Ablations showed payload dictionarying and columnar varint layout both contributed; raw binary alone did not beat compressed JSONL.

## Boundaries and scale limits

Synthetic ledger data only; no public production ledger corpus, no independent codec implementation, no end-to-end query/audit workload, and no multi-GB or operational storage validation.

## Claim scope

On a deterministic synthetic evidence-ledger corpus of five 50,000-record fixed-seed shards, a columnar binary ledger encoding compressed with real zstd-6 averaged 50.279 bytes/record versus 70.882 bytes/record for canonical JSONL compressed with zstd-6, with successful binary decode checks.

## Why it stopped

Medium synthetic evidence supports the storage mechanism but does not provide external-corpus or operational evidence required for a paper.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete test is to repeat the same benchmark on a real released ledger/audit/event corpus with query and verification latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus binary evidence ledger compression and query benchmark
- Success threshold: Binary columnar+zstd-6 <= 0.85 * JSONL+zstd-6 bytes on the real corpus, with decode success and simple query throughput no worse than 2x JSONL parse/query time.
- Stop condition: Stop if the real corpus result is >0.95x JSONL+zstd-6 size or if decode/query overhead exceeds 2x without an offsetting storage gain.

## Evidence references

- Artifact root: `<local-path>/projects/binary-evidence-ledger-corpus-benchmark-against-gzip-and-z-6a60939fbb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
