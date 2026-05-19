# Entropy-Gated Local Model Cascade

Status: `compute_scale_blocked`
Project ID: `entropy-gated-local-model-cascade-e53ac0edbaa3`
Run ID: `entropy-gated-local-model-cascade-e53ac0edbaa3-20260515T042030684969+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7250694f55c4

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy classification evidence supports the entropy-gating mechanism but does not directly validate local language-model cascade quality, latency, batching, or memory behavior.

## Recommended next action

Stop this run as a proxy-supported but not paper-ready result; next run should perform a direct local LLM cascade benchmark with validation-set entropy thresholds and measured serving latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Local LLM Entropy-Gated Cascade Benchmark
- Success threshold: On held-out test sets, cascade quality is within 1 percentage point of large-only while reducing large-model calls by at least 50% and measured p50 or mean latency by at least 30% versus large-only.
- Stop condition: Stop as negative if validation-selected entropy thresholds cannot reach within 1 percentage point of large-only quality below 80% of large-only measured latency on either benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gated-local-model-cascade-e53ac0edbaa3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
