# Trace-Replay Validation of Structured Ledger Rejection Sampling

Status: `useful_signal`
Project ID: `trace-replay-validation-of-structured-ledger-rejection-sam-d667538718`
Run ID: `trace-replay-validation-of-structured-ledger-rejection-sam-d667538718-20260515T181746820088+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6c0528d418f3

## What looked useful

Structured trace replay reproduced all clean rejection-sampling decisions and detected all injected semantic ledger invariant violations after trace hashes were recomputed, while an outcome-only baseline detected none.

## Boundaries and scale limits

Synthetic proposal generator, small fixed ledger schema, no real LLM/generated traces, no production accounting data, no independent codebase validator, and no long-horizon or large-schema stress test.

## Claim scope

Controlled Tier 1 synthetic double-entry ledger test: 20 seeds, 500 accepted transactions per seed, exact clean trace replay, and 500 internally hash-consistent semantic corruption injections.

## Why it stopped

No-paper closure: mechanism supported only in a controlled synthetic Tier 1 test, not in realistic model-generated or production ledger traces.

## Recommended next action

Run a bounded deepen validation using real model-generated ledger JSON and an independently implemented replay validator before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-Generated Ledger Trace-Replay Validation
- Success threshold: Clean replay agreement equals 1.0, structured semantic corruption detection is at least 0.95, and structured replay beats outcome-only and hash-only baselines by at least 0.5 absolute detection rate.
- Stop condition: Stop if clean replay agreement falls below 0.99, semantic corruption detection falls below 0.95, or realistic traces cannot be generated/parsed without substantial manual repair.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-validation-of-structured-ledger-rejection-sam-d667538718`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
