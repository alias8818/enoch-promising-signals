# Hierarchical Landmark Memory with Bounded O(sqrt(n)) State

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `hierarchical-landmark-memory-with-bounded-o-sqrt-n-state-71d6a457f6b2`
Run ID: `hierarchical-landmark-memory-with-bounded-o-sqrt-n-state-71d6a457f6b2-20260514T175125867797+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/28a4940a68c0

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic iid exact-recall accuracy decayed from 0.11355 at n=1024 to 0.02581 at n=65536 for the hierarchical ~3sqrt(n)-state memory, so the broad arbitrary-memory claim is not supported; this is not a full language-model validation.

## Recommended next action

Stop this run as a proxy early falsification of arbitrary O(sqrt(n)) recall; next run should test a learned hierarchical memory only on structured long-context tasks with explicit dense baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Hierarchical Landmark Memory on Structured Long-Context Recall
- Success threshold: Hierarchical memory reaches at least 95% of dense-baseline recall accuracy at the largest tested n while using no more than 4sqrt(n) retained state items and showing no monotonic collapse with n.
- Stop condition: Stop if learned/adaptive hierarchical memory remains below 80% of dense-baseline recall accuracy at two consecutive larger n values under matched parameter and compute budgets.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-landmark-memory-with-bounded-o-sqrt-n-state-71d6a457f6b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
