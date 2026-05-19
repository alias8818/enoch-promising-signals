# Bounded Production-Style Strict N-gram Drafting CPU Serving Validation

Status: `useful_signal`
Project ID: `bounded-production-style-strict-n-gram-drafting-cpu-servin-4ef349b27f`
Run ID: `bounded-production-style-strict-n-gram-drafting-cpu-servin-4ef349b27f-20260515T085456753286+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Bounded Production-Style Strict N-gram Drafting CPU Serving Validation: internal_generated:bounded-production-style-strict-n-gram-drafting-cpu-servin-4ef349b27f

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Mixed bounded validation rather than full publication evidence: exact greedy equivalence held and repetitive prompts reached 3.946x speedup, but the unfavorable natural control produced no meaningful serving acceleration.

## Recommended next action

Stop as not paper-ready: bounded direct CPU validation supports the strict n-gram mechanism on repetitive contexts but the natural-prompt control achieved only 1.003x speedup and 0% target-forward reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production Trace Strict N-gram Drafting CPU Serving Validation
- Success threshold: On a representative production-like trace, achieve >=1.5x micro throughput, >=30% target-forward reduction, exact greedy output equivalence, and no p95 latency regression versus cached greedy baseline.
- Stop condition: Stop if exact-span repetition produces median accepted draft length <=1 or if throughput remains <1.2x baseline after n-gram/draft-length tuning.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-production-style-strict-n-gram-drafting-cpu-servin-4ef349b27f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
