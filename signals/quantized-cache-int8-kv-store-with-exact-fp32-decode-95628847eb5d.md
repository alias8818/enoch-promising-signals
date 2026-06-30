# Quantized Cache: INT8 KV Store with Exact FP32 Decode

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `quantized-cache-int8-kv-store-with-exact-fp32-decode-95628847eb5d`
Run ID: `quantized-cache-int8-kv-store-with-exact-fp32-decode-95628847eb5d-20260609T025207937999+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/480fb0c46c7f

## What looked useful

A reproducible NumPy probe showed ordinary FP32 K/V tensors round-trip exactly for only about 1.3-1.6% of elements under per-vector symmetric INT8 quantization, while a grid-restricted positive control round-tripped exactly. Synthetic attention outputs had mean relative L2 error 0.00847 and zero bitwise-exact outputs after quantized decode.

## Boundaries and scale limits

Experiments were CPU-vectorized synthetic tensor probes, not a real transformer serving stack. The exactness conclusion is scale-independent for INT8-only arbitrary FP32 encoding, but downstream quality and throughput of approximate INT8 KV caching were only proxied.

## Claim scope

Arbitrary FP32 K/V tensors cannot be stored as INT8 symbols with per-vector FP32 scales and then decoded bitwise exactly back to the original FP32 values; exact decode is only possible for values already restricted to the quantization grid or with additional side information.

## Why it stopped

Proxy/early falsification: bounded direct exactness tests plus the INT8-versus-FP32 information bound rule out arbitrary FP32 exact decode from INT8-only KV storage, but this is not a full real-model validation of approximate INT8 KV behavior.

## Recommended next action

Stop exact-decode work unless a new codec specifies grid-constrained K/V generation or explicitly budgets residual side information; treat approximate INT8 KV caching as a separate engineering evaluation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/quantized-cache-int8-kv-store-with-exact-fp32-decode-95628847eb5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
