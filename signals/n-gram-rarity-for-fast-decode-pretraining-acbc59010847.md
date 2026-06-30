# N-Gram Rarity for Fast Decode Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-gram-rarity-for-fast-decode-pretraining-acbc59010847`
Run ID: `n-gram-rarity-for-fast-decode-pretraining-acbc59010847-20260525T180131049210+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9dc65dc46b70

## What looked useful

Naive n-gram rarity weighting appears too blunt for fast-decode pretraining: it can increase seen rare-4-gram top-1 accuracy, but it did not transfer to rare continuation accuracy or exact rollout and worsened validation loss.

## Boundaries and scale limits

Two seeds, tiny causal Transformer, synthetic corpus, greedy continuation metrics; no natural-language corpus, GPT-2-small-scale training, production serving benchmark, or teacher/draft speculative decoding acceptance measurement.

## Claim scope

In a controlled small-decoder synthetic pretraining probe, raw inverse-frequency 4-gram loss weighting did not improve greedy rare phrase continuation versus ordinary cross-entropy; aggressive weighting was harmful and mild weighting only improved seen-4-gram memorization.

## Why it stopped

Early bounded falsification: the direct local proxy for fast deterministic decode showed no rare-continuation gain over baseline, so this is not paper-positive without a different objective and direct acceptance evidence.

## Recommended next action

Stop this naive raw-rarity objective as no-paper evidence; if continuing, run a bounded teacher/draft speculative-decoding follow-up with selective rare-span weighting and acceptance-rate metrics on natural text.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Selective Rare-Span Weighting for Draft-Model Acceptance
- Success threshold: At least 5% relative improvement in rare-bucket teacher/draft top-1 agreement or accepted tokens per speculative step, with less than 1% relative degradation in overall validation loss and common-bucket acceptance.
- Stop condition: Stop if selective weighting fails to improve rare-bucket acceptance in a smoke plus one medium run, or if any rare-bucket gain is offset by more than 1% overall/common acceptance degradation.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-rarity-for-fast-decode-pretraining-acbc59010847`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
