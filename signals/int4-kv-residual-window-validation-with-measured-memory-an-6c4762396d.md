# Int4 KV residual-window validation with measured memory and standard language metrics

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `58`
Project ID: `int4-kv-residual-window-validation-with-measured-memory-an-6c4762396d`
Run ID: `int4-kv-residual-window-validation-with-measured-memory-an-6c4762396d-20260514T122906793120+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Int4 KV residual-window validation with measured memory and standard language metrics: internal_generated:int4-kv-residual-window-validation-with-measured-memory-an-6c4762396d

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct bounded validation supports the residual-window mechanism only partially: int4-r128 still increased perplexity by 17.7% while saving 37.5% packed cache bytes, and stronger memory-saving variants had larger quality loss; operational memory savings were not demonstrated because no int4 attention kernel was available.

## Recommended next action

Stop this depth-4 follow-up: direct GPT-2/WikiText-2 validation found stable packed-cache savings but unacceptable perplexity regressions for paper-readiness, and controller lineage is already at the follow-up cap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/int4-kv-residual-window-validation-with-measured-memory-an-6c4762396d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
