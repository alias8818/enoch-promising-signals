# Tokenizer-level schema-aware speculative decoding with small LMs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tokenizer-level-schema-aware-speculative-decoding-with-sma-4a2f61182c`
Run ID: `tokenizer-level-schema-aware-speculative-decoding-with-sma-4a2f61182c-20260520T000222714489+0000`

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

- Parent run decision: Grammar and Schema-Aware Speculative Decoding: enoch://control-plane/projects/grammar-and-schema-aware-speculative-decoding-cb7d3228e5bd/runs/grammar-and-schema-aware-speculative-decoding-cb7d3228e5bd-20260519T234016662262+0000
- ChatGPT Pro speculative decoding research map 2026-05-19: file://new-chatgpt-pro-ideas-05-19.md
- Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: file://new-chatgpt-pro-ideas-05-19.md

## What looked useful

Schema-aware speculative decoding directly improved both constrained JSON validity and draft/target token agreement in the controlled small-LM setting, supporting the mechanism but not publication readiness.

## Boundaries and scale limits

Synthetic compact JSON schema only; finite automaton with 10 valid completions per prompt; deterministic chunk tokenizer; token n-gram LMs rather than neural transformer LMs; no GPU serving latency, BPE/SentencePiece tokenizer edge cases, nested schemas, sampling, or real workload prompts tested.

## Claim scope

In a controlled dependency-free Tier 1 test using token n-gram small LMs, a tokenizer-level finite-schema mask for compact JSON requests improved request-valid output rate from 0.0 to 1.0 and increased accepted draft tokens per target call from 1.271 to 4.750 at gamma=5, with the same validity improvement persisting for gamma 2, 3, and 8.

## Why it stopped

Tier 1 direct mechanism test completed with useful positive signal, but evidence remains synthetic and n-gram based, so this run is no-paper rather than paper-positive.

## Recommended next action

Run a bounded deepen follow-up with a real tokenizer and small neural target/draft models, comparing schema-aware speculative decoding against unconstrained speculative decoding and constrained target-only decoding on nested JSON schemas.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer neural small-LM schema-aware speculative decoding
- Success threshold: Schema-aware speculative decoding reaches at least 0.99 schema-valid outputs and at least 25% higher accepted tokens per target call than unconstrained speculative decoding without worse latency than constrained target-only decoding.
- Stop condition: Stop if schema-aware decoding fails to improve accepted tokens per target call by at least 10% over unconstrained speculative decoding or if tokenizer masking overhead makes it slower than constrained target-only decoding on the bounded benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/tokenizer-level-schema-aware-speculative-decoding-with-sma-4a2f61182c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
