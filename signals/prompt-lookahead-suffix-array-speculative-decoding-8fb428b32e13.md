# Prompt-Lookahead Suffix-Array Speculative Decoding

Status: `useful_signal`
Project ID: `prompt-lookahead-suffix-array-speculative-decoding-8fb428b32e13`
Run ID: `prompt-lookahead-suffix-array-speculative-decoding-8fb428b32e13-20260516T160741493442+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/651118c6a43c

## What looked useful

Prompt suffix-array proposals are accepted frequently when the target model continues repeated prompt structure, yielding large target-call reductions in copy-heavy cases and preserving greedy output exactly under verification. The same mechanism provides little benefit on low-repetition prose controls.

## Boundaries and scale limits

Only distilgpt2 and Qwen/Qwen2.5-0.5B-Instruct were tested; prompts were synthetic/proxy workloads; implementation uses full-sequence forwards instead of production KV-cache serving; no natural long-context corpus, batching, sampling, or large-model validation was run.

## Claim scope

On small local greedy-decoding benchmarks with synthetic copy-heavy prompts, exact suffix-array prompt lookahead can preserve target-model output while reducing target forward calls by roughly 74-81% on copy-heavy cases; low-repetition prompts show little or no benefit.

## Why it stopped

No-paper useful signal: this run supports the mechanism on synthetic/proxy copy-heavy prompts but does not provide natural-workload or production-serving evidence needed for a bounded paper.

## Recommended next action

Run a bounded deepen study with a KV-cache implementation on natural long-context copy/retrieval/code datasets, comparing suffix-array prompt lookahead against greedy decoding and simpler n-gram lookup baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache prompt suffix lookahead on natural long-context copy workloads
- Success threshold: At least 20% end-to-end latency reduction on the high-repetition natural-task stratum, no output changes under greedy verification, and no more than 5% slowdown on low-repetition controls after index overhead is included.
- Stop condition: Stop if natural high-repetition tasks show less than 10% end-to-end latency improvement or if suffix-index overhead causes more than 5% slowdown on low-repetition controls.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookahead-suffix-array-speculative-decoding-8fb428b32e13`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
