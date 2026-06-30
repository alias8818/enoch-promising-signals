# Polynomial-Commitment Spot-Checks for Volunteer Gradients

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `polynomial-commitment-spot-checks-for-volunteer-gradients-e2fe87a1ab87`
Run ID: `polynomial-commitment-spot-checks-for-volunteer-gradients-e2fe87a1ab87-20260526T053200967336+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fcaeefd6eeab

## What looked useful

Coordinate spot-check detection matched hypergeometric sampling predictions. A one-coordinate attack caused 100x relative gradient error and +34.707 loss delta while 1,024 checks detected it only 5.3%; 95% detection would require 19,001 of 20,000 coordinates. Dense and 1% corruptions were detected efficiently.

## Boundaries and scale limits

Single-process CPU experiment on 20,000-dimensional logistic-regression gradients with 2,048 examples and simulated binding polynomial digest; no production KZG/IPA proof costs, deep-network gradients, multi-client aggregation, or adaptive attackers were tested.

## Claim scope

Bounded synthetic logistic-regression gradient experiment showing that polynomial-commitment coordinate spot checks catch dense or 1%-level corruption according to the sampling law, but do not cheaply catch sparse high-impact corruption.

## Why it stopped

Proxy/early falsification of standalone coordinate spot checks: the experiment directly tested coordinate sampling but proxied production polynomial commitments and deep-training settings; sparse high-impact attacks evade cheap checks by the sampling law.

## Recommended next action

Stop this standalone coordinate spot-check idea as no-paper evidence; the next bounded test should add random linear projection or norm-bound checks and measure whether sparse high-impact attacks are caught without near-full-vector verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Random-projection checks for committed volunteer gradients
- Success threshold: At dimension 20,000, detect the one-coordinate high-impact attack with at least 95% empirical probability using no more than 1,024 verifier-side scalar checks or equivalent recomputation cost, while preserving detection of 1% and dense attacks.
- Stop condition: Stop if projection checks cannot exceed 50% detection on the one-coordinate high-impact attack under the same 1,024-check budget or if their verifier cost approaches full-gradient recomputation.

## Evidence references

- Artifact root: `<local-path>/projects/polynomial-commitment-spot-checks-for-volunteer-gradients-e2fe87a1ab87`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
