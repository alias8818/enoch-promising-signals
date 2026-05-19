# Medium Multi-Model Contradiction Recovery Confirmation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-multi-model-contradiction-recovery-confirmation-43a57b2c44`
Run ID: `medium-multi-model-contradiction-recovery-confirmation-43a57b2c44-20260513T212543261072+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
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

- Internal Enoch project: Medium Multi-Model Contradiction Recovery Confirmation: internal_generated:medium-multi-model-contradiction-recovery-confirmation-43a57b2c44

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 direct synthetic evidence supports explicit contradiction recovery but fails the predeclared per-model multi-turn threshold for two of five models and remains vulnerable to a last-mention shortcut baseline.

## Recommended next action

Stop this run as no-paper mixed evidence; next run should test live tool-trace contradiction recovery where last-mention heuristics are insufficient.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Tool-Trace Contradiction Recovery Without Last-Mention Shortcut
- Success threshold: All tested models or an explicitly scoped model class must achieve >=90% live contradiction recovery and >=90% clean/stale controls while first-mention and last-mention baselines remain below 70% on contradiction tasks.
- Stop condition: Stop as negative if recovery drops below 90% for more than one model family or if heuristic baselines solve the benchmark, indicating the test still does not isolate contradiction recovery.

## Evidence references

- Artifact root: `<local-path>/projects/medium-multi-model-contradiction-recovery-confirmation-43a57b2c44`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
