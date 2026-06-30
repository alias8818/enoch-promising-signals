# Natural-text robustness for gradient-matched tiny data selection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-text-robustness-for-gradient-matched-tiny-data-sel-e79e0660ee`
Run ID: `natural-text-robustness-for-gradient-matched-tiny-data-sel-e79e0660ee-20260528T143853270357+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Gradient-Matched Tiny Data Selection for Local Pretraining: enoch://control-plane/projects/gradient-matched-tiny-data-selection-for-local-pretraining-e961c3e82c64/runs/gradient-matched-tiny-data-selection-for-local-pretraining-e961c3e82c64-20260528T070613325937+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/06d174cb09bf

## What looked useful

Perturbed-pool gradient matching achieved 0.6119 clean and 0.5998 perturbed validation accuracy versus 0.5727 and 0.5674 for stratified random, and stayed within about 0.02 accuracy of clean-pool gradient matching. Exact selected examples were unstable, with clean/perturbed Jaccard overlap 0.0407.

## Boundaries and scale limits

Single cached SST-2 dataset; 2,000 candidate examples; 872 validation examples; synthetic natural-text perturbations; BoW/logistic learner; one subset size; five training seeds. No transformer fine-tuning, human paraphrases, multi-dataset validation, or LLM-scale pretraining evidence.

## Claim scope

In a Tier-1 controlled SST-2 test with a BoW/logistic classifier, a 64-example subset selected by gradient matching on naturally perturbed candidate text retained downstream clean and perturbed validation accuracy within 0.05 of clean-pool gradient matching and at least 0.03 above stratified random.

## Why it stopped

No-paper closure: the small direct test supports the mechanism but is not publication-grade because it uses a BoW/logistic learner, synthetic perturbations, and one dataset/subset budget.

## Recommended next action

Run a bounded transformer-encoder follow-up on SST-2 or MRPC using the same clean-versus-perturbed gradient-selection threshold and a paraphrase or multi-operator perturbation set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer encoder robustness check for perturbed gradient-matched text coresets
- Success threshold: Perturbed-pool gradient matching remains within 0.05 absolute validation accuracy of clean-pool gradient matching and beats stratified random by at least 0.03 on both clean and perturbed validation.
- Stop condition: Stop as unsupported if perturbed-pool gradient matching misses either threshold on the transformer test or if gains are within random-control variance across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/natural-text-robustness-for-gradient-matched-tiny-data-sel-e79e0660ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
