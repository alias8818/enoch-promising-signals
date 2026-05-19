# Variance-Guided Data Selection for Tiny LM Pretraining

Status: `useful_signal`
Project ID: `variance-guided-data-selection-for-tiny-lm-pretraining-3c3146778b0c`
Run ID: `variance-guided-data-selection-for-tiny-lm-pretraining-3c3146778b0c-20260517T203116210106+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/277817e856cd

## What looked useful

Variance is a useful diagnostic for underrepresented structured data, but it must be constrained by quality and coverage. Raw high variance and high loss both over-selected noisy examples; low variance over-selected common examples; bandpassed variance improved rare-domain loss but traded away common-domain coverage.

## Boundaries and scale limits

Synthetic token corpus; 2-layer tiny causal transformer; three seeds; short GB10 runs; no real text corpus, tokenizer, downstream tasks, GPT-2-small-class baseline, or large-scale pretraining.

## Claim scope

On a bounded synthetic tiny-LM pretraining proxy, raw ensemble-variance data selection is harmful because it selects noisy examples; a simple mean-loss bandpass variant finds rare structured domains and improves rare-domain validation loss, but does not improve aggregate validation loss over random selection.

## Why it stopped

No-paper closure: the local proxy gives a mixed/useful signal but early-falsifies the broad claim that variance-guided selection alone improves tiny-LM pretraining.

## Recommended next action

Run a bounded real-text deepen test that combines variance with explicit quality and coverage constraints; require aggregate validation perplexity improvement over random and quality-only controls without domain collapse.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Coverage-Constrained Variance Selection on Real Tiny-LM Text
- Success threshold: Coverage-constrained variance beats random and quality/loss-only selectors by at least 2% validation perplexity at the same token budget, while no evaluated domain/source slice regresses by more than 1%.
- Stop condition: Stop if constrained variance fails to beat random and quality/loss-only on aggregate validation perplexity, or if its gains come from domain/source collapse.

## Evidence references

- Artifact root: `<local-path>/projects/variance-guided-data-selection-for-tiny-lm-pretraining-3c3146778b0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
