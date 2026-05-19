# Production-trace provenance ledger validation against mature tracing baselines

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `production-trace-provenance-ledger-validation-against-matu-84b6cf9286`
Run ID: `production-trace-provenance-ledger-validation-against-matu-84b6cf9286-20260514T000106768031+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Production-trace provenance ledger validation against mature tracing baselines: internal_generated:production-trace-provenance-ledger-validation-against-matu-84b6cf9286

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic replication showed 105/105 tamper detections and 0/15 false positives for the full ledger, but this is not full production-trace validation and cannot support a paper now.

## Recommended next action

Stop at depth 4: the bounded synthetic benchmark supports the ledger mechanism but fails the Tier 4 paper-readiness gate without real production traces and deployed mature tracing baselines.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/production-trace-provenance-ledger-validation-against-matu-84b6cf9286`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
