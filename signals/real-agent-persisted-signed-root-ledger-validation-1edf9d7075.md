# Real-agent persisted signed-root ledger validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `88`
Project ID: `real-agent-persisted-signed-root-ledger-validation-1edf9d7075`
Run ID: `real-agent-persisted-signed-root-ledger-validation-1edf9d7075-20260523T165658261392+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `88`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Agent Trace Checksum Ledger On Real Tool-Call Logs: enoch://control-plane/projects/agent-trace-checksum-ledger-on-real-tool-call-logs-f301133575/runs/agent-trace-checksum-ledger-on-real-tool-call-logs-f301133575-20260523T155049683887+0000
- Parent run decision: Live signed-root checksum ledger for agent tool-call traces: enoch://control-plane/projects/live-signed-root-checksum-ledger-for-agent-tool-call-trace-522d69f843/runs/live-signed-root-checksum-ledger-for-agent-tool-call-trace-522d69f843-20260523T164725208271+0000

## What looked useful

Signed persisted roots detected content edits, forged truncate/reanchor, and fork replacement in 1500/1500 relevant trials, while unsigned and hash-only baselines failed expected controls. The same signed-root mechanism detected rollback to an older valid signed snapshot in 0/500 trials, showing that signed roots alone do not validate freshness under filesystem rollback.

## Boundaries and scale limits

The workload is synthetic rather than integrated with a production agent framework; validation is local filesystem persistence only and does not include external transparency logs, TPM/TEE counters, remote timestamping, quorum storage, or datacenter-scale agent traffic.

## Claim scope

Local persisted agent-session ledgers with Ed25519-signed roots over session id, length, and rolling content root, tested on fixed-seed synthetic real-agent-like append traces with on-disk checkpoints and restart verification.

## Why it stopped

Bounded direct validation found a mechanism boundary: persisted signed roots provide integrity against unsigned tampering but cannot prove freshness after replay of an older ledger plus its valid older signed root.

## Recommended next action

Stop this standalone signed-root claim; the next concrete test should add an external monotonic or append-only latest-root anchor and rerun the same rollback/fork/tamper matrix.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Monotonic anchored signed-root ledger rollback validation
- Success threshold: Signed-root-plus-monotonic-anchor detects at least 499/500 rollback replays and at least 499/500 of each tamper/fork/reanchor attack, with zero clean verification failures; signed-root-only remains at 0/500 rollback detection as the control.
- Stop condition: Stop if the anchored variant has any reproducible clean verification failure, detects fewer than 499/500 rollback replays, or requires external/private infrastructure unavailable to the worker.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-persisted-signed-root-ledger-validation-1edf9d7075`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
