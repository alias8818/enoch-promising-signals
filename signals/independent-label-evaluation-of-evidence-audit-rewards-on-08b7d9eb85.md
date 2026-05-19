# Independent-label evaluation of evidence-audit rewards on model-generated tool-agent summaries

Status: `useful_signal`
Project ID: `independent-label-evaluation-of-evidence-audit-rewards-on-08b7d9eb85`
Run ID: `independent-label-evaluation-of-evidence-audit-rewards-on-08b7d9eb85-20260513T203906668174+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Independent-label evaluation of evidence-audit rewards on model-generated tool-agent summaries: internal_generated:independent-label-evaluation-of-evidence-audit-rewards-on-08b7d9eb85

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier-3 bounded validation on 240 model-generated tool-agent summary cases failed the strict independent acceptability threshold; the result is not paper-positive and remains synthetic rather than human-labeled production evidence.

## Recommended next action

Stop this run as no-paper: the bounded direct synthetic model-generation evaluation found only 3.75% strict acceptable summaries for evidence-audit selection despite partial-score gains.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-label replication of evidence-audit reward selection on real tool-agent traces
- Success threshold: At least +15 percentage points acceptable-rate improvement over the best baseline, at least 30% absolute acceptable rate, and no worse unsupported-claim rate.
- Stop condition: Stop as negative if acceptable-rate improvement is under 10 percentage points, absolute acceptable rate remains below 20%, or unsupported-claim rate worsens by more than 3 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/independent-label-evaluation-of-evidence-audit-rewards-on-08b7d9eb85`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
