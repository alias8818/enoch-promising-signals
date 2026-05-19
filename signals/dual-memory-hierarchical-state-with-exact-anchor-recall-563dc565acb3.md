# Dual-Memory Hierarchical State with Exact Anchor Recall

Status: `useful_signal`
Project ID: `dual-memory-hierarchical-state-with-exact-anchor-recall-563dc565acb3`
Run ID: `dual-memory-hierarchical-state-with-exact-anchor-recall-563dc565acb3-20260514T130252673967+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5e489342e2ab

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic exact-lookup evidence supports the anchor-recall mechanism but does not validate the full neural architecture claim or meet the publication-grade evidence gate.

## Recommended next action

Stop this run as proxy-only mixed evidence; do not write a paper unless a follow-up trainable, parameter-matched validation succeeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trainable Dual-Memory Anchor Recall Against Parameter-Matched Baselines
- Success threshold: Dual-memory model improves long-lag anchored recall by at least 20 absolute percentage points over the best parameter-matched baseline at comparable non-anchor loss, across at least three random seeds.
- Stop condition: Stop if the trainable dual-memory model fails to beat the best parameter-matched baseline by 10 absolute recall points in a smoke-scale run or requires unbounded anchor memory to match the oracle.

## Evidence references

- Artifact root: `<local-path>/projects/dual-memory-hierarchical-state-with-exact-anchor-recall-563dc565acb3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
