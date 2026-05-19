# Real agent trace replay evidence-ledger poisoning validation

Status: `compute_scale_blocked`
Project ID: `real-agent-trace-replay-evidence-ledger-poisoning-validati-cd96859f9d`
Run ID: `real-agent-trace-replay-evidence-ledger-poisoning-validati-cd96859f9d-20260513T200743230195+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Real agent trace replay evidence-ledger poisoning validation: internal_generated:real-agent-trace-replay-evidence-ledger-poisoning-validati-cd96859f9d

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Controlled trace replay passed the Tier 2 mechanism threshold, but this is not full validation because the traces, tasks, and answerer are local deterministic fixtures rather than real agent logs or a live production-equivalent agent.

## Recommended next action

Stop this run as no-paper: the Tier 2 controlled replay supports the mechanism, but publication-grade validation needs real stored agent traces replayed through the same attack/control matrix.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay evidence-ledger poisoning on real stored agent traces
- Success threshold: Across at least 500 real replayed traces, naive/schema/hash-only ASR >= 0.30 under well-formed poison, defended ASR <= 0.05, defended clean accuracy >= 0.95 of the no-attack baseline, and poison-citation rate explains at least 80% of successful attacks.
- Stop condition: Stop if real traces cannot be obtained without private/human access, or if naive replay ASR is below 0.10 with confidence intervals excluding the 0.30 threshold.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-trace-replay-evidence-ledger-poisoning-validati-cd96859f9d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
