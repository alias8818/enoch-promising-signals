# 2-bit KV-Cache with Residual Hot-Token Buffers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `2-bit-kv-cache-with-residual-hot-token-buffers-de4bdb4f177d`
Run ID: `2-bit-kv-cache-with-residual-hot-token-buffers-de4bdb4f177d-20260607T222356136710+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/291a0c948d7c

## What looked useful

Targeted residual hot-token buffers can nearly eliminate 2-bit KV attention-output error when the residual mask covers the high-attention token rows; same-size random and recency buffers barely help, showing the benefit depends on hot-token selection rather than memory overhead alone.

## Boundaries and scale limits

No real transformer model, perplexity, generation quality, decode latency, online eviction, or full serving stack was tested. Synthetic hot keys were norm-salient, which advantages the key-norm selector. Results should not be generalized to arbitrary LLM KV caches without real activation-trace validation.

## Claim scope

Synthetic multi-head attention tensors with persistent hot-token structure: a 2% residual high-precision KV token buffer selected by calibration attention mass or key norm reduced 2-bit attention-output relative MSE from about 0.203 to 0.00018 while retaining about 5.7x compression vs fp16.

## Why it stopped

No-paper closure: the mechanism is supported only by synthetic attention-cache experiments, not by direct real-model serving or language-model quality evidence.

## Recommended next action

Stop this run as a synthetic useful-signal result; deepen with a real GPT-2-small-class KV-trace experiment using online hot-token selection and direct perplexity/latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace validation for 2-bit residual hot-token buffers
- Success threshold: At a 1-4% residual-token budget, the online hot-token residual method should cut 2-bit-only attention-output relative MSE by at least 10x and recover at least half of the 2-bit perplexity/loss degradation versus fp16, while outperforming random and recency residual controls at the same memory budget.
- Stop condition: Stop if hot-token residual selection fails to beat random and recency controls by at least 2x on attention-output relative MSE or if decode overhead eliminates the memory/latency advantage versus a 4-bit KV cache.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-residual-hot-token-buffers-de4bdb4f177d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
