# Transformer-scale residual hidden-state router for frozen local LM specialists

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `transformer-scale-residual-hidden-state-router-for-frozen-6d36c9a4d8`
Run ID: `transformer-scale-residual-hidden-state-router-for-frozen-6d36c9a4d8-20260514T172956846502+0000`

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

- Internal Enoch project: Transformer-scale residual hidden-state router for frozen local LM specialists: internal_generated:transformer-scale-residual-hidden-state-router-for-frozen-6d36c9a4d8

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Fixed-seed Tier 2 validation showed the learned residual hidden-state router did not beat the frozen dense baseline or the no-residual hidden ablation, although oracle residual selection showed useful specialist information exists.

## Recommended next action

Stop this run as a Tier 2 no-paper result; only run a bounded deepen follow-up for hard or entropy-regularized residual routing if the controller wants to test the diagnosed soft-gate gap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-gated residual hidden-state router for frozen local LM specialists
- Success threshold: On the fixed-seed synthetic setup, residual hard/regularized routing must improve held-out NLL by at least 5 percent versus frozen base and no-residual hidden router, and recover at least half of the oracle residual-hidden improvement; natural-language promotion requires the same direction across three seeds.
- Stop condition: Stop if hard or entropy-regularized residual routing still ties or underperforms the frozen base/no-residual ablation, or if gate sharpness improves without NLL improvement.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-scale-residual-hidden-state-router-for-frozen-6d36c9a4d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
