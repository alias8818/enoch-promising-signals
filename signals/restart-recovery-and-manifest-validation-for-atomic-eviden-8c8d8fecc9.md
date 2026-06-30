# Restart recovery and manifest validation for atomic evidence ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `restart-recovery-and-manifest-validation-for-atomic-eviden-8c8d8fecc9`
Run ID: `restart-recovery-and-manifest-validation-for-atomic-eviden-8c8d8fecc9-20260528T010013221711+0000`

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

- Parent run decision: Real-trace crash and concurrency validation for CPU agent evidence ledgers: enoch://control-plane/projects/real-trace-crash-and-concurrency-validation-for-cpu-agent-e4a8419480/runs/real-trace-crash-and-concurrency-validation-for-cpu-agent-e4a8419480-20260527T221053264063+0000
- Parent run decision: Cryptographic Evidence Ledger for CPU Agent Tool Calls: enoch://control-plane/projects/cryptographic-evidence-ledger-for-cpu-agent-tool-calls-5e9b72700233/runs/cryptographic-evidence-ledger-for-cpu-agent-tool-calls-5e9b72700233-20260527T191941085746+0000

## What looked useful

Atomic hashed manifests had 0 accepted corrupt records and 0 lost committed records across 600 crash-only trials, while the non-atomic manifest baseline lost 38400 committed records and errored in 50% of crash-only trials. Hash validation was necessary under bit flips: removing hashes accepted corrupt records in 134/150 bitflip trials, matching the naive JSONL baseline, while the hashed manifest accepted none.

## Boundaries and scale limits

Tested 3600 local trials with 256 records per trial, one segment per trial, single-process writers, deterministic disk-state mutations, and simple JSONL/manifest baselines. Not validated with arbitrary process kills, concurrent writers, multi-segment compaction, filesystem matrix testing, SQLite WAL/LMDB, or production evidence-ledger integration.

## Claim scope

In a fixed-seed synthetic restart-recovery harness with small file-backed evidence ledgers, atomic replacement of a hashed manifest preserved committed records across crash-style temp/manifest interruption states and rejected media-corrupted segments instead of silently accepting corrupted evidence.

## Why it stopped

Tier-2 medium synthetic validation produced a useful mechanism signal, but it is not paper-positive because crash behavior was modeled by deterministic disk mutations and the baselines were simple file ledgers rather than production-grade storage systems.

## Recommended next action

Run a bounded process-kill validation on ext4 and xfs with randomized kill points, multi-segment append workloads, and SQLite WAL or LMDB as a stronger real baseline before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-kill filesystem validation for atomic hashed evidence manifests
- Success threshold: Zero accepted corrupted records and zero lost acknowledged records for crash-only kill trials, materially fewer silent corrupt acceptances than the no-hash ablation under corruption injection, and median write latency no more than 3x the SQLite WAL or LMDB baseline for the tested workload.
- Stop condition: Stop as negative if any reproducible crash-only process-kill case loses acknowledged records or accepts corrupted evidence in the atomic hashed-manifest variant, or if write latency exceeds 3x the stronger baseline without a compensating integrity advantage.

## Evidence references

- Artifact root: `<local-path>/projects/restart-recovery-and-manifest-validation-for-atomic-eviden-8c8d8fecc9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
