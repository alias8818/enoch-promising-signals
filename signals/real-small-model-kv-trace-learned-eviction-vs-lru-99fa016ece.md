# Real small-model KV trace learned eviction vs LRU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-small-model-kv-trace-learned-eviction-vs-lru-99fa016ece`
Run ID: `real-small-model-kv-trace-learned-eviction-vs-lru-99fa016ece-20260613T045133571435+0000`

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

- Parent run decision: Bounded KV Cache: Learned Eviction vs LRU Baseline: enoch://control-plane/projects/bounded-kv-cache-learned-eviction-vs-lru-baseline-d623efb415b3/runs/bounded-kv-cache-learned-eviction-vs-lru-baseline-d623efb415b3-20260613T041402048126+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/3aa1f9434937

## What looked useful

Learned eviction beat LRU on all 12 held-out trace-fraction pairs. Mean retained-attention improvements were 0.087753 at 12.5% cache, 0.087971 at 25% cache, and 0.068072 at 50% cache, corresponding to relative gains of 14.45%, 12.52%, and 8.18%.

## Boundaries and scale limits

Trace replay only; no actual KV tensors were evicted during decoding, no answer-quality/perplexity/latency metrics were measured, and the prompt/model/corpus scale is too small for publication-grade claims.

## Claim scope

On 12 hand-written prompts traced through distilgpt2, with 8 train traces and 4 held-out eval traces, a ridge-regression learned eviction scorer retained more real attention-derived KV utility than an LRU/sliding-window baseline at 12.5%, 25%, and 50% cache fractions.

## Why it stopped

Tier 1 direct trace evidence supports the mechanism, but the run is not paper-ready because it is trace replay rather than integrated decoding with quality and latency metrics.

## Recommended next action

Run a bounded end-to-end evicted-decoding follow-up on a GPT-2-small-class model, measuring perplexity or task accuracy under identical learned-vs-LRU KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-LM KV eviction quality test
- Success threshold: Learned eviction must improve perplexity or task accuracy over LRU by at least 2% relative at two or more cache budgets without more than 10% runtime overhead, across at least three held-out prompt sets.
- Stop condition: Stop if learned eviction fails to beat LRU on end-to-end quality at two cache budgets or if eviction overhead exceeds 10% without a quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-model-kv-trace-learned-eviction-vs-lru-99fa016ece`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
