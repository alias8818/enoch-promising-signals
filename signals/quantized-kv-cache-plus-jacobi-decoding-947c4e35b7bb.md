# Quantized KV Cache Plus Jacobi Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-kv-cache-plus-jacobi-decoding-947c4e35b7bb`
Run ID: `quantized-kv-cache-plus-jacobi-decoding-947c4e35b7bb-20260530T043704180688+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c14bdb765dcf

## What looked useful

Jacobi decoding matched each precision's own sequential greedy baseline exactly with zero fallbacks in all non-smoke sweeps. Int8 KV also matched full-precision sequential outputs on 3712/3712 generated tokens. Int4 KV drifted on 24/3712 generated tokens, concentrated in the block-8 stress run, so int4 is not supported as a quality-preserving default in this probe.

## Boundaries and scale limits

Random untrained small transformers only; no trained LLM, no perplexity or human quality metrics, no GPU kernels, no real KV-cache bandwidth measurement, no batching or long-context serving validation. Timings are proxy only and not speedup evidence.

## Claim scope

CPU-only NumPy toy causal-transformer mechanism probe of greedy block-Jacobi decoding with per-token/per-head KV quantization; int8 and int4 tested across 3712 non-smoke generated tokens.

## Why it stopped

Bounded proxy/mechanism evidence only; it supports an implementation direction but does not directly validate trained-model quality or serving speed.

## Recommended next action

Stop this run as no-paper useful signal; next run should test int8 KV plus Jacobi on a trained small autoregressive model with real text prompts and exact-match/perplexity/acceptance metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained small-LM validation of int8 KV cache plus Jacobi decoding
- Success threshold: Int8 has <=0.5% generated-token mismatch versus full-precision greedy decoding, no Jacobi-vs-own-sequential mismatches, no material acceptance-rate loss versus full precision, and a measured KV memory reduction; int4 must either meet the same threshold or be rejected.
- Stop condition: Stop if int8 exceeds 0.5% greedy-token mismatch, introduces any unrecovered Jacobi mismatch versus its own sequential baseline, or requires runtime beyond the local budget without GPU/kernel evidence.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-kv-cache-plus-jacobi-decoding-947c4e35b7bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
