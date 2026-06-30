# Hash-Chained Tamper-Evident Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-tamper-evident-evidence-ledger-486b9313b67d`
Run ID: `hash-chained-tamper-evident-evidence-ledger-486b9313b67d-20260620T022240798599+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5b2f9aeee881

## What looked useful

Streaming append maintained 26284-71474 entries/s and verification maintained 35878-102985 entries/s in the bounded Python prototype. Hash-chain append cost about 3x plain JSONL append and verification cost about 7x plain JSONL scan. Mutation, deletion, and reorder were detected without anchors, but tail truncation verified cleanly unless an external length/head anchor was supplied. Naive tail-rescanning append was non-viable, dropping to about 1003 entries/s at only 1000 entries and causing the initial 10000-entry run to be stopped.

## Boundaries and scale limits

Tested only on local synthetic JSONL records at 100 and 10000 entries with target payload sizes of 512 and 4096 bytes. Did not test concurrent writers, crash recovery, fsync durability, trusted timestamping, digital signatures, real evidence schemas, remote storage, or adversaries who can replace both ledger and anchor.

## Claim scope

A single-process Python JSONL hash-chain ledger can detect payload mutation, middle deletion, and adjacent reorder at 100 and 10000 synthetic-entry scale, and can detect tail truncation only when verification includes an external anchor with expected length and head hash.

## Why it stopped

Bounded local evidence supports the mechanism only with an external anchor for rollback detection and falsifies the naive tail-rescanning append path; this is not publication-grade evidence.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should focus on crash-safe anchored persistence and concurrent append behavior rather than larger synthetic throughput alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-safe anchored evidence ledger with concurrent appenders
- Success threshold: Across at least 100 crash-injection trials and a 4-writer 10000-entry run, recovered ledgers verify cleanly up to the last acknowledged anchor, lose no acknowledged anchored entries, detect all simulated rollback/tail-truncation attempts after the last anchor, and keep append throughput within 5x plain JSONL.
- Stop condition: Stop if concurrent append produces unrecoverable duplicate indexes, corrupt JSONL entries, or any undetected rollback after an anchor; otherwise stop after the defined crash-injection and 4-writer workload completes.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-tamper-evident-evidence-ledger-486b9313b67d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
