# Medium validation of deployable PPL/uncertainty gates for no-KV-reuse LM cascades

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `medium-validation-of-deployable-ppl-uncertainty-gates-for-05dff99f7d`
Run ID: `medium-validation-of-deployable-ppl-uncertainty-gates-for-05dff99f7d-20260515T072806793447+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
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

- Internal Enoch project: Medium validation of deployable PPL/uncertainty gates for no-KV-reuse LM cascades: internal_generated:medium-validation-of-deployable-ppl-uncertainty-gates-for-05dff99f7d

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier-2 direct validation found real PPL gate signal but only break-even deployable savings: calibrated PPL averaged +0.52% estimated no-KV savings across three seeds, with one negative seed and one seed beyond the 1 pp accuracy-loss target.

## Recommended next action

Do not write a paper from this run; only continue with a bounded direct-evidence follow-up that tests larger model scale gaps and requires calibrated >=15% no-KV-reuse savings at <=1 pp quality loss across datasets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded scale-gap validation of calibrated PPL gates for no-KV LM cascades
- Success threshold: Across datasets and seeds, calibrated PPL or uncertainty gates achieve >=15% measured/estimated no-KV-reuse cost savings while staying within <=1 pp accuracy loss and <=0.03 NLL increase versus always-large, and beat random/length matched controls.
- Stop condition: Stop negative if any tested model pair with small/large latency ratio <=0.20 still fails to achieve >=10% calibrated savings at <=1 pp accuracy loss, or if savings remain only in oracle held-out sweeps.

## Evidence references

- Artifact root: `<local-path>/projects/medium-validation-of-deployable-ppl-uncertainty-gates-for-05dff99f7d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
