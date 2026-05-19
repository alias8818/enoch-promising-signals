# Entropy-Gated Local Cascade Router

Status: `compute_scale_blocked`
Project ID: `entropy-gated-local-cascade-router-d0a9f5ce3010`
Run ID: `entropy-gated-local-cascade-router-d0a9f5ce3010-20260514T152257265253+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/406d9f2e6535

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy/local benchmark only; the tested cascade met the predeclared proxy success threshold in 15% of trials, achieved 0 of 3 dataset-level successes, and underperformed random fallback on average at fixed 10%, 25%, and 50% expert budgets.

## Recommended next action

Stop this run as a proxy early falsification: entropy predicted cheap-model errors, but the local cascade failed robust same-budget random controls and is not paper-ready without direct LLM evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small/Large LM Entropy Cascade Evaluation
- Success threshold: Entropy routing matches large-model quality within 1 percentage point or task-equivalent margin, uses <=50% large-model calls, and beats random and confidence controls at the same expert budget on every task.
- Stop condition: Stop if entropy routing fails to beat same-budget random fallback on any task, or if the large model is not consistently stronger than the small model.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gated-local-cascade-router-d0a9f5ce3010`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
