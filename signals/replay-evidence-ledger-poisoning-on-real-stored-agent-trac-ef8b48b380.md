# Replay evidence-ledger poisoning on real stored agent traces

Status: `useful_signal`
Project ID: `replay-evidence-ledger-poisoning-on-real-stored-agent-trac-ef8b48b380`
Run ID: `replay-evidence-ledger-poisoning-on-real-stored-agent-trac-ef8b48b380-20260513T201306786346+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Replay evidence-ledger poisoning on real stored agent traces: internal_generated:replay-evidence-ledger-poisoning-on-real-stored-agent-trac-ef8b48b380

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 3 bounded direct-trace validation passed, but the evidence ledgers and clean replay labels were reconstructed from stored trace events rather than captured as native production evidence-ledger records.

## Recommended next action

Stop this run as no-paper: the mechanism is supported on reconstructed ledgers from 496 real stored traces, but publication-grade closure requires native evidence-ledger traces and a production-equivalent replay agent.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Native evidence-ledger poisoning with live replay agent
- Success threshold: Across at least 300 native ledger traces, clean replay accuracy >= 0.90; untrusted well-formed ASR >= 0.50 for the unprotected baseline; provenance-plus-corroboration defended ASR <= 0.05 with defended accuracy >= 0.90.
- Stop condition: Stop if native traces cannot be obtained, if clean replay accuracy is below 0.90 before attack, or if untrusted well-formed ASR is below 0.20 for the unprotected baseline.

## Evidence references

- Artifact root: `<local-path>/projects/replay-evidence-ledger-poisoning-on-real-stored-agent-trac-ef8b48b380`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
