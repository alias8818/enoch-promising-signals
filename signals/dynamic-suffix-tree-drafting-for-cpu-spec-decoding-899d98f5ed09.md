# Dynamic Suffix Tree Drafting for CPU Spec-Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-suffix-tree-drafting-for-cpu-spec-decoding-899d98f5ed09`
Run ID: `dynamic-suffix-tree-drafting-for-cpu-spec-decoding-899d98f5ed09-20260629T063232294516+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/520493da9a0d

## What looked useful

Suffix-trie drafting is useful when suffix continuations repeat heavily: 3.2776 accepted tokens/step on copy_bursts versus 3.0362 for the best fixed n-gram control, and 3.4083 on local_text versus 2.9365. It is not universally better: ngram_1 beat suffix_trie on Markov data, and IID acceptance was effectively zero.

## Boundaries and scale limits

Tested only on synthetic/local 50k-token streams with exact-token offline validation; no real LLM tokenizer trace, target-model verifier, KV-cache interaction, batching, stochastic sampling, or production CPU decoder integration was measured.

## Claim scope

A bounded offline CPU proxy shows an online reversed suffix trie can improve exact draft-token acceptance on repeated-continuation streams, but it does not broadly dominate cheap n-gram controls and has no practical value on IID streams.

## Why it stopped

Proxy evidence is mixed: the mechanism works on repeated streams but fails to justify a standalone CPU speculative decoding claim without direct tokenizer/decoder measurements.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should evaluate suffix-trie plus n-gram fallback on real tokenizer traces with wall-clock target verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-trace suffix-trie drafting with repetition-gated fallback
- Success threshold: At least 10% wall-clock tokens/second improvement over the best n-gram-only control on repeated traces, no statistically meaningful slowdown on low-repetition traces, and peak memory below 2x the n-gram control.
- Stop condition: Stop if suffix-trie plus fallback fails to beat n-gram-only by 5% on repeated traces or exceeds 2x memory without corresponding wall-clock gain.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-suffix-tree-drafting-for-cpu-spec-decoding-899d98f5ed09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
