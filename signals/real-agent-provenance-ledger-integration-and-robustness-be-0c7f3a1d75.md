# Real-agent provenance ledger integration and robustness benchmark

Status: `useful_signal`
Project ID: `real-agent-provenance-ledger-integration-and-robustness-be-0c7f3a1d75`
Run ID: `real-agent-provenance-ledger-integration-and-robustness-be-0c7f3a1d75-20260513T214616743376+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9dfb8883a5d0

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Controlled direct subprocess test supports tamper detection for the implemented ledger, but this is not production-agent integration, not a long-run robustness benchmark, and not publication-grade novelty evidence.

## Recommended next action

Stop this run as a no-paper Tier 1 mechanism-support result; run a bounded medium direct integration on real LangGraph/Codex-style traces before reconsidering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-agent provenance ledger integration benchmark
- Success threshold: 100% detection of tested non-key-compromise tampering attacks, zero false failures on clean replay, successful checkpoint recovery after restart, and p95 append overhead below 1 ms/event on at least 10000 real events.
- Stop condition: Stop if clean replay fails, any non-key-compromise tampering attack is missed, checkpoint recovery fails, or p95 append overhead exceeds 1 ms/event after straightforward implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-provenance-ledger-integration-and-robustness-be-0c7f3a1d75`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
