# Exact-Anchor State Checkpoints for Long-Episode Agents

Status: `compute_scale_blocked`
Project ID: `exact-anchor-state-checkpoints-for-long-episode-agents-f63e4455279a`
Run ID: `exact-anchor-state-checkpoints-for-long-episode-agents-f63e4455279a-20260515T145202172209+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8f955958c14a

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic proxy supports exact-anchor recovery under oracle audits, but it is not direct evidence on real long-episode agents and is therefore not paper-positive.

## Recommended next action

Stop this run as a proxy-only positive mechanism result, not a full validation; run a bounded real-agent follow-up before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-Anchor Checkpointing in a Real Long-Episode Agent Runtime
- Success threshold: Exact anchors improve task success by at least 15 percentage points over the best baseline while increasing total wall-clock or token/tool cost by no more than 50% on the same task set.
- Stop condition: Stop if exact restore cannot be implemented for the real runtime, if replay nondeterminism prevents valid restoration in more than 10% of audited faults, or if exact anchors fail to beat the best baseline by 15 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-state-checkpoints-for-long-episode-agents-f63e4455279a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
