# Real LLM/tool-agent provenance ledger validation with concurrent traces

Status: `useful_signal`
Project ID: `real-llm-tool-agent-provenance-ledger-validation-with-conc-e05539bbf7`
Run ID: `real-llm-tool-agent-provenance-ledger-validation-with-conc-e05539bbf7-20260513T235036215072+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Real LLM/tool-agent provenance ledger validation with concurrent traces: internal_generated:real-llm-tool-agent-provenance-ledger-validation-with-conc-e05539bbf7

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 3 bounded validation supported the controlled mechanism over 12,000 real local LLM/tool events, but evidence remains insufficient for publication because it used a tiny model, a local harness, and weak baselines rather than production agent traces and mature provenance-system comparisons.

## Recommended next action

Stop this run as no-paper despite positive mechanism evidence; only a depth-4 production-trace follow-up should proceed, with mature provenance baselines and crash/fault injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-trace provenance ledger validation against mature tracing baselines
- Success threshold: Clean replay after recovery on at least 100,000 production-like events; 100% detection of non-key-compromise injected corruptions; at least one mature baseline misses a documented subset of consequential corruptions; p99 append overhead remains below 1 ms/event.
- Stop condition: Stop negative if production-like integration cannot be run, if p99 append overhead exceeds 1 ms/event, if clean recovery replay fails, or if mature baselines detect the same consequential corruptions with comparable overhead and lower complexity.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-tool-agent-provenance-ledger-validation-with-conc-e05539bbf7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
