# Exact-Anchor Prefix Caching for Multi-Turn Long-Context Reuse

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-prefix-caching-for-multi-turn-long-context-reuse-3a8f8e6f89a9`
Run ID: `exact-anchor-prefix-caching-for-multi-turn-long-context-reuse-3a8f8e6f89a9-20260529T175231516507+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ece0442c89b7

## What looked useful

Exact-anchor layout is useful only when all stable long-context bytes appear before any per-turn mutable content. In the 32k-token-proxy condition, exact_anchor_first reduced prompt-token work by 95.77% and kept the anchor end in the common prefix on 100% of cached turns; a mutable request id before the same corpus reduced work by only 0.012%.

## Boundaries and scale limits

No real LLM server, provider cache, tokenizer, latency, billing, KV-memory, or eviction behavior was measured. Corpus and turns were synthetic; largest corpus was 32k regex-token proxy tokens over 32 sessions and 24 turns.

## Claim scope

Synthetic multi-turn prompt assembly benchmark showing that byte-exact anchored-first long-context layout preserves common-prefix cacheability across 2k, 8k, and 32k token-proxy corpora, while mutable text before the corpus destroys useful prefix reuse.

## Why it stopped

Synthetic/proxy-only useful signal, not direct publication-grade validation of an LLM serving cache.

## Recommended next action

Stop paper path for this run; run a bounded real-server follow-up measuring cached-token counters and first-token latency on vLLM or SGLang with the same five prompt layouts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real prefix-cache latency validation for exact-anchor prompt layouts
- Success threshold: At 32k or larger context, anchored-first layout should preserve at least 80% cached-token reuse after the first turn and reduce median first-token latency by at least 2x versus mutable-before-anchor controls.
- Stop condition: Stop if real cache counters show less than 20% reuse advantage for anchored-first layout over mutable-before-anchor controls, or if the serving stack cannot expose cache-hit or latency evidence.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-prefix-caching-for-multi-turn-long-context-reuse-3a8f8e6f89a9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
