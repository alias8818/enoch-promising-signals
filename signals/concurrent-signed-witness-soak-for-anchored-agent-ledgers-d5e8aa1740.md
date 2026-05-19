# Concurrent Signed Witness Soak for Anchored Agent Ledgers

Status: `useful_signal`
Project ID: `concurrent-signed-witness-soak-for-anchored-agent-ledgers-d5e8aa1740`
Run ID: `concurrent-signed-witness-soak-for-anchored-agent-ledgers-d5e8aa1740-20260519T182948897270+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Parent run decision: Persisted Multi-Process Witness Validation for Anchored Agent Ledgers: enoch://control-plane/projects/persisted-multi-process-witness-validation-for-anchored-ag-c8419f5d56/runs/persisted-multi-process-witness-validation-for-anchored-ag-c8419f5d56-20260519T175157286071+0000
- Parent run decision: Multi-Trace External-Witness Validation for Anchored Merkleized Agent Ledgers: enoch://control-plane/projects/multi-trace-external-witness-validation-for-anchored-merkl-600a7b18f0/runs/multi-trace-external-witness-validation-for-anchored-merkl-600a7b18f0-20260519T172758327087+0000

## What looked useful

Mechanism support is strong in the bounded harness: full signed witnesses achieved 100% fork detection and 100% forgery rejection with zero audit failures; anchor-only controls detected 0% of forks; unsigned controls rejected 0% of forgeries and accepted about 98% of forged entries. This isolates witness comparison as the fork-detection mechanism and signature verification as the authenticity mechanism.

## Boundaries and scale limits

Not a deployed distributed ledger validation. The run did not test crash recovery, durable database/storage corruption, network partitions, Byzantine witnesses, quorum-threshold sweeps, adversarial schedulers beyond seeded delay/shuffle, external timestamping or anchoring services, independent implementations, or overnight/production-duration operation.

## Claim scope

In a deterministic single-process Python harness with real Ed25519 signatures, 7 witnesses, quorum 4, randomized witness delays, shuffled concurrent submission, injected same-agent/same-seq forks, injected forged entries, and signed Merkle-style receipt anchors, the signed-witness-anchor mechanism detected all injected equivocations, rejected all forged entries, and produced zero receipt or anchor audit failures across medium and scaled local trials.

## Why it stopped

Mechanism supported by direct deterministic local evidence, but not paper-positive because the validation is a single-process synthetic harness rather than a real distributed anchored ledger. Follow-up is not recommended here because controller follow-up depth is already 4.

## Recommended next action

Stop under the strict paper gate and depth-4 cap; treat this as a reusable bounded harness, not a paper result. Any independent future campaign should port the mechanism to a real distributed persistent implementation and test crash/recovery, Byzantine witnesses, partitions, and external anchoring.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/concurrent-signed-witness-soak-for-anchored-agent-ledgers-d5e8aa1740`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
