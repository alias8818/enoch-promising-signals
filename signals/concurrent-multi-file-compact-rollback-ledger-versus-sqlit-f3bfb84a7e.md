# Concurrent multi-file compact rollback ledger versus SQLite WAL for tool-wrapper crashes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `concurrent-multi-file-compact-rollback-ledger-versus-sqlit-f3bfb84a7e`
Run ID: `concurrent-multi-file-compact-rollback-ledger-versus-sqlit-f3bfb84a7e-20260609T152855279107+0000`

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

- Parent run decision: Durable compact rollback ledger for real tool-wrapper crashes: enoch://control-plane/projects/durable-compact-rollback-ledger-for-real-tool-wrapper-cras-3787ec8079/runs/durable-compact-rollback-ledger-for-real-tool-wrapper-cras-3787ec8079-20260609T103345305082+0000
- Parent run decision: Rollback Ledger: Recovery Logging for Tool Errors: enoch://control-plane/projects/rollback-ledger-recovery-logging-for-tool-errors-f91053ffd9e7/runs/rollback-ledger-recovery-logging-for-tool-errors-f91053ffd9e7-20260609T031113668928+0000

## What looked useful

The compact rollback ledger recovered correctly in 1,200 injected crash/recovery transactions with zero throughput worker exits, while the unsafe no-rollback control failed every condition. SQLite WAL rollback metadata also recovered correctly but had 832 no-crash throughput worker exits from sqlite3 OperationalError disk I/O errors, making the practical baseline result mixed and not paper-ready.

## Boundaries and scale limits

No power-loss testing, no ext4/NVMe or tmpfs replication, no production trace workload, and SQLite WAL failures may be specific to the /mnt/usb project filesystem or process model.

## Claim scope

Bounded local Python harness with synthetic multi-file tool-wrapper transactions, process-crash injection, rollback recovery, fixed seeds, SQLite WAL rollback-metadata baseline, fsync-off ledger ablation, and no-rollback control.

## Why it stopped

Medium local evidence supports the ledger mechanism and the no-rollback failure mode, but the SQLite WAL throughput result is environment-sensitive and the run lacks power-loss and alternate-filesystem replication.

## Recommended next action

Stop the paper path for this run; rerun the exact SQLite WAL versus ledger harness on local ext4/NVMe and tmpfs to separate filesystem-specific WAL I/O errors from design-level concurrency fragility.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Filesystem-controlled SQLite WAL versus compact rollback ledger crash harness
- Success threshold: Ledger has zero correctness failures and zero throughput exits across all conditions; SQLite WAL result is classified by whether it has zero throughput exits on ext4/tmpfs or repeats the disk I/O failure pattern.
- Stop condition: Stop if SQLite WAL succeeds on ext4/tmpfs, because the current WAL failure should then be treated as filesystem-specific; also stop if ledger shows any recovery correctness failure.

## Evidence references

- Artifact root: `<local-path>/projects/concurrent-multi-file-compact-rollback-ledger-versus-sqlit-f3bfb84a7e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
