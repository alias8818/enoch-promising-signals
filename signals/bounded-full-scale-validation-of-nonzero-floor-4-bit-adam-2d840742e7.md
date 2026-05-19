# Bounded full-scale validation of nonzero-floor 4-bit Adam second moments

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `bounded-full-scale-validation-of-nonzero-floor-4-bit-adam-2d840742e7`
Run ID: `bounded-full-scale-validation-of-nonzero-floor-4-bit-adam-2d840742e7-20260514T090756836651+0000`

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

- Internal Enoch project: Bounded full-scale validation of nonzero-floor 4-bit Adam second moments: internal_generated:bounded-full-scale-validation-of-nonzero-floor-4-bit-adam-2d840742e7

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded direct validation supports the nonzero-floor mechanism but falsifies publication readiness: zero-floor 4-bit collapses, nonzero-floor trains, and the best tuned floor does not robustly beat a tuned real AdamW baseline.

## Recommended next action

Stop paper escalation for this run; only pursue one final depth-4 follow-up if it implements storage-real 4-bit state and tests GPT-2-small-class loss/memory against a tuned AdamW baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Storage-real GPT-2-small validation of tuned nonzero-floor 4-bit Adam second moments
- Success threshold: Across at least 3 fixed seeds, storage-real nonzero-floor 4-bit Adam reaches validation loss within 1% of tuned AdamW while reducing measured second-moment optimizer-state memory by at least 75% and avoiding zero-floor collapse.
- Stop condition: Stop if tuned AdamW remains better by more than 1% validation loss, if the packed implementation fails to deliver at least 75% second-moment memory reduction, or if any seed diverges under the best tuned nonzero-floor setting.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-full-scale-validation-of-nonzero-floor-4-bit-adam-2d840742e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
