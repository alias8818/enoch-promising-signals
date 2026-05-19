# Process-kill SQLite WAL quorum cleanup under concurrent readers

Status: `useful_signal`
Project ID: `process-kill-sqlite-wal-quorum-cleanup-under-concurrent-re-4b10ee88e8`
Run ID: `process-kill-sqlite-wal-quorum-cleanup-under-concurrent-re-4b10ee88e8-20260517T214343364639+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Process-kill SQLite WAL quorum cleanup under concurrent readers: internal_generated:process-kill-sqlite-wal-quorum-cleanup-under-concurrent-re-4b10ee88e8

## What looked useful

Across smoke, medium, and stress validation, process-kill-aware quorum checkpointing reclaimed 0 WAL bytes while legitimate survivor readers remained active; ordinary TRUNCATE checkpoint reclaimed the WAL only after those readers exited, with clean integrity and row-count checks.

## Boundaries and scale limits

Tested up to 64 concurrent readers, 32 killed readers, 150000 post-snapshot writes, and 109752712-byte WAL files over 111 non-destructive trials; not a 24-hour soak, network filesystem test, or live-writer unsafe WAL deletion protocol.

## Claim scope

Local single-node SQLite WAL experiments with real OS reader processes, SIGKILL of half the readers, survivor readers holding old snapshots, and non-destructive checkpoint-based cleanup policies.

## Why it stopped

Direct bounded validation falsified the success threshold: quorum cleanup produced exactly 0 byte reclamation during active survivor readers in 111 non-destructive trials, including a 64-reader stress condition with a 109752712-byte WAL.

## Recommended next action

Stop this follow-up line for non-destructive quorum WAL cleanup under active readers; the direct mechanism failed at stress scale, and further work should change the problem to preventing long snapshots or designing a separately validated unsafe rewrite protocol.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/process-kill-sqlite-wal-quorum-cleanup-under-concurrent-re-4b10ee88e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
