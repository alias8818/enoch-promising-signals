# Merkle-Root Shuffle Audit for Volunteer Data Samplers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-root-shuffle-audit-for-volunteer-data-samplers-39b05be1e5b1`
Run ID: `merkle-root-shuffle-audit-for-volunteer-data-samplers-39b05be1e5b1-20260621T035012659206+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dd37f5976891

## What looked useful

Honest inclusion proofs verified and forged leaves were detected, but a duplicate-containing committed sequence still gave valid local proofs, and seed grinding raised mean priority hits in the first 100 assignments from a 5.0 random expectation to 12.63 when selecting among 1000 candidate seeds.

## Boundaries and scale limits

No live volunteers, public randomness beacon, cryptographic shuffle implementation, signed receipts, privacy review, or field-scale adversarial deployment were tested. Seed grinding used a reproducible Python PRNG model.

## Claim scope

Deterministic synthetic audit of a 1000-sample volunteer assignment shuffle shows Merkle roots are useful for per-assignment inclusion proofs but insufficient alone for permutation validity or shuffle fairness.

## Why it stopped

Bounded synthetic evidence shows the standalone Merkle-root shuffle audit is only a component, not a sufficient fairness or permutation protocol; this is a no-paper useful signal rather than full validation.

## Recommended next action

Stop paper path for the standalone Merkle-root audit; the concrete next action is an end-to-end controlled-protocol test with public manifest verification, non-grindable external randomness, aggregate permutation evidence, and signed volunteer receipts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end controlled Merkle shuffle audit with external randomness and receipt checks
- Success threshold: Detect 100% of injected duplicate, omission, forged-assignment, replay, and seed-grinding attacks across at least 100 deterministic synthetic deployments of 1000 or more samples, with zero false positives on honest runs.
- Stop condition: Stop if any required protocol control cannot be implemented locally, if honest verification has false positives, or if any injected attack class evades detection after the controls are enabled.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-root-shuffle-audit-for-volunteer-data-samplers-39b05be1e5b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
