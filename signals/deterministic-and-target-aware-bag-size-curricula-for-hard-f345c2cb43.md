# Deterministic and Target-Aware Bag-Size Curricula for Hard Superposition

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `72`
Project ID: `deterministic-and-target-aware-bag-size-curricula-for-hard-f345c2cb43`
Run ID: `deterministic-and-target-aware-bag-size-curricula-for-hard-f345c2cb43-20260514T125006737432+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `72`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- external source URL present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Efficient Pre-Training with Token Superposition: https://arxiv.org/abs/2605.06546
- TST Branch Oracle: Discriminative Proxy Ranking for Token-Superposition Variant Selection: https://arxiv.org/abs/2605.06546

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Controlled small direct test on the hard target distribution found target_aware final hard-target MSE 7.27% worse than fixed_hard, despite beating naive deterministic_linear; this is not a full-scale validation, but it directly falsifies the stated Tier 1 threshold.

## Recommended next action

Stop this follow-up as a Tier 1 direct early falsification: target_aware missed the configured hard-target success threshold by losing to fixed_hard on 8/8 paired seeds.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-and-target-aware-bag-size-curricula-for-hard-f345c2cb43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
