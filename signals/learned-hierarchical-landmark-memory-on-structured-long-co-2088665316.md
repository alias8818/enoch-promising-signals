# Learned Hierarchical Landmark Memory on Structured Long-Context Recall

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `98`
Project ID: `learned-hierarchical-landmark-memory-on-structured-long-co-2088665316`
Run ID: `learned-hierarchical-landmark-memory-on-structured-long-co-2088665316-20260514T175556755185+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/28a4940a68c0

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Positive controlled synthetic Tier 1 mechanism evidence, but not publication-grade direct evidence; the result is architecture-biased and lacks scale, ablations, robustness, and naturalistic validation.

## Recommended next action

Stop paper gating for this run; use the positive Tier 1 synthetic result to run a bounded medium confirmation with parameter-matched dense/retrieval baselines, hierarchy ablations, and longer/noisier structured recall.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Confirmation of Hierarchical Landmark Memory on Robust Structured Recall
- Success threshold: Mean long-context exact-match accuracy at least 85% and at least 25 percentage points above every parameter-matched baseline across 5 seeds, with every landmark ablation dropping by at least 15 percentage points on the long split.
- Stop condition: Stop as negative if the full landmark model falls below 70% mean long-context accuracy, beats the best matched baseline by less than 10 percentage points, or ablations do not materially reduce long-context accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/learned-hierarchical-landmark-memory-on-structured-long-co-2088665316`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
