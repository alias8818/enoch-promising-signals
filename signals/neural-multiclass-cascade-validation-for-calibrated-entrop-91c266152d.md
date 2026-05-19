# Neural multiclass cascade validation for calibrated entropy routing

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `neural-multiclass-cascade-validation-for-calibrated-entrop-91c266152d`
Run ID: `neural-multiclass-cascade-validation-for-calibrated-entrop-91c266152d-20260514T101536760676+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Neural multiclass cascade validation for calibrated entropy routing: internal_generated:neural-multiclass-cascade-validation-for-calibrated-entrop-91c266152d

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct full-split validation with fixed seeds showed a mixed/negative result: calibrated entropy routing reduced proxy cost by 6.7% on FashionMNIST at a 0.24 percentage-point accuracy drop, but on CIFAR-10 it cost 3.96% more with a 4.10 percentage-point accuracy drop; a longer CIFAR-10 run still cost 9.32% more with a 2.48 percentage-point accuracy drop.

## Recommended next action

Stop this line as not paper-ready: the bounded validation found only FashionMNIST mechanism support, while CIFAR-10 failed the accuracy-preserving and cost-reducing thresholds even after stronger training.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/neural-multiclass-cascade-validation-for-calibrated-entrop-91c266152d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
