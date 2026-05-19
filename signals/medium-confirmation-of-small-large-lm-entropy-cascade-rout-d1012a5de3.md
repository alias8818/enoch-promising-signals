# Medium Confirmation of Small/Large LM Entropy Cascade Routing

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `medium-confirmation-of-small-large-lm-entropy-cascade-rout-d1012a5de3`
Run ID: `medium-confirmation-of-small-large-lm-entropy-cascade-rout-d1012a5de3-20260514T153806743669+0000`

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

- Internal Enoch project: Medium Confirmation of Small/Large LM Entropy Cascade Routing: internal_generated:medium-confirmation-of-small-large-lm-entropy-cascade-rout-d1012a5de3

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium confirmation produced mixed direct evidence rather than publication-grade support: at 80% calibration target entropy recovered 79.0% of the small-to-large NLL gap with 69.5% large calls, but measured sequential cost was about 1.018x all-large and max-prob confidence was slightly better.

## Recommended next action

Stop this run as no-paper: medium direct evidence shows entropy routing beats random but fails to establish entropy-specific superiority over max-prob and does not reduce measured sequential cost at the 80% recovery target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Conditional serving benchmark for entropy versus confidence cascade routing
- Success threshold: At least 80% recovery of the all-small to all-large quality gap with at least 15% measured end-to-end cost or latency reduction versus all-large, and entropy must beat max-prob at matched measured cost on most evaluated settings.
- Stop condition: Stop if measured cost reduction is below 15% at 80% quality-gap recovery, or if max-prob/confidence baselines match or beat entropy at matched cost across the tested settings.

## Evidence references

- Artifact root: `<local-path>/projects/medium-confirmation-of-small-large-lm-entropy-cascade-rout-d1012a5de3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
