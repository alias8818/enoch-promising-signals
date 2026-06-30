# Held-Out Probe Tasks for Cheating Detection in Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `held-out-probe-tasks-for-cheating-detection-in-volunteer-training-fca4aec2e71b`
Run ID: `held-out-probe-tasks-for-cheating-detection-in-volunteer-training-fca4aec2e71b-20260613T002135244900+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f8f9e63f7a3f

## What looked useful

With uncompromised probes, recall rose from 0.620 at 2 probes to 0.881 at 24 probes while FPR stayed near 1%; with 8 probes and equal probe/training leakage at p=0.97, recall collapsed to 0.006 and balanced accuracy to 0.498. Probe secrecy is the central condition for the mechanism.

## Boundaries and scale limits

Synthetic-only Monte Carlo; no real volunteer behavior, no real task content, no adaptive adversaries, no longitudinal leakage dynamics, and no direct fairness analysis beyond calibrated honest false-positive rates. The result does not validate deployment performance.

## Claim scope

In a synthetic volunteer-training model with 40 ordinary training items, 2-24 held-out probes, 20% cheater prevalence, and a detector calibrated at the 99th percentile on honest volunteers, train-minus-probe discrepancy detects many answer-key cheaters when ordinary training answers are compromised and held-out probes remain secret.

## Why it stopped

Synthetic useful signal only; no direct human volunteer evidence or operational probe-security validation, so this is not publication-grade closure.

## Recommended next action

Run a bounded human or high-fidelity online pilot with randomized answer-key exposure and pre-registered held-out probe scoring before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Randomized Pilot of Held-Out Probe Detection in Volunteer Training
- Success threshold: At least 70% recall at <=2% FPR on labeled exposed versus unexposed participants, with no large subgroup-specific false-positive spike and a documented probe-secrecy audit.
- Stop condition: Stop if recall is below 50% at 2% FPR, if probe secrecy cannot be audited, or if honest low-skill participants are disproportionately flagged after calibration.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-probe-tasks-for-cheating-detection-in-volunteer-training-fca4aec2e71b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
