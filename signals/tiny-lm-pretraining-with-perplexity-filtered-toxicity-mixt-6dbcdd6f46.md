# Tiny LM Pretraining With Perplexity-Filtered Toxicity Mixtures

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-lm-pretraining-with-perplexity-filtered-toxicity-mixt-6dbcdd6f46`
Run ID: `tiny-lm-pretraining-with-perplexity-filtered-toxicity-mixt-6dbcdd6f46-20260602T202850782322+0000`

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

- Parent run decision: Perplexity Filtering Removes Harmful Samples in Tiny Pretraining: enoch://control-plane/projects/perplexity-filtering-removes-harmful-samples-in-tiny-pretraining-4a22a3fead2f/runs/perplexity-filtering-removes-harmful-samples-in-tiny-pretraining-4a22a3fead2f-20260602T153214156693+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aa233e0bb664

## What looked useful

Perplexity-filtered toxic mixtures improved clean validation PPL by 1.20% in the primary moderate-mixture test and by 5.07% in the high-contamination stress test versus unfiltered toxic mixtures; coherent-toxic PPL improved by 2.56% and 8.65% respectively, while noisy-toxic PPL worsened as expected from filtering noisy artifacts.

## Boundaries and scale limits

Synthetic corpora, tiny character-level neural LM, 5 seeds per setting, 1200 SGD steps, simple n-gram filter, no real toxicity dataset, no transformer-scale model, no stochastic generation toxicity evaluation.

## Claim scope

In a controlled synthetic tiny character-LM pretraining setup, clean-domain perplexity filtering of toxic examples separates coherent toxic examples from noisy toxic artifacts and helps at high toxic-mixture intensity; the moderate-mixture primary test showed the same direction but did not meet the predeclared 5% clean-PPL threshold.

## Why it stopped

Tier 1 controlled small direct test completed; evidence is mixed but useful, with primary moderate-mixture threshold miss and high-contamination stress threshold pass, so the run is no-paper rather than paper-positive.

## Recommended next action

Run a bounded real-corpus small-transformer deepen test with matched sequence-item budgets, real clean/toxic splits, a reference-LM perplexity filter, toxicity generation metrics, and at least three seeds; do not write a paper from this synthetic tiny-LM result alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus small-transformer test of perplexity-filtered toxic pretraining mixtures
- Success threshold: Filtered mix improves clean held-out PPL by at least 3% versus unfiltered toxic mix, does not worsen toxic-domain PPL by more than 5%, and does not increase generated-toxicity metrics versus unfiltered across at least three seeds.
- Stop condition: Stop as no-paper if filtered mix fails the 3% clean-PPL improvement threshold, worsens toxic-domain PPL by more than 5%, or increases generated-toxicity metrics versus unfiltered.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-lm-pretraining-with-perplexity-filtered-toxicity-mixt-6dbcdd6f46`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
