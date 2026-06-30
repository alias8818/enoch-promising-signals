# VM power-cut crash matrix for anchored hash-chain ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `vm-power-cut-crash-matrix-for-anchored-hash-chain-ledger-cae1c0e04b`
Run ID: `vm-power-cut-crash-matrix-for-anchored-hash-chain-ledger-cae1c0e04b-20260604T015640929506+0000`

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

- Parent run decision: Anchored crash-safe hash-chain ledger for small agents: enoch://control-plane/projects/anchored-crash-safe-hash-chain-ledger-for-small-agents-c2044f2e60/runs/anchored-crash-safe-hash-chain-ledger-for-small-agents-c2044f2e60-20260603T180313855351+0000
- Parent run decision: Hash-chain evidence ledger for small agents: enoch://control-plane/projects/hash-chain-evidence-ledger-for-small-agents-c7e2f2fe7ca5/runs/hash-chain-evidence-ledger-for-small-agents-c7e2f2fe7ca5-20260602T205920905641+0000

## What looked useful

Across 810 targeted split-window SIGKILL crash trials, all variants had pre-recovery torn-tail JSON errors and 0 post-truncation validation errors, with identical recovered-prefix statistics. Across 120 clean/mutation controls, anchored validation detected 15/15 prefix payload rewrites while the recomputed-CRC baseline detected 0/15.

## Boundaries and scale limits

This did not perform actual VM power removal, hypervisor reset, host page-cache loss, disk write-cache loss, reboot recovery, filesystem matrixing, or external anchor service persistence checks. Fsync ablations were measured only under SIGKILL process cuts on local files.

## Claim scope

In a local fixed-seed process hard-cut proxy, an anchored hash-chain append ledger and a CRC append-log baseline both reject torn tails and recover to the same valid prefix after truncation; the anchored chain additionally detects controlled prefix payload rewrites that a recomputed-CRC baseline accepts.

## Why it stopped

Medium local evidence supports the integrity mechanism but does not support the named VM power-cut crash claim; anchored hash-chain durability was identical to the real CRC append-log baseline under the tested process-cut proxy.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded deepening test should run the same matrix inside a VM with host-triggered hard poweroff/reset and disk cache mode controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Host-triggered VM hard-power crash matrix for anchored hash-chain ledger
- Success threshold: At least 500 targeted VM hard-power crash trials with 0 undetected accepted corruptions for anchored validation, explicit rollback/prefix rewrite detection advantage over baseline, and recovered-prefix durability metrics reported separately from integrity metrics.
- Stop condition: Stop if VM hard-power orchestration cannot produce reproducible crash cutpoints, if anchored validation accepts any corrupted or rollback state, or if its only advantage remains a synthetic mutation result without VM reboot evidence.

## Evidence references

- Artifact root: `<local-path>/projects/vm-power-cut-crash-matrix-for-anchored-hash-chain-ledger-cae1c0e04b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
