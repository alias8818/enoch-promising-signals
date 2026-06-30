# Curriculum ordering for tiny pretraining data

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `curriculum-ordering-for-tiny-pretraining-data-54516dcc86be`
Run ID: `curriculum-ordering-for-tiny-pretraining-data-54516dcc86be-20260621T194716656714+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fe247ee87606

## What looked useful

Random ordering produced the best mean overall validation loss (0.9903). Easy-to-hard, hard-to-easy, and block-shuffle were worse by +1.2301, +0.7675, and +0.4261 loss respectively, although easy-to-hard slightly improved the hard-family slice at large overall cost.

## Boundaries and scale limits

Does not validate or falsify transformer-scale, real-corpus, tokenizer-level, long-run, or multi-node pretraining curricula.

## Claim scope

Bounded NumPy char-RNN probe on a deterministic tiny synthetic corpus comparing random, easy-to-hard, hard-to-easy, and block-shuffled sample orderings under a fixed 8-epoch update budget.

## Why it stopped

Bounded direct small-LM evidence does not support naive curriculum ordering as an overall improvement; this is an early scoped negative/useful-signal result, not a full-scale validation.

## Recommended next action

Stop this run as no-paper useful evidence; if continuing locally, test a mixture-balanced or competence-annealed curriculum on a tiny transformer and real small text corpus before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mixture-balanced curricula for tiny transformer pretraining
- Success threshold: Mixture-balanced curriculum beats random by at least 3% mean overall validation loss or matches overall loss within 1% while reducing worst-slice loss by at least 5%, with no slice regression above 2%.
- Stop condition: Stop if the curriculum fails to beat or match random on overall validation loss across 5 seeds or reproduces any large slice regression.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-ordering-for-tiny-pretraining-data-54516dcc86be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
