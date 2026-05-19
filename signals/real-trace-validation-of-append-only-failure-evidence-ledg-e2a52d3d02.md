# Real-trace validation of append-only failure evidence ledger

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `real-trace-validation-of-append-only-failure-evidence-ledg-e2a52d3d02`
Run ID: `real-trace-validation-of-append-only-failure-evidence-ledg-e2a52d3d02-20260514T074516857314+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Real-trace validation of append-only failure evidence ledger: internal_generated:real-trace-validation-of-append-only-failure-evidence-ledg-e2a52d3d02

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 3 real-trace validation produced mixed evidence rather than publication-grade support: reconstructed append-only ledgers recovered 100% of 1180 failure events across 546 usable traces, but the best baseline recovered 89.15%, so the predeclared event-recall gap failed.

## Recommended next action

Stop this branch as not paper-ready: the real-trace ledger had perfect parser-label recall, but it failed the predeclared 20-point improvement threshold versus the tail-window baseline and still needs native checkpointed append-only storage for a stronger claim.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-validation-of-append-only-failure-evidence-ledg-e2a52d3d02`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
