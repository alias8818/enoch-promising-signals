# Perplexity-quantile data selection for tiny GPT-2-class pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-quantile-data-selection-for-tiny-gpt-2-class-pretraining-d983c186ba9e`
Run ID: `perplexity-quantile-data-selection-for-tiny-gpt-2-class-pretraining-d983c186ba9e-20260619T174202720095+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3dedabb33ff9

## What looked useful

Mid-reference-perplexity selection won against random in 3/3 calibrated seeds with mean validation loss 8.2310 versus random 8.2795 (mean delta -0.0485). Low- and high-perplexity buckets were worse than random on average.

## Boundaries and scale limits

This does not validate GPT-2-small/full-scale pretraining, large mixed-domain corpora, long training schedules, downstream transfer, or production data selection. Evidence is limited to WikiText-2, three seeds, short runs, and a small target model.

## Claim scope

On WikiText-2 with a 6.7M-parameter GPT-2-like target trained for 220 steps per condition, selecting documents from the middle of a GPT-2 reference-perplexity distribution improved held-out validation loss versus random equal-token selection across three calibrated seeds.

## Why it stopped

No-paper useful signal: the local direct evidence supports the mid-perplexity mechanism, but it is short-run, small-model, and WikiText-2-specific rather than publication-grade validation.

## Recommended next action

Run a bounded deepen study with a larger GPT-2-small-class or near-124M target, at least 6 seeds, a larger mixed-domain corpus, and the same low/mid/high/random quantile controls before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Larger bounded validation of mid-perplexity selection for GPT-2-class pretraining
- Success threshold: Mid-perplexity selection beats random and both extreme quantile buckets in mean validation loss across seeds, with a mean improvement of at least 0.03 loss or a statistically credible downstream transfer gain at matched compute.
- Stop condition: Stop if mid-perplexity does not beat random in at least 4 of 6 seeds or if its mean validation loss is not at least 0.01 better than random after the longer schedule.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-quantile-data-selection-for-tiny-gpt-2-class-pretraining-d983c186ba9e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
