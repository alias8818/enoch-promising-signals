# Perplexity-Filtered Tiny Pretraining on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-filtered-tiny-pretraining-on-cpu-82b8fe8565ea`
Run ID: `perplexity-filtered-tiny-pretraining-on-cpu-82b8fe8565ea-20260523T074954489467+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5c3a1e9f2dce

## What looked useful

Low-perplexity filtering improved target validation perplexity versus random in every confirmation run; mean relative improvement was 72.2%, with per-contamination means of 89.3%, 88.1%, 74.0%, and 37.5% at 15%, 30%, 50%, and 80% clean pool fractions. The filter also enriched clean documents from 15.1% random purity to 74.0% at the hardest 15% clean setting, and to 100% at 30% or higher clean settings.

## Boundaries and scale limits

Synthetic templated data, n-gram scorer, n-gram target model, document-budget matching only; no neural transformer, subword tokenizer, real web corpus, downstream task, or large-scale pretraining was tested.

## Claim scope

In a controlled synthetic noisy-corpus proxy, a clean-seed document perplexity filter improved equal-budget tiny word-trigram target validation perplexity versus random sampling across 32 runs and 4 contamination levels.

## Why it stopped

Closed as a useful synthetic proxy signal, not a full validation or paper-ready result.

## Recommended next action

Run a bounded direct-evidence follow-up on a real mixed text corpus with a tiny neural LM and equal token budgets; stop this worker run as useful no-paper proxy evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Tiny Neural LM Test of Clean-Seed Perplexity Filtering
- Success threshold: Low-perplexity filtering beats random sampling by at least 5% relative target validation perplexity in all seeds or by at least 10% mean relative improvement without worse compute cost.
- Stop condition: Stop if filtering fails to beat random in at least 2 of 3 seeds, if selected data collapses diversity enough to worsen validation loss, or if CPU-only runtime projects above the local budget without GPU or scale-out approval.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-tiny-pretraining-on-cpu-82b8fe8565ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
