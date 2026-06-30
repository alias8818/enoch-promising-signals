# Live signed-root checksum ledger for agent tool-call traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-signed-root-checksum-ledger-for-agent-tool-call-trace-522d69f843`
Run ID: `live-signed-root-checksum-ledger-for-agent-tool-call-trace-522d69f843-20260523T164725208271+0000`

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

- Parent run decision: Agent Trace Checksum Ledger On Real Tool-Call Logs: enoch://control-plane/projects/agent-trace-checksum-ledger-on-real-tool-call-logs-f301133575/runs/agent-trace-checksum-ledger-on-real-tool-call-logs-f301133575-20260523T155049683887+0000
- Parent run decision: ChecksumToolCallLedger: enoch://control-plane/projects/checksumtoolcallledger-9cf46586c45f/runs/checksumtoolcallledger-9cf46586c45f-20260523T154208525078+0000

## What looked useful

Live authenticated roots materially improved tamper detection latency over an offline trusted-final-root hash chain while retaining full attack coverage in the benchmark. A sparse every-16-events authenticated-root ablation preserved full detection with median latency of 3 events and near-baseline append throughput.

## Boundaries and scale limits

Synthetic traces only; single-process CPU benchmark; HMAC authenticated roots rather than public-key signatures; no real agent-framework integration, crash recovery, multi-writer concurrency, key rotation, remote timestamping, or external transparency log.

## Claim scope

On synthetic but structurally direct agent tool-call traces of 50,000 events across 7 fixed seeds, per-event HMAC-authenticated checksum roots detected all tested tampering attacks with zero event-latency and 1.47x median append slowdown versus a trusted-final-root hash-chain baseline.

## Why it stopped

No-paper closure: the mechanism is supported by Tier 2 synthetic fixed-seed evidence, but publication readiness requires real trace integration and persistence/concurrency validation.

## Recommended next action

Run a bounded real-trace deepen follow-up with one agent framework emitter, durable checkpoint persistence across restart, and baselines for final-root hash chain plus external append-only storage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent persisted signed-root ledger validation
- Success threshold: On real emitted traces, detect 100% of tested attacks with zero clean false positives, median append slowdown below 2x versus final-root hash chain, and median non-truncation detection latency at least 10x lower than final-root hash chain.
- Stop condition: Stop if persisted checkpoints cannot survive restart without trusted in-memory state, if real-trace append overhead exceeds 2x after straightforward batching/sparse signing, or if any non-clean attack escapes detection under the stated threat model.

## Evidence references

- Artifact root: `<local-path>/projects/live-signed-root-checksum-ledger-for-agent-tool-call-trace-522d69f843`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
