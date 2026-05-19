# Uncertainty-gated anchor KV eviction across real LMs and cache budgets

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `78`
Project ID: `uncertainty-gated-anchor-kv-eviction-across-real-lms-and-c-49749d6603`
Run ID: `uncertainty-gated-anchor-kv-eviction-across-real-lms-and-c-49749d6603-20260515T064708202150+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Uncertainty-gated anchor KV eviction across real LMs and cache budgets: internal_generated:uncertainty-gated-anchor-kv-eviction-across-real-lms-and-c-49749d6603

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded direct validation on real LMs showed uncertainty-gated anchors beat sliding windows in most cases but failed to consistently beat the simpler fixed-anchor baseline; fixed anchors won 13/20 budget cases while uncertainty anchors won 5/20.

## Recommended next action

Stop this uncertainty-gated-anchor claim as not paper-ready; any future work should separate simple fixed anchors from uncertainty selection and require uncertainty anchors to beat fixed anchors across larger long-context real-LM suites.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Fixed-prefix anchors versus sliding KV cache on long-context real-LM tasks
- Success threshold: Fixed anchors must beat sliding by at least 5% relative NLL or task-error reduction on a majority of model/task/budget cases and must not lose materially to random anchors.
- Stop condition: Stop if fixed anchors fail to beat sliding on most long-context cases, or if gains disappear when evaluated beyond GPT-2-family WikiText spans.

## Evidence references

- Artifact root: `<local-path>/projects/uncertainty-gated-anchor-kv-eviction-across-real-lms-and-c-49749d6603`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
