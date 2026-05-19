# Bounded Full-Scale Memory-Pressure Validation for Streamed AdamW Moments

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `78`
Project ID: `bounded-full-scale-memory-pressure-validation-for-streamed-6f56b891a0`
Run ID: `bounded-full-scale-memory-pressure-validation-for-streamed-6f56b891a0-20260514T021736732067+0000`

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

- Internal Enoch project: Bounded Full-Scale Memory-Pressure Validation for Streamed AdamW Moments: internal_generated:bounded-full-scale-memory-pressure-validation-for-streamed-6f56b891a0

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct full-scale optimizer-state validation found large memory-headroom gains but prohibitive streamed moment I/O overhead; this is not a full training result and does not justify paper writing.

## Recommended next action

Stop this paper path: bounded full-scale GB10 validation supports the memory mechanism but shows about 49x streamed-step slowdown at 6B elements over three steps, so it is not paper-positive without a new I/O/state backend.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Async or Host-Resident Streamed AdamW Backend in a Real Training Loop
- Success threshold: At model-scale, retain at least 35 GiB additional MemAvailable versus resident AdamW while keeping mean step time no more than 2x resident and matching loss within 1% over the validation window.
- Stop condition: Stop if the improved backend remains slower than 2x resident after 100 steps, loses the memory-headroom advantage below 35 GiB, or shows loss divergence above 1%.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-full-scale-memory-pressure-validation-for-streamed-6f56b891a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
