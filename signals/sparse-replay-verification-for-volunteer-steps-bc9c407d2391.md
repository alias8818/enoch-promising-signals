# Sparse Replay Verification for Volunteer Steps

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-replay-verification-for-volunteer-steps-bc9c407d2391`
Run ID: `sparse-replay-verification-for-volunteer-steps-bc9c407d2391-20260629T222512809695+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e54a04d551a

## What looked useful

Risk-weighted sparse replay reached 0.439 workflow detection versus 0.356 for random sparse replay at equal 0.167 replay fraction, with 0.0 false-positive rate, but the 0.0836 absolute lift was below the >=0.10 success threshold.

## Boundaries and scale limits

20 replicates, 500 synthetic workflows per replicate, 24 steps per workflow, 4 verified steps per workflow, injected hash mismatches only; no real volunteer logs, live integrations, LLM-generated claims, privacy constraints, or adaptive adversaries.

## Claim scope

In a deterministic synthetic volunteer workflow replay benchmark, risk-weighted sparse replay at a 4-of-24 step budget improved tampered-workflow detection over random sparse replay, but the improvement did not meet the predeclared success threshold.

## Why it stopped

Bounded synthetic evidence was directional but missed the predeclared detection-lift threshold; this is proxy evidence, not full validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test calibrated risk scoring on semi-synthetic or real replay traces with known ground truth before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated sparse replay risk scoring on realistic volunteer traces
- Success threshold: >=0.12 absolute workflow detection lift over random_sparse at equal replay fraction, false-positive rate <=0.01, and non-overlapping or clearly separated bootstrap confidence intervals.
- Stop condition: Stop if calibrated policy lift remains below 0.08 absolute detection rate or false positives exceed 0.01 on clean workflows.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-replay-verification-for-volunteer-steps-bc9c407d2391`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
