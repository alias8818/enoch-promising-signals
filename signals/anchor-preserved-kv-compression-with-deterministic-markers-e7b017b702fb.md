# Anchor-Preserved KV Compression with Deterministic Markers

Status: `compute_scale_blocked`
Project ID: `anchor-preserved-kv-compression-with-deterministic-markers-e7b017b702fb`
Run ID: `anchor-preserved-kv-compression-with-deterministic-markers-e7b017b702fb-20260515T153314745247+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1997a6324910

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic attention evidence supports anchor-preserved marker retrieval when anchors fit the cache budget, but this is not full validation and overload tests show recency loss and degraded marker accuracy when markers consume or exceed the budget.

## Recommended next action

Stop this run as a proxy-only mixed result; next action is a bounded real-transformer KV-cache evaluation before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Transformer Anchor-Preserved KV Cache Evaluation
- Success threshold: At least 20 percentage-point marker-answer accuracy improvement over the best non-anchor baseline at two cache budgets, with recent-context accuracy degradation no worse than 5 percentage points and measured memory savings matching the intended KV budget.
- Stop condition: Stop if anchor-preserved KV improves synthetic retention but fails to improve real-model marker-answer accuracy by at least 10 percentage points over the best matched-budget baseline, or if recent-context accuracy drops more than 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserved-kv-compression-with-deterministic-markers-e7b017b702fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
