# True 4 GB-capped fused DPLR Adam validation

Status: `useful_signal`
Project ID: `true-4-gb-capped-fused-dplr-adam-validation-3f2b80a8d7`
Run ID: `true-4-gb-capped-fused-dplr-adam-validation-3f2b80a8d7-20260514T012356749601+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: True 4 GB-capped fused DPLR Adam validation: internal_generated:true-4-gb-capped-fused-dplr-adam-validation-3f2b80a8d7

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium fixed-seed validation with AdamW baseline and rank-0 ablation found that DPLR rank-8 is not the best capped optimizer; this is not a full production fused-kernel validation, but it is sufficient Tier 2 evidence against the stated DPLR contribution.

## Recommended next action

Stop this DPLR-Adam validation as no-paper: Tier 2 evidence supports the 4 GiB state cap but the rank-8 DPLR mechanism loses to the simpler rank-0/factored control on test loss, test accuracy, throughput, and state size.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: 4 GB-capped rank-0 factored optimizer validation
- Success threshold: Under a true 4 GiB optimizer-state cap, rank-0/factored optimizer matches or improves validation loss versus DPLR rank-8 and stays within 5% of AdamW quality while delivering at least 2x DPLR throughput on the same hardware and seed budget.
- Stop condition: Stop if rank-0/factored fails to beat DPLR rank-8 on either validation loss or throughput in the fixed-seed GPT-2-small-class run, or if a full-step large-parameter run cannot stay under the 4 GiB optimizer-state cap.

## Evidence references

- Artifact root: `<local-path>/projects/true-4-gb-capped-fused-dplr-adam-validation-3f2b80a8d7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
