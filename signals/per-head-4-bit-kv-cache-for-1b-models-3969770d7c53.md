# Per-head 4-bit KV cache for 1B models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-4-bit-kv-cache-for-1b-models-3969770d7c53`
Run ID: `per-head-4-bit-kv-cache-for-1b-models-3969770d7c53-20260602T210931120320+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4174e93ed6b9

## What looked useful

Per-head int4 cache storage reached about 4.0x projected compression, but naive PyTorch int4 unpack/dequantize plus attention was 3.23x, 3.28x, and 3.41x slower than FP16 attention at sequence lengths 512, 2048, and 8192. Attention-output relative L2 error remained about 0.28 on random KV.

## Boundaries and scale limits

No real 1B model activations, perplexity, generation quality, fused int4 attention kernel, or end-to-end serving throughput were tested. All-layer memory was analytically projected; timing used a single synthetic layer.

## Claim scope

Synthetic GB10 single-token decode benchmark for a naive per-head-global symmetric 4-bit KV cache with 16 layers projected, 16 KV heads, head dimension 64, and sequence lengths 512/2048/8192. The result supports near-4x cache storage reduction but rejects this straightforward packed-dequantize-then-attend path as a latency improvement and flags nontrivial attention-output distortion on random KV.

## Why it stopped

Proxy early falsification rather than full validation: the simple per-head-global packed int4 implementation saves memory but is slower than FP16 and numerically noisy under synthetic 1B-class decode geometry.

## Recommended next action

Stop this run as a proxy early falsification of the naive per-head-global int4 KV path; the next bounded test should use real 1B-model KV activations and a fused int4 attention kernel before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-activation fused int4 KV cache test for a 1B decoder
- Success threshold: At 8k context, fused int4 KV decode is at least 1.2x faster than FP16 while reducing KV memory by at least 3.5x and keeping perplexity degradation within 5% or mean logit cosine similarity above 0.99 on the evaluation set.
- Stop condition: Stop if real-activation per-head int4 relative attention/logit error remains high, perplexity degrades beyond 5%, or fused int4 decode is not faster than FP16 at 8k context.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-4-bit-kv-cache-for-1b-models-3969770d7c53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
