# Exact Anchor Index with Bounded KV Cache for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-index-with-bounded-kv-cache-for-cpu-inference-5d424dfe7d0b`
Run ID: `exact-anchor-index-with-bounded-kv-cache-for-cpu-inference-5d424dfe7d0b-20260607T150328640651+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7a69b6f68e37

## What looked useful

Constructive counterexample: two prefixes with identical sparse anchor and tail state produced a 9.59 max-absolute difference in exact next-token attention output. Bounded replay matched full-cache attention within 7.22e-16 max error but was about 6.1x slower at 8192 tokens while reducing hot KV memory by 42.7x in the proxy.

## Boundaries and scale limits

No real LLM weights, tokenizer, multi-layer hidden-state replay, quantized KV, production CPU cache behavior, or long-context serving workload was tested. Sequence lengths were 128 to 8192 with dim 32 or 64 on one CPU worker process.

## Claim scope

Synthetic single-head attention tests show that sparse anchors plus a bounded live KV tail are not sufficient for exact arbitrary-prefix attention, while chunked replay from token ids can exactly match a full KV cache for deterministic layer-0 K/V at substantial CPU latency cost.

## Why it stopped

Proxy/local evidence constructively falsifies sparse-anchor-only exactness; exact bounded-hot-KV replay is possible in the toy setting but is a costly memory/latency tradeoff and not a paper-ready CPU inference result.

## Recommended next action

Stop this no-paper run; only revisit if a precise algorithm is proposed that bounds total exact state rather than storing/replaying all old K/V information elsewhere.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact multi-layer replay checkpoint budget for bounded-hot KV CPU decode
- Success threshold: At 1024 or more tokens, max logit error <= 1e-5 versus full KV while total stored state is at least 4x smaller than full KV and latency overhead is <= 2x.
- Stop condition: Stop if exactness requires storing full historical KV/activation-equivalent state or if latency overhead exceeds 5x before 1024 tokens.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-index-with-bounded-kv-cache-for-cpu-inference-5d424dfe7d0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
