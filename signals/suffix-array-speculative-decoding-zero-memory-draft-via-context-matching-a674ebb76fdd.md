# Suffix-Array Speculative Decoding: Zero-Memory Draft via Context Matching

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-zero-memory-draft-via-context-matching-a674ebb76fdd`
Run ID: `suffix-array-speculative-decoding-zero-memory-draft-via-context-matching-a674ebb76fdd-20260523T084507890191+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c52acf841528

## What looked useful

On synthetic repeat contexts, suffix-array prompt lookup accepted 3.8250 tokens/step and beat fixed prompt-local n-grams on accepted tokens/step. On Tiny Shakespeare, it accepted only 0.1365 tokens/step with 2.33% proposed-token acceptance despite a 73.56% proposal rate, indicating frequent low-value drafts on ordinary natural text.

## Boundaries and scale limits

16 Tiny Shakespeare episodes and 16 synthetic repeat episodes with 1024-token prompts, 256-token continuations, max draft 8, simple regex tokenization, and exact replay-token acceptance proxy. No target language model, KV-cache integration, optimized native suffix array, BPE tokenizer, batching, or broad corpus validation.

## Claim scope

Bounded offline oracle replay over prompt-local context matching: suffix-array prompt lookup can draft useful continuations in repeat-heavy contexts, but did not produce enough accepted tokens on Tiny Shakespeare natural text to support a general speculative-decoding claim.

## Why it stopped

Proxy/early falsification of the broad natural-text claim: exact replay acceptance on natural text was too low to plausibly offset verification overhead, while the positive repeat control only supports a narrower copy-heavy mechanism.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test end-to-end prompt-lookup speculation with a small open target model and compare wall-clock speed against no-draft and n-gram prompt lookup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Small-Model Prompt-Lookup Speculative Decoding
- Success threshold: At least 1.15x wall-clock tokens/second over no-draft and at least 1.05x over n-gram prompt lookup on copy-heavy prompts, with no material slowdown on ordinary natural-text prompts.
- Stop condition: Stop if target-model verified acceptance stays below 0.5 accepted tokens/step or wall-clock throughput fails to beat no-draft on the copy-heavy benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-zero-memory-draft-via-context-matching-a674ebb76fdd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
