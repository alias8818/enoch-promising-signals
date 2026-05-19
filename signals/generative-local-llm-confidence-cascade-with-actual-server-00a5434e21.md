# Generative local LLM confidence cascade with actual server tail latency

Status: `compute_scale_blocked`
Project ID: `generative-local-llm-confidence-cascade-with-actual-server-00a5434e21`
Run ID: `generative-local-llm-confidence-cascade-with-actual-server-00a5434e21-20260515T044522937978+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Generative local LLM confidence cascade with actual server tail latency: internal_generated:generative-local-llm-confidence-cascade-with-actual-server-00a5434e21

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium direct HTTP-server validation showed +41.28% p95 latency only by accepting 100% blankish small-model outputs; a stricter 0.90 threshold still accepted 33% blankish outputs and made cascade p95 29.50% slower than large-only.

## Recommended next action

Stop this raw confidence-cascade line: direct actual-server runs falsified the joint latency and usable-output threshold, and a longer run is not warranted without a different calibrated gate.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/generative-local-llm-confidence-cascade-with-actual-server-00a5434e21`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
