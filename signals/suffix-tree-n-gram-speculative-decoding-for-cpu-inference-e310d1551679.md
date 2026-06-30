# Suffix-tree n-gram speculative decoding for CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-n-gram-speculative-decoding-for-cpu-inference-e310d1551679`
Run ID: `suffix-tree-n-gram-speculative-decoding-for-cpu-inference-e310d1551679-20260522T121510641440+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c1981d2fd8ee

## What looked useful

Suffix n-gram speculation has a strong necessary-condition signal for repetitive/code-like contexts but is workload-sensitive; the simple heuristic achieved only 4.15% verifier-call reduction on word-tokenized controller instructions while reaching 78.79-93.75% on repeated prose/code/synthetic word-token corpora and 91.50-93.70% on repeated code/synthetic byte-token corpora.

## Boundaries and scale limits

No real transformer model, no production BPE tokenizer, no actual CPU end-to-end LLM latency measurement, no block-verification kernel measurement, and only small local corpora. Results should not be read as a full CPU inference speedup claim.

## Claim scope

Dependency-free oracle-continuation mechanism probe of online suffix n-gram speculative decoding on local repetitive, code-like, synthetic, mixed, and controller-prompt corpora. The supported scoped claim is that exact prompt/history n-gram drafts can reduce verifier invocations by about 79-94% on repetitive/code-like proxy corpora, but are weak on less regular instruction text under a simple most-recent-match heuristic.

## Why it stopped

Proxy-only mixed result: useful verifier-call reduction signal on repetitive/code-like corpora, weak signal on controller-style instruction text, and no real LLM wall-clock benchmark.

## Recommended next action

Run a direct small-model CPU inference follow-up using a real tokenizer/model and identical greedy-output verification; stop this run because the present evidence is a proxy mechanism result, not a full validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU prompt-lookup speculative decoding with a small real language model
- Success threshold: At least 10% wall-clock speedup on repeated code/log prompts with exact greedy-output equality and no more than 5% slowdown on nonrepetitive prompts.
- Stop condition: Stop as negative if exact-output speculative decoding fails to produce a latency win on repeated code/log prompts or introduces more than 5% slowdown on nonrepetitive prompts after implementation overhead is optimized enough that lookup p95 is below 1 ms.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-n-gram-speculative-decoding-for-cpu-inference-e310d1551679`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
