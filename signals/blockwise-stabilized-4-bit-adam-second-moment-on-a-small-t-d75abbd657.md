# Blockwise stabilized 4-bit Adam second moment on a small transformer

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `blockwise-stabilized-4-bit-adam-second-moment-on-a-small-t-d75abbd657`
Run ID: `blockwise-stabilized-4-bit-adam-second-moment-on-a-small-t-d75abbd657-20260514T085706750253+0000`

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

- Internal Enoch project: Blockwise stabilized 4-bit Adam second moment on a small transformer: internal_generated:blockwise-stabilized-4-bit-adam-second-moment-on-a-small-t-d75abbd657

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 direct small-transformer evidence supports the nonzero-floor mechanism and falsifies naive 4-bit quantization, but the slow scale-decay stabilized variant underperformed the simpler floor-only ablation and the run is not publication-grade.

## Recommended next action

Stop this run as not paper-ready; the bounded next action is a direct GPT-2-small-class or parameter-matched subword-transformer validation of the floor-only 4-bit second-moment variant with a realistic packed/fused optimizer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded full-scale validation of nonzero-floor 4-bit Adam second moments
- Success threshold: Across at least three fixed seeds, floor-only 4-bit second moments must remain finite, reduce optimizer state by at least 40%, and stay within 0.01 validation loss or 1% perplexity of AdamW without requiring materially slower wall-clock training in a realistic implementation.
- Stop condition: Stop if floor-only 4-bit diverges in any repeated seed, loses more than 0.01 validation loss or 1% perplexity versus AdamW at matched budget, or realistic packing/fusion fails to produce meaningful memory savings.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-stabilized-4-bit-adam-second-moment-on-a-small-t-d75abbd657`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
