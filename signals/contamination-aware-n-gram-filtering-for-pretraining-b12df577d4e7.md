# Contamination-aware n-gram filtering for pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `contamination-aware-n-gram-filtering-for-pretraining-b12df577d4e7`
Run ID: `contamination-aware-n-gram-filtering-for-pretraining-b12df577d4e7-20260528T114612824177+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/45f7ea8c7955

## What looked useful

Across 10 seeds with 6000 clean docs and 240 eval docs, IDF-weighted filtering removed 100% of injected contamination, retained 99.72% of clean docs, restored benchmark perplexity to 1.001x clean-reference, and avoided the naive hard-overlap filter's 25.41 percentage-point clean-retention loss.

## Boundaries and scale limits

Synthetic documents, exact injected contamination, word-level 5-grams, and a trigram LM proxy only; no real web corpus, tokenizer-scale, transformer pretraining, or benchmark-suite validation was run.

## Claim scope

In a deterministic synthetic contamination setup with a smoothed word trigram LM, IDF-weighted 5-gram overlap filtering removed all injected exact benchmark contamination while preserving nearly all clean documents and restoring eval/clean perplexity to clean-reference behavior.

## Why it stopped

Proxy evidence supports the mechanism but does not directly validate contamination-aware n-gram filtering for real pretraining.

## Recommended next action

Run a bounded small-transformer follow-up on an open text corpus with injected held-out contamination and matched sequence-item budgets; stop this run because current evidence is synthetic/trigram proxy evidence, not paper-ready direct validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer validation of rarity-weighted n-gram decontamination
- Success threshold: Rarity-weighted filtering removes >=95% injected contamination, retains >=98% clean tokens, restores benchmark/eval loss to within 5% of clean-reference, and improves clean-token retention by >=10 percentage points versus naive hard overlap.
- Stop condition: Stop if the weighted filter misses >5% injected exact contamination at thresholds that retain >=98% clean tokens, or if clean held-out loss is >5% worse than clean-reference under matched sequence-item budgets.

## Evidence references

- Artifact root: `<local-path>/projects/contamination-aware-n-gram-filtering-for-pretraining-b12df577d4e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
