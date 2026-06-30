# Commit-reveal checkpoint fingerprinting for volunteer training integrity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-checkpoint-fingerprinting-for-volunteer-training-integrity-a708b271ac96`
Run ID: `commit-reveal-checkpoint-fingerprinting-for-volunteer-training-integrity-a708b271ac96-20260528T002813921274+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d89cab63ee6d

## What looked useful

The simple projection-only checkpoint-fingerprint mechanism is not enough for integrity: held-out accept rates were honest 0.972, random norm-matched 0.856, stale replay 0.942, interpolation 0.989, and known-challenge forgery 1.000 at a threshold calibrated to the honest 5th percentile. AUC was 0.503 for stale replay and 0.496 for interpolation, but reveal-before-commit forgery passed perfectly, supporting the need for commit-reveal ordering.

## Boundaries and scale limits

Toy synthetic data and small parameter counts only; no real distributed volunteer training, no neural network checkpoints, no wall-clock proof-of-work, and no sophisticated partial-training adversaries beyond stale, interpolation, random norm-matched, and adaptive known-challenge forgery variants.

## Claim scope

In a synthetic logistic-regression checkpoint audit with 24 seeds, 512 parameters, 256 sparse projection bits, and held-out calibration, simple commit-before-reveal sparse projection fingerprints over checkpoint deltas are insufficient as a volunteer training-integrity check: stale replay and skip-5 interpolation pass at nearly honest rates. Commit-before-reveal ordering remains necessary because reveal-before-commit permits trivial adaptive projection forgery.

## Why it stopped

Proxy early falsification: the scoped toy experiment directly tested the simple commit-reveal projection fingerprint and found it cannot reject stale or interpolated checkpoints, so it should not be scaled as-is.

## Recommended next action

Stop this mechanism as no-paper evidence; a next bounded deepen test should add cumulative unpredictable transcript beacons or richer verifier statistics and require false accept below 5% at at least 90% honest acceptance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cumulative transcript beacons for checkpoint integrity
- Success threshold: Held-out false accept rate below 5% for each attack at at least 90% honest acceptance, with less than 2% training-time overhead in the small workload.
- Stop condition: Stop if stale replay or skip/interpolation false accept remains above 20% at 90% honest acceptance, or if overhead exceeds 10% before reaching a real small neural-network workload.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-checkpoint-fingerprinting-for-volunteer-training-integrity-a708b271ac96`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
