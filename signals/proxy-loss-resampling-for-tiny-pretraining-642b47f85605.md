# Proxy-Loss Resampling for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `proxy-loss-resampling-for-tiny-pretraining-642b47f85605`
Run ID: `proxy-loss-resampling-for-tiny-pretraining-642b47f85605-20260601T034529977632+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ccb67017f137

## What looked useful

Raw proxy loss is a poor standalone resampling score in this setting: with noisy data it concentrates 79.6-81.1% expected sample probability on random-noise examples, and even on clean-only data high-proxy resampling remains about +1.02 nats worse than uniform.

## Boundaries and scale limits

Synthetic Markov/noise corpus only; 3 seeds; tiny transformer; short local GB10 runs; no real tokenizer/web-text corpus, GPT-2-small-class scale, long schedule, or downstream task evaluation.

## Claim scope

In a bounded synthetic tiny-transformer pretraining test, raw high proxy-loss resampling under equal token budget was worse than uniform sampling on clean validation loss, both when the training corpus contained 25% unlearnable random sequences and when the corpus was fully clean.

## Why it stopped

Bounded proxy/tiny-LM evidence is an early falsification of raw high proxy-loss resampling, not a full-scale natural-text validation.

## Recommended next action

Stop treating raw high proxy loss as the candidate method; if continuing locally, test a learnability-adjusted score such as proxy loss decrease between early and late proxy checkpoints before any larger real-text run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learnability-Adjusted Proxy Resampling
- Success threshold: Learnability-adjusted sampling improves mean clean validation loss versus uniform by at least 0.05 nats on the noisy task without exceeding the training noise fraction by more than 10 percentage points, and is no worse than uniform by more than 0.02 nats on the clean-only ablation.
- Stop condition: Stop if learnability-adjusted sampling is worse than uniform by at least 0.05 nats on either noisy or clean-only mean validation loss, or if it still concentrates more than 50% expected sample probability on random-noise examples.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-loss-resampling-for-tiny-pretraining-642b47f85605`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
