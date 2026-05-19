# Multi-model true-document anchor KV retention validation

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `multi-model-true-document-anchor-kv-retention-validation-5578b6c16f`
Run ID: `multi-model-true-document-anchor-kv-retention-validation-5578b6c16f-20260515T162823084239+0000`

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

- Internal Enoch project: Multi-model true-document anchor KV retention validation: internal_generated:multi-model-true-document-anchor-kv-retention-validation-5578b6c16f

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded direct multi-model validation on 96 true Wikitext documents supports anchors versus recency/non-anchor controls but fails the real-baseline novelty threshold.

## Recommended next action

Stop this lineage: the mechanism is real, but true-document anchor retention is not paper-ready because it ties same-size streaming retention exactly and does not robustly beat H2O across models.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/multi-model-true-document-anchor-kv-retention-validation-5578b6c16f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
