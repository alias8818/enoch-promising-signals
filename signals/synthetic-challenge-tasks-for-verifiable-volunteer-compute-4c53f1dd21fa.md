# Synthetic Challenge Tasks for Verifiable Volunteer Compute

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `synthetic-challenge-tasks-for-verifiable-volunteer-compute-4c53f1dd21fa`
Run ID: `synthetic-challenge-tasks-for-verifiable-volunteer-compute-4c53f1dd21fa-20260621T184402158932+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f179458392af

## What looked useful

Freivalds-verified matrix multiplication provided deterministic, tunably sized synthetic tasks with valid outputs accepted, corrupted outputs rejected near the expected 2^-k false-accept bound, and verification 25x to 191x cheaper than solving at n=384 depending on k. Hash proof-of-work verified in about 0.5 microseconds but had high single-task solve variance and does not represent useful compute.

## Boundaries and scale limits

Largest direct matrix task was 384 x 384 int64 on one local CPU/NumPy environment; no real volunteer network, GPU heterogeneity, incentive layer, replay defense, or adaptive adversary evaluation was tested.

## Claim scope

Small local synthetic benchmark of hash-threshold proof-of-work and Freivalds-verified dense matrix multiplication as challenge-task templates for verifiable volunteer compute.

## Why it stopped

The result is a small synthetic/local mechanism benchmark, useful for selecting a challenge family but not direct/full validation of verifiable volunteer compute.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should test larger matrices, heterogeneous CPU/GPU timing, and adaptive/corrupted submissions with fresh verifier randomness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heterogeneous Freivalds Challenge Robustness Benchmark
- Success threshold: At n >= 1024, k >= 8 verification is at least 20x cheaper than solving, all valid outputs pass, and corrupted-output empirical acceptance is statistically consistent with <= 2^-k across tested corruption patterns.
- Stop condition: Stop if larger tasks lose the solve/verify advantage below 10x, valid outputs fail verification, corrupted-output acceptance substantially exceeds 2^-k, or the run becomes CPU-only and cannot finish inside the bounded resource budget.

## Evidence references

- Artifact root: `<local-path>/projects/synthetic-challenge-tasks-for-verifiable-volunteer-compute-4c53f1dd21fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
