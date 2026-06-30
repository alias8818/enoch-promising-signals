# Surface-feature quality filter for tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `surface-feature-quality-filter-for-tiny-cpu-pretraining-1323043e9db2`
Run ID: `surface-feature-quality-filter-for-tiny-cpu-pretraining-1323043e9db2-20260613T105840322724+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/258851e1b744

## What looked useful

quality_top_70pct selected 99.15% clean records from a 69.70% clean synthetic mix and improved clean validation NLL by 2.208% versus unfiltered, while random 70% subsampling improved only 0.243%. The same filter worsened noise validation NLL from 3.5338 to 5.6495, showing distribution narrowing.

## Boundaries and scale limits

Synthetic data only; tiny character context model only; no real web corpus, tokenizer-based transformer, downstream evaluation, multilingual/code/table retention test, or full-scale pretraining.

## Claim scope

On a synthetic clean/noisy text mixture, a cheap surface-feature quality filter improved clean-domain validation NLL for a tiny NumPy character LM under fixed CPU training steps, outperforming matched random subsampling and a length-only control.

## Why it stopped

Proxy-only synthetic evidence supports a mechanism but is not direct/full validation for real tiny CPU pretraining.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same filter against random and length controls on a real small corpus with a tokenizer-based tiny transformer and equal-token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny transformer test for surface quality filtering
- Success threshold: Surface-quality filtering improves clean held-out NLL by at least 1% versus unfiltered and by at least 0.5% versus random and length-only controls, while non-prose/noise-domain NLL degradation remains below 10%.
- Stop condition: Stop as negative if the surface filter does not beat both random and length controls on clean held-out NLL, or if it improves clean NLL only by discarding valuable non-prose domains with more than 10% NLL degradation.

## Evidence references

- Artifact root: `<local-path>/projects/surface-feature-quality-filter-for-tiny-cpu-pretraining-1323043e9db2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
