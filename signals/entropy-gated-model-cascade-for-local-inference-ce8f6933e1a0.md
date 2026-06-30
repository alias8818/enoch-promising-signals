# Entropy-Gated Model Cascade for Local Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `entropy-gated-model-cascade-for-local-inference-ce8f6933e1a0`
Run ID: `entropy-gated-model-cascade-for-local-inference-ce8f6933e1a0-20260525T171041427494+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/aef8ea46c8ed

## What looked useful

A conservative zero-drop calibration rule yielded mean cascade accuracy 0.9244 versus large-model accuracy 0.9220, worst delta 0.0000, mean expert rate 0.2036, and mean modeled speedup 1.369x over five shuffled splits. A permissive 0.5 percentage-point calibration-drop rule failed on one split, showing threshold selection is a key risk.

## Boundaries and scale limits

Single classification dataset, two related encoder classifiers, 200-example calibration splits, 672-example test splits, and modeled sequential cascade latency from isolated model timings rather than an integrated serving benchmark. No generative LLM, multitask, production batching, or large-expert validation was performed.

## Claim scope

On GLUE/SST-2 validation with DistilBERT SST-2 as the small model and BERT-base SST-2 as the larger expert, conservative entropy gating preserved larger-model accuracy across five shuffled calibration/test splits while accepting about 80% of examples at the small-model stage and reducing modeled sequential per-example latency.

## Why it stopped

The run produced direct bounded evidence for the mechanism but not broad or publication-grade validation; the aggressive-threshold failure means the simple cascade is useful but not robust enough to claim as a paper result.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should implement an integrated serving benchmark with confidence-bound entropy calibration and compare entropy against margin/max-probability gates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated serving benchmark for confidence-calibrated entropy cascades
- Success threshold: Across all tested datasets, cascade accuracy is no more than 0.5 percentage points below large-only accuracy and measured p50 latency improves by at least 1.25x with no p95 regression above 5%.
- Stop condition: Stop if any dataset loses more than 1.0 percentage point accuracy at less than 1.1x measured latency speedup after confidence-bound threshold tuning.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gated-model-cascade-for-local-inference-ce8f6933e1a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
