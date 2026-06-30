# Real Storage Crash-Recovery Attestation Test for Local-First Replicas

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-storage-crash-recovery-attestation-test-for-local-fir-deec61abdf`
Run ID: `real-storage-crash-recovery-attestation-test-for-local-fir-deec61abdf-20260612T101543576051+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Concurrent Replica Crash-Recovery Test for Local-First Evidence Attestation: enoch://control-plane/projects/concurrent-replica-crash-recovery-test-for-local-first-evi-120d5ce617/runs/concurrent-replica-crash-recovery-test-for-local-first-evi-120d5ce617-20260612T101013987234+0000
- Parent run decision: Baseline and Crash-Recovery Evaluation for Local-First Evidence Attestation: enoch://control-plane/projects/baseline-and-crash-recovery-evaluation-for-local-first-evi-ff2f17e0fe/runs/baseline-and-crash-recovery-evaluation-for-local-first-evi-ff2f17e0fe-20260612T100001059088+0000

## What looked useful

Across the final bounded run, attested_full completed 8/8 trials with 9600 requested writes, 5860 acknowledged writes, 256 crash injections, 0 acknowledged writes missing after recovery, 100% digest convergence, and 0 verification-error trials. The no_attestation_full control accepted tampered persisted state in 8/8 trials while converging in 0/8, and the unauthenticated_full rejection control produced verification errors in 8/8 trials.

## Boundaries and scale limits

Tested only on one GB10 host with local SQLite files, 8 fixed-seed trials per variant, 1200 requested writes per trial, 3 replicas, and process-kill crashes. It did not test power loss, kernel panic, disk/controller resets, filesystem fault injection, multi-device replication, large databases, compaction, schema migrations, or adversaries with the attestation key.

## Claim scope

Bounded local process-crash recovery for three SQLite-backed local-first replicas: row-level keyed attestation preserved all acknowledged writes and converged after repeated SIGKILL/restart cycles, and rejected unauthenticated/tampered persisted rows in the tested harness.

## Why it stopped

No-paper useful signal: direct process-crash and tamper evidence supports the mechanism locally, but real storage crash-recovery publication claims require power-loss or block-device fault-injection evidence beyond this run.

## Recommended next action

Run a bounded deepen test on a loopback block device or VM using dm-flakey/qemu power-cut fault injection to test whether the same attestation catches corruption or lost acknowledged writes under filesystem/device failure semantics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-Device Fault-Injection Attestation Test for SQLite Local-First Replicas
- Success threshold: For at least 8 fixed-seed fault-injection trials, the attested durable variant has zero missing acknowledged writes, zero false accepts of corrupted rows, and 100% convergence or explicit rejection; the no-attestation control accepts at least one divergent/corrupted recovered state.
- Stop condition: Stop as negative if any acknowledged write is silently lost or any corrupted/tampered row is accepted by the attested durable variant, or if the fault-injection platform cannot produce reproducible storage-level failures.

## Evidence references

- Artifact root: `<local-path>/projects/real-storage-crash-recovery-attestation-test-for-local-fir-deec61abdf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
