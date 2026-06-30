# Perplexity Binning for Quality/Noise Tradeoff

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-binning-for-quality-noise-tradeoff-937fd067d741`
Run ID: `perplexity-binning-for-quality-noise-tradeoff-937fd067d741-20260601T033521572314+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ccb67017f137

## What looked useful

Perplexity binning was useful as a diagnostic axis: high perplexity isolated injected noise and low-middle perplexity isolated mostly clean documents. However, naive lowest-perplexity selection was not reliable because it concentrated boilerplate, and toy n-gram validation loss favored that low-diversity bin in all replicates.

## Boundaries and scale limits

Synthetic contamination, word n-gram scorer, word n-gram downstream proxy, five small CPU-only replicates, no transformer scorer, no neural LM training, no generation-quality evaluation, and no web-scale corpus.

## Claim scope

In a controlled WikiText-derived contaminated corpus scored by a small word trigram reference LM, perplexity bins reproducibly separated clean, boilerplate-heavy, and noisy regions; the low-middle perplexity bin had the best composition, while the lowest-perplexity bin was boilerplate-heavy.

## Why it stopped

No-paper closure: local evidence supports a useful diagnostic mechanism but does not directly validate improved modern LM training quality; the available downstream n-gram proxy is confounded by boilerplate.

## Recommended next action

Run a bounded deepen test with a transformer reference scorer and small neural LM training to compare equal-token random, lowest, low-middle, middle, and highest perplexity selections on held-out perplexity plus diversity/generation diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-scored perplexity bins for neural LM data selection
- Success threshold: Low-middle perplexity selection improves held-out clean neural LM perplexity by at least 2% versus random and lowest-perplexity selections while keeping measured noise below 5% and avoiding a lower unique-token ratio than random by more than 10%.
- Stop condition: Stop as negative if low-middle selection fails to beat random on held-out neural LM perplexity in at least 3 of 5 seeds or if its diversity/boilerplate diagnostics are worse than random.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-binning-for-quality-noise-tradeoff-937fd067d741`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
