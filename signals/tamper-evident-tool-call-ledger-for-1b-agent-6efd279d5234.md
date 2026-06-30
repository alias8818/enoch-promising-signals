# Tamper-evident tool-call ledger for 1B agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tamper-evident-tool-call-ledger-for-1b-agent-6efd279d5234`
Run ID: `tamper-evident-tool-call-ledger-for-1b-agent-6efd279d5234-20260528T210950930918+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57ea2dc6f7d8

## What looked useful

The tested ledger design is practical enough for normal tool-call rates and catches payload mutation, deletion, reordering, truncation, and chain rehashing without the HMAC secret, but it needs real-agent integration and anchoring evidence before any paper claim.

## Boundaries and scale limits

Synthetic tool-call traces only; no real 1B-agent inference loop, concurrent writers, crash recovery, key rotation, remote append-only storage, or independent checkpoint anchoring were tested.

## Claim scope

A canonical JSON hash-chain ledger with per-entry payload hashes and HMAC-authenticated roots detected five classes of post-hoc tampering on synthetic 10,000-entry tool-call traces and sustained about 41k ledger writes/s and 44k verifications/s locally.

## Why it stopped

No-paper useful signal: this was a synthetic local mechanism test, not direct 1B-agent deployment evidence or a full validation.

## Recommended next action

Run a bounded deepen test by integrating the ledger into a real small or 1B-class agent harness and replaying actual tool-call sessions with crash/restart and concurrent write checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent integration test for tamper-evident tool-call ledger
- Success threshold: At least 99% of actual tool calls recorded and verified with under 5 ms median per-call ledger overhead, all predefined tamper cases detected, and crash/restart preserving verifier consistency.
- Stop condition: Stop if real-agent integration drops or reorders calls without detectable verifier failure, adds over 20 ms median per-call overhead, or cannot preserve checkpoints across restart.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-tool-call-ledger-for-1b-agent-6efd279d5234`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
