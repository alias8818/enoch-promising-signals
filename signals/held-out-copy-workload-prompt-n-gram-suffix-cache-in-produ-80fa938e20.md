# Held-out copy-workload prompt n-gram suffix cache in production-style KV serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `held-out-copy-workload-prompt-n-gram-suffix-cache-in-produ-80fa938e20`
Run ID: `held-out-copy-workload-prompt-n-gram-suffix-cache-in-produ-80fa938e20-20260531T212940934088+0000`

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

- Parent run decision: N-gram suffix cache speculative decoding for GPT-2-small: enoch://control-plane/projects/n-gram-suffix-cache-speculative-decoding-for-gpt-2-small-b5e134599158/runs/n-gram-suffix-cache-speculative-decoding-for-gpt-2-small-b5e134599158-20260531T131941200993+0000
- Parent run decision: Prompt-only n-gram suffix-cache speculation with KV-cache serving baselines: enoch://control-plane/projects/prompt-only-n-gram-suffix-cache-speculation-with-kv-cache-afaf5e6f20/runs/prompt-only-n-gram-suffix-cache-speculation-with-kv-cache-afaf5e6f20-20260531T171213942538+0000

## What looked useful

Suffix hits were high on repeated copied records: 80.25% hit rate and 62.69% accounted prefill-token savings versus 14.38% for exact-prefix cache. However, real GPT-2 KV splice correctness was non-exact: mean exact-to-spliced KL 0.0304, p95 KL 0.0738, mean logit L2 447.3, and 96.25% top-1 match with 3/80 mismatches.

## Boundaries and scale limits

Tested 800 prompts per primary run, GPT-2/distilgpt2 only, synthetic copied records rather than real production traces, next-token logit correctness rather than full generation quality, and accounting-level prefill savings rather than an integrated vLLM/TensorRT-LLM scheduler benchmark.

## Claim scope

On a synthetic held-out copied-record prompt workload with fixed seeds and cached GPT-2-class causal LMs, n-gram suffix lookup can identify repeated suffixes and reduce accounted prefill tokens versus no-cache and exact-prefix-cache baselines, but naive cross-prefix suffix KV splicing changes model logits and is not an exact production KV cache.

## Why it stopped

Medium fixed-seed evidence supports the hit-rate/savings mechanism but falsifies naive cross-prefix suffix KV reuse as an exact production-style cache because it changes real-model next-token logits and caused GPT-2 top-1 mismatches.

## Recommended next action

Stop exact-cache paper path; if continuing, test a bounded approximate/corrected variant that recomputes a suffix tail window and requires both retained prefill savings and materially lower logit divergence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tail-window recomputation for approximate n-gram suffix KV reuse
- Success threshold: At K <= 32, retain at least 40% prefill-token savings over no-cache on the primary workload, reduce GPT-2 mean KL below 0.005, and observe zero top-1 mismatches across at least 200 cross-prefix suffix-reuse pairs.
- Stop condition: Stop if K <= 64 still has any top-1 mismatches or mean KL >= 0.01, or if retained savings falls below exact-prefix-cache savings.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-copy-workload-prompt-n-gram-suffix-cache-in-produ-80fa938e20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
