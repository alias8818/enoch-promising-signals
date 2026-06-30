# Medium shared-filesystem crash-recovery confirmation for the evidence ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-shared-filesystem-crash-recovery-confirmation-for-t-d4f0511791`
Run ID: `medium-shared-filesystem-crash-recovery-confirmation-for-t-d4f0511791-20260611T052659393422+0000`

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

- Parent run decision: Crash-consistent evidence ledger under concurrent home-worker writes: enoch://control-plane/projects/crash-consistent-evidence-ledger-under-concurrent-home-wor-00ab05c0fa/runs/crash-consistent-evidence-ledger-under-concurrent-home-wor-00ab05c0fa-20260611T051609883848+0000
- Parent run decision: Lightweight Evidence Ledger for Home GPU Workers: enoch://control-plane/projects/lightweight-evidence-ledger-for-home-gpu-workers-b9da40e1e11d/runs/lightweight-evidence-ledger-for-home-gpu-workers-b9da40e1e11d-20260611T022906027415+0000

## What looked useful

Buffered JSONL that acknowledges before flush is unsafe under writer crashes; staged checksum recovery and SQLite WAL FULL were clean; simple flushed JSONL was also clean for process crashes, so the staged ledger's stronger machinery needs power-loss testing to show a decisive durability advantage.

## Boundaries and scale limits

Process-crash-only test on a local ext4 filesystem; no host power loss, reboot, distributed filesystem, NFS/SMB, disk cache, torn-write, kernel panic, multi-host, or long-duration stress validation.

## Claim scope

On one ext4 shared workspace with 6 local writer processes, fixed seeds, and SIGKILL writer crashes, a staged checksum evidence ledger recovered all acknowledged records with zero corrupt entries across 40 trials and 21,155 acknowledged records, matching SQLite WAL FULL on safety metrics.

## Why it stopped

Tier 2 process-crash confirmation produced useful mechanism support but did not establish publication-grade advantage over the flushed JSONL baseline and did not test real power-loss durability.

## Recommended next action

Stop as no-paper useful signal; run a bounded power-loss or block-device fault-injection follow-up comparing flushed JSONL, SQLite WAL FULL, and staged checksum fsync after crash-reboot recovery.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Power-loss fault injection for staged checksum evidence ledger durability
- Success threshold: staged_checksum_fsync and sqlite_wal_full have zero missing acknowledged records and zero corrupt accepted records while flushed_jsonl shows at least one reproducible missing acknowledged or corrupt accepted record under the same crash-reboot schedule.
- Stop condition: Stop if the fault-injection environment cannot reliably prove writes were interrupted after acknowledgement, or if all variants including flushed_jsonl remain clean across the fixed-seed crash-reboot schedule.

## Evidence references

- Artifact root: `<local-path>/projects/medium-shared-filesystem-crash-recovery-confirmation-for-t-d4f0511791`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
