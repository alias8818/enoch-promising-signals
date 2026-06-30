# Cheating-Resistant Validation via Deterministic Replay Seeds

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cheating-resistant-validation-via-deterministic-replay-seeds-dd414134d1b6`
Run ID: `cheating-resistant-validation-via-deterministic-replay-seeds-dd414134d1b6-20260530T012911059825+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/af9cadb02690

## What looked useful

Public validation seeds allowed a memorizing submitter to score 1.0000 validation accuracy while holding only 0.4983 holdout accuracy; private deterministic replay reduced the same submitter to 0.4898 private accuracy with 300/300 exact replays. Low-entropy commitments were brute-forced quickly up to 20 bits.

## Boundaries and scale limits

Synthetic data only; no real submitted model artifacts, no adaptive leaderboard probing, no multi-party audit, no production benchmark infrastructure, and no non-seed leakage channels were tested.

## Claim scope

In a 300-trial synthetic binary-classification benchmark, a private high-entropy committed seed revealed only after submission made deterministic validation exactly replayable and removed exact public-validation memorization score inflation.

## Why it stopped

Closed as no-paper useful signal because the evidence is a bounded synthetic proxy, not direct validation of a deployed benchmark protocol.

## Recommended next action

Run a bounded real-harness follow-up with actual submitted artifacts, high-entropy commitment generation, replay logs, and adversarial submissions that test leaderboard probing and seed inference.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Harness Replay Seed Validation Against Adaptive Submitters
- Success threshold: Private replay reduces adversarial validation-to-holdout inflation by at least 80% versus public-seed validation while preserving 100% replay reproducibility across all audited submissions.
- Stop condition: Stop if private replay fails exact audit reproducibility, if high-entropy commitments cannot be implemented without hidden state, or if adaptive probing retains more than 20% of the public-seed inflation.

## Evidence references

- Artifact root: `<local-path>/projects/cheating-resistant-validation-via-deterministic-replay-seeds-dd414134d1b6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
