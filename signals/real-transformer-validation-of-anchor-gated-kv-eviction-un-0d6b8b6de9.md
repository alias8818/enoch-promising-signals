# Real-transformer validation of anchor-gated KV eviction under matched cache budgets

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `98`
Project ID: `real-transformer-validation-of-anchor-gated-kv-eviction-un-0d6b8b6de9`
Run ID: `real-transformer-validation-of-anchor-gated-kv-eviction-un-0d6b8b6de9-20260513T222726740745+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9e6a59ec3aba

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Small controlled real-transformer KV-cache test supports anchor retention under matched budgets, but the workload is handcrafted and short, so it is not full validation or paper-positive evidence.

## Recommended next action

Stop this Tier 1 run as mechanism-supported but not paper-grade; run a medium direct validation on a modern long-context model with natural retrieval examples, cache-budget sweeps, baseline controls, and memory/latency telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium natural long-context validation of anchor-gated KV eviction
- Success threshold: Anchor-gated eviction improves answer-region NLL by at least 20% relative to sliding-window at two or more matched cache budgets while keeping neutral-text NLL within 5% of the best matched-budget baseline and not increasing measured decode latency by more than 10%.
- Stop condition: Stop if the anchor policy fails to beat sliding-window by at least 10% answer-region NLL at two cache budgets or causes more than 10% neutral-text NLL regression versus the best matched-budget baseline.

## Evidence references

- Artifact root: `<local-path>/projects/real-transformer-validation-of-anchor-gated-kv-eviction-un-0d6b8b6de9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
