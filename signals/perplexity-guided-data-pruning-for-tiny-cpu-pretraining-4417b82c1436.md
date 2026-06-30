# Perplexity-Guided Data Pruning for Tiny CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-guided-data-pruning-for-tiny-cpu-pretraining-4417b82c1436`
Run ID: `perplexity-guided-data-pruning-for-tiny-cpu-pretraining-4417b82c1436-20260608T090700988282+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48a4ed233ae9

## What looked useful

Perplexity-guided pruning is useful as a cheap quality/noise filter under a fixed byte budget, but the clean-only control warns against treating low perplexity as a universal data-quality criterion for tiny pretraining.

## Boundaries and scale limits

Small proxy only: byte n-gram reference and target models, four public-domain books, 1024-byte chunks, synthetic corruptions, no neural transformer, no tokenizer study, no downstream tasks, no large-scale web data.

## Claim scope

In a bounded NumPy byte-trigram probe on Gutenberg text, reference-perplexity pruning improves tiny CPU LM validation loss when the candidate pool contains obvious synthetic corruptions, but low/median perplexity pruning does not improve and slightly worsens selection from already-clean natural text.

## Why it stopped

Proxy/local evidence is mixed: it supports the noise-filtering mechanism but early-falsifies the broad claim that perplexity pruning generally helps clean tiny pretraining data.

## Recommended next action

Run a bounded neural-LM follow-up on a naturally noisy corpus with clean-only controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural tiny-LM validation of perplexity pruning as quality filtering
- Success threshold: Low or median reference-perplexity pruning must improve clean held-out validation loss by at least 0.05 bits/token or an equivalent statistically stable threshold versus random on noisy data, while not degrading clean-only data by more than the random baseline variability.
- Stop condition: Stop if the neural run shows no improvement over random on noisy data or repeats the clean-only degradation without a compensating noisy-corpus gain.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-guided-data-pruning-for-tiny-cpu-pretraining-4417b82c1436`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
