# Adaptive Queue-Depth Router for Local Model Cascades

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-queue-depth-router-for-local-model-cascades-b159d0823591`
Run ID: `adaptive-queue-depth-router-for-local-model-cascades-b159d0823591-20260605T213838416749+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1fd369b1bf6e

## What looked useful

Queue-pressure feedback can recover deadline-weighted utility versus an untuned fixed confidence threshold, but naive pressure-based threshold lowering loses to better static thresholds under higher load and falls below all-small routing in overload.

## Boundaries and scale limits

No real local models, GPU batching, KV-cache behavior, token-length distributions, real confidence calibration, or task-level accuracy were measured. Results are mechanism-level simulation evidence only.

## Claim scope

In a deterministic synthetic two-stage cascade queueing simulation with 6000 requests per seed, 12 seeds, stochastic arrivals/service times, and a 900 ms deadline, a queue-depth-aware threshold beat the originally selected fixed threshold across tested loads but did not dominate a sweep of tuned static thresholds.

## Why it stopped

Synthetic mechanism evidence was mixed: adaptive routing helped against the initial fixed baseline but failed to beat the stronger tuned-static control at moderate-to-high load, so this is not a paper-ready validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should replay actual local small/large model requests and compare adaptive routing against an online-tuned static threshold plus all-small/all-large controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Replay for Queue-Depth Cascade Routing
- Success threshold: Adaptive routing improves deadline-weighted utility by at least 3% relative to the best tuned static-threshold control in at least two adjacent non-overload load regimes without losing more than 1% in overload.
- Stop condition: Stop if adaptive routing fails to beat the tuned static-threshold control by at least 1% in the first real-model load sweep or if all-small dominates utility across all saturation and overload regimes.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-queue-depth-router-for-local-model-cascades-b159d0823591`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
