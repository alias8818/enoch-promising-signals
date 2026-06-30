# Prompt-only n-gram suffix-cache speculation with KV-cache serving baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-only-n-gram-suffix-cache-speculation-with-kv-cache-afaf5e6f20`
Run ID: `prompt-only-n-gram-suffix-cache-speculation-with-kv-cache-afaf5e6f20-20260531T171213942538+0000`

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

- Parent run decision: N-gram suffix cache speculative decoding for GPT-2-small: enoch://control-plane/projects/n-gram-suffix-cache-speculative-decoding-for-gpt-2-small-b5e134599158/runs/n-gram-suffix-cache-speculative-decoding-for-gpt-2-small-b5e134599158-20260531T131941200993+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/eeb1ceb17c75

## What looked useful

The prompt-only n-gram cache mechanism works when the model is already copying prompt text: n=3/4/5 all kept exact greedy parity and achieved >11x aggregate forward-call reduction with about 96.5% draft-token acceptance. This is useful Tier 1 mechanism evidence, not paper-ready validation.

## Boundaries and scale limits

Six constructed natural-language copy examples, small model, short prompts around 500 tokens, single-request Hugging Face harness, Python KV-cache cloning, greedy decoding only, no held-out production traffic or continuous batching.

## Claim scope

In a controlled copy-heavy prompt regime using distilgpt2 greedy decoding, an automatic prompt-only n-gram suffix cache with real KV-cache verification preserved exact output on 6/6 examples and reduced target forward calls by 11.82x versus ordinary greedy KV-cache decoding.

## Why it stopped

Tier 1 direct mechanism threshold was met, but the workload is constructed and too small for a paper claim.

## Recommended next action

Run one bounded deepen validation in a production-style KV-cache serving path on a held-out RAG/extraction copy workload with automatic suffix localization and non-copy overhead controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out copy-workload prompt n-gram suffix cache in production-style KV serving
- Success threshold: Exact output parity, >=1.5x end-to-end latency speedup on copy workload, accepted tokens per verification call >=4, and <=5% latency regression on non-copy prompts.
- Stop condition: Stop if exact parity fails, accepted tokens per verification call fall below 2 on copy prompts, or non-copy overhead exceeds 10% after straightforward implementation fixes.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-only-n-gram-suffix-cache-speculation-with-kv-cache-afaf5e6f20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
