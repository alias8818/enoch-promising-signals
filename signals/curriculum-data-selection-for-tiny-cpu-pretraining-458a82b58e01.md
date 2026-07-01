# Curriculum data selection for tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `curriculum-data-selection-for-tiny-cpu-pretraining-458a82b58e01`
Run ID: `curriculum-data-selection-for-tiny-cpu-pretraining-458a82b58e01-20260605T220335305259+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0220a6649e00

## What looked useful

Quality filtering may matter more than staged curriculum ordering for tiny CPU-budget pretraining when noisy/high-entropy chunks are present; however, filtering sacrifices noisy-distribution coverage and the tested staged curriculum was effectively tied with random on the main mixed target.

## Boundaries and scale limits

Synthetic character corpus, MLP next-character model, 20 seeds, 89,600 training samples per strategy/seed, no real tokenizer, no Transformer, no downstream tasks, and no full-scale pretraining corpus.

## Claim scope

In a synthetic NumPy-only tiny character-LM proxy with fixed CPU token/update budget, strict quality filtering improved clean and mixed validation loss versus random sampling, while the tested easy-to-hard curriculum schedule did not improve clean or mixed validation over random.

## Why it stopped

Proxy-only useful signal: the staged curriculum hypothesis was not supported on clean/mixed validation, while quality filtering showed a strong synthetic mechanism that is not sufficient for paper-positive claims.

## Recommended next action

Run a bounded real-corpus follow-up with a tiny GPT-style Transformer, matched sequence-item budgets, random versus quality-filtered versus curriculum schedules, and held-out perplexity on clean/mixed/noisy slices.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny Transformer test of quality filtering versus curriculum scheduling
- Success threshold: Quality-filtered or curriculum strategy improves mixed held-out perplexity by at least 5% versus random across at least 8 of 10 paired seeds without more than 15% degradation on a declared coverage slice.
- Stop condition: Stop if neither quality filtering nor curriculum beats random mixed perplexity by 2% in a 5-seed pilot, or if improvements only come from excluding evaluation-relevant coverage slices.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-data-selection-for-tiny-cpu-pretraining-458a82b58e01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
