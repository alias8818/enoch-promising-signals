# Perplexity-Filter Threshold Ablation for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-filter-threshold-ablation-for-tiny-pretraining-5251349a6fe9`
Run ID: `perplexity-filter-threshold-ablation-for-tiny-pretraining-5251349a6fe9-20260609T211211892076+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e1d7582ea778

## What looked useful

Mean validation losses over seeds 7, 11, and 13: unfiltered clean/diverse/mixed 2.3199/2.2979/2.4763; keep_q50 improved clean to 2.2617; keep_q80 improved diverse to 2.2657; keep_q95 best preserved mixed at 2.4727. Very strict keep_q35 hurt diverse and mixed despite improving clean.

## Boundaries and scale limits

Synthetic corpus, character tokenizer, trigram external perplexity scorer, approximately 0.2M-parameter Transformer, 1,013,760 training tokens per condition, and short training runs. Not evidence for web-scale or GPT-2-small-class pretraining without real-corpus confirmation.

## Claim scope

In a three-seed synthetic character-level tiny causal LM pretraining probe, document perplexity filtering showed threshold-dependent tradeoffs: stricter filtering improved clean held-out loss, moderate filtering best improved diverse held-out loss, and permissive filtering best preserved the mixed distribution.

## Why it stopped

The result is a controlled tiny/synthetic mechanism probe with moderate evidence, not full validation or publication-grade evidence for broad pretraining.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded test should repeat the same threshold sweep on a real small text corpus with subword tokenization and matched random-retention controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus perplexity threshold ablation with random-retention controls
- Success threshold: A thresholded condition must improve its target validation loss by at least 0.02 nats over both unfiltered and matched random-retention controls in at least two of three seeds, without a larger regression on the mixed validation distribution.
- Stop condition: Stop as unsupported if thresholded filtering fails to beat matched random retention on the target validation losses or if gains disappear across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filter-threshold-ablation-for-tiny-pretraining-5251349a6fe9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
