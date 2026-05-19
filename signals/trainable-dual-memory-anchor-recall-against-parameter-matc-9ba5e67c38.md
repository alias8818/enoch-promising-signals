# Trainable Dual-Memory Anchor Recall Against Parameter-Matched Baselines

Status: `compute_scale_blocked`
Project ID: `trainable-dual-memory-anchor-recall-against-parameter-matc-9ba5e67c38`
Run ID: `trainable-dual-memory-anchor-recall-against-parameter-matc-9ba5e67c38-20260514T131026504620+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5e489342e2ab

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Mechanism support is limited to a controlled synthetic Tier-1 test; evidence is not publication-grade because no language-model-scale, naturalistic, or layout-ablation validation was run.

## Recommended next action

Stop this worker run as no-paper: the Tier-1 synthetic direct test supports the mechanism but is not full validation; next run should test a GPT-2-small-class or similarly dense sequence baseline with ablations of the fixed anchor-layout prior.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-Small-Class Dual-Memory Anchor Recall With Layout Ablations
- Success threshold: Dual-memory reaches at least 85% OOD recall accuracy and exceeds the best dense baseline by at least 20 absolute percentage points across 3 seeds while preserving the advantage in the layout-ablation condition.
- Stop condition: Stop if the dense baseline closes the OOD gap below 10 percentage points, if the dual-memory model fails below 70% OOD accuracy, or if the advantage only exists with fixed even/odd anchor layout.

## Evidence references

- Artifact root: `<local-path>/projects/trainable-dual-memory-anchor-recall-against-parameter-matc-9ba5e67c38`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
