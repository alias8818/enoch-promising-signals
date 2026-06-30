# Gradient Consistency Scoring for Byzantine Detection in Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-consistency-scoring-for-byzantine-detection-in-volunteer-training-133132474544`
Run ID: `gradient-consistency-scoring-for-byzantine-detection-in-volunteer-training-133132474544-20260526T052151040517+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a7ef6cb17638

## What looked useful

GCS pair-median scoring achieved AUROC 1.000 on sign-flip and 0.917 on Gaussian attacks, but only 0.467 on orthogonal stealth and 0.000 on same-direction scaling. Filtering by GCS reduced relative aggregate error for sign-flip by 0.834 and Gaussian by 0.189, but worsened orthogonal stealth by -0.165 and same-direction scaling by -0.255. The method is useful as a directional-inconsistency feature, not as a general Byzantine defense.

## Boundaries and scale limits

Synthetic one-round gradients only; 50 clients, 128 dimensions, 64 samples per client, 10-30% Byzantine clients, four heterogeneity settings, four attack families, 20 seeds per condition. No real multi-round model training, adaptive adversary, unknown Byzantine fraction, or large-model volunteer deployment was tested.

## Claim scope

In a reproducible synthetic one-round volunteer training simulation with logistic-regression gradients, pairwise gradient-consistency scoring detects directionally inconsistent Byzantine updates such as sign-flip and random Gaussian attacks, but fails as a standalone detector for direction-preserving same-direction scaling and orthogonal stealth perturbations.

## Why it stopped

No-paper useful signal: the local synthetic evidence supports a narrow mechanism but falsifies the broader standalone-detector claim; this is not a full validation.

## Recommended next action

Run a bounded hybrid-detector follow-up that combines GCS with norm, magnitude, temporal consistency, and update-effect features on a small multi-round neural training benchmark with adaptive attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Gradient-Consistency Byzantine Detector on Multi-Round Volunteer Training
- Success threshold: Hybrid detector improves mean relative aggregate error or downstream validation loss by at least 20% over the best single-feature baseline while maintaining AUROC >= 0.85 on at least three of four attack families.
- Stop condition: Stop if the hybrid detector fails to beat the best norm/magnitude baseline on aggregate quality in two independent non-IID settings or if GCS adds no positive ablation value.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-consistency-scoring-for-byzantine-detection-in-volunteer-training-133132474544`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
