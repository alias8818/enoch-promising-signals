# SQLite WAL Quorum Ledger With Prepare/Commit Cleanup

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sqlite-wal-quorum-ledger-with-prepare-commit-cleanup-580bb7741c`
Run ID: `sqlite-wal-quorum-ledger-with-prepare-commit-cleanup-580bb7741c-20260517T212805372657+0000`

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

- Internal Enoch project: SQLite WAL Quorum Ledger With Prepare/Commit Cleanup: internal_generated:sqlite-wal-quorum-ledger-with-prepare-commit-cleanup-580bb7741c

## What looked useful

Across five fixed seeds, cleanup matched the no-cleanup prepare/commit ablation on acknowledged visible commits with zero lost acknowledged entries, zero phantoms, and zero divergent payloads, while reducing dangling prepared txids from mean 198 to 0 and partial committed txids from mean 72 to 0. Throughput was similar to no-cleanup but far below direct quorum and single SQLite WAL baselines.

## Boundaries and scale limits

Single-process synthetic workload; no OS process kill, power-loss testing, multi-process reader/writer contention, network partitioning, real multi-host deployment, or corrupted-file recovery. Operations were limited to 1500 append attempts per seed across five seeds.

## Claim scope

In a local five-replica SQLite WAL quorum harness with synchronous FULL transactions, fixed seeds, and injected interruption between protocol steps, prepare/commit cleanup removed all dangling prepared and partial committed transaction ids while preserving acknowledged quorum-visible commits.

## Why it stopped

Tier 2 local evidence supports the cleanup mechanism, but the evidence remains synthetic and not publication-grade; finalize as no-paper useful signal.

## Recommended next action

Run a real process-level crash/restart and concurrent reader/writer follow-up before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-kill SQLite WAL quorum cleanup under concurrent readers
- Success threshold: Across at least 10 fixed seeds and 100000 append attempts total, cleanup has zero lost acknowledged commits, zero phantom visible commits, zero divergent payloads, zero final dangling prepared or partial committed txids, and no more than 15% throughput overhead versus no-cleanup prepare/commit.
- Stop condition: Stop as negative if any acknowledged commit is lost, any phantom quorum-visible commit appears, divergent quorum payloads appear, or cleanup leaves persistent residue in two or more seeds.

## Evidence references

- Artifact root: `<local-path>/projects/sqlite-wal-quorum-ledger-with-prepare-commit-cleanup-580bb7741c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
