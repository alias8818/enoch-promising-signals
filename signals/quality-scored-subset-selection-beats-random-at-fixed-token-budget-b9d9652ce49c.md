# Quality-Scored Subset Selection Beats Random at Fixed Token Budget

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-scored-subset-selection-beats-random-at-fixed-token-budget-b9d9652ce49c`
Run ID: `quality-scored-subset-selection-beats-random-at-fixed-token-budget-b9d9652ce49c-20260610T011203070256+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e1da85b33ea

## What looked useful

At a 30,000-token budget with 1,800 noisy training examples and 1,000 clean test examples, the primary quality selector averaged 0.7315 accuracy and 0.7322 macro-F1 across two seeds, versus random means of 0.5876 accuracy and 0.5775 macro-F1 across 160 total random controls. The selector exceeded every random trial in both completed seeds and selected subsets with about +0.1846 higher clean-label fraction.

## Boundaries and scale limits

Evidence is limited to one dataset family, four classes, sparse TF-IDF logistic regression, synthetic 25% symmetric label noise, two completed medium seeds, and word-token budgets. It does not validate LLM pretraining, instruction tuning, natural web-data quality scores, exact tokenizer budgets, or broad cross-dataset robustness.

## Claim scope

In a bounded noisy-label 20 Newsgroups text-classification benchmark, cross-validated confidence scoring with token-normalized, class-balanced selection beat random subsets at the same word-token budget.

## Why it stopped

Closed as a no-paper useful signal because the mechanism is supported in a bounded proxy benchmark, but the evidence is not broad or direct enough for a publication-grade claim. Seed 47 was stopped after two medium checkpoints to respect the CPU-only 15-minute resource-efficiency contract.

## Recommended next action

Run a bounded follow-up with clean-data controls, additional real text datasets, budget sweeps, and at least five completed seeds to determine whether the signal is robust beyond synthetic label noise.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robustness of quality-scored fixed-budget subset selection across clean and noisy text datasets
- Success threshold: Quality-density class-balanced selection improves macro-F1 by at least 0.03 over random mean in most noisy settings, beats the 95th percentile of random trials in at least two datasets, and does not lose more than 0.02 macro-F1 on clean controls.
- Stop condition: Stop if quality selection fails to beat random by 0.03 macro-F1 in two datasets at noisy settings or if gains are explained entirely by shorter examples or class-balance controls.

## Evidence references

- Artifact root: `<local-path>/projects/quality-scored-subset-selection-beats-random-at-fixed-token-budget-b9d9652ce49c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
