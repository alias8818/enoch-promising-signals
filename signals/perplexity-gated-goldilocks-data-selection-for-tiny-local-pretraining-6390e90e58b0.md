# Perplexity-Gated Goldilocks Data Selection for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-gated-goldilocks-data-selection-for-tiny-local-pretraining-6390e90e58b0`
Run ID: `perplexity-gated-goldilocks-data-selection-for-tiny-local-pretraining-6390e90e58b0-20260602T184244220384+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/31f9a80fb709

## What looked useful

Goldilocks mean validation loss was 2.41939 versus random 2.48844 and high-perplexity 2.80166, but low-perplexity was 2.41801 and won two of three seeds. Perplexity gating is useful as a noise filter here, not as evidence for preferring a middle perplexity band.

## Boundaries and scale limits

Three local seeds, 180k selected-character budgets, 300 training steps per strategy, character-level Transformer, synthetic easy/noisy distractors, n-gram scorer, and held-out Wikitext-2 validation only; no subword LM, neural scorer, natural web-scale corpus, or GPT-2-small-class training.

## Claim scope

On a Wikitext-2-based mixed clean/easy/noisy candidate pool, a character n-gram perplexity gate improves tiny character-Transformer validation loss by filtering high-perplexity noisy examples, but middle-band Goldilocks selection does not reliably outperform a low-perplexity clean-example control.

## Why it stopped

Bounded direct tiny-LM evidence is mixed for the Goldilocks hypothesis: middle perplexity beats random and high-perplexity noisy selection, but does not beat the simpler low-perplexity control.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded test should use a natural corpus with duplicate/boilerplate low-perplexity examples and a neural scorer to test whether Goldilocks beats low-perplexity when low perplexity is not synonymous with clean in-domain text.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Goldilocks gating under natural low-perplexity boilerplate pressure
- Success threshold: Goldilocks must beat both random and low-perplexity controls by at least 0.03 validation-loss points on mean across seeds while maintaining lower duplication than low-perplexity selection.
- Stop condition: Stop as negative if Goldilocks fails to beat low-perplexity or deduplicated-low controls across three seeds at the same token budget.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-gated-goldilocks-data-selection-for-tiny-local-pretraining-6390e90e58b0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
