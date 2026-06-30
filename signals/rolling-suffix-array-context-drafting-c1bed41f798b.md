# Rolling suffix-array context drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rolling-suffix-array-context-drafting-c1bed41f798b`
Run ID: `rolling-suffix-array-context-drafting-c1bed41f798b-20260524T044733896526+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9b19fa4a73f3

## What looked useful

Suffix-array lookup preserves the exact-match drafting mechanism while using far less memory than a naive all-context hash table at long contexts, but it is much slower in this implementation and exact copied continuations perform poorly on Tiny Shakespeare, with about 0.111 accepted tokens per 8-token draft and zero full 8-token drafts accepted.

## Boundaries and scale limits

No target LLM, tokenizer-specific model distribution, KV-cache integration, GPU serving path, batching, or end-to-end speculative decoding speedup was tested. The suffix-array implementation is a naive Python prefix-search index, not an optimized LCP/FM-index/suffix-automaton implementation. Corpora are small and local.

## Claim scope

Bounded local probe of exact-match rolling suffix-array context drafting over small token streams: synthetic repeated motifs, duplicated project prompt text, and 60k-token Tiny Shakespeare. Metrics cover draft acceptance length, coverage, build time, query throughput, and rough Python index memory versus an exact-context hash baseline.

## Why it stopped

Bounded local evidence supports a memory tradeoff but not a practical or paper-ready drafting method: naive suffix-array queries are 12x-34x slower than hash lookup at context 64, and natural-language exact-match copied drafts accept only about 0.111 tokens per 8-token draft.

## Recommended next action

Do not pursue the naive suffix-array drafter as paper-ready; run one bounded optimized-index follow-up only if the goal is to test whether LCP/FM-index acceleration can keep the memory advantage while reaching hash-like query throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LCP-accelerated suffix-index context drafting
- Success threshold: At context 64 on the 60k-token Tiny Shakespeare probe, use under 10 MB index memory, reach at least 50000 qps, preserve acceptance metrics within 1% absolute of the exact-match baseline, and then show positive end-to-end target-model decoding speedup before claiming practical value.
- Stop condition: Stop if optimized suffix-index query throughput remains below 10000 qps at context 64 or if exact-match acceptance on natural-language text remains below 0.25 accepted tokens per 8-token draft without a separate model-based acceptance gain.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-suffix-array-context-drafting-c1bed41f798b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
