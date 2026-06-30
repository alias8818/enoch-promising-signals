# Context-Adaptive N-gram Speculation with Acceptance Feedback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `context-adaptive-n-gram-speculation-with-acceptance-feedback-84f9659be898`
Run ID: `context-adaptive-n-gram-speculation-with-acceptance-feedback-84f9659be898-20260527T210713947694+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1f0ab6a3dfc7

## What looked useful

Adaptive order selection improved synthetic shifted-stream speedup by a mean 3.81% over best static across five seeds, but underperformed best static on Tiny Shakespeare by 2.69%; oracle order selection had only 3.08% real-text headroom.

## Boundaries and scale limits

The target model was proxied by held-out token streams; results use regex tokenization and target-call speedup proxy rather than neural model wall-clock decoding, KV-cache behavior, GPU scheduling, or multi-corpus evaluation.

## Claim scope

A CPU-only proxy experiment found that online acceptance-feedback selection among n-gram draft orders can beat the best fixed order on a controlled synthetic shifted stream, but this simple adaptive UCB policy did not beat the best fixed n-gram order on a Tiny Shakespeare real-text token stream.

## Why it stopped

Bounded proxy evidence is mixed: the mechanism works on synthetic shifts, but the real-text proxy fails the practical success threshold of beating the best static n-gram baseline, so this is not publication-grade validation.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded test should implement a real GPT-2-small tokenizer/verifier loop and compare adaptive feedback against static unigram, longest-suffix n-gram, and adaptive draft-length baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer GPT-2-small n-gram speculation with acceptance feedback
- Success threshold: Adaptive feedback must improve wall-clock tokens/sec or target-call speedup by at least 5% over the best static/backoff n-gram baseline on at least two real prompt distributions without regressing the third by more than 1%.
- Stop condition: Stop if adaptive feedback fails to beat the best static/backoff baseline on two of three real prompt distributions or if oracle headroom over the best static/backoff baseline is below 3% across all distributions.

## Evidence references

- Artifact root: `<local-path>/projects/context-adaptive-n-gram-speculation-with-acceptance-feedback-84f9659be898`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
