# Multi-model live-agent validation of evidence-ledger rollback tools

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `multi-model-live-agent-validation-of-evidence-ledger-rollb-2bafcbdb12`
Run ID: `multi-model-live-agent-validation-of-evidence-ledger-rollb-2bafcbdb12-20260514T082606745955+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Multi-model live-agent validation of evidence-ledger rollback tools: internal_generated:multi-model-live-agent-validation-of-evidence-ledger-rollb-2bafcbdb12

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct multi-model validation on 1440 local-model generations was mixed: rollback_visible improved accuracy by only 1.46 pp over append_only while reducing bad-value leakage from 19.38% to 5.00%, so mechanism support is insufficient for publication readiness.

## Recommended next action

Stop this run as no-paper: the bounded live-agent validation showed strong stale-evidence leakage reduction but failed the preregistered 20 percentage-point final-answer accuracy threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tool-call rollback ledger validation on stronger live agents
- Success threshold: rollback_visible must improve final-answer accuracy by at least 20 percentage points over both append_only and annotated_append while reducing stale-value leakage and keeping unparseable outputs at or below 5%.
- Stop condition: Stop if stronger agents still show less than 10 percentage-point accuracy gain, if leakage reduction disappears, or if parse/tool-call compliance remains too poor to score reliably.

## Evidence references

- Artifact root: `<local-path>/projects/multi-model-live-agent-validation-of-evidence-ledger-rollb-2bafcbdb12`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
