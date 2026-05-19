# Real trace restart recovery for isolated ledger tailing

Status: `useful_signal`
Project ID: `real-trace-restart-recovery-for-isolated-ledger-tailing-422e23e008`
Run ID: `real-trace-restart-recovery-for-isolated-ledger-tailing-422e23e008-20260518T212352688766+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Real trace restart recovery for isolated ledger tailing: internal_generated:real-trace-restart-recovery-for-isolated-ledger-tailing-422e23e008

## What looked useful

The direct controls separated the mechanism: a no-cursor seek-to-end baseline lost most post-crash entries, checkpoint-only preserved coverage but duplicated one batch per crash, and checkpoint plus rewind plus dedup preserved exact sink contents across 1M-event and full-trace validations.

## Boundaries and scale limits

Single public trace replayed locally; no live concurrent append workload, no production database WAL, no host or filesystem crash fault injection, and no multi-ledger replication scale.

## Claim scope

On a local file-backed append-only ledger built from the full NASA July 1995 request trace, an isolated tailer using durable byte checkpoints, bounded rewind, and an idempotent SQLite sink recovered from 400 forced SIGKILL restarts with zero missing and zero duplicate events.

## Why it stopped

Closed as a no-paper useful signal: the scoped local mechanism is supported, but external validity and novelty are insufficient for publication-grade evidence.

## Recommended next action

Run a bounded live-append validation against a real SQLite or Postgres-style ledger with concurrent producer, forced tailer SIGKILL, and independent reconciliation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live append restart recovery for isolated ledger tailing
- Success threshold: Across at least 5 fixed-seed runs and at least 1,000,000 produced events total, the proposed tailer has 0 missing source events, 0 duplicate sink events, and p95 restart catch-up under 2 seconds while both controls fail in their predicted modes.
- Stop condition: Stop negative if any proposed run has unreconciled missing or duplicate committed events, or if the mechanism requires a rewind bound larger than the retained ledger/WAL window under the configured workload.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-restart-recovery-for-isolated-ledger-tailing-422e23e008`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
