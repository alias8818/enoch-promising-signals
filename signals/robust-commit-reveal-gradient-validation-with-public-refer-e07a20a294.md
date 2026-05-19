# Robust Commit-Reveal Gradient Validation With Public Reference Agreement

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `robust-commit-reveal-gradient-validation-with-public-refer-e07a20a294`
Run ID: `robust-commit-reveal-gradient-validation-with-public-refer-e07a20a294-20260518T125604274012+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Robust Commit-Reveal Gradient Validation With Public Reference Agreement: internal_generated:robust-commit-reveal-gradient-validation-with-public-refer-e07a20a294

## What looked useful

Commit-reveal transcript integrity worked, and public-reference agreement detected obvious sign-flip/random attacks under a strict threshold, but the validator failed the robust mechanism test because it rejected 98-100% of honest gradients in no-attack fixed-threshold controls and accepted 100% of reference-mimic attackers in both fixed-threshold and top-75% ablations.

## Boundaries and scale limits

Small local model and dataset; commit-reveal was simulated as hash-before-reveal transcript integrity rather than a deployed network protocol; no large-model or multi-node training was run.

## Claim scope

In a fixed-seed local federated digits simulation with a linear classifier, public-reference cosine agreement is not robust as a standalone gradient validator: it either rejects most honest gradients under fixed calibration or accepts adaptive reference-mimic attackers under rank-based calibration.

## Why it stopped

Tier 2 fixed-seed validation produced a no-paper negative: the mechanism detects some obvious attacks but fails under honest calibration drift and public-reference-mimic attacks.

## Recommended next action

Stop pursuing public-reference agreement as a standalone gradient validator; only revisit with an added private/secret challenge or a robust aggregation hybrid that has an explicit adaptive-attack success threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/robust-commit-reveal-gradient-validation-with-public-refer-e07a20a294`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
