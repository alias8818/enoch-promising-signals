# Trace-Based Ledger-Constrained Decoding for 1B Tool Agents

Status: `compute_scale_blocked`
Project ID: `trace-based-ledger-constrained-decoding-for-1b-tool-agents-8d68ea8865`
Run ID: `trace-based-ledger-constrained-decoding-for-1b-tool-agents-8d68ea8865-20260514T201826598758+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/75713d80857c

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 controlled direct test supports the mechanism, but evidence is still finite-candidate and small-scale rather than publication-grade full tool-agent validation.

## Recommended next action

Stop this run as mechanism-supported but not paper-ready; next run should integrate token-level ledger-constrained generation and compare unconstrained, syntax-only, and state-only baselines on at least 100 ledger tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-Level Ledger-Constrained Decoding on 1B Tool Agents
- Success threshold: Ledger-constrained decoding achieves at least 90% valid trace rate and at least 25 percentage point absolute success improvement over the best non-ledger baseline without more than 2x median decoding latency.
- Stop condition: Stop if ledger-constrained decoding fails to beat the best non-ledger baseline by at least 10 percentage points on success after 100 tasks, or if median decoding latency exceeds 3x the best baseline.

## Evidence references

- Artifact root: `<local-path>/projects/trace-based-ledger-constrained-decoding-for-1b-tool-agents-8d68ea8865`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
