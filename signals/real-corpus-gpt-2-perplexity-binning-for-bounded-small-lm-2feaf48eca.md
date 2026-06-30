# Real-corpus GPT-2 perplexity binning for bounded small-LM pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-gpt-2-perplexity-binning-for-bounded-small-lm-2feaf48eca`
Run ID: `real-corpus-gpt-2-perplexity-binning-for-bounded-small-lm-2feaf48eca-20260609T165005270331+0000`

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

- Parent run decision: Perplexity-filtered corpus selection for bounded GPT-2-small pretraining: enoch://control-plane/projects/perplexity-filtered-corpus-selection-for-bounded-gpt-2-small-pretraining-a354d2dfcef8/runs/perplexity-filtered-corpus-selection-for-bounded-gpt-2-small-pretraining-a354d2dfcef8-20260609T120811594552+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/839721ff4c4c

## What looked useful

Real-corpus GPT-2 perplexity binning did not meet the predeclared useful-signal threshold: low-PPL averaged only 0.59% better than random and was worse in one seed; no bin beat random by >=5% in any of three seeds. High-PPL selection averaged 4.51% worse than random, suggesting very high teacher-perplexity text may be harmful for early tiny-LM pretraining under this budget.

## Boundaries and scale limits

Small Wikitext-2 corpus subset, 900 scored candidate docs per seed, 160 docs per condition, tiny 4-layer 128-embedding student, 120 optimizer steps, GPT-2 tokenizer/teacher, one validation corpus, equal document count and equal optimizer steps but not strict equal available-token matching.

## Claim scope

In a three-seed Tier 1 Wikitext-2 experiment using GPT-2 teacher perplexity bins and identical tiny GPT-style students trained from scratch for 120 steps, low/mid/high teacher-PPL binning did not produce a robust >=5% validation perplexity improvement over random example selection; high-PPL bins were usually worse.

## Why it stopped

Small direct controlled test failed the predeclared >=5% improvement threshold and showed seed instability, so it is an early no-paper result rather than full validation.

## Recommended next action

Stop this paper track at no-paper useful signal; if deepening, run a token-matched version with longer training and >=5 seeds before considering any larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-matched GPT-2 perplexity bins for small-LM pretraining
- Success threshold: A bin condition must beat random-control validation perplexity by >=5% on mean across >=5 seeds, with at least 4/5 seeds directionally positive and no hidden token-exposure advantage.
- Stop condition: Stop if no bin reaches >=5% mean validation perplexity improvement over random, if the result remains seed-unstable, or if gains disappear after token matching.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-gpt-2-perplexity-binning-for-bounded-small-lm-2feaf48eca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
