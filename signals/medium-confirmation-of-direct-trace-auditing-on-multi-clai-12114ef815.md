# Medium Confirmation of Direct Trace Auditing on Multi-Claim Reports

Status: `useful_signal`
Project ID: `medium-confirmation-of-direct-trace-auditing-on-multi-clai-12114ef815`
Run ID: `medium-confirmation-of-direct-trace-auditing-on-multi-clai-12114ef815-20260514T222446730450+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Medium Confirmation of Direct Trace Auditing on Multi-Claim Reports: internal_generated:medium-confirmation-of-direct-trace-auditing-on-multi-clai-12114ef815

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium confirmation met the synthetic threshold versus whole-report and shuffled-trace controls, but the no-trace structured ablation tied direct trace exactly and the evidence is not publication-grade real-report validation.

## Recommended next action

Stop this run as no-paper: the medium synthetic benchmark supports claim-level auditing but not trace-specific novelty; next run should use real multi-claim reports with trace-quality perturbations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-report validation of trace-specific gains in multi-claim auditing
- Success threshold: Direct trace auditing improves claim-level F1 by at least 0.08 over the strong no-trace baseline and at least 0.15 over whole-report auditing while maintaining precision >= 0.85 across fixed splits.
- Stop condition: Stop if direct traces do not beat the strong no-trace baseline by at least 0.03 F1 on the first fixed 100-report validation slice, or if reliable claim/source labels cannot be constructed.

## Evidence references

- Artifact root: `<local-path>/projects/medium-confirmation-of-direct-trace-auditing-on-multi-clai-12114ef815`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
