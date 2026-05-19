# Medium real-agent provenance ledger integration benchmark

Status: `useful_signal`
Project ID: `medium-real-agent-provenance-ledger-integration-benchmark-c8aa9f7b11`
Run ID: `medium-real-agent-provenance-ledger-integration-benchmark-c8aa9f7b11-20260513T220118736198+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Medium real-agent provenance ledger integration benchmark: internal_generated:medium-real-agent-provenance-ledger-integration-benchmark-c8aa9f7b11

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 local LangGraph evidence supports the provenance mechanism, but it remains synthetic/local and is insufficient for publication-grade real-agent claims.

## Recommended next action

Stop this run as mechanism-supported but not paper-ready; next run should validate the ledger on real LLM/tool-agent traces with concurrency and developer-facing diagnosis metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM/tool-agent provenance ledger validation with concurrent traces
- Success threshold: Full ledger attribution or diagnosis success >= 0.90, tamper detection >= 0.99, replay/consistency >= 0.85, mean latency overhead <= 25%, storage growth <= 6x, and statistically clear improvement over baseline across both real workloads.
- Stop condition: Stop if real workloads show attribution or diagnosis success below 0.80, tamper detection below 0.95, mean overhead above 35%, or storage growth above 8x after straightforward implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-agent-provenance-ledger-integration-benchmark-c8aa9f7b11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
