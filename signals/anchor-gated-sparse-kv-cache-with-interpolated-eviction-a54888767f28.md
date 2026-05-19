# Anchor-Gated Sparse KV Cache with Interpolated Eviction

Status: `compute_scale_blocked`
Project ID: `anchor-gated-sparse-kv-cache-with-interpolated-eviction-a54888767f28`
Run ID: `anchor-gated-sparse-kv-cache-with-interpolated-eviction-a54888767f28-20260513T221643215169+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9e6a59ec3aba

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy benchmark found small aligned-synthetic gains but no robust advantage under anchor drift/decoys, so this is not paper-positive full validation.

## Recommended next action

Stop this run as a proxy-level mixed result; only proceed with a bounded real-transformer KV-cache follow-up if direct evidence is required.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer validation of anchor-gated KV eviction under matched cache budgets
- Success threshold: At two or more cache budgets, improve real-task quality by at least 3% relative over the best sparse baseline while preserving memory/runtime targets and showing no worse than 1% relative regression on drift/adversarial cases.
- Stop condition: Stop if the policy fails to beat the best sparse baseline on real-model quality at matched budget or if anchor-quality diagnostics show gains only in hand-aligned synthetic traces.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-sparse-kv-cache-with-interpolated-eviction-a54888767f28`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
