# Real-Corpus Quality+Perplexity Selection Probe for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-corpus-quality-perplexity-selection-probe-for-tiny-pr-a9bb96dfe1`
Run ID: `real-corpus-quality-perplexity-selection-probe-for-tiny-pr-a9bb96dfe1-20260612T084105279157+0000`

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

- Parent run decision: Quality+Perplexity Scored Data Selection for Tiny Pretraining: enoch://control-plane/projects/quality-perplexity-scored-data-selection-for-tiny-pretraining-27e74ec447cd/runs/quality-perplexity-scored-data-selection-for-tiny-pretraining-27e74ec447cd-20260611T171517937338+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/33572c430bc7

## What looked useful

The combined selector reduced mean validation bpc versus random by only 0.51%, below the 1% threshold, and was 0.46% worse than perplexity-only selection. Perplexity-only selection was the best condition and improved mean validation bpc by about 0.97% versus random, while the simple quality heuristic alone was harmful.

## Boundaries and scale limits

Small direct Tier 1 test only: character-level model, Wikitext-2, simple hand-built quality heuristic, validation-derived 5-gram perplexity signal, two seeds, about 320k selected training characters per condition. Not evidence about large tokenized LMs, learned quality classifiers, broad corpora, or datacenter-scale pretraining.

## Claim scope

On Wikitext-2 with equal-token selected chunks and a tiny character Transformer trained for 1000 steps across two seeds, a simple quality+5-gram-perplexity selector did not beat random by the predeclared 1% validation-bpc margin and did not beat the better single-signal selector.

## Why it stopped

Tier 1 direct small test completed and the quality+perplexity selector missed both predeclared success margins; this is an early falsification of the scoped threshold, not a full-scale validation.

## Recommended next action

Stop this run as a direct early falsification of the tested quality+perplexity threshold; the only bounded next action worth taking is a separate confirmation of perplexity-only versus a better quality-gated selector.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer LM Confirmation of Perplexity-Only Versus Quality-Gated Selection
- Success threshold: Quality-gated perplexity must beat random by at least 1% validation loss/perplexity and beat perplexity-only by at least 0.5% with non-overlapping paired-seed mean improvement; otherwise close as perplexity-only useful signal.
- Stop condition: Stop if quality-gated perplexity is worse than perplexity-only after three paired seeds or if tokenizer-based perplexity-only fails to beat random by 0.5%.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-quality-perplexity-selection-probe-for-tiny-pr-a9bb96dfe1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
