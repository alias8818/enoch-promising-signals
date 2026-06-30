# Bounded Evidence Ledger for Volunteer Home AI Training Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-evidence-ledger-for-volunteer-home-ai-training-verification-f5602b11ac69`
Run ID: `bounded-evidence-ledger-for-volunteer-home-ai-training-verification-f5602b11ac69-20260605T173227778465+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d7ba9c7bd4a7

## What looked useful

A bounded evidence ledger is useful as an integrity and plausibility filter, not as a standalone proof of real volunteer training compute.

## Boundaries and scale limits

The experiment used synthetic event streams rather than real model training, private home hardware, remote attestation, or external telemetry. It ran 1,000,000 records on one CPU process and does not validate fleet-scale volunteer training.

## Claim scope

A synthetic bounded test of signed, hash-chained volunteer training event records shows that ledger rules reject replay, stale-history, step-jump, token-rate-inflation, and payload-tamper records, but accept plausible signed fabrications that obey monotonicity and rate bounds.

## Why it stopped

Early scoped falsification of the strong ledger-only verification claim: plausible signed fabrication passed all bounded ledger checks in synthetic trials, so full verification requires external compute-binding evidence.

## Recommended next action

Stop this ledger-only run; the next bounded test should add an independent compute-binding signal and measure whether it rejects plausible signed fabrication without high false rejection of honest traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compute-bound Attestation for Bounded Volunteer Training Ledgers
- Success threshold: At least 95% rejection of plausible fabricated records at no more than 1% false rejection of honest records in a reproducible bounded local test.
- Stop condition: Stop if the compute-binding mechanism cannot be implemented locally, adds overhead above 10x ledger-only verification, or fails to reduce plausible-fabrication acceptance below 50%.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-evidence-ledger-for-volunteer-home-ai-training-verification-f5602b11ac69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
