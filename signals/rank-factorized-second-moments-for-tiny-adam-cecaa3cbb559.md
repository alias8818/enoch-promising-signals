# Rank-factorized second moments for tiny Adam

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `rank-factorized-second-moments-for-tiny-adam-cecaa3cbb559`
Run ID: `rank-factorized-second-moments-for-tiny-adam-cecaa3cbb559-20260608T093125187758+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b2be2b147e7d

## What looked useful

Rank-4 used 22,400 second-moment elements versus AdamW's 242,304 (90.76% reduction), but in the 1000-step best-observed comparison tuned AdamW reached mean validation loss 2.8918 while tuned rank-4 ended at 4.2229 and 77.2% of AdamW throughput. The method plateaued and degraded after a promising 200-step proxy result.

## Boundaries and scale limits

Synthetic data only; tiny 2-layer transformer only; no real corpus, GPT-2-small-class model, fused implementation, distributed scale, or long training run. Only one factor-update rule was implemented; rank-4/8/16 default-LR and rank-4 LR probes were tested.

## Claim scope

Pure low-rank NMF-style factorized second-moment AdamW was tested on a synthetic tiny-transformer next-token task. It reduces stored second-moment elements but does not preserve AdamW-like optimization over a 1000-step persistence check.

## Why it stopped

Proxy plus direct tiny-transformer evidence is an early falsification rather than full validation: the tested variant saves memory but fails to preserve tuned AdamW optimization over 1000 steps.

## Recommended next action

Stop this pure rank-factorized second-moment variant as a paper path; if continuing locally, test a diagonal-plus-low-rank second-moment estimator with an explicit persistence threshold before any larger run.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Diagonal-plus-low-rank second moments for tiny Adam
- Success threshold: Across 3 seeds, mean final validation loss within 0.1 of tuned AdamW after 1000 steps, no degradation from step 500 to 1000, at least 50% second-moment state reduction, and at least 70% of AdamW throughput.
- Stop condition: Stop if the diagonal-plus-low-rank variant remains more than 0.1 validation loss worse than tuned AdamW or shows late degradation on the 1000-step synthetic persistence check.

## Evidence references

- Artifact root: `<local-path>/projects/rank-factorized-second-moments-for-tiny-adam-cecaa3cbb559`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
