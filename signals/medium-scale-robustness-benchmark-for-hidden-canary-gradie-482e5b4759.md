# Medium-Scale Robustness Benchmark for Hidden Canary Gradient Audits

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-scale-robustness-benchmark-for-hidden-canary-gradie-482e5b4759`
Run ID: `medium-scale-robustness-benchmark-for-hidden-canary-gradie-482e5b4759-20260515T032422982886+0000`

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

- Internal Enoch project: Medium-Scale Robustness Benchmark for Hidden Canary Gradient Audits: internal_generated:medium-scale-robustness-benchmark-for-hidden-canary-gradie-482e5b4759

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium fixed-seed benchmark found learned canary behavior and high raw gradient AUC, but wrong-trigger/no-trigger controls and input/target-label baselines falsify the robust hidden-canary audit claim.

## Recommended next action

Stop this hidden-canary paper path; the Tier 2 result supports raw label-anomaly gradient detection but not a trigger-specific hidden canary audit beyond baselines.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Gradient Dot Audits for Label-Flip Anomaly Detection
- Success threshold: Gradient-dot audit improves AUROC by at least 0.10 over the best non-gradient baseline and reaches AUROC >= 0.85 on two datasets while maintaining <= 0.60 AUROC on clean-label hard-example controls.
- Stop condition: Stop if gradient-dot AUROC fails to exceed the best non-gradient baseline by 0.05 on either of two fixed-seed datasets or if target-label/input shortcuts explain the ranking.

## Evidence references

- Artifact root: `<local-path>/projects/medium-scale-robustness-benchmark-for-hidden-canary-gradie-482e5b4759`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
