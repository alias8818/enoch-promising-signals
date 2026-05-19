# Depth-4 robustness validation of top-k QWED interpolation on GPT-2-small-class models

Status: `useful_signal`
Project ID: `depth-4-robustness-validation-of-top-k-qwed-interpolation-dc1d13dfd0`
Run ID: `depth-4-robustness-validation-of-top-k-qwed-interpolation-dc1d13dfd0-20260518T204642864036+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Depth-4 robustness validation of top-k QWED interpolation on GPT-2-small-class models: internal_generated:depth-4-robustness-validation-of-top-k-qwed-interpolation-dc1d13dfd0

## What looked useful

Top-k QWED was consistently worse than GPT-2 across k={16,64,256} at alpha 0.5 by about +0.067 NLL and remained worse across alpha={0.1,0.3,0.5,0.7,0.9} at k=64. Dense probability interpolation barely beat GPT-2 at alpha 0.9, showing the negative result is specific to the tested QWED top-k weighting rather than all interpolation.

## Boundaries and scale limits

One GPT-2-small-class model pair, one benchmark corpus, 98,304 target tokens per main condition, three fixed seeds, k ablations at alpha 0.5, and alpha sweep at k=64. The original QWED method was not formally specified in the workspace, so this is not a universal rejection of every possible QWED definition.

## Claim scope

For the explicit rank- and entropy-weighted top-k probability interpolation operationalization implemented in scripts/evaluate_topk_qwed.py, evaluated with gpt2 and distilgpt2 on WikiText-2 next-token NLL, top-k QWED does not robustly improve over the stronger GPT-2 baseline.

## Why it stopped

Bounded direct validation of the explicit tested QWED operationalization failed to beat a real GPT-2-small-class baseline, and the missing original QWED definition prevents a publication-grade positive replication.

## Recommended next action

Stop this depth-4 branch as no-paper evidence; do not recommend another follow-up from this run because the controller lineage is already at follow-up depth 4.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/depth-4-robustness-validation-of-top-k-qwed-interpolation-dc1d13dfd0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
