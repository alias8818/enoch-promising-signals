# 2-bit per-head KV lookup tables for 2x context on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `2-bit-per-head-kv-lookup-tables-for-2x-context-on-gb10-ee92553e2909`
Run ID: `2-bit-per-head-kv-lookup-tables-for-2x-context-on-gb10-ee92553e2909-20260528T215443164277+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0390c3e9c4a0

## What looked useful

The memory arithmetic is favorable, but the tested per-head scalar 2-bit LUT mechanism does not preserve attention outputs: normal KV median attention-output relative MSE was 0.220 with median cosine 0.883, decayed KV median MSE was 0.291, and heavy-tailed KV median MSE was 0.996. Naive LUT dequantized decode was slower than fp16 in every case.

## Boundaries and scale limits

No pretrained LLM perplexity or retrieval evaluation, no fused packed 2-bit attention kernel, no real activation trace, and no multi-layer accumulated error measurement.

## Claim scope

On GB10 synthetic KV tensors up to heads=32, dim=128, seq=8192, per-head 4-entry scalar 2-bit LUT K/V storage gives about 8x raw KV memory reduction but produces large attention-output distortion and is slower when implemented as dequantize-then-attend.

## Why it stopped

Proxy early falsification: the isolated KV-cache mechanism failed attention-fidelity and naive decode-speed checks before a full LLM validation was warranted.

## Recommended next action

Stop the simple per-head scalar 2-bit LUT path; only revisit with a bounded groupwise/per-channel or outlier-aware 2-bit KV quantization test using the same attention-output diagnostics before kernel work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Outlier-aware groupwise 2-bit KV quantization for GB10 attention
- Success threshold: Attention-output relative MSE <= 0.05 and cosine >= 0.98 across tested distributions/traces while retaining at least 2x effective KV memory reduction.
- Stop condition: Stop if heavy-tailed or real KV traces exceed 0.10 attention-output relative MSE, or if the method requires metadata that reduces effective memory savings below 2x.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-per-head-kv-lookup-tables-for-2x-context-on-gb10-ee92553e2909`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
