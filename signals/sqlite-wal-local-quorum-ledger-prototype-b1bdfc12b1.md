# SQLite/WAL Local Quorum Ledger Prototype

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sqlite-wal-local-quorum-ledger-prototype-b1bdfc12b1`
Run ID: `sqlite-wal-local-quorum-ledger-prototype-b1bdfc12b1-20260517T212112551899+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bc7881660028

## What looked useful

SQLite WAL works as a per-replica append substrate in the controlled test, but the naive local quorum protocol is insufficient: exactly-quorum acknowledged records can lose read quorum after one of their two replicas is deleted, and partial unacknowledged writes leave sequence debris that harms progress.

## Boundaries and scale limits

Single-process local test only; 500 deterministic append attempts per scenario; no concurrent writers, process-kill fault injection, real power-loss testing, filesystem matrix, or distributed deployment.

## Claim scope

A local Python prototype using three SQLite WAL databases showed that all-replica acknowledged writes can be recovered and repaired after one replica loss, but quorum-only acknowledged writes under controlled partial-write faults cannot satisfy exact acknowledged-prefix recovery after losing one replica.

## Why it stopped

Direct Tier 1 controlled test falsified the naive quorum-ack durability threshold; this is not a full production validation, but it is a direct early falsification of the scoped mechanism.

## Recommended next action

Stop this run as a no-paper useful signal; next, test a revised prepare/commit plus repair-before-ack protocol against the same partial-write and one-replica-loss threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SQLite WAL Quorum Ledger With Prepare/Commit Cleanup
- Success threshold: For at least 500 deterministic mixed-fault append attempts, recover 100% of acknowledged records and 0 unacknowledged records before loss, after one-replica loss, and after repair.
- Stop condition: Stop if any acknowledged record is unrecoverable after one-replica loss, any unacknowledged record is promoted, or replicas cannot converge after repair.

## Evidence references

- Artifact root: `<local-path>/projects/sqlite-wal-local-quorum-ledger-prototype-b1bdfc12b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
