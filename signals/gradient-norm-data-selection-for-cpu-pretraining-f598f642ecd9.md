# Gradient-Norm Data Selection for CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-norm-data-selection-for-cpu-pretraining-f598f642ecd9`
Run ID: `gradient-norm-data-selection-for-cpu-pretraining-f598f642ecd9-20260524T221121236481+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e971ea2dbc86

## What looked useful

High initial gradient norm was a strong structure/domain detector in this small LM proxy: selected clean fraction was 1.000 versus 0.309 for random, clean loss improved 33.8%, but mixed loss worsened 26.0%. Unconstrained raw gradient-norm selection can distort the training distribution.

## Boundaries and scale limits

No transformer, no real text corpus, no GPT-2-small-class baseline, no downstream tasks, and no dynamic rescoring. The result should not be generalized to large-scale pretraining without direct validation.

## Claim scope

Dependency-free CPU probe with an analytical softmax bigram next-token language model on a synthetic 30% structured / 70% random corpus mixture. Raw initial per-example gradient norm selected clean structured examples and improved clean validation loss, but worsened mixed-distribution validation loss.

## Why it stopped

No-paper useful signal: the local direct LM proxy found a mechanism, but the predefined success threshold failed because mixed-distribution validation worsened materially.

## Recommended next action

Stop paper route for raw unconstrained gradient-norm selection; run a bounded follow-up testing mixture-constrained or normalized gradient-norm selection on a small transformer and real text mixture.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mixture-Constrained Gradient-Norm Selection for Small Transformer Pretraining
- Success threshold: At the same selected fraction and training-token budget, constrained or normalized gradient-norm selection improves target validation loss by at least 3% over random and keeps mixed validation loss within 2% of random across at least three seeds.
- Stop condition: Stop if constrained or normalized gradient-norm selection fails to beat random on target validation or worsens mixed validation loss by more than 2% in the small-transformer setting.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-data-selection-for-cpu-pretraining-f598f642ecd9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
