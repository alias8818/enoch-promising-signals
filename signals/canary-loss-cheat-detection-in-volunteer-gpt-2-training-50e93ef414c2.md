# Canary-Loss Cheat Detection in Volunteer GPT-2 Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `canary-loss-cheat-detection-in-volunteer-gpt-2-training-50e93ef414c2`
Run ID: `canary-loss-cheat-detection-in-volunteer-gpt-2-training-50e93ef414c2-20260629T180139010799+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/74f95ca5e0d1

## What looked useful

Across 8 seeds per condition, a zero-honest-FP threshold detected 5/8 cheaters with one canary insertion and 8/8 cheaters with 3, 10, 20, or 40 insertions; 40 insertions gave mean cheater z=16.59 versus mean honest z=0.086 and AUROC 1.0.

## Boundaries and scale limits

Tested only on a small 2-layer 96-wide GPT-style model trained from scratch on synthetic token data; not tested on real GPT-2-small, natural language corpora, federated aggregation, update-only observability, or adaptive adversaries.

## Claim scope

In a controlled synthetic causal-transformer setup, repeated high-entropy canary insertion into a volunteer's local training stream makes that volunteer's final model assign unusually low canary loss relative to matched decoys and honest controls.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only in a synthetic proxy, not direct volunteer GPT-2 training.

## Recommended next action

Run a bounded direct GPT-2-small or nanoGPT-on-natural-text follow-up with held-out honest calibration and canary exposure sweep before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2-small canary-loss detection on natural text
- Success threshold: At least 95% true-positive rate at no more than 1% false-positive rate for a predeclared canary exposure level, with the effect persisting across at least 5 seeds and natural-text controls.
- Stop condition: Stop if cheater and honest normalized canary-loss distributions overlap enough that AUROC is below 0.8 or the predeclared false-positive target cannot be met.

## Evidence references

- Artifact root: `<local-path>/projects/canary-loss-cheat-detection-in-volunteer-gpt-2-training-50e93ef414c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
