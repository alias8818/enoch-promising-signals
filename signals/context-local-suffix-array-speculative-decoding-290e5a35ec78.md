# Context-Local Suffix-Array Speculative Decoding

Status: `useful_signal`
Project ID: `context-local-suffix-array-speculative-decoding-290e5a35ec78`
Run ID: `context-local-suffix-array-speculative-decoding-290e5a35ec78-20260516T133541918070+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d3ba195640b7

## What looked useful

The mechanism works strongly when text actually repeats earlier spans, reaching about 9x verifier-call upper bound on periodic synthetic text and 1.5x-1.65x on copy-bursty synthetic text, but natural prose showed only about 1.0x-1.12x upper-bound speedup with nontrivial CPU retrieval overhead.

## Boundaries and scale limits

No neural target model, BPE tokenizer, optimized rolling suffix index, GPU serving path, code/log corpus, or large-scale latency study was run. Reported speedups are verifier-call upper bounds, not end-to-end wall-clock speedups.

## Claim scope

A bounded proxy tested exact context-local suffix-copy drafts against future tokens on two natural prose corpora and two synthetic repetition controls using simple word/punctuation tokenization and local windows up to 2048 tokens.

## Why it stopped

Proxy early falsification for general natural prose: exact local suffix-copy acceptance was near zero to modest on Alice and Tiny Shakespeare, while positive controls confirmed the mechanism only under repetition-heavy conditions.

## Recommended next action

Stop this run as a no-paper useful signal; the broad natural-prose claim is only weakly supported by proxy evidence, but a bounded follow-up should test optimized suffix-copy drafting on highly repetitive real domains such as code or logs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized suffix-copy speculative decoding on repetitive real corpora
- Success threshold: Mean end-to-end latency speedup of at least 1.25x on a repetitive real corpus, with no regression larger than 5% on the natural-prose control and confidence intervals excluding 1.0x for the positive domain.
- Stop condition: Stop if optimized retrieval overhead eliminates verifier-call gains or if repetitive real corpora fail to exceed 1.10x end-to-end speedup against greedy decoding.

## Evidence references

- Artifact root: `<local-path>/projects/context-local-suffix-array-speculative-decoding-290e5a35ec78`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
