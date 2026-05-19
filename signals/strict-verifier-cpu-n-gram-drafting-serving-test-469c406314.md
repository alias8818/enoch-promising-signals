# Strict-Verifier CPU N-gram Drafting Serving Test

Status: `compute_scale_blocked`
Project ID: `strict-verifier-cpu-n-gram-drafting-serving-test-469c406314`
Run ID: `strict-verifier-cpu-n-gram-drafting-serving-test-469c406314-20260515T084446775951+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Strict-Verifier CPU N-gram Drafting Serving Test: internal_generated:strict-verifier-cpu-n-gram-drafting-serving-test-469c406314

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium fixed-seed CPU benchmark supported the mechanism but did not meet the strict paper gate for multi-model, concurrent, production-style serving evidence.

## Recommended next action

Stop this run as no-paper-yet: Tier 2 evidence supports the strict n-gram drafting mechanism, but full publication evidence needs bounded production-style serving validation across larger CPU-feasible models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded Production-Style Strict N-gram Drafting CPU Serving Validation
- Success threshold: For the best predeclared n-gram configuration, exact-match all requests, >=1.5x p50 tokens/sec versus greedy, no p95 latency regression greater than 10%, and random/no-draft controls <=1.1x greedy on both target models.
- Stop condition: Stop as negative if exact match fails, if best n-gram speedup is <1.2x on either model, or if p95 latency regresses by more than 25% under concurrent load.

## Evidence references

- Artifact root: `<local-path>/projects/strict-verifier-cpu-n-gram-drafting-serving-test-469c406314`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
