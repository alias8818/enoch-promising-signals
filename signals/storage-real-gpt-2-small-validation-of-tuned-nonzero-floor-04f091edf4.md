# Storage-real GPT-2-small validation of tuned nonzero-floor 4-bit Adam second moments

Status: `useful_signal`
Project ID: `storage-real-gpt-2-small-validation-of-tuned-nonzero-floor-04f091edf4`
Run ID: `storage-real-gpt-2-small-validation-of-tuned-nonzero-floor-04f091edf4-20260514T094156395854+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Storage-real GPT-2-small validation of tuned nonzero-floor 4-bit Adam second moments: internal_generated:storage-real-gpt-2-small-validation-of-tuned-nonzero-floor-04f091edf4

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Storage-real tuned 4-bit second moments were stable and compact but underperformed FP32 AdamW by +0.2606 mean final eval loss after 1000 steps across three seeds; controller follow-up depth is 4, so no further deepen/retry follow-up is recommended.

## Recommended next action

Stop this depth-4 follow-up: bounded direct GPT-2-small evidence supports the nonzero-floor mechanism but shows a consistent loss gap and throughput penalty versus FP32 AdamW, so it is not paper-ready.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/storage-real-gpt-2-small-validation-of-tuned-nonzero-floor-04f091edf4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
