# Medium Non-IID Adaptive Validation of Commit-Reveal Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-non-iid-adaptive-validation-of-commit-reveal-volunt-7a8e1754ac`
Run ID: `medium-non-iid-adaptive-validation-of-commit-reveal-volunt-7a8e1754ac-20260515T014806814095+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Medium Non-IID Adaptive Validation of Commit-Reveal Volunteer Training: internal_generated:medium-non-iid-adaptive-validation-of-commit-reveal-volunt-7a8e1754ac

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 synthetic non-IID validation showed strong mechanism support, but the evidence is not a full real-workload validation and does not justify paper writing.

## Recommended next action

Stop this run at Tier 2: synthetic medium evidence supports the mechanism but is not publication-grade; run a bounded real-FL deepening study next if the controller continues the line.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-FL Validation of Commit-Reveal Volunteer Training
- Success threshold: Across at least 5 fixed seeds, commit-reveal reduces backdoor attack success by >=50 percentage points versus revealed validation and no-validation FedAvg, keeps clean accuracy within 1 percentage point of clean control, and outperforms or matches the robust aggregation baseline on ASR without worse worst-client accuracy.
- Stop condition: Stop if commit-reveal fails to reduce ASR by at least 25 percentage points in the first real-dataset smoke run, or if it loses more than 2 percentage points clean accuracy versus clean control after tuning validation tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/medium-non-iid-adaptive-validation-of-commit-reveal-volunt-7a8e1754ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
