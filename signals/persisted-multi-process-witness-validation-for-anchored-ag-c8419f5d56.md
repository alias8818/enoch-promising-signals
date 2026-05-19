# Persisted Multi-Process Witness Validation for Anchored Agent Ledgers

Status: `useful_signal`
Project ID: `persisted-multi-process-witness-validation-for-anchored-ag-c8419f5d56`
Run ID: `persisted-multi-process-witness-validation-for-anchored-ag-c8419f5d56-20260519T175157286071+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Parent run decision: Multi-Trace External-Witness Validation for Anchored Merkleized Agent Ledgers: enoch://control-plane/projects/multi-trace-external-witness-validation-for-anchored-merkl-600a7b18f0/runs/multi-trace-external-witness-validation-for-anchored-merkl-600a7b18f0-20260519T172758327087+0000

## What looked useful

Persisted independent witnesses provided a robust mechanism-level tamper signal: baseline attack detection was 0.0, witness attack detection was 1.0, witness clean false-positive rate was 0.0, restarted witnesses recovered from persisted state, and one deleted witness DB still left enough quorum evidence to detect tampering. The main measured cost was throughput dropping to about 37.6% of baseline and p95 append latency increasing from about 0.17 ms to about 0.65 ms in the 100k-event grid.

## Boundaries and scale limits

Evidence is local and synthetic: no real agent traces, no concurrent multi-agent writers, no networked witnesses, no cryptographic signatures, no public/external timestamp anchors, no Byzantine witness model, and no full 24-hour soak or host-crash fault injection.

## Claim scope

In a local SQLite/WAL synthetic ledger with three independent persisted witness processes and quorum=2, persisted witness validation detected all tested ledger rewrite, delete, truncate, witness-restart, and one-witness-loss scenarios across 3.5M total generated events, while a single-process hash-chain baseline accepted all tested rehashed attacks.

## Why it stopped

Closed as no-paper useful signal: the scoped local mechanism is supported, but the run lacks real/concurrent agent workloads, cryptographic identity, external anchors, Byzantine/network faults, and a full soak needed for publication-grade anchored-ledger claims.

## Recommended next action

Run one bounded deepen validation with concurrent multi-agent writers, signed witness attestations, external append-only anchors, and crash/corruption fault injection; otherwise stop because the current result is useful mechanism evidence but not paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent Signed Witness Soak for Anchored Agent Ledgers
- Success threshold: Attack detection rate must be 1.0, clean false-positive rate must be <= 0.001, no accepted clean event may lose quorum after recovery, sustained throughput must be >= 1,000 events/s, and p95 append latency must be < 5 ms.
- Stop condition: Stop and finalize negative if any attack class is accepted by witness-backed validation, clean false positives exceed 0.001, quorum recovery loses accepted clean events, or throughput/latency misses the threshold by more than 20% after implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/persisted-multi-process-witness-validation-for-anchored-ag-c8419f5d56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
