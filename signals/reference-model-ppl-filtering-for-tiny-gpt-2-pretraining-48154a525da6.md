# Reference-Model PPL Filtering for Tiny GPT-2 Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `reference-model-ppl-filtering-for-tiny-gpt-2-pretraining-48154a525da6`
Run ID: `reference-model-ppl-filtering-for-tiny-gpt-2-pretraining-48154a525da6-20260628T133301983649+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cb0d99f13efd

## What looked useful

distilgpt2 low-PPL filtering beat random mixed selection in 3/3 seeds with mean final validation loss delta -0.0566 and selected clean examples almost perfectly; weak tiny-gpt2 reference failed to enrich clean text and failed to beat random mixed.

## Boundaries and scale limits

Synthetic corruptions, 64 candidates per confirmation run, 24 selected training items, 96 validation items, 15 training steps, CPU-only local run, three confirmation seeds. Not a full Tiny GPT-2 pretraining or real-corpus data filtering validation.

## Claim scope

On a small WikiText-derived corpus with synthetic corruptions, low-perplexity filtering using a capable pretrained reference LM (distilgpt2) selected clean examples and improved clean validation loss for fresh tiny GPT-2-style models under a 15-step bounded training budget.

## Why it stopped

No-paper useful signal: bounded synthetic-contamination evidence supports the mechanism but is not direct/full-scale pretraining validation.

## Recommended next action

Run a bounded medium follow-up on a naturally noisy real corpus with equal-token training for at least 1k-5k optimizer steps and thresholds chosen from held-out reference-PPL quantiles.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-corpus validation of reference-PPL filtering for Tiny GPT-2 pretraining
- Success threshold: Low-PPL filtered training improves final clean validation loss over random equal-token baseline in at least 2/3 seeds by at least 0.03 nats without reducing token budget.
- Stop condition: Stop if low-PPL filtering fails to beat random equal-token baseline in at least 2/3 seeds or if reference scoring cannot separate candidate quality better than random.

## Evidence references

- Artifact root: `<local-path>/projects/reference-model-ppl-filtering-for-tiny-gpt-2-pretraining-48154a525da6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
