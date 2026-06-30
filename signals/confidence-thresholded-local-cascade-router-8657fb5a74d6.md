# Confidence-thresholded local cascade router

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-thresholded-local-cascade-router-8657fb5a74d6`
Run ID: `confidence-thresholded-local-cascade-router-8657fb5a74d6-20260621T035544776196+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5f990dbbbaa

## What looked useful

Threshold 0.60 was best under calibrated confidence with accuracy 0.9818 versus remote-only 0.9850 and 91.50% cost savings. Threshold 0.80 was the cheapest threshold satisfying the guardrail across calibrated, overconfident-OOD, and globally miscalibrated conditions, with 76.42% cost savings in the calibrated row.

## Boundaries and scale limits

Synthetic task distribution and simulated confidence/correctness only; no real model logits, real serving traces, latency measurements, user-quality labels, or calibration curves were tested.

## Claim scope

On a deterministic 20,000-task synthetic binary routing benchmark with simulated local confidence and three tested confidence-shift conditions, a confidence-thresholded local cascade can satisfy a 1 percentage point accuracy-loss guardrail versus a remote-only baseline while reducing mean remote-equivalent cost.

## Why it stopped

No-paper closure: this run produced useful synthetic mechanism evidence, but the hypothesis is not validated on real inference traces or latency/cost measurements.

## Recommended next action

Run a bounded replay using real local-model logits and labels, including reliability/ECE diagnostics, and require at least 50% remote-call cost reduction while staying within 1 percentage point of the remote-only quality baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-logit calibration replay for confidence-thresholded local cascade routing
- Success threshold: At least 50% mean cost or remote-call reduction versus remote-only with accuracy no more than 1 percentage point below remote-only on the aggregate set and no more than 2 percentage points below remote-only on OOD/domain-shift slices.
- Stop condition: Stop as negative if no threshold meets the accuracy guardrail after calibration or if the best guardrail-satisfying threshold saves less than 25% mean cost.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-thresholded-local-cascade-router-8657fb5a74d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
