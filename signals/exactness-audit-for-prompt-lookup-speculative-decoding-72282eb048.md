# Exactness audit for prompt lookup speculative decoding

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `exactness-audit-for-prompt-lookup-speculative-decoding-72282eb048`
Run ID: `exactness-audit-for-prompt-lookup-speculative-decoding-72282eb048-20260515T101508780832+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Exactness audit for prompt lookup speculative decoding: internal_generated:exactness-audit-for-prompt-lookup-speculative-decoding-72282eb048

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Verified prompt lookup matched the autoregressive target distribution to numerical precision across exact finite sweeps with flawed controls that diverged strongly; this is mechanism support, not publication readiness.

## Recommended next action

Stop this depth-4 follow-up: the direct exact finite audit supports target-distribution preservation and found no paper-ready exactness violation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/exactness-audit-for-prompt-lookup-speculative-decoding-72282eb048`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
