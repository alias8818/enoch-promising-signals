# Redundant Small-Agent Jury with Evidence Ledgers

Status: `useful_signal`
Project ID: `redundant-small-agent-jury-with-evidence-ledgers-b9ea9ef9d440`
Run ID: `redundant-small-agent-jury-with-evidence-ledgers-b9ea9ef9d440-20260514T191405670380+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/13c56c7c9b90

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic proxy supports the ledger-aggregation mechanism but does not provide direct publication-grade evidence with real agents, real retrieval, or real evidence ledgers.

## Recommended next action

Stop this run as proxy-only; run a bounded real-LLM evidence-grounded benchmark before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-Model Evidence-Ledger Jury Benchmark
- Success threshold: Audited ledger jury beats answer-only majority by at least 5 absolute accuracy points and does not increase hallucinated evidence rate, with total cost no more than 2x the majority baseline.
- Stop condition: Stop if audited ledgers fail to beat majority by 3 absolute points on a 200-example pilot or if evidence hallucination increases by more than 2 absolute points.

## Evidence references

- Artifact root: `<local-path>/projects/redundant-small-agent-jury-with-evidence-ledgers-b9ea9ef9d440`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
