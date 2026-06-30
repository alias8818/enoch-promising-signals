# Perplexity-gated data selection for tiny local pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-gated-data-selection-for-tiny-local-pretraining-938e495d2f9d`
Run ID: `perplexity-gated-data-selection-for-tiny-local-pretraining-938e495d2f9d-20260629T140639811956+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e50efb8a17e4

## What looked useful

A simple perplexity gate worked better as a coarse rejection filter than as a standalone top-low-perplexity selector: high-perplexity text hurt validation loss in 8/8 confirmation seed comparisons, but low-perplexity text had mixed small effects versus random.

## Boundaries and scale limits

Only WikiText-2, character tokens, short local GB10 runs, 180k-character selected training slices, 400-800 optimization steps, and a tiny Transformer were tested; no BPE, GPT-2-small-class, large corpus, long-run, or web-scale validation was performed.

## Claim scope

On WikiText-2 with a character-level 5-gram validation-domain scorer and a tiny 2-layer character Transformer trained under matched character budgets, top low-perplexity selection was not robustly better than random, while high-perplexity selection was consistently worse than random.

## Why it stopped

Direct local evidence was mixed for low-perplexity selection and therefore insufficient for a positive paper claim; the consistent high-perplexity negative control is useful but not enough to justify paper writing.

## Recommended next action

Stop this run as no-paper evidence; a bounded follow-up should test diversity-aware or band-pass perplexity gating against random on the same WikiText setup before any larger-scale pretraining claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-aware perplexity gates for tiny local pretraining
- Success threshold: Band-pass or diversity-aware gating beats random by at least 1% relative validation perplexity and beats naive low-perplexity selection in at least 4/5 paired seeds, while high-perplexity remains worse than random.
- Stop condition: Stop if no non-random gate beats random by at least 0.5% relative validation perplexity after 5 paired seeds, or if improvements are smaller than seed-to-seed variance.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-gated-data-selection-for-tiny-local-pretraining-938e495d2f9d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
