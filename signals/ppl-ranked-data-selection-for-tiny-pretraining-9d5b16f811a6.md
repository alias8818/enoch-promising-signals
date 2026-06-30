# PPL-Ranked Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `ppl-ranked-data-selection-for-tiny-pretraining-9d5b16f811a6`
Run ID: `ppl-ranked-data-selection-for-tiny-pretraining-9d5b16f811a6-20260529T111420974381+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9c7d9b00b62d

## What looked useful

Naive PPL-quantile data selection was worse than random in the main 48-chunk run: low_ppl +0.0204 NLL, mid_ppl +0.0163 NLL, high_ppl +0.0302 NLL versus random. A 24-chunk robustness run repeated the pattern: low_ppl +0.0105, mid_ppl +0.0011, high_ppl +0.0890 versus random.

## Boundaries and scale limits

The test used a smoothed character 4-gram reference scorer, a tiny character next-token neural LM, one public text corpus, two small selected-token budgets, and three seeds per strategy. It does not cover subword tokenization, learned reference LMs, large corpora, GPT-2-small-class models, downstream tasks, or diversity-preserving PPL-aware sampling.

## Claim scope

In a bounded NumPy character-level tiny-pretraining setup on Tiny Shakespeare, selecting contiguous low-, middle-, or high-reference-perplexity chunk quantiles did not beat random chunk selection under equal token budgets.

## Why it stopped

Direct small-scale evidence did not support the naive PPL-ranked selection hypothesis; this is not a full-scale validation, but it is enough to reject the tested local selection rule as paper-positive.

## Recommended next action

Stop this run as a bounded local negative; a separate follow-up should test PPL-stratified or diversity-preserving selection rather than contiguous PPL quantiles.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PPL-Stratified Data Selection for Tiny Pretraining
- Success threshold: PPL-stratified/diversity-preserving selection improves mean held-out NLL versus random by at least 0.01 across seeds while no single seed regresses by more than 0.005 NLL.
- Stop condition: Stop if stratified/diversity-preserving selection is tied with or worse than random at two selected-token budgets, or if diagnostics show the apparent gain is caused by leakage or duplicate removal rather than PPL-aware sampling.

## Evidence references

- Artifact root: `<local-path>/projects/ppl-ranked-data-selection-for-tiny-pretraining-9d5b16f811a6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
