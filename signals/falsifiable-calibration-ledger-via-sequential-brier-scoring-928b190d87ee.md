# Falsifiable Calibration Ledger via Sequential Brier Scoring

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `falsifiable-calibration-ledger-via-sequential-brier-scoring-928b190d87ee`
Run ID: `falsifiable-calibration-ledger-via-sequential-brier-scoring-928b190d87ee-20260529T052913612136+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/87997efde574

## What looked useful

A direct counterexample shows cumulative Brier can reliably favor a miscalibrated but more informative forecaster over a calibrated uninformative forecaster; in 1,000 trials of 2,000 events, the miscalibrated forecaster won by Brier in 100% of trials while mean ECE was about 0.0996 versus 0.0089 for the calibrated climatology.

## Boundaries and scale limits

Synthetic binary streams only; no real human/model forecast traces, adversarial governance, nonstationary deployment, or large-scale operational ledger was tested.

## Claim scope

Sequential cumulative Brier score alone was tested as a calibration ledger on controlled binary forecast streams.

## Why it stopped

Early direct falsification on controlled binary streams: sequential Brier score alone confounds calibration with information/sharpness and therefore cannot certify calibration by itself.

## Recommended next action

Stop this Brier-only calibration-ledger claim; a bounded follow-up should test a multi-metric ledger that keeps Brier for accuracy but adds sequential reliability diagnostics for calibration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sequential multi-metric forecast ledger with separate reliability diagnostics
- Success threshold: The diagnostic flags the informative-miscalibrated forecaster in at least 95% of 1,000 trials at horizon 2,000 while keeping false alarms below 5% for calibrated forecasters; Brier remains reported only as accuracy, not calibration.
- Stop condition: Stop if the added reliability diagnostic either fails the 95% detection threshold or exceeds the 5% false alarm threshold on calibrated streams.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-calibration-ledger-via-sequential-brier-scoring-928b190d87ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
