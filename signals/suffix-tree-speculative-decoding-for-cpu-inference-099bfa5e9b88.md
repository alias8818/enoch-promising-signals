# Suffix-Tree Speculative Decoding for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-for-cpu-inference-099bfa5e9b88`
Run ID: `suffix-tree-speculative-decoding-for-cpu-inference-099bfa5e9b88-20260525T062041425460+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4f14132308e8

## What looked useful

Suffix-index speculative drafting can cut idealized verifier calls by 67.91% to 92.49% on exact-repeat-heavy streams with about 1.3-1.8 us proposal overhead, but gives only 0.94% call reduction on Markov-like non-repeating noise.

## Boundaries and scale limits

No real LLM logits, KV-cache behavior, tokenizer effects, batching, or end-to-end CPU inference tokens/s were measured; datasets were small and designed to expose repeat/no-repeat regimes.

## Claim scope

Oracle-proxy CPU benchmark of an online suffix-index drafter over already accepted tokens on four small synthetic/local token streams.

## Why it stopped

Closed as no-paper useful signal because the evidence is an oracle proxy that supports the mechanism only for repeat-heavy workloads and does not directly validate end-to-end CPU inference speedup.

## Recommended next action

Run a bounded real CPU LLM integration test using this suffix drafter with adaptive draft length, comparing tokens/s against greedy decoding and a simple n-gram baseline on repeated and non-repeated prompt suites.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM suffix-drafter integration with adaptive draft length
- Success threshold: At least 20% median tokens/s improvement on repeat-heavy prompts, less than 5% median slowdown on non-repeating prompts, and exact greedy-equivalent outputs under deterministic decoding.
- Stop condition: Stop if integration overhead causes more than 5% slowdown on repeat-heavy prompts or if accepted draft length under real model verification is below 1.2 tokens on repeated/templated suites.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-for-cpu-inference-099bfa5e9b88`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
