# Cross-Home Signed Persistent Trace Consensus Ledger Replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `cross-home-signed-persistent-trace-consensus-ledger-replay-92f6aa6195`
Run ID: `cross-home-signed-persistent-trace-consensus-ledger-replay-92f6aa6195-20260527T062013629453+0000`

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

- Parent run decision: Replay Realistic Smart-Home Event Traces Through Trace Consensus Ledger: enoch://control-plane/projects/replay-realistic-smart-home-event-traces-through-trace-con-c72f8b097f/runs/replay-realistic-smart-home-event-traces-through-trace-con-c72f8b097f-20260526T231851360705+0000
- Parent run decision: Trace-Based Consensus Ledger Evaluation for Smart-Home Agent Actions: enoch://control-plane/projects/trace-based-consensus-ledger-evaluation-for-smart-home-age-f8054ed932/runs/trace-based-consensus-ledger-evaluation-for-smart-home-age-f8054ed932-20260526T172301271866+0000

## What looked useful

Signed persistence and quorum each mattered in the bounded replay model: signed persistent consensus detected 11/11 forged signed edits while unsigned persistent replay detected 0/11 forged-chain edits; clean signed persistence recovered 100% of expected quorum operations while signed ephemeral replay recovered about 80.9%; no-quorum replay over-accepted all proposals and had zero local convergence.

## Boundaries and scale limits

Simulation-only evidence. No real home devices, production filesystem failure modes, clock skew, key compromise, privacy UX, multi-process implementation, long-term compaction, or wide-area deployment were validated. CPU-only bounded run used 24 tamper trials per variant plus 8 clean-control trials, not an overnight production trace corpus.

## Claim scope

In a deterministic 7-home simulator with fixed seeds, crash/drop injection, persistent JSONL ledgers, Ed25519 signatures, per-home hash chains, quorum replay, and forged-chain tamper controls, signed persistent consensus replay converged under union replay, detected all signed tamper trials, recovered all expected quorum operations in clean controls, and recovered substantially more crash-affected quorum operations than an ephemeral signed baseline.

## Why it stopped

Mechanism support is useful but not publication-grade because evidence is simulation-only and cross-home union replay, not independent local partial ledgers, is required for convergence.

## Recommended next action

Stop short of paper writing; the next useful bounded step is a small real multi-process prototype that replays actual persisted ledgers across isolated home directories and validates crash/tamper recovery against this simulator's thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-process persisted ledger replay prototype with crash and tamper injection
- Success threshold: Across fixed-seed multi-process runs, signed persistent consensus must recover 100% of clean expected quorum operations, detect 100% of signed tamper attempts, outperform signed ephemeral recovery by at least 10 percentage points under crash/loss, and stay below 2x unsigned persistent build-time overhead.
- Stop condition: Stop if clean signed persistent replay fails to recover 99% of expected quorum operations, if signed tamper detection is below 100%, or if implementation overhead exceeds 2x unsigned persistence before reaching 10k events.

## Evidence references

- Artifact root: `<local-path>/projects/cross-home-signed-persistent-trace-consensus-ledger-replay-92f6aa6195`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
