# Embedding-Guided Shard Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `embedding-guided-shard-selection-for-tiny-pretraining-dc545f8168ad`
Run ID: `embedding-guided-shard-selection-for-tiny-pretraining-dc545f8168ad-20260607T153416234749+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/74bd16827ba8

## What looked useful

Across two corrected medium runs, SVD embedding selection reduced loss by 0.3400 and 0.4921 nats versus the per-run random mean, averaging a 33.8% relative perplexity reduction. Guided selectors selected 100% target-category shards while random selections averaged 30.6%.

## Boundaries and scale limits

Small corpus, clean category structure, target-like shards present in the source pool, tiny 2-layer Transformer, two medium corpus-shuffle seeds, no GPT-2-small-class or web-scale validation.

## Claim scope

On a 20 Newsgroups tiny-pretraining proxy with disjoint target query and target evaluation documents, fixed-budget TF-IDF/SVD shard selection improved held-out target-domain causal-LM validation loss versus random shard selection.

## Why it stopped

The result is a corrected small/medium proxy confirmation of the mechanism, not a full validation of embedding-guided pretraining data selection.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up with GPT-2-small-class scale, neural embeddings, sparse-retrieval controls, and a rarity/noise ablation before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-Small-Class Neural Embedding Shard Selection With Rarity Ablation
- Success threshold: Neural embedding selection beats the random mean and sparse lexical control by at least 0.10 nats held-out target loss in at least two of three seeds without increasing token budget.
- Stop condition: Stop as negative if neural embedding selection fails to beat sparse lexical selection or random mean under the rarity/noise ablation after the planned seeds.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-guided-shard-selection-for-tiny-pretraining-dc545f8168ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
