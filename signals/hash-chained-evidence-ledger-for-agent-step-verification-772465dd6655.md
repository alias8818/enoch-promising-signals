# Hash-Chained Evidence Ledger for Agent Step Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-evidence-ledger-for-agent-step-verification-772465dd6655`
Run ID: `hash-chained-evidence-ledger-for-agent-step-verification-772465dd6655-20260531T115413332885+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f587edc8ca0e

## What looked useful

At 100k synthetic records, ledger generation reached about 106k records/s, validation about 296k records/s, and storage overhead was about 1.44x. Ordinary tampering was detected, while a recomputed suffix passed without an external head anchor and failed with one.

## Boundaries and scale limits

Synthetic payloads only; single-process local Python implementation; no real agent runtime integration; no remote timestamping, transparency log, crash recovery, concurrent writers, or compromised-anchor adversary test.

## Claim scope

A deterministic Python canonical-JSON hash-chain ledger detects local modification, deletion, insertion, and reordering in synthetic agent-step traces with low CPU overhead, but only detects fully recomputed suffix rewrites when the expected ledger head is externally anchored.

## Why it stopped

Bounded local evidence produced a useful mechanism boundary, but this is synthetic/proxy evidence and not a direct production-agent validation.

## Recommended next action

Stop this no-paper run; if continuing, integrate periodic immutable head anchoring into a real agent trace recorder and test crash/retry/concurrent-writer behavior.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored Agent Trace Ledger Integration Test
- Success threshold: All tamper scenarios including suffix rewrite are detected when anchors are retained; crash/retry/concurrent append recovery preserves a valid audit chain; overhead remains below 2x storage and below 10 ms p95 per recorded step for a representative local agent workload.
- Stop condition: Stop if anchored integration cannot reliably preserve or verify ledger heads across crash/retry/concurrent-writer scenarios, or if overhead exceeds the success threshold by more than 2x.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-evidence-ledger-for-agent-step-verification-772465dd6655`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
