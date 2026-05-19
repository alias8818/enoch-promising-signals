# Medium natural long-context validation of anchor-gated KV eviction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-natural-long-context-validation-of-anchor-gated-kv-913bb4d635`
Run ID: `medium-natural-long-context-validation-of-anchor-gated-kv-913bb4d635-20260513T223227243252+0000`

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

- Internal Enoch project: Medium natural long-context validation of anchor-gated KV eviction: internal_generated:medium-natural-long-context-validation-of-anchor-gated-kv-913bb4d635

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium natural-text GPT-2-small evaluation supports anchor-gated retention over same maximum-budget recency/random controls and a period-only ablation, but anchor-gated retention remains +0.7345 mean NLL worse than full context and was not validated in an optimized KV-serving backend.

## Recommended next action

Stop this run as no-paper; run a bounded optimized-backend follow-up only if the controller wants direct memory, throughput, and published-baseline evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized long-context anchor-gated KV eviction against published baselines
- Success threshold: At 50% or lower KV memory, anchor-gated eviction must be within +0.15 mean NLL of full context, beat published matched-budget baselines by at least 0.05 mean NLL, and improve measured decode throughput by at least 10% versus full-cache decoding.
- Stop condition: Stop if anchor-gated eviction remains more than +0.15 mean NLL worse than full context, fails to beat a published matched-budget baseline, or cannot show a throughput gain in the optimized backend.

## Evidence references

- Artifact root: `<local-path>/projects/medium-natural-long-context-validation-of-anchor-gated-kv-913bb4d635`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
