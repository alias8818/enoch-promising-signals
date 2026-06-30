# Outlier-Weighted Residual Channels via Activation Magnitude Tracking

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `outlier-weighted-residual-channels-via-activation-magnitude-tracking-708511e7ea14`
Run ID: `outlier-weighted-residual-channels-via-activation-magnitude-tracking-708511e7ea14-20260601T011301232920+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/03d2b34b4c60

## What looked useful

Activation magnitude tracking reliably finds stable high-magnitude channels and improves regularized readout performance when high-magnitude channels include target signal (+1.65% relative MSE at gamma 1.0 in aligned, +3.46% in mixed). It fails when high-magnitude channels are nuisance-only (-3.15% relative MSE at gamma 1.0), and stronger weighting increases both upside and downside.

## Boundaries and scale limits

No transformer, language-model, token-sequence, nonlinear training, real dataset, GPT-2-class baseline, or end-to-end validation was run. Evidence is a bounded mechanism probe, not a full architecture result.

## Claim scope

Synthetic residual-channel regression proxy with 256 channels, small calibration/readout training sets, ridge readouts, and controlled aligned, nuisance, and mixed outlier-channel scenarios.

## Why it stopped

Bounded proxy produced mixed evidence and a clear failure mode: magnitude alone is not a reliable channel-importance criterion, so the broad hypothesis is not supported without an additional usefulness signal.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should add a usefulness gate, such as gradient/loss-correlation or causal ablation, before applying activation-magnitude weights in a tiny transformer residual stream.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Magnitude-plus-usefulness gated residual channel weighting
- Success threshold: Across at least 30 synthetic seeds and 3 real/semi-real task seeds, gated weighting improves validation loss or readout MSE versus unweighted by at least 1% in signal-outlier settings and does not degrade nuisance-heavy settings by more than 1%.
- Stop condition: Stop if the usefulness gate either removes the aligned/mixed gain, still degrades nuisance settings by more than 1%, or requires compute beyond a bounded tiny-model experiment.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-weighted-residual-channels-via-activation-magnitude-tracking-708511e7ea14`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
