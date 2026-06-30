# Gradient Norm-Profile Cheating Detector for CPU Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-norm-profile-cheating-detector-for-cpu-volunteer-training-7072cc979d0b`
Run ID: `gradient-norm-profile-cheating-detector-for-cpu-volunteer-training-7072cc979d0b-20260613T012101959520+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/908164cba090

## What looked useful

Gradient norm profiles are useful as a cheap screening feature but are not sufficient as a standalone cheating detector because a malicious client can preserve clean update norms while changing update direction.

## Boundaries and scale limits

Synthetic logistic regression only: 24 clients, 4 cheaters, 90 rounds, 16 seeds per attack, no real volunteer traces, no neural-network benchmark, no adaptive adversaries, and detector input limited to scalar norm histories.

## Claim scope

In a bounded synthetic CPU federated logistic-regression setting, gradient norm-profile scores detect norm-distorting and label-flip cheating but fail or become weak for norm-preserving random-direction and stale-replay cheating.

## Why it stopped

Bounded synthetic evidence is mixed and includes a direct norm-only counterexample, so this is not publication-grade validation of a standalone gradient norm-profile detector.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should add a direction-sensitive sketch or robust-aggregate cosine feature and test whether it closes the norm-preserving failure mode.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Add Direction-Sensitive Sketches to Gradient Norm-Profile Volunteer Cheating Detection
- Success threshold: Held-out mean AUROC >= 0.85 and F1 >= 0.60 for norm_matched_random and stale_replay without reducing scale_up or label_flip AUROC below 0.90.
- Stop condition: Stop if direction-sensitive features cannot exceed norm-only AUROC by at least 0.20 on norm_matched_random and stale_replay in the same bounded CPU setup.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-profile-cheating-detector-for-cpu-volunteer-training-7072cc979d0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
