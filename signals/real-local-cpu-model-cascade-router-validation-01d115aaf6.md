# Real local CPU model cascade router validation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-local-cpu-model-cascade-router-validation-01d115aaf6`
Run ID: `real-local-cpu-model-cascade-router-validation-01d115aaf6-20260620T230035546741+0000`

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

- Parent run decision: Local cascade router: complexity-classifier dispatch on CPU: enoch://control-plane/projects/local-cascade-router-complexity-classifier-dispatch-on-cpu-09119cc43a7c/runs/local-cascade-router-complexity-classifier-dispatch-on-cpu-09119cc43a7c-20260620T224413107748+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/08f267be815c

## What looked useful

The calibrated confidence router was faster than large-only inference but failed the predeclared held-out accuracy-retention threshold: cascade accuracy 0.890625 versus large-only 0.90625, with 1.7219x total-latency speedup and 1.953% escalation. The larger classifier improved over small-only, but confidence gating selected too few examples and reduced accuracy below both baselines.

## Boundaries and scale limits

Single dataset, single seed, unbatched CPU inference, two classifier models, no generative tasks, no production traffic, no quantized runtime, and no multi-task routing.

## Claim scope

Tier 1 local CPU SST-2 validation of a two-stage confidence cascade using DistilBERT SST-2 as the small model and BERT SST-2 as the large model on 128 calibration and 256 held-out validation examples.

## Why it stopped

Controlled small direct test failed the stated threshold: cascade accuracy was more than 0.01 below large-only accuracy despite exceeding the latency speedup requirement.

## Recommended next action

Stop this run as a no-paper useful negative signal; a bounded deepen follow-up should test learned/calibrated routing features beyond raw max softmax confidence on several text-classification tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated multi-feature CPU cascade router across small classification tasks
- Success threshold: Learned router mean held-out accuracy >= large-only accuracy - 0.01 on each task and mean total-latency speedup vs large-only >= 1.25x, with no task losing more than 2 accuracy points.
- Stop condition: Stop if the learned router fails to beat raw confidence routing on at least two tasks or if calibration does not transfer to held-out splits within the stated accuracy bound.

## Evidence references

- Artifact root: `<local-path>/projects/real-local-cpu-model-cascade-router-validation-01d115aaf6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
