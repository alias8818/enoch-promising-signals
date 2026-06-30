# Concurrent evidence ledger crash-recovery probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `concurrent-evidence-ledger-crash-recovery-probe-318df51513`
Run ID: `concurrent-evidence-ledger-crash-recovery-probe-318df51513-20260607T192611922998+0000`

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

- Parent run decision: Evidence-Ledger CPU Agent: enoch://control-plane/projects/evidence-ledger-cpu-agent-f04c1a8e4fc7/runs/evidence-ledger-cpu-agent-f04c1a8e4fc7-20260607T063118526769+0000
- Parent run decision: Real-agent evidence ledger durability probe: enoch://control-plane/projects/real-agent-evidence-ledger-durability-probe-d0c0d4c8e8/runs/real-agent-evidence-ledger-durability-probe-d0c0d4c8e8-20260607T133648776921+0000

## What looked useful

Across 5 seeds and 8 concurrent workers, sqlite_wal, jsonl_lock_crc_fsync, and jsonl_lock_crc_no_fsync all had 0 missing acknowledged records and 0 corrupt records; the unsafe split-write ablation lost 10366 of 15396 acknowledged records and produced 10225 corrupt records.

## Boundaries and scale limits

Synthetic local filesystem benchmark only; no power-loss, disk-full, network filesystem, multi-host writer, long-duration, or production trace validation. The no-fsync variant is only supported for process crashes, not power failure.

## Claim scope

On a single local CPU worker using process-kill crash injection, locked single-write JSONL records with checksum envelopes recovered all acknowledged records across 5 fixed seeds, matching SQLite WAL on correctness; unlocked split writes failed reproducibly.

## Why it stopped

Tier 2 local evidence supports the process-crash mechanism but is not paper-positive because it excludes power-loss, disk-full, filesystem, multi-host, and long-duration durability validation.

## Recommended next action

Stop this run as no-paper useful evidence; run a bounded deepen test of batched/group-commit JSONL with disk-full and power-loss style fault simulation against SQLite WAL.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Group-commit evidence ledger under disk and power-loss fault injection
- Success threshold: Batched fsync JSONL has 0 missing acknowledged records and 0 corrupt records across all fixed seeds and fault classes, while achieving at least 50% of SQLite WAL throughput; no-fsync must fail or be explicitly scoped away under power-loss simulation.
- Stop condition: Stop if any locked/checksummed fsync JSONL variant loses an acknowledged record or produces corruption under a reproducible fixed-seed fault where SQLite WAL remains clean, or if valid power-loss/disk fault simulation cannot be run locally.

## Evidence references

- Artifact root: `<local-path>/projects/concurrent-evidence-ledger-crash-recovery-probe-318df51513`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
