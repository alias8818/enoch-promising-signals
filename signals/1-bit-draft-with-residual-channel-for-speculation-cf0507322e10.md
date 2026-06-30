# 1-bit draft with residual channel for speculation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `1-bit-draft-with-residual-channel-for-speculation-cf0507322e10`
Run ID: `1-bit-draft-with-residual-channel-for-speculation-cf0507322e10-20260524T193223217261+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b3865595438b

## What looked useful

Rank-4 residual used 10.94% of dense FP32 storage and improved mean acceptance overlap over pure 1-bit by +0.0235, +0.0371, and +0.0470 at teacher scales 1.0, 1.5, and 2.0. Rank-8 residual improved by +0.0456, +0.0691, and +0.0868. Residual-only rank 4 was worse than pure 1-bit, supporting the correction-channel mechanism.

## Boundaries and scale limits

No real language-model training, tokenizer/corpus, autoregressive speculative decoding loop, hardware 1-bit kernel, or accepted tokens/sec measurement was performed. Results are distribution-proxy evidence only.

## Claim scope

In a synthetic fixed-hidden-state next-token distribution-matching proxy, adding a small full-precision low-rank residual channel to a 1-bit linear draft consistently improved one-token speculative acceptance overlap and KL versus a pure 1-bit draft across 3 seeds and 3 teacher sharpness levels.

## Why it stopped

Closed as no-paper useful signal because the result supports the mechanism only in a synthetic one-step proxy, not in direct LM serving evidence.

## Recommended next action

Run a deepen follow-up with a small pretrained or quickly trained LM teacher/draft pair and measure accepted tokens/sec plus acceptance length in an actual speculative decoding loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM speculative decoding test for 1-bit draft plus residual channel
- Success threshold: At matched or clearly reported memory cost, residual draft improves accepted tokens/sec by at least 10% over pure 1-bit and improves acceptance length without detectable distribution mismatch versus the teacher-only sampler.
- Stop condition: Stop if residual overhead erases accepted-token throughput gains, if acceptance improvement is below 5% over pure 1-bit across two seeds/tasks, or if correctness checks fail.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-draft-with-residual-channel-for-speculation-cf0507322e10`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
