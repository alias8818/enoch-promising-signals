# Calibrated confidence gates for strict-baseline cascades on larger UCI datasets

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `calibrated-confidence-gates-for-strict-baseline-cascades-o-5d6a5cadc6`
Run ID: `calibrated-confidence-gates-for-strict-baseline-cascades-o-5d6a5cadc6-20260523T123704950032+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Medium multi-dataset CPU validation for confidence-threshold cascades: enoch://control-plane/projects/medium-multi-dataset-cpu-validation-for-confidence-thresho-7c5d3ec130/runs/medium-multi-dataset-cpu-validation-for-confidence-thresho-7c5d3ec130-20260523T113010252534+0000
- Parent run decision: Strict-baseline confidence cascade validation on larger real datasets: enoch://control-plane/projects/strict-baseline-confidence-cascade-validation-on-larger-re-1d9308b110/runs/strict-baseline-confidence-cascade-validation-on-larger-re-1d9308b110-20260523T121144949435+0000

## What looked useful

A corrected fixed-prediction control found mean ECE improved from raw 0.0355 to isotonic 0.0154, but Platt produced no frontier change because it preserves confidence ranking, and isotonic worsened mean cost at the strong-accuracy target by +0.5734 with only a 30.8% win rate. Strict confidence thresholds also did not show robust risk-control gains.

## Boundaries and scale limits

Bounded to Adult, Bank Marketing, MAGIC, and Spambase; cheap model logistic regression; strong model random forest; binary tabular classification; CPU-only local validation. Broader claims would require more datasets and model families.

## Claim scope

On four binary UCI tabular datasets across five fixed seeds, calibrating the confidence gate for a fixed cheap logistic-regression baseline before deferring to a random-forest strong baseline improves confidence calibration, especially with isotonic regression, but does not reliably improve the cascade cost/accuracy frontier or strict accepted-risk control versus raw confidence.

## Why it stopped

Direct corrected validation on larger UCI datasets produced a mixed/negative result for the cascade claim: calibration improved ECE but not target cascade metrics.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful evidence; do not recommend another chained follow-up under the controller cap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-confidence-gates-for-strict-baseline-cascades-o-5d6a5cadc6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
