# Filesystem crash-consistency matrix for atomic ledger compaction

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `filesystem-crash-consistency-matrix-for-atomic-ledger-comp-c18e481bce`
Run ID: `filesystem-crash-consistency-matrix-for-atomic-ledger-comp-c18e481bce-20260522T201232137528+0000`

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

- Parent run decision: Kill-Point Durability and Compaction Test for File-Backed Agent Ledger: enoch://control-plane/projects/kill-point-durability-and-compaction-test-for-file-backed-3ba9ef3648/runs/kill-point-durability-and-compaction-test-for-file-backed-3ba9ef3648-20260522T161816627621+0000
- Parent run decision: File-Backed Concurrent Small-Agent Ledger Rollback Test: enoch://control-plane/projects/file-backed-concurrent-small-agent-ledger-rollback-test-5ee92bd339/runs/file-backed-concurrent-small-agent-ledger-rollback-test-5ee92bd339-20260522T154144494293+0000

## What looked useful

The useful signal is a reproducible crash-consistency matrix showing the mechanism: file fsync alone is insufficient under conservative persistence rules, and deleting old ledger state before durable manifest switch is unsafe. The robust protocol requires fsyncing the new snapshot, renaming it, fsyncing the directory, fsyncing the new manifest, renaming it, fsyncing the directory, and only then deleting old log state.

## Boundaries and scale limits

No real block-device crash/reboot testing was possible in this unprivileged container. The result does not cover ext4/xfs/btrfs/f2fs journaling behavior, storage-controller writeback, actual kernel recovery, or concurrent ledger workloads.

## Claim scope

Deterministic protocol-level crash-state enumeration for an atomic ledger compaction model shows that unsafe rename-only, file-fsync-only, and delete-before-manifest protocols can produce unrecoverable crash images, while full file fsync plus directory fsync with deferred old-log deletion has zero modeled invariant failures across the tested profiles.

## Why it stopped

The run produced only model-based protocol evidence, not the requested Tier 4 paper-readiness replication across real filesystems. Local compute is not the blocker; missing privileged crash-injection storage infrastructure is the limiting factor.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful evidence; the next meaningful validation would require a separate privileged filesystem crash campaign, but no follow-up is recommended because the controller lineage is already at depth 4.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/filesystem-crash-consistency-matrix-for-atomic-ledger-comp-c18e481bce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
