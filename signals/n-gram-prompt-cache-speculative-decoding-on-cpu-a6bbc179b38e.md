# N-gram Prompt Cache Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-prompt-cache-speculative-decoding-on-cpu-a6bbc179b38e`
Run ID: `n-gram-prompt-cache-speculative-decoding-on-cpu-a6bbc179b38e-20260521T214724385784+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0a08af3db827

## What looked useful

Synthetic repeated text reached 92.46% optimistic target-call reduction and 82.22% acceptance/proposed. Local code and docs/logs reached 36.99-44.13% optimistic target-call reduction and 52.04-59.47% accepted coverage, but only 7.51-8.61% of proposed bytes matched, indicating substantial wasted verification unless a real model/tokenizer improves proposal precision.

## Boundaries and scale limits

Tested up to 1 MB per corpus with byte tokens, one CPU Python process, local files, and oracle exact-match acceptance. No tokenizer, neural language model, real speculative acceptance, KV-cache behavior, or wall-clock LLM tokens/sec was measured.

## Claim scope

A byte-token proxy benchmark shows that per-prompt n-gram continuation caches have low CPU overhead and can recover substantial exact-match continuation coverage on repetitive, code-like, and log/doc-like local text, but this is only an optimistic target-call proxy and not a measured neural decoder speedup.

## Why it stopped

Proxy-only medium benchmark supports the reuse mechanism but does not validate neural speculative decoding or real CPU speedup, so it is not paper-ready.

## Recommended next action

Stop this run as a proxy useful signal; the next concrete action is a bounded real-model CPU validation using a small autoregressive LM/tokenizer and identical prompts to measure actual tokens/sec and accepted model tokens per verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU validation of n-gram prompt-cache speculative decoding
- Success threshold: At least 15% median wall-clock tokens/sec improvement on repetitive local code/log prompts with generated-token equivalence under greedy decoding and no more than 10% slowdown on low-reuse prompts.
- Stop condition: Stop if median speedup is below 5%, generated text diverges under greedy decoding, or low-reuse prompts slow down by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-prompt-cache-speculative-decoding-on-cpu-a6bbc179b38e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
