# Group-commit evidence ledger under disk and power-loss fault injection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `group-commit-evidence-ledger-under-disk-and-power-loss-fau-8c702723c6`
Run ID: `group-commit-evidence-ledger-under-disk-and-power-loss-fau-8c702723c6-20260608T000813945428+0000`

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

- Parent run decision: Concurrent evidence ledger crash-recovery probe: enoch://control-plane/projects/concurrent-evidence-ledger-crash-recovery-probe-318df51513/runs/concurrent-evidence-ledger-crash-recovery-probe-318df51513-20260607T192611922998+0000
- Parent run decision: Real-agent evidence ledger durability probe: enoch://control-plane/projects/real-agent-evidence-ledger-durability-probe-d0c0d4c8e8/runs/real-agent-evidence-ledger-durability-probe-d0c0d4c8e8-20260607T133648776921+0000

## What looked useful

Group commit had 0/100000 acknowledged-loss trials in the honest power-loss condition and 15035.57 mean entries/s versus 909.79 for per-entry fsync, a 16.52x throughput improvement at group size 16. Under disk-tail truncate/corrupt/zero faults it lost acknowledged entries in about 99.5% of trials while preserving prefix validity, so checksum commit metadata detects damage but does not provide disk-fault survival.

## Boundaries and scale limits

Power loss and disk-tail faults were simulated rather than induced by physical power cycling or dm-flakey/block-device fault injection. Filesystem throughput was measured only on the local /dev/drbd1032 workspace filesystem. The ledger model is append-only single-process and does not validate distributed evidence semantics.

## Claim scope

On a deterministic local crash-storage harness with 1.6M trials and a local fsync benchmark, group commit preserved acknowledged entries under honest power loss and improved throughput versus per-entry fsync, but single-copy group commit did not preserve acknowledged entries under durable-tail disk corruption/truncation.

## Why it stopped

Bounded validation supports the power-loss fsync-amortization mechanism but falsifies the stronger disk-fault survival claim for the tested single-copy design; this is not full physical power-loss validation and not paper-ready.

## Recommended next action

Stop this run as no-paper useful evidence; a next bounded deepen test should evaluate replicated commit records or mirrored segment footers under the same disk-tail fault model plus dm-flakey if available.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replicated group-commit footers for disk-tail fault survival
- Success threshold: Zero acknowledged loss under honest power loss, zero prefix violations under all tested faults, and <=1000 acknowledged-loss trials out of 100000 for each disk-tail fault mode while retaining at least 8x throughput over per-entry fsync.
- Stop condition: Stop if replicated metadata still loses acknowledged entries in more than 1000/100000 disk-tail fault trials for any tail fault mode, or if throughput drops below 8x the per-entry fsync baseline.

## Evidence references

- Artifact root: `<local-path>/projects/group-commit-evidence-ledger-under-disk-and-power-loss-fau-8c702723c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
