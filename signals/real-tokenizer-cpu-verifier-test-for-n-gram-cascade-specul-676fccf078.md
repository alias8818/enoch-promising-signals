# Real-tokenizer CPU verifier test for n-gram cascade speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-tokenizer-cpu-verifier-test-for-n-gram-cascade-specul-676fccf078`
Run ID: `real-tokenizer-cpu-verifier-test-for-n-gram-cascade-specul-676fccf078-20260530T071035793276+0000`

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

- Parent run decision: CPU Speculative Decoding via N-gram Cascade: enoch://control-plane/projects/cpu-speculative-decoding-via-n-gram-cascade-415a20b3b586/runs/cpu-speculative-decoding-via-n-gram-cascade-415a20b3b586-20260530T032813438751+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8eee2585211c

## What looked useful

Static train-only n-gram tables nearly but did not cross the Tier 1 threshold (best 1.235 tokens/target call). Online recent-cache n-grams crossed it for draft lengths 2, 4, and 8, peaking at 1.304 tokens/target call and 23.32% fewer target calls than greedy, with mean CPU proposal time about 7.31 us/call and mean prefix verification time about 1.47 us/proposal.

## Boundaries and scale limits

Single corpus, single tokenizer, oracle held-out token stream, Python implementation, no real LLM target pass, no GPU serving latency, no batching, no sampler/quality interaction, and no cross-domain robustness. Static train-only n-grams did not reach the 1.25 threshold; the positive bounded signal depends on online cache updates.

## Claim scope

In a Tier 1 controlled CPU-only oracle-verifier test on 50k held-out GPT-2 BPE tokens from Tiny Shakespeare, an online recent-cache n-gram cascade reduced target verifier calls versus a greedy one-token baseline; the best tested configuration reached 1.304 emitted tokens per target call with low-microsecond CPU proposal and verification overhead.

## Why it stopped

Tier 1 direct CPU verifier threshold was met, but the result remains an oracle-token verifier mechanism test rather than publication-grade end-to-end model-serving evidence.

## Recommended next action

Run a bounded end-to-end speculative decoding test around a small real target model, using the dynamic recent-cache n-gram proposer and measuring wall-clock throughput, accepted tokens, and quality-equivalent outputs against greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-model n-gram cascade speculative decoding latency test
- Success threshold: At least 10% wall-clock tokens/sec improvement over greedy decoding at output-equivalent settings, with no more than 5% CPU overhead and consistent target forward-pass reduction on at least two prompt sets.
- Stop condition: Stop if target-call reduction fails to translate into at least 5% wall-clock speedup in the small-model implementation or if output equivalence/quality cannot be maintained under deterministic decoding.

## Evidence references

- Artifact root: `<local-path>/projects/real-tokenizer-cpu-verifier-test-for-n-gram-cascade-specul-676fccf078`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
