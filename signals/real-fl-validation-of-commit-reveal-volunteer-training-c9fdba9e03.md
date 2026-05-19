# Real-FL Validation of Commit-Reveal Volunteer Training

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `88`
Project ID: `real-fl-validation-of-commit-reveal-volunteer-training-c9fdba9e03`
Run ID: `real-fl-validation-of-commit-reveal-volunteer-training-c9fdba9e03-20260515T015205869170+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `88`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Real-FL Validation of Commit-Reveal Volunteer Training: internal_generated:real-fl-validation-of-commit-reveal-volunteer-training-c9fdba9e03

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded full validation found mechanism support but not paper-ready evidence: commit-reveal matched audit_no_commit accuracy rather than showing a distinctive advantage over the real control.

## Recommended next action

Stop as no-paper: bounded real-dataset FL validation supports audit-based robustness and commit accountability telemetry, but commit-reveal did not outperform an audit-only control; only a final depth-4 adaptive-accountability test is worth considering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Withholding Accountability Test for Commit-Reveal FL
- Success threshold: Commit-reveal reduces silent/adaptive malicious defaults by at least 80% versus audit_no_commit, keeps malicious accepted update rate below 5%, and maintains final test accuracy within 1 percentage point of the better of audit_no_commit or robust_clip across at least five fixed seeds.
- Stop condition: Stop negative if commit-reveal again matches audit-only on accountability metrics, loses more than 1 percentage point accuracy to audit-only/robust_clip, or requires assumptions unavailable in a deployable volunteer FL protocol.

## Evidence references

- Artifact root: `<local-path>/projects/real-fl-validation-of-commit-reveal-volunteer-training-c9fdba9e03`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
