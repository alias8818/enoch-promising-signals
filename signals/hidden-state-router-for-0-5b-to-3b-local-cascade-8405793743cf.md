# Hidden-state router for 0.5B-to-3B local cascade

Status: `compute_scale_blocked`
Project ID: `hidden-state-router-for-0-5b-to-3b-local-cascade-8405793743cf`
Run ID: `hidden-state-router-for-0-5b-to-3b-local-cascade-8405793743cf-20260514T232338382090+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a85c4f8125fc

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy early falsification rather than full validation: on three 400-example MMLU subset runs, the hidden-state router was unstable and usually failed to beat entropy, margin, or max-probability baselines at matched escalation budgets.

## Recommended next action

Stop this run as a proxy early falsification of the simple final-token linear hidden-state router; run a bounded larger direct follow-up only if testing richer routers and stronger baselines is desired.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Larger cost-aware hidden-state cascade router with stronger baselines
- Success threshold: Hidden-state router improves held-out cost-adjusted accuracy by at least 2 absolute percentage points over the best tuned confidence baseline at 20% and 30% escalation, with the effect positive on every domain and stable across seeds.
- Stop condition: Stop if hidden-state router AUC remains below 0.60 or matched-budget accuracy fails to beat the best confidence baseline on two independent domains.

## Evidence references

- Artifact root: `<local-path>/projects/hidden-state-router-for-0-5b-to-3b-local-cascade-8405793743cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
