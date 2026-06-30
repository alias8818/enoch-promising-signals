# Gradient-Free Influence Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-free-influence-data-selection-for-tiny-pretraining-6e123d5276ad`
Run ID: `gradient-free-influence-data-selection-for-tiny-pretraining-6e123d5276ad-20260528T180252005053+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/10efd384d24c

## What looked useful

Gradient-free validation n-gram scoring produced 100% target purity and reduced mean test CE from 6.1372 for random selection to 5.5709 for GFI selection; paired GFI-random test CE delta was -0.5663 with approximate 95% CI [-0.6975, -0.4351]. Anti-GFI degraded to 7.7418 mean test CE.

## Boundaries and scale limits

Synthetic Markov data only; 64-token sequences; 320 selected sequences; 220 optimizer steps; sub-GPT-2-scale tiny Transformer; no natural-language corpus, tokenizer, or large-scale pretraining validation.

## Claim scope

On a synthetic four-domain token pretraining probe with a 35% target-domain candidate pool, a validation-bigram gradient-free influence proxy selected target-aligned data and improved tiny causal Transformer target test cross-entropy versus random and anti-selected controls over 5 seeds.

## Why it stopped

This run produced a useful synthetic mechanism signal, but synthetic-only tiny-pretraining evidence is not sufficient for a paper-ready validation.

## Recommended next action

Run a bounded real-text domain-selection follow-up using the same no-gradient scoring protocol against random, perplexity filtering, and embedding-retrieval baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text bounded validation for gradient-free influence data selection
- Success threshold: GFI must improve mean target test CE over random by at least 0.05 and beat or tie perplexity filtering within paired confidence intervals without anti-GFI showing similar gains.
- Stop condition: Stop if GFI fails to beat random on mean paired target test CE or if gains disappear when distractor domains are label-balanced and validation text is held out.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-free-influence-data-selection-for-tiny-pretraining-6e123d5276ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
