# Real-Transformer Anchor-Preserved KV Cache Evaluation

Status: `compute_scale_blocked`
Project ID: `real-transformer-anchor-preserved-kv-cache-evaluation-fff3f43dd3`
Run ID: `real-transformer-anchor-preserved-kv-cache-evaluation-fff3f43dd3-20260515T154222711630+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1997a6324910

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Controlled direct KV-cache pruning on distilgpt2 and gpt2 showed anchor retention reduced KL to full cache versus sliding by 34-99%, but random retention beat anchor in several model/budget cases; this is not a full validation.

## Recommended next action

Stop this run as a mixed Tier 1 direct result: anchor preservation beats sliding-window eviction on real Transformer KV caches, but not random retention consistently, so it is mechanism support rather than paper-ready validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-Corpus Anchor KV Retention Against Non-Recency Controls
- Success threshold: Anchor or adaptive-anchor retention must reduce mean KL-to-full-cache by at least 20% versus sliding and by at least 10% versus the best random/stratified nonlocal control in at least two models and two cache budgets, with no worse than 1% absolute degradation in task/recall accuracy.
- Stop condition: Stop as negative if anchor retention fails to beat the best random/stratified nonlocal control in more than one model/budget pair or if full-cache cached-forward equivalence exceeds 1e-3 max absolute logit drift.

## Evidence references

- Artifact root: `<local-path>/projects/real-transformer-anchor-preserved-kv-cache-evaluation-fff3f43dd3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
