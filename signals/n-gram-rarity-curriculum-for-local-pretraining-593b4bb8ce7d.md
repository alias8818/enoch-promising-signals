# N-gram Rarity Curriculum for Local Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-rarity-curriculum-for-local-pretraining-593b4bb8ce7d`
Run ID: `n-gram-rarity-curriculum-for-local-pretraining-593b4bb8ce7d-20260528T063953343266+0000`

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

Across two imbalance regimes and six total seeds, rare-first scheduling reduced rare-token validation loss by 0.22 to 0.31 nats versus random and slightly improved overall validation loss; common-first worsened both metrics.

## Boundaries and scale limits

Synthetic corpus only; tiny 2-layer Transformer; 600-step runs; no natural text, tokenizer-level rarity, GPT-2-small-class model, long convergence check, or datacenter-scale validation.

## Claim scope

In a synthetic tiny-Transformer causal LM proxy with rare token templates, rare-first ordering by inverse-frequency 3-gram score improved held-out rare-token loss versus random sampling under a fixed short training budget, with a common-first anti-curriculum moving in the opposite direction.

## Why it stopped

Closed as no-paper useful signal: the evidence supports the synthetic mechanism but remains a proxy rather than direct local-pretraining validation.

## Recommended next action

Run a bounded real-text follow-up using tokenizer-level n-gram rarity on a small open corpus with GPT-2-small-class or parameter-matched models before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-level n-gram rarity curriculum on small real-text pretraining
- Success threshold: Rare-first reduces held-out rare n-gram loss by at least 0.05 nats versus random with no more than 1% relative degradation in overall validation perplexity across at least three seeds.
- Stop condition: Stop if rare-first fails to beat random on rare n-gram loss in two real-text settings or if gains disappear at the longer-budget persistence checkpoint.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-rarity-curriculum-for-local-pretraining-593b4bb8ce7d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
