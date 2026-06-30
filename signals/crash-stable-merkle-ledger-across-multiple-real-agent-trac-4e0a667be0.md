# Crash-stable Merkle ledger across multiple real agent trace sessions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `crash-stable-merkle-ledger-across-multiple-real-agent-trac-4e0a667be0`
Run ID: `crash-stable-merkle-ledger-across-multiple-real-agent-trac-4e0a667be0-20260607T152405257417+0000`

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

- Parent run decision: Persistent Merkle evidence ledger on real agent traces: enoch://control-plane/projects/persistent-merkle-evidence-ledger-on-real-agent-traces-25d665e69e/runs/persistent-merkle-evidence-ledger-on-real-agent-traces-25d665e69e-20260607T113719278486+0000
- Parent run decision: Merkle Agent Evidence Ledger: enoch://control-plane/projects/merkle-agent-evidence-ledger-5ddcac58453d/runs/merkle-agent-evidence-ledger-5ddcac58453d-20260607T073828825028+0000

## What looked useful

The mechanism worked on real agent traces: merkle_fsync had 100/100 prefix-correct truncation recoveries and 100/100 semantic tamper detections. Plain JSONL and SQLite WAL baselines did not detect semantic payload tampering; the no-payload-hash ablation also failed semantic tamper detection, supporting payload binding as the key mechanism.

## Boundaries and scale limits

Crash evidence is bounded to local file truncation/corruption injection and does not cover real power loss, kernel writeback reordering, full-disk behavior, concurrent multi-process writers, remote filesystems, or cross-machine replication.

## Claim scope

On 32 local real Enoch/Codex JSONL trace sessions containing 3,161 events, a payload-bound framed Merkle append ledger recovered verified prefixes under deterministic truncation faults and detected semantic payload tampering across fixed-seed trials.

## Why it stopped

No-paper useful signal: Tier 2 medium evidence supports the mechanism, but crash stability was tested with deterministic truncation/fault injection rather than direct power-loss or kernel-level crash behavior.

## Recommended next action

Run a bounded process-kill and filesystem fault-injection follow-up on a scratch mount to test real crash ordering, torn writes, and concurrent append recovery before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-kill and filesystem-fault validation for crash-stable Merkle trace ledger
- Success threshold: Merkle ledger achieves at least 99.9% verified-prefix recovery, 100% semantic tamper detection in targeted trials, no accepted forked roots under concurrent append attempts, and less than 10x throughput overhead versus plain JSONL on the same filesystem.
- Stop condition: Stop as negative if any verified-prefix recovery failure, undetected semantic tamper, accepted forked root, or unrecoverable writer-state corruption is observed in the fixed-seed process-kill/fault suite.

## Evidence references

- Artifact root: `<local-path>/projects/crash-stable-merkle-ledger-across-multiple-real-agent-trac-4e0a667be0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
