# Influence-Score Data Selection Beats Random Sampling at 50M Params

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `influence-score-data-selection-beats-random-sampling-at-50m-params-807c8688817e`
Run ID: `influence-score-data-selection-beats-random-sampling-at-50m-params-807c8688817e-20260619T190615935883+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fbfae992bbdc

## What looked useful

Influence scoring selected more helpful examples on average than random sampling (0.433 vs 0.369 helpful fraction) but won final validation loss on only 1 of 3 calibrated seeds. Mean delta slightly favored influence because one win was larger, while the median seed favored random.

## Boundaries and scale limits

Synthetic data only; 49,764,096-parameter target model; 900-example pools; 180 selected examples; 90 target training steps; three calibrated seeds; no real-corpus pretraining, Hessian-inverse influence estimate, long-horizon convergence, or broad data-quality benchmark.

## Claim scope

In a controlled synthetic 50M-class causal transformer test, first-order validation-gradient alignment influence scores enriched useful examples versus random sampling but did not reliably improve validation loss at equal selected subset size and training step budget.

## Why it stopped

Proxy/local 50M-class evidence is mixed and does not support the broad claim that influence-score data selection beats random sampling.

## Recommended next action

Stop this run as no-paper evidence; a bounded deepen follow-up should test a stabilized influence selector over at least 10 seeds before attempting any real-corpus scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized influence scoring for reliable 50M-class synthetic subset selection
- Success threshold: Win final validation loss in >=8/10 seeds with positive mean and median relative validation-loss reduction versus random sampling.
- Stop condition: Stop as negative if stabilized scoring wins fewer than 7/10 seeds or if median validation-loss improvement is non-positive.

## Evidence references

- Artifact root: `<local-path>/projects/influence-score-data-selection-beats-random-sampling-at-50m-params-807c8688817e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
