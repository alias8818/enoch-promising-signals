# Live append restart recovery for isolated ledger tailing

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `live-append-restart-recovery-for-isolated-ledger-tailing-1e380a0ab2`
Run ID: `live-append-restart-recovery-for-isolated-ledger-tailing-1e380a0ab2-20260518T213254346295+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Live append restart recovery for isolated ledger tailing: internal_generated:live-append-restart-recovery-for-isolated-ledger-tailing-1e380a0ab2

## What looked useful

The recovery mechanism is bounded and reproducible: exact restart recovery requires either an idempotent sink that absorbs replay or an atomic sink+cursor transaction boundary. Isolated tailing plus a separate cursor is insufficient under restart injection.

## Boundaries and scale limits

30 seeds x 300 records for the main and control restart conditions, plus a 20-seed no-crash control. Uses local file append, explicit fsync cursor persistence, deterministic injected restarts, and synthetic framed records. It does not include real process kill/restart, production ledgers, remote sinks, filesystem crash/power-loss testing, compaction, or multi-writer ledgers.

## Claim scope

In a deterministic local file-backed crash-injection harness for live append ledger tailing, exact restart recovery is not achieved by an isolated byte-cursor tailer alone. Cursor-before-sink loses records; sink-before-cursor duplicates records unless the sink is idempotent by stable record ID. A modeled atomic sink+cursor commit is a positive control.

## Why it stopped

Moderate direct local evidence supports a useful mechanism-level result but not publication readiness; the broad exact-recovery claim is unsupported without additional sink semantics.

## Recommended next action

Stop this follow-up at depth 4; use the result as no-paper engineering evidence that any future production claim must specify idempotent sink semantics or an atomic sink+cursor commit.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/live-append-restart-recovery-for-isolated-ledger-tailing-1e380a0ab2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
