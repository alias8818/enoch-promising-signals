# Suffix-array speculative decoding for CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-for-cpu-inference-9568c506d08b`
Run ID: `suffix-array-speculative-decoding-for-cpu-inference-9568c506d08b-20260530T080413454386+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ba852333a41c

## What looked useful

Naive suffix-array drafting is not compelling for word-like LLM-token continuations on this corpus, but exact-match retrieval can produce multi-token drafts in low-cardinality/repetitive streams. Future work should test copied-context/code/log domains with a real CPU LLM verifier and an optimized range-count lookup.

## Boundaries and scale limits

No actual LLM verifier, tokenizer, KV-cache path, or end-to-end CPU latency was measured. Byte-token results used only the first 250,000 bytes and 5,000 held-out positions after a larger byte run was stopped for CPU-budget reasons. The result should not be generalized to 7B-class CPU inference or broad natural-language serving.

## Claim scope

Bounded proxy on tiny Shakespeare: suffix-array exact-match drafting gives only 1.1041x ideal verifier-call reduction with word tokens, but a constrained byte-token diagnostic reaches 2.0744x ideal verifier-call reduction on repetitive low-cardinality text.

## Why it stopped

Proxy evidence is mixed and not publication-grade: word-token drafting produced only a 10.4% ideal call reduction before overhead, while the stronger byte-token result does not directly validate LLM-token CPU inference.

## Recommended next action

Stop this run as no-paper proxy evidence; run one direct CPU LLM follow-up using llama.cpp or an equivalent local verifier, comparing suffix-array drafting against greedy decoding and a hash n-gram baseline on copied-context/code/log prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM latency test for suffix-array drafting on copied-context prompts
- Success threshold: At least 1.20x end-to-end tokens/sec over greedy decoding and at least 1.10x over a hash n-gram draft baseline on copied-context/code/log prompts, with lookup p95 below 10% of verifier iteration time.
- Stop condition: Stop if suffix-array speculative decoding is below 1.05x greedy speedup or does not beat the hash n-gram baseline on two prompt domains after lookup optimization.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-for-cpu-inference-9568c506d08b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
