# Self-Speculative Decoding with Target Model Only

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-with-target-model-only-a845d8938d82`
Run ID: `self-speculative-decoding-with-target-model-only-a845d8938d82-20260608T121935336052+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f44864991620

## What looked useful

The simple target-only early-layer draft path had low acceptance (2.50%-16.22% across GPT-2-small float32 grid configurations) and was slower than full greedy decoding; best aggregate wall speedup was 0.846x and best estimated compute speedup was 0.893x.

## Boundaries and scale limits

The run used GPT-2-small, short prompts, greedy decoding, unbatched inference, and a simple non-KV-cache harness. It did not test 7B+ models, sampled decoding, long contexts, batched serving, optimized kernels, or trained early-exit heads/adapters.

## Claim scope

On GPT-2-small greedy decoding with 8 short prompts, a zero-training target-only self-draft made from the target model's own early layers preserved float32 greedy outputs but did not improve latency or estimated compute cost.

## Why it stopped

Bounded proxy/direct early falsification: direct GPT-2-small float32 exactness and latency tests showed low acceptance and no speedup; larger optimized validation would only be warranted after a stronger draft mechanism clears this local threshold.

## Recommended next action

Stop this exact no-training early-layer draft variant; a bounded follow-up should test whether a trained target-only early-exit head can raise acceptance enough to beat greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a target-only early-exit draft head for self-speculative decoding
- Success threshold: On GPT-2-small, at least 50% aggregate draft acceptance, exact greedy output preservation, and at least 1.10x aggregate wall-clock speedup versus full greedy decoding on a held-out prompt set.
- Stop condition: Stop as negative if a trained target-only draft head fails to reach 40% acceptance or 1.05x wall-clock speedup under the same bounded compute budget.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-with-target-model-only-a845d8938d82`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
