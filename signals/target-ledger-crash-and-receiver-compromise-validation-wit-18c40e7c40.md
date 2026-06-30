# Target-ledger crash and receiver-compromise validation with filesystem fault injection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `target-ledger-crash-and-receiver-compromise-validation-wit-18c40e7c40`
Run ID: `target-ledger-crash-and-receiver-compromise-validation-wit-18c40e7c40-20260609T231631847885+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Disk-backed signed Merkle ledger durability and two-agent synchronization: enoch://control-plane/projects/disk-backed-signed-merkle-ledger-durability-and-two-agent-32bea5d5d6/runs/disk-backed-signed-merkle-ledger-durability-and-two-agent-32bea5d5d6-20260609T020905041154+0000
- Parent run decision: Process-kill durability and asymmetric-signature sync test for disk-backed Merkle ledger: enoch://control-plane/projects/process-kill-durability-and-asymmetric-signature-sync-test-55faf807a5/runs/process-kill-durability-and-asymmetric-signature-sync-test-55faf807a5-20260609T151845286522+0000

## What looked useful

Across 4,000 scenarios, the naive baseline failed to detect same-sequence receiver rewrites (0.0 detection rate), while the hash+receipt design detected all same-sequence rewrites in the clean filesystem condition (1.0 detection rate, mean 200 receipt mismatches). Under partial-last-write faults, hash recovery kept a valid prefix with 1.0 recovery success and exposed acknowledged-but-missing records through receipts; naive recovery failed integrity/parsing in that condition.

## Boundaries and scale limits

Synthetic Python harness only; not validated on ext4/xfs, real power loss, FUSE/dm-flakey, SQLite/RocksDB/WAL, distributed replication, production key boundaries, or a deployed target-ledger implementation.

## Claim scope

In a deterministic local filesystem-fault harness, a hash-chained receiver ledger with sender-held acknowledgement hashes detects crash-induced acknowledged-record loss and post-compromise same-sequence rewrites; a receiver-local ledger without external receipts does not provide receiver-compromise resistance.

## Why it stopped

No-paper useful signal: the local harness supports the mechanism only with sender-held anchored receipts and directly falsifies receiver-local-only compromise resistance, but it is not production filesystem evidence.

## Recommended next action

Stop paper escalation for this run; if continuing, validate the same receipt/auditor invariant against a real WAL-backed implementation under FUSE or dm-flakey filesystem fault injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: WAL-backed target-ledger validation under FUSE/dm-flakey crash faults
- Success threshold: Across at least 100 fixed-seed crash/compromise trials, the WAL-backed hash+receipt design recovers only valid prefixes, detects at least 99% of acknowledged-record loss or same-sequence rewrites, and beats the local-only baseline on rewrite detection by at least 90 percentage points.
- Stop condition: Stop if the real WAL-backed implementation silently accepts corrupted state, fails to detect same-sequence rewrites with external receipts, or cannot outperform the local-only baseline under the same injected faults.

## Evidence references

- Artifact root: `<local-path>/projects/target-ledger-crash-and-receiver-compromise-validation-wit-18c40e7c40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
