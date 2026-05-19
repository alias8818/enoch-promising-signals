# Optimized Persistent Merkle KV Ledger With Crash-Restart Adversarial Persistence

Status: `useful_signal`
Project ID: `optimized-persistent-merkle-kv-ledger-with-crash-restart-a-9dcce7bc1b`
Run ID: `optimized-persistent-merkle-kv-ledger-with-crash-restart-a-9dcce7bc1b-20260518T010004168884+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Optimized Persistent Merkle KV Ledger With Crash-Restart Adversarial Persistence: internal_generated:optimized-persistent-merkle-kv-ledger-with-crash-restart-a-9dcce7bc1b

## What looked useful

The optimized prototype reached 1785.65 ops/s on the 5000-op medium comparison versus 122.41 ops/s for full snapshots and 175.79 ops/s for WAL plus full Merkle recompute; it also reached 1930.82 ops/s on a 100000-op optimized run. Clean recovery roots matched, and 2500 total injected optimized-WAL faults across medium and large runs recovered to valid committed prefixes.

## Boundaries and scale limits

Tested on one host with generated workloads up to 100000 commits and a 262144-leaf tree. Faults were post-hoc persisted-file truncation/corruption, not real power-loss or process-kill campaigns. No production KV engine, concurrency, deletes, checkpoint compaction, range proofs, or trace-derived workload was evaluated.

## Claim scope

In a local Python prototype using per-operation fsync, a CRC-framed append-only WAL with incremental Merkle path updates preserved prefix-consistent crash-restart recovery under injected WAL truncation/corruption and substantially outperformed full-snapshot and WAL/full-Merkle-recompute controls on synthetic fixed-seed workloads.

## Why it stopped

Evidence supports the mechanism in a bounded synthetic prototype but is not paper-positive because it lacks production baselines, real crash scheduling, and broader storage-engine functionality.

## Recommended next action

Stop this run as no-paper useful evidence; the concrete next bounded test is a production-baseline process-kill campaign against LMDB/RocksDB/SQLite-style persistence with deletes and checkpoints.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-baseline crash campaign for incremental Merkle WAL KV
- Success threshold: Across at least 500 real process-kill crash trials and 100000 committed operations, recover 100% to valid committed prefixes, achieve at least 3x throughput over the authenticated full-recompute control, and stay within 2x throughput of the unauthenticated production KV baseline.
- Stop condition: Stop if any committed-prefix recovery violation appears, if deletes/checkpoints cannot be made crash-consistent, or if throughput is less than 1.5x the authenticated full-recompute control after implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/optimized-persistent-merkle-kv-ledger-with-crash-restart-a-9dcce7bc1b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
