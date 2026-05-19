# Real-agent evaluation of evidence-ledger rollback benchmark

Status: `useful_signal`
Project ID: `real-agent-evaluation-of-evidence-ledger-rollback-benchmar-138960146a`
Run ID: `real-agent-evaluation-of-evidence-ledger-rollback-benchmar-138960146a-20260514T081027742941+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Real-agent evaluation of evidence-ledger rollback benchmark: internal_generated:real-agent-evaluation-of-evidence-ledger-rollback-benchmar-138960146a

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

The fixed-seed real local LLM evaluation met the rollback benchmark thresholds, but the evidence is generated, single-model, ID-based, and uses a strong rollback-tool state intervention, so it is not publication-grade.

## Recommended next action

Stop this run as Tier 2 mechanism-supported but not paper-ready; run a bounded next-tier multi-model live-agent validation before any publication claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-model live-agent validation of evidence-ledger rollback tools
- Success threshold: Rollback-ledger tool state improves exact ledger accuracy by at least 0.30 absolute and reduces rolled-back false-positive retention by at least 50% versus the strongest non-rollback baseline on depth > 0 cases, while preserving at least 0.90 exact accuracy on depth-0 controls across at least two model families.
- Stop condition: Stop if the effect does not reproduce across two model families, if free-form scoring collapses below 0.80 exact accuracy for the rollback tool condition, or if manual audit finds more than 10% ambiguous ground truth.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evaluation-of-evidence-ledger-rollback-benchmar-138960146a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
