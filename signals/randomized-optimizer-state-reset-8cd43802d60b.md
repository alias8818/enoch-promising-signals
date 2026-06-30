# Randomized Optimizer State Reset

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `randomized-optimizer-state-reset-8cd43802d60b`
Run ID: `randomized-optimizer-state-reset-8cd43802d60b-20260528T202443443620+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/24065d3f03ce

## What looked useful

Across 48 paired reset-vs-baseline comparisons, reset variants won 12, tied 3, and lost 33 by held-out accuracy; aggregate mean test-accuracy delta was -0.00133 absolute, and every per-variant paired summary worsened held-out loss versus AdamW.

## Boundaries and scale limits

Only small synthetic classification tasks and simple random reset schedules were tested; no real datasets, transformers, large models, long pretraining, or adaptive reset triggers were evaluated.

## Claim scope

Naive randomized elementwise resets of AdamW exp_avg and exp_avg_sq did not reliably improve held-out accuracy or loss for small MLPs on noisy moons and 3-class spiral synthetic classification tasks over 8 fixed seeds per task.

## Why it stopped

Bounded direct small-task evidence is negative/mixed and insufficient for a paper; this is not a full-scale falsification of all optimizer reset ideas.

## Recommended next action

Stop this naive randomized reset line as no-paper evidence; only revisit with an adaptive stale-momentum trigger and direct real-data controls, not with more random reset sweeps.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/randomized-optimizer-state-reset-8cd43802d60b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
