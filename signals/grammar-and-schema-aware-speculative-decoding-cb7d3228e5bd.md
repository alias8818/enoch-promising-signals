# Grammar and Schema-Aware Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `grammar-and-schema-aware-speculative-decoding-cb7d3228e5bd`
Run ID: `grammar-and-schema-aware-speculative-decoding-cb7d3228e5bd-20260519T234016662262+0000`

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

- ChatGPT Pro speculative decoding research map 2026-05-19: file://new-chatgpt-pro-ideas-05-19.md
- Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: file://new-chatgpt-pro-ideas-05-19.md

## What looked useful

Across flat and nested finite JSON schemas, grammar-aware draft proposals improved tokens per target pass by 1.71x-3.40x at mismatch 0.6 and 1.71x-3.42x in a low-mismatch control, while reducing invalid proposal rate by roughly 0.37-0.45 absolute.

## Boundaries and scale limits

Synthetic character-level schemas only; no transformer runtime, tokenizer-level grammar, production JSON Schema engine, GPU serving, or wall-clock LLM latency validation.

## Claim scope

In a reproducible finite JSON-schema simulation with a trie verifier and weak character-level draft distribution, grammar-aware draft masking improves speculative decoding target-pass efficiency and reduces invalid draft proposals versus a grammar-unaware draft under the same verifier.

## Why it stopped

Closed as no-paper useful signal because current evidence is a synthetic finite-language proxy, not direct LLM decoding validation.

## Recommended next action

Run a bounded tokenizer-level follow-up with a small real target/draft LM pair and JSON-schema masks, measuring accepted draft tokens, target forward passes, and wall-clock tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-level schema-aware speculative decoding with small LMs
- Success threshold: Grammar-aware drafting improves wall-clock constrained generation throughput by at least 15% and accepted tokens per target forward pass by at least 25% on both schemas without changing output validity.
- Stop condition: Stop if tokenizer-level grammar masking adds enough overhead that throughput gain is below 5% on both schemas or if accepted-token efficiency does not improve by at least 10%.

## Evidence references

- Artifact root: `<local-path>/projects/grammar-and-schema-aware-speculative-decoding-cb7d3228e5bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
