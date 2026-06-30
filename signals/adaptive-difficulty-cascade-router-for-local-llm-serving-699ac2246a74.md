# Adaptive Difficulty Cascade Router for Local LLM Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-difficulty-cascade-router-for-local-llm-serving-699ac2246a74`
Run ID: `adaptive-difficulty-cascade-router-for-local-llm-serving-699ac2246a74-20260613T121021059025+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/747cee35096f

## What looked useful

Small-model margin had some predictive signal for correctness (AUC 0.6535), and same-sample thresholding showed an apparent 1.16x speedup at near-large accuracy. However, calibration-to-held-out transfer failed: the selected threshold reached only 0.6333 held-out accuracy versus 0.7333 for large-only, and no held-out oracle threshold both preserved large accuracy within 0.02 and beat large-only serial latency.

## Boundaries and scale limits

One dataset, one main model pair, no production serving stack, no concurrent request queueing, no learned router, and threshold selection evaluated on a 60-example held-out split.

## Claim scope

Local GB10 inference probe on 120 HellaSwag validation examples using SmolLM2-360M as the small model, Qwen2.5-1.5B as the large model, continuation scoring, and a serial margin-threshold cascade.

## Why it stopped

Held-out evidence did not support the threshold-only adaptive difficulty cascade; this is a bounded local inference result, not a full production-serving validation.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded action is to test a learned router with richer features on a larger train/validation/test split before considering production serving experiments.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Difficulty Router for Local LLM Cascades
- Success threshold: On held-out data, learned router accuracy >= large-only accuracy - 0.02 and estimated serial seconds/example <= 0.90 * large-only seconds/example on both tasks or on the pooled predeclared benchmark.
- Stop condition: Stop if the learned router fails to beat the best margin-threshold baseline or cannot meet the accuracy tolerance at any route rate that saves at least 10% serial compute.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-difficulty-cascade-router-for-local-llm-serving-699ac2246a74`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
