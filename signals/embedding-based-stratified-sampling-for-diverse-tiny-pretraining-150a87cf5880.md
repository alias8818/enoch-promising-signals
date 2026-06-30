# Embedding-Based Stratified Sampling for Diverse Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `embedding-based-stratified-sampling-for-diverse-tiny-pretraining-150a87cf5880`
Run ID: `embedding-based-stratified-sampling-for-diverse-tiny-pretraining-150a87cf5880-20260528T071022534896+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/06d174cb09bf

## What looked useful

Embedding-stratified sampling reduced mean perplexity from 20.568 to 19.080 and worst-label perplexity from 24.086 to 21.972 over five seeds, while increasing sample label entropy from 0.931 to 1.179 and reducing mean pairwise embedding cosine from 0.396 to 0.314. Oracle label stratification remained stronger at 17.968 mean perplexity.

## Boundaries and scale limits

Evidence is synthetic and uses hashed TF-IDF embeddings plus a count-based bigram LM proxy. It does not validate real-corpus tiny neural pretraining, tokenizer effects, noisy web domains, or larger model scales. AG News loading stalled during smoke and produced no real-dataset metrics.

## Claim scope

On a deterministic four-domain synthetic news corpus with a 70/10/10/10 imbalanced unlabeled pool and balanced heldout set, embedding-cluster stratified sampling selected a more diverse fixed-budget corpus than uniform sampling and improved smoothed word-bigram heldout perplexity.

## Why it stopped

Closed as no-paper useful signal because the positive mechanism evidence is synthetic/proxy-only; it is not a full validation of embedding-based stratified sampling for real tiny pretraining.

## Recommended next action

Run a bounded real-corpus neural LM follow-up using cached/downloadable AG News or TinyStories, equal token budgets, and a tiny Transformer/GRU to test whether the synthetic diversity-to-perplexity signal survives real text.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Tiny LM Validation of Embedding-Stratified Sampling
- Success threshold: Embedding-stratified sampling improves balanced heldout perplexity by at least 3% versus uniform and reduces worst-domain perplexity by at least 5% across at least three seeds without using labels.
- Stop condition: Stop if real-dataset loading remains unavailable, if embedding clusters fail to improve diversity over uniform, or if neural LM heldout perplexity is not better than uniform by the success threshold.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-based-stratified-sampling-for-diverse-tiny-pretraining-150a87cf5880`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
