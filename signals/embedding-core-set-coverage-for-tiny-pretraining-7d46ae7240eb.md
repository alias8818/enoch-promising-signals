# Embedding Core-Set Coverage for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `embedding-core-set-coverage-for-tiny-pretraining-7d46ae7240eb`
Run ID: `embedding-core-set-coverage-for-tiny-pretraining-7d46ae7240eb-20260604T203823963022+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fd0adc3b10ec

## What looked useful

Coverage-based subset selection beat random by mean validation loss delta -0.004520 in the 5-seed confirmation run and won 4 of 5 paired seeds, while centroid selection was +0.010468 worse than random. The effect is small but directly tested in tiny pretraining.

## Boundaries and scale limits

Single corpus, byte-level tokenizer, simple TF-IDF embeddings, 1200 candidate documents, 250 kB selected budget, 5 training seeds, 2000 steps per seed, tiny model only; no GPT-2-small-class, BPE, semantic embedding, multi-corpus, or large-scale validation.

## Claim scope

On Wikitext-2 with a 250 kB selected-corpus budget, simple TF-IDF embedding farthest-first coverage gave a small validation-loss improvement for a byte-level 4-layer 128-wide tiny causal Transformer trained for 2000 steps, compared with random selection; centroid-nearest selection was worse.

## Why it stopped

No-paper closure: local evidence is a useful scoped tiny-pretraining signal, but it is too small and narrow for publication-grade validation.

## Recommended next action

Run a bounded deepen test with BPE tokenization, document-length controls, semantic embeddings versus TF-IDF, and a GPT-2-small-class or parameter-matched tiny baseline before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE and Length-Controlled Core-Set Selection for Tiny GPT Pretraining
- Success threshold: Coreset must beat both random and length-stratified random by at least 0.3% mean validation loss with at least 4 of 5 paired-seed wins, while centroid remains no better than random or is explained by diagnostics.
- Stop condition: Stop as unsupported if coreset fails to beat length-stratified random in at least 4 of 5 paired seeds or if length controls explain the full observed gain.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-core-set-coverage-for-tiny-pretraining-7d46ae7240eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
