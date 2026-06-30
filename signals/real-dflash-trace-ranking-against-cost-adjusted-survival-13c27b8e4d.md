# Real DFlash Trace Ranking Against Cost-Adjusted Survival

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-dflash-trace-ranking-against-cost-adjusted-survival-13c27b8e4d`
Run ID: `real-dflash-trace-ranking-against-cost-adjusted-survival-13c27b8e4d-20260520T011147617690+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: enoch://control-plane/projects/spec-decoding-oracle-trace-ranker-20250519/runs/spec-decoding-oracle-trace-ranker-20250519-20260520T010147036783+0000
- Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: file://new-chatgpt-pro-ideas-05-19.md

## What looked useful

Cost-adjusted survival recovered only 70.3% of held-out oracle score and underperformed a static train-best k=4 baseline, which recovered 93.3%; bootstrap CI for advantage over static was entirely negative.

## Boundaries and scale limits

This was not actual DFlash: no diffusion draft checkpoint, verifier hidden-state trace, production prompt distribution, batching, or measured DFlash latency was used. The result covers a small CPU-only GPT-2/distilgpt2 held-out trace test.

## Claim scope

On a 48-prompt real GPT-2-family speculative trace stand-in, uncalibrated draft-confidence cost-adjusted survival did not rank branch lengths well enough to approach the realized cost-adjusted oracle.

## Why it stopped

Controlled small direct stand-in falsified the uncalibrated cost-adjusted survival threshold rather than validating DFlash-scale ranking.

## Recommended next action

Stop this branch as a no-paper useful negative; only revisit with actual DFlash traces plus calibrated survival estimates compared against static and prefix-replay controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Survival Ranking on Actual DFlash Trace Logs
- Success threshold: Calibrated survival ranker achieves held-out oracle ratio >= 0.95 and mean advantage over the best static/prefix control > 0 with 95% bootstrap CI excluding zero.
- Stop condition: Stop if actual DFlash traces are unavailable or calibrated survival fails to beat the strongest static/prefix control on the held-out split.

## Evidence references

- Artifact root: `<local-path>/projects/real-dflash-trace-ranking-against-cost-adjusted-survival-13c27b8e4d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
