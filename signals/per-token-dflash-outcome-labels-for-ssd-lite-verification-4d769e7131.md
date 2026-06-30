# Per-token DFlash outcome labels for SSD-lite verification prediction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `per-token-dflash-outcome-labels-for-ssd-lite-verification-4d769e7131`
Run ID: `per-token-dflash-outcome-labels-for-ssd-lite-verification-4d769e7131-20260520T015407832810+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: SSD-lite outcome prediction on real DFlash verification traces: enoch://control-plane/projects/ssd-lite-outcome-prediction-on-real-dflash-verification-tr-bbe1c536e9/runs/ssd-lite-outcome-prediction-on-real-dflash-verification-tr-bbe1c536e9-20260519T233514486181+0000
- Parent run decision: SSD-lite Verification-Outcome Prediction for DFlash: enoch://control-plane/projects/ssd-lite-verification-outcome-prediction-for-dflash-cc1d23c80a4f/runs/ssd-lite-verification-outcome-prediction-for-dflash-cc1d23c80a4f-20260519T231446393478+0000

## What looked useful

Token-plus-DFlash achieved mean AUC 0.8727 versus 0.5845 for token-only and 0.5144 for randomized-label control; all five fixed seeds improved over both controls.

## Boundaries and scale limits

Synthetic arithmetic traces only; no real model-generated SSD-lite traces, no large language model verifier pipeline, no held-out task-family transfer, and no deployment-time leakage audit.

## Claim scope

In a deterministic synthetic SSD-lite arithmetic verifier, per-token DFlash prefix outcome labels substantially improve partial-prefix final verification prediction over token-only and randomized-label controls across five fixed seeds.

## Why it stopped

Tier-2 local synthetic validation supports the mechanism but is not paper-grade direct evidence on real SSD-lite model traces.

## Recommended next action

Run the same prediction protocol on real model-generated SSD-lite traces with DFlash labels computed only from information available at the intended prefix inference point.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace DFlash prefix labels for SSD-lite verification prediction
- Success threshold: Mean AUC improvement of at least 0.05 over token-only and randomized-label controls across at least five fixed seeds, with every seed non-negative and no leakage findings.
- Stop condition: Stop if DFlash improves mean AUC by less than 0.02 over token-only, fails to beat randomized labels, or requires non-causal final-outcome information.

## Evidence references

- Artifact root: `<local-path>/projects/per-token-dflash-outcome-labels-for-ssd-lite-verification-4d769e7131`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
