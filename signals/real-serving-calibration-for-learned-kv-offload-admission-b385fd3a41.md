# Real-Serving Calibration for Learned KV Offload Admission

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `28`
Project ID: `real-serving-calibration-for-learned-kv-offload-admission-b385fd3a41`
Run ID: `real-serving-calibration-for-learned-kv-offload-admission-b385fd3a41-20260519T041743447198+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `28`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Real-Serving Calibration for Learned KV Offload Admission: internal_generated:real-serving-calibration-for-learned-kv-offload-admission-b385fd3a41

## What looked useful

Hard pressure guards were necessary for stability. Real-serving calibration did not create a measurable advantage over tuned threshold admission, and unguarded learned admission produced catastrophic tail-latency failures under long-context and bursty workloads.

## Boundaries and scale limits

No production inference server, real transformer KV cache manager, or private production trace was used. Results are local calibrated simulation evidence, not publication-grade real-serving evidence.

## Claim scope

On a local GB10-calibrated closed-loop serving simulator with fixed seeds, learned KV offload admission trained from immediate oracle labels did not beat simple pressure-threshold baselines; guarded learned policies matched the guard rather than improving on it.

## Why it stopped

Moderate local calibrated evidence directly falsified the learned-admission advantage over real threshold baselines in the tested closed-loop setting; guarded variants showed the guard, not calibration, carried the result.

## Recommended next action

Stop this follow-up at depth 4; do not write a paper from this result. A future distinct project would need a real serving-system integration or a closed-loop control learner, not another incremental proxy follow-up.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-serving-calibration-for-learned-kv-offload-admission-b385fd3a41`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
