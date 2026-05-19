# Gradient Dot Audits for Label-Flip Anomaly Detection

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `78`
Project ID: `gradient-dot-audits-for-label-flip-anomaly-detection-063cd69498`
Run ID: `gradient-dot-audits-for-label-flip-anomaly-detection-063cd69498-20260515T033422957542+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Gradient Dot Audits for Label-Flip Anomaly Detection: internal_generated:gradient-dot-audits-for-label-flip-anomaly-detection-063cd69498

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded direct validation found a real clean-audit gradient-dot mechanism signal, but it underperformed simple baselines overall by -0.257 mean AUROC and -0.144 mean AP, so the result is not paper-ready.

## Recommended next action

Stop the broad paper claim; if the controller permits one final depth-4 follow-up, test the narrowed binary high-noise regime on larger datasets against loss, confidence, margin, and gradient-norm baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Binary High-Noise Gradient-Dot Audit Validation
- Success threshold: Gradient-dot audit beats the best simple baseline by at least +0.03 mean AUROC and +0.05 mean AP across datasets, with positive paired 95% confidence intervals and no catastrophic dataset failures.
- Stop condition: Stop negative if the paired mean AUROC or AP advantage over the best simple baseline is non-positive after the fixed dataset and seed grid.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-dot-audits-for-label-flip-anomaly-detection-063cd69498`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
