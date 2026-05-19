# Per-seed noninferiority test for confidence-router cascades on a larger direct task

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-seed-noninferiority-test-for-confidence-router-cascade-2a5353e1a8`
Run ID: `per-seed-noninferiority-test-for-confidence-router-cascade-2a5353e1a8-20260518T235253493340+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4a1d9380147a

## What looked useful

Conservative validation calibration rescued the confidence-router cascade: the confirmed run had mean cascade accuracy 0.6840 vs strong accuracy 0.6830, worst bootstrap lower bound -0.65 pp, and mean expensive-call reduction 37.3%. The primary less-conservative rule reduced calls more but failed strict bootstrap noninferiority on one seed.

## Boundaries and scale limits

Single dataset, local scikit-learn text classifiers, five seeds, and invocation-count cost only. The implementation uses separate vectorizers and does not establish production wall-clock latency or API dollar-cost savings. Naive threshold selection at the full 1.0 percentage-point validation margin failed the strict per-seed bootstrap criterion.

## Claim scope

On full 20 Newsgroups text classification with five train/validation seeds, a conservative confidence-router cascade using a 0.25 percentage-point validation selection margin passed per-seed paired-bootstrap noninferiority at a 1.0 percentage-point test margin while reducing expensive-model invocations by at least 31.8% on every seed.

## Why it stopped

Moderate direct evidence supports a calibration-sensitive mechanism, but it is not paper-positive because it uses one dataset, a post-primary sensitivity-selected calibration margin, and invocation reduction rather than optimized serving latency.

## Recommended next action

Stop this run as no-paper useful evidence; next run should pre-register the 0.25 pp validation selection margin and test cross-dataset robustness plus a shared-feature latency measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pre-registered conservative confidence-router validation on a second direct text task
- Success threshold: Every seed has paired-bootstrap lower 95% CI for cascade-minus-strong accuracy >= -1.0 percentage point, every seed reduces expensive-model invocations by >=25%, and optimized median inference latency is lower than strong-only inference.
- Stop condition: Stop as negative if any seed fails the bootstrap noninferiority threshold or if invocation savings do not translate into optimized latency savings.

## Evidence references

- Artifact root: `<local-path>/projects/per-seed-noninferiority-test-for-confidence-router-cascade-2a5353e1a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
