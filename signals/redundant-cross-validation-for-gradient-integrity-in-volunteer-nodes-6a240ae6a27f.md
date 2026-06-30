# Redundant Cross-Validation for Gradient Integrity in Volunteer Nodes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `redundant-cross-validation-for-gradient-integrity-in-volunteer-nodes-6a240ae6a27f`
Run ID: `redundant-cross-validation-for-gradient-integrity-in-volunteer-nodes-6a240ae6a27f-20260529T055533362812+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/bf00ef5b85bd

## What looked useful

Redundant cross-validation can preserve training quality against coarse corruptions, especially sign-flip attacks, but simple triplicate majority can accept coherent bad majorities and tolerance-based checks miss small biased updates. Pair rejection was strongest for 30% sign-flip corruption, improving accuracy from 0.238 to 0.892 at 2x gradient compute while dropping about 42% of minibatches.

## Boundaries and scale limits

Single-process CPU simulation only; no real volunteer nodes, network effects, stale parameters, privacy constraints, collusion controls, adaptive adversaries, large neural models, or wall-clock distributed throughput measurements.

## Claim scope

NumPy synthetic logistic-regression proxy with independent volunteer corruption, redundant minibatch gradient recomputation, and similarity-threshold validation across sign-flip, random, scale, bias, and tolerance-conforming stealth-bias attacks.

## Why it stopped

Proxy evidence is mixed and not publication-grade: the mechanism works for large inconsistent corruptions but fails to detect tolerance-conforming bias and can accept coherent corrupt majorities.

## Recommended next action

Stop this run as no-paper useful signal; next concrete test is a bounded multi-process trainer with adaptive/colluding adversaries and an explicit robust-aggregation baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive and Colluding Volunteer Gradient Validation in a Multi-Process Trainer
- Success threshold: At 30% corrupt worker processes, the best proposed method must keep final accuracy within 3 percentage points of clean training, accept fewer than 5% of corrupt gradients, and preserve at least 70% of logical minibatches with no more than 3x gradient compute.
- Stop condition: Stop if adaptive or colluding adversaries cause more than 10 percentage points accuracy loss or more than 20% corrupt-gradient acceptance after threshold tuning, because the mechanism would not justify larger-scale validation.

## Evidence references

- Artifact root: `<local-path>/projects/redundant-cross-validation-for-gradient-integrity-in-volunteer-nodes-6a240ae6a27f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
