# Kill-Point Durability and Compaction Test for File-Backed Agent Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `kill-point-durability-and-compaction-test-for-file-backed-3ba9ef3648`
Run ID: `kill-point-durability-and-compaction-test-for-file-backed-3ba9ef3648-20260522T161816627621+0000`

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

- Parent run decision: Real Small-Agent Evidence Ledger Rollback Harness: enoch://control-plane/projects/real-small-agent-evidence-ledger-rollback-harness-644b4e665f/runs/real-small-agent-evidence-ledger-rollback-harness-644b4e665f-20260522T145924343297+0000
- Parent run decision: File-Backed Concurrent Small-Agent Ledger Rollback Test: enoch://control-plane/projects/file-backed-concurrent-small-agent-ledger-rollback-test-5ee92bd339/runs/file-backed-concurrent-small-agent-ledger-rollback-test-5ee92bd339-20260522T154144494293+0000

## What looked useful

Corrected full validation ran 11,000 child-process kill trials across 500 fixed seeds, two variants, and 11 kill points. The safe_atomic protocol had 0/5,500 failures, 0 missing acknowledged records, and 0 corrupt committed lines. The unsafe_inplace baseline had 2,000/5,500 failures, 192,500 missing acknowledged records, and 1,000 corrupt committed lines, concentrated at partial append acknowledgment and destructive compaction kill points.

## Boundaries and scale limits

The test did not simulate power loss, kernel panic, storage write-cache loss, multiple filesystems, multi-writer concurrency, concurrent readers, very large ledgers, or realistic agent semantic replay workloads. Extra unacknowledged append records were allowed because ordinary process-kill tests do not model power-loss durability.

## Claim scope

On this CPU worker and local filesystem context, a single-writer file-backed ledger using fsync for acknowledged appends plus fsynced temp snapshot, atomic replace, directory fsync, and post-replace log truncation preserved all acknowledged records across 5,500 deterministic process-SIGKILL append/compaction trials with 128-record compaction inputs.

## Why it stopped

Bounded process-kill validation supports the mechanism but is not publication-grade crash-consistency evidence.

## Recommended next action

Stop this run as no-paper useful signal; next run should extend the same harness to filesystem crash-consistency testing with ext4/xfs variants, fsync ablations, and VM or dm-flakey power-fault style injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Filesystem crash-consistency matrix for atomic ledger compaction
- Success threshold: Safe protocol has zero missing acknowledged records and zero corrupt committed records across the filesystem crash matrix, while at least one ablation reproduces statistically clear failures at the expected write/replace/truncate kill points.
- Stop condition: Stop as negative if the safe protocol loses any acknowledged record or exposes corrupt committed records under the crash matrix, or if ablations do not distinguish the proposed mechanism from simpler baselines.

## Evidence references

- Artifact root: `<local-path>/projects/kill-point-durability-and-compaction-test-for-file-backed-3ba9ef3648`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
