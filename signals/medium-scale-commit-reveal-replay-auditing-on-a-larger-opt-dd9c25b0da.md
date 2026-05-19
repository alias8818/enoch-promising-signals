# Medium-scale commit-reveal replay auditing on a larger optimizer trace

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `100`
Project ID: `medium-scale-commit-reveal-replay-auditing-on-a-larger-opt-dd9c25b0da`
Run ID: `medium-scale-commit-reveal-replay-auditing-on-a-larger-opt-dd9c25b0da-20260515T003526773194+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `100`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Medium-scale commit-reveal replay auditing on a larger optimizer trace: internal_generated:medium-scale-commit-reveal-replay-auditing-on-a-larger-opt-dd9c25b0da

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Thirty thousand total real optimizer steps across three seeds support exact commit-reveal replay and expected tamper-detection behavior, but the evidence is still medium-scale and lacks large-model/distributed protocol validation.

## Recommended next action

Stop this worker run as supportive Tier 2 medium confirmation, not paper-ready; next run should perform a bounded full-scale validation on a realistic large-model or distributed optimizer trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded full-scale commit-reveal replay auditing on a realistic large-model optimizer trace
- Success threshold: Honest replay must stay exact or within a predeclared numerical tolerance for all audited transitions; commit-reveal detection rates must remain within binomial 95% intervals around the hypergeometric expectation for all schedules; post-hoc/adaptive controls must show materially weaker guarantees for sparse corruption; verifier overhead must be reported and plausibly bounded for the target deployment.
- Stop condition: Stop if replay is nondeterministic beyond the predeclared tolerance, detection leaves the expected sampling intervals, canonical trace encoding is not stable across the target environment, or storage/replay overhead is impractical.

## Evidence references

- Artifact root: `<local-path>/projects/medium-scale-commit-reveal-replay-auditing-on-a-larger-opt-dd9c25b0da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
