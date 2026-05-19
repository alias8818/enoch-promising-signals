# Structured Ledger Rejection Sampling for Local Agents

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `structured-ledger-rejection-sampling-for-local-agents-75263160c1cb`
Run ID: `structured-ledger-rejection-sampling-for-local-agents-75263160c1cb-20260515T180921869281+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6c0528d418f3

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic proxy supports the mechanism but does not provide direct/full validation for local LLM agents or publication-grade evidence.

## Recommended next action

Stop this run as proxy-only no-paper evidence; next run should replay ledger rejection sampling on real local-agent traces with retry/reflection baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replay Validation of Structured Ledger Rejection Sampling
- Success threshold: At least 40% fewer invalid tool executions than retry/reflection controls, success within 2 percentage points of the best baseline, and total latency/proposal cost no more than 2.5x on a fixed trace or benchmark suite.
- Stop condition: Stop if ledger extraction errors exceed 10%, invalid-action reduction is below 20%, or success falls more than 5 percentage points below the best retry/reflection baseline.

## Evidence references

- Artifact root: `<local-path>/projects/structured-ledger-rejection-sampling-for-local-agents-75263160c1cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
