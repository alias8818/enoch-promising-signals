# Sparse Gradient Fingerprints for Volunteer Training Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-gradient-fingerprints-for-volunteer-training-validation-c25aae8dbc12`
Run ID: `sparse-gradient-fingerprints-for-volunteer-training-validation-c25aae8dbc12-20260525T081221431398+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ed250168d09

## What looked useful

Sparse gradient fingerprints are useful as hidden challenges against random, stale, scaled, sign-flipped, label-shuffled, and partially zeroed updates, but public or known coordinates are bypassed by an adaptive attacker that matches sampled coordinates and corrupts the rest of the update.

## Boundaries and scale limits

Synthetic data, 9,610-parameter MLP, 360 validation trials, full gradients computed internally before sampling, no real volunteer network, no efficient sparse-coordinate recomputation kernel, no large-model or collusion validation.

## Claim scope

On a synthetic small-MLP classification task, hidden sparse coordinate checks over 0.083% to 10.656% of gradient parameters detected tested nonadaptive invalid volunteer updates with near-perfect detection and negligible honest false positives.

## Why it stopped

No paper-positive closure: the local mechanism works against nonadaptive attacks but an adaptive known-coordinate bypass fully defeats sparse checking without hidden or commit-reveal sampling.

## Recommended next action

Run a bounded protocol follow-up that forces binding update commitment before coordinate reveal, then measure adaptive attacker detection and honest false-positive rates on the same harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-reveal sparse gradient fingerprints against adaptive volunteer updates
- Success threshold: At k <= 128 on the 9,610-parameter model, honest false-positive rate <= 1% and adaptive pre-commit invalid-update detection >= 95% across random, stale, scaled, label-shuffled, and partial-zero attacks.
- Stop condition: Stop if adaptive pre-commit detection is below 90% at k=128 or if honest false positives exceed 2%, because the mechanism is not robust enough for bounded protocol validation.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-gradient-fingerprints-for-volunteer-training-validation-c25aae8dbc12`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
