# Bounded scale-gap validation of calibrated PPL gates for no-KV LM cascades

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `78`
Project ID: `bounded-scale-gap-validation-of-calibrated-ppl-gates-for-n-08c789374b`
Run ID: `bounded-scale-gap-validation-of-calibrated-ppl-gates-for-n-08c789374b-20260515T073822983682+0000`

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

- Internal Enoch project: Bounded scale-gap validation of calibrated PPL gates for no-KV LM cascades: internal_generated:bounded-scale-gap-validation-of-calibrated-ppl-gates-for-n-08c789374b

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct bounded validation on Wikitext-2 GPT-2-family no-KV cascades found that max-accept calibration missed the held-out +0.05 nats/token budget across all tested scale gaps; conservative curves show only modest non-paper savings.

## Recommended next action

Stop the paper path for max-accept calibrated PPL gates; if one final depth-4 follow-up is allowed, test a conservative risk-controlled quantile gate across multiple datasets and seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Risk-controlled conservative quantile gates for no-KV GPT-2-family cascades
- Success threshold: For every required dataset/split/model-pair condition, target-call rate must drop by at least 10% while held-out mean NLL degradation stays at or below +0.05 nats/token; any condition exceeding +0.05 nats/token falsifies the follow-up.
- Stop condition: Stop and finalize negative if any required condition exceeds +0.05 nats/token or if median target-call reduction is below 10%.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-scale-gap-validation-of-calibrated-ppl-gates-for-n-08c789374b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
