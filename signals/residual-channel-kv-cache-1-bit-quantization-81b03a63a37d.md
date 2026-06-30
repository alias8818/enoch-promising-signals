# Residual-Channel KV Cache 1-Bit Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-kv-cache-1-bit-quantization-81b03a63a37d`
Run ID: `residual-channel-kv-cache-1-bit-quantization-81b03a63a37d-20260529T140513328573+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/cf50c4e48289

## What looked useful

Energy-selected residual channels materially reduce 1-bit KV-cache attention reconstruction error in residual-heavy synthetic caches: 12.5% fp16 residual channels lowered rel_mse from 0.917 to 0.311 versus 0.883 for random residual selection at the same storage. On normal caches, energy and random residual selection were nearly indistinguishable. On Student-t caches, residual 1-bit remained worse than int2 and much worse than int4. Int4 dominated fidelity across all distributions.

## Boundaries and scale limits

No pretrained language model, no real prompt KV activations, no perplexity/generation metrics, no fused bit-packed kernel, and no long-context serving workload. Results should be treated as mechanism evidence only.

## Claim scope

Synthetic CUDA attention reconstruction for batch=1, heads=8, sequence=1024, queries=128, dim=64 across normal, Student-t, and residual-heavy KV distributions. Energy-selected residual fp16 channels improve 1-bit KV cache reconstruction when channel energy is concentrated, but the scheme is not competitive with int4 in these tests.

## Why it stopped

Proxy attention reconstruction produced mixed support: channel selection helps in concentrated-channel settings, but residual 1-bit is not broadly competitive with int4 and has no real-model validation here.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded test should use a small pretrained decoder and real KV activations before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Activation Residual 1-Bit KV Cache Probe on a Small Decoder
- Success threshold: Energy residual 1-bit should reduce perplexity/logit drift by at least 50% versus all-channel 1-bit and random residual at the same residual fraction, while staying within 10% relative quality degradation of int2 at equal or better compression.
- Stop condition: Stop if energy residual selection is not better than random residual on real activations, or if int2/int4 dominate both fidelity and compression-adjusted practicality.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-kv-cache-1-bit-quantization-81b03a63a37d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
