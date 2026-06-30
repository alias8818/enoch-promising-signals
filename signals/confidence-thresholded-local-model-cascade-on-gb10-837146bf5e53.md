# Confidence-thresholded local model cascade on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-thresholded-local-model-cascade-on-gb10-837146bf5e53`
Run ID: `confidence-thresholded-local-model-cascade-on-gb10-837146bf5e53-20260628T140013935511+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1d6ea97e5fcf

## What looked useful

Threshold 0.98 reached 0.9335 accuracy versus 0.9106 small-only and 0.9243 large-only on 872 SST-2 validation examples; direct selected-threshold timing was 929.4 examples/s versus 749.8 examples/s for the large-only baseline from the full validation run, with 96/872 fallback calls.

## Boundaries and scale limits

Single classification dataset, single model pair, threshold selected from the same validation table, no held-out calibration split, no multi-task robustness, and not a full generative local LLM serving benchmark.

## Claim scope

On the GLUE SST-2 validation split on GB10, a confidence-thresholded local classifier cascade using DistilBERT SST-2 as the small model and siebert/sentiment-roberta-large-english as fallback improved accuracy at threshold 0.98 while calling the fallback on 11.0% of examples and running faster than large-only inference.

## Why it stopped

No-paper useful signal: the local proxy supports the mechanism, but evidence is too narrow and threshold-selected on the evaluation table for a paper-positive decision.

## Recommended next action

Run a held-out calibration/evaluation follow-up across at least three classification datasets or model pairs, selecting thresholds only on calibration data and reporting direct end-to-end timing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out calibration test for confidence-thresholded local cascades
- Success threshold: For at least two of three task/model pairs, a calibration-selected threshold improves accuracy over small-only, stays within 0.5 percentage points of or exceeds large-only accuracy, and reduces large-model calls by at least 70% with direct throughput above large-only.
- Stop condition: Stop if calibration-selected thresholds fail to beat small-only accuracy or require more than 50% fallback calls on two task/model pairs.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-thresholded-local-model-cascade-on-gb10-837146bf5e53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
