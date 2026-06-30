# Perplexity-filtered data selection for tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-filtered-data-selection-for-tiny-pretraining-20eba2e13d28`
Run ID: `perplexity-filtered-data-selection-for-tiny-pretraining-20eba2e13d28-20260611T000703134761+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5e21c5e3a066

## What looked useful

Naive lowest-perplexity filtering was worse than random in mean validation perplexity and won 0/3 seeds; random won 2/3 seeds. This suggests low proxy perplexity alone may over-select easy/narrow text for tiny pretraining.

## Boundaries and scale limits

Small corpus, line-level candidates, one proxy scorer, 3 seeds, 256k target-training tokens per condition, tiny target architecture, and validation perplexity only; not evidence about large-corpus or long-schedule pretraining.

## Claim scope

On WikiText-2 with a frozen distilgpt2 proxy, 60k selected proxy-token budget, and a freshly initialized 2-layer GPT-2-like tiny causal LM trained for 250 steps per condition, selecting the lowest proxy-perplexity text did not improve validation perplexity over random or high-perplexity selection.

## Why it stopped

Bounded direct proxy experiment falsified the simple lowest-proxy-perplexity selection rule for this tiny pretraining setup; this is not a full-scale validation.

## Recommended next action

Stop this naive-filtering run; a bounded follow-up should test proxy-perplexity quantile mixtures with diversity/length controls before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantile and diversity controls for perplexity-filtered tiny pretraining
- Success threshold: A non-random quantile or mixture condition improves mean validation loss over random by at least 0.03 with overlapping controls ruled out and wins at least 4/5 seeds.
- Stop condition: Stop if no controlled quantile or mixture beats random by at least 0.01 mean validation loss after 5 seeds, or if gains disappear after length/deduplication controls.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-data-selection-for-tiny-pretraining-20eba2e13d28`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
