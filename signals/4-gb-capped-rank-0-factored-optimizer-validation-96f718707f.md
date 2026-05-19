# 4 GB-capped rank-0 factored optimizer validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `4-gb-capped-rank-0-factored-optimizer-validation-96f718707f`
Run ID: `4-gb-capped-rank-0-factored-optimizer-validation-96f718707f-20260514T013426752425+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
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

- Internal Enoch project: 4 GB-capped rank-0 factored optimizer validation: internal_generated:4-gb-capped-rank-0-factored-optimizer-validation-96f718707f

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded direct validation met the optimizer-state cap but failed the AdamW-quality threshold: rank0 was +0.10995 nats/token worse than AdamW mean final validation loss after 600 steps across three fixed seeds.

## Recommended next action

Stop this validation as no-paper; only pursue one final depth-4 follow-up testing a hybrid rank0 momentum/sketch variant under the same fixed-seed AdamW loss-gap criterion if the controller permits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid rank0 momentum under a 4 GiB optimizer-state cap
- Success threshold: Mean final validation loss within 0.03 nats/token of AdamW across seeds 11, 17, and 23, all runs finite, and measured/projected optimizer state <=4 GiB.
- Stop condition: Stop if the hybrid remains >0.03 nats/token worse than AdamW on the bounded validation, exceeds the 4 GiB optimizer-state cap, or is not better than the current rank0 factored optimizer.

## Evidence references

- Artifact root: `<local-path>/projects/4-gb-capped-rank-0-factored-optimizer-validation-96f718707f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
