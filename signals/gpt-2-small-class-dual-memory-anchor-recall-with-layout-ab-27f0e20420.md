# GPT-2-Small-Class Dual-Memory Anchor Recall With Layout Ablations

Status: `useful_signal`
Project ID: `gpt-2-small-class-dual-memory-anchor-recall-with-layout-ab-27f0e20420`
Run ID: `gpt-2-small-class-dual-memory-anchor-recall-with-layout-ab-27f0e20420-20260514T131527022804+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: GPT-2-Small-Class Dual-Memory Anchor Recall With Layout Ablations: internal_generated:gpt-2-small-class-dual-memory-anchor-recall-with-layout-ab-27f0e20420

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Corrected no-leak synthetic Tier 2 evidence supports the mechanism, but the run used a 3.3M toy model and oracle context slot/layout ids rather than publication-grade GPT-2-small-class evidence.

## Recommended next action

Stop this run as no-paper; run a bounded GPT-2-small-class follow-up without oracle slot labels to test whether learned layout memory reproduces the synthetic effect.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: No-Oracle GPT-2-Small-Class Dual-Memory Layout Recall
- Success threshold: Mean held-out shuffled-layout accuracy >= 0.90 for learned-layout dual memory and >= 0.20 absolute accuracy improvement over both dense and no-layout controls across three fixed seeds.
- Stop condition: Stop if learned-layout dual memory fails to exceed 0.50 held-out shuffled-layout accuracy after matched training budget, or if dense/no-layout controls close the gap below 0.20 absolute accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-dual-memory-anchor-recall-with-layout-ab-27f0e20420`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
