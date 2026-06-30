# Gradient-Free Data Selection via Loss Trajectory Clustering

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-free-data-selection-via-loss-trajectory-clustering-bef3cc4e77a4`
Run ID: `gradient-free-data-selection-via-loss-trajectory-clustering-bef3cc4e77a4-20260608T222413953391+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7b7a88ab66bb

## What looked useful

Loss trajectories were diagnostic: LTC selected cleaner data than random (0.9167 vs 0.8468 clean fraction) and more hard/rare clean examples, but its mean test accuracy was lower than random (0.8395 vs 0.8728) and lower than low-final-loss selection (0.9075). The simple low-final-loss baseline won 7/8 seeds versus random and 8/8 seeds versus LTC.

## Boundaries and scale limits

Evidence is limited to an MLP on synthetic tabular classification with 8000 training examples per seed, 3000 clean test examples per seed, 8 seeds, 35% subset selection budget, 8 probe epochs, and 32 final training epochs. It does not validate or invalidate LLM-scale, natural-language, or cross-model data curation.

## Claim scope

In a bounded synthetic noisy-label multiclass classification test, loss-trajectory clustering produced interpretable data-regime clusters but the tested cluster-based fixed-budget selector did not improve final clean test accuracy over random selection or a simpler low-final-probe-loss selector.

## Why it stopped

Corrected fixed-budget proxy experiment showed the concrete loss-trajectory clustering selector underperformed random by 0.0332 mean accuracy and low-final-loss by 0.0680, so the tested selection hypothesis is not supported despite useful diagnostic clustering.

## Recommended next action

Stop this project as no-paper evidence; the next bounded test should only proceed as a follow-up that uses clusters for diversity constraints on top of low-final-loss ranking, with low-final-loss as the primary baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cluster-stratified low-loss data selection
- Success threshold: Mean overall accuracy must be at least within 0.005 of low-final-loss selection while improving hard-clean or rare-clean subgroup accuracy by at least 0.015, measured over the same 8 seeds or more.
- Stop condition: Stop if cluster-stratified low-loss trails low-final-loss by more than 0.01 mean overall accuracy or fails to improve either hard-clean or rare-clean subgroup accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-free-data-selection-via-loss-trajectory-clustering-bef3cc4e77a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
