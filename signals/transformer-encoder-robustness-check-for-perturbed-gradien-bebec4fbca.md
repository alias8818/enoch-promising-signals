# Transformer encoder robustness check for perturbed gradient-matched text coresets

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `transformer-encoder-robustness-check-for-perturbed-gradien-bebec4fbca`
Run ID: `transformer-encoder-robustness-check-for-perturbed-gradien-bebec4fbca-20260529T181241395522+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Gradient-Matched Tiny Data Selection for Local Pretraining: enoch://control-plane/projects/gradient-matched-tiny-data-selection-for-local-pretraining-e961c3e82c64/runs/gradient-matched-tiny-data-selection-for-local-pretraining-e961c3e82c64-20260528T070613325937+0000
- Parent run decision: Natural-text robustness for gradient-matched tiny data selection: enoch://control-plane/projects/natural-text-robustness-for-gradient-matched-tiny-data-sel-e79e0660ee/runs/natural-text-robustness-for-gradient-matched-tiny-data-sel-e79e0660ee-20260528T143853270357+0000

## What looked useful

Gradient matching sometimes improved over stratified random, but the embedding-centroid ablation was consistently stronger on perturbed accuracy. Perturb-aware gradient selection did not repair robustness and was weaker than clean gradient matching and centroid selection.

## Boundaries and scale limits

Three fixed seeds on one dataset, one compact transformer architecture, one coreset size, and one perturbation family; not a pretrained/BERT-scale or multi-dataset validation.

## Claim scope

On AG News with a locally trained compact transformer encoder, 400-example balanced coresets selected from 4,000 training examples, and lexical dropout plus adjacent-swap perturbations, gradient-matched and perturb-aware gradient-matched text coresets do not provide a robust advantage over simpler embedding-centroid coverage.

## Why it stopped

Medium local validation directly tested the robustness claim with fixed seeds, perturbation controls, ablations, and real baselines, and the target perturbed accuracy did not support the gradient-matched coreset hypothesis.

## Recommended next action

Stop this follow-up as a no-paper useful negative; use embedding coverage as the baseline to beat before spending larger validation on gradient-matched text coresets.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/transformer-encoder-robustness-check-for-perturbed-gradien-bebec4fbca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
