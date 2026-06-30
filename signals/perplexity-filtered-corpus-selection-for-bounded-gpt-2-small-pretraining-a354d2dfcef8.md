# Perplexity-filtered corpus selection for bounded GPT-2-small pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-filtered-corpus-selection-for-bounded-gpt-2-small-pretraining-a354d2dfcef8`
Run ID: `perplexity-filtered-corpus-selection-for-bounded-gpt-2-small-pretraining-a354d2dfcef8-20260609T120811594552+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/839721ff4c4c

## What looked useful

Low-perplexity filtering beat random on validation loss in all 3 confirmation seeds: mean low_ppl val_loss 1.5577 vs random 2.0483, mean delta -0.4906. High-perplexity selection was much worse: mean val_loss 4.2736, mean delta vs random +2.2253.

## Boundaries and scale limits

Synthetic documents, character-level tiny decoder, bigram scorer, 240k train-token streams, 450 optimizer steps per condition, 3 seeds; no GPT-2-small scale, pretrained GPT-2 perplexity scorer, real web corpus, downstream transfer, or diversity/deduplication controls.

## Claim scope

In a synthetic mixed-quality corpus with a bigram perplexity proxy and tiny GPT-style decoder, selecting low-perplexity documents improved clean held-out validation loss versus equal-budget random selection across 3 seeds.

## Why it stopped

Proxy-only useful signal; evidence supports the filtering mechanism locally but is not direct GPT-2-small or real-corpus validation.

## Recommended next action

Run a bounded real-corpus follow-up using a GPT-2 tokenizer and pretrained GPT-2 perplexity scorer, with low/mid/random/high perplexity bins and deduplication controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2 perplexity binning for bounded small-LM pretraining
- Success threshold: Low or mid perplexity selection improves mean held-out validation loss by at least 5% versus random across 3 seeds without worse repetition/diversity metrics.
- Stop condition: Stop if low and mid perplexity bins fail to beat random by at least 2% mean validation loss improvement or if selected data is dominated by duplicates/boilerplate.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-corpus-selection-for-bounded-gpt-2-small-pretraining-a354d2dfcef8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
