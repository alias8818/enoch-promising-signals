# Anchor-Delta KV Compression for Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-delta-kv-compression-for-long-context-9d6611a628c9`
Run ID: `anchor-delta-kv-compression-for-long-context-9d6611a628c9-20260525T221521568958+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3a0eedd186f6

## What looked useful

Anchor-delta KV compression appears to exploit local K/V smoothness enough to halve attention-output error relative to direct quantization in many tested settings, but it pays extra anchor bytes and remains unvalidated as a deployable decoding cache.

## Boundaries and scale limits

Trace-level evaluation only: GPT-2 small, WikiText-2, maximum 1024-token windows, reconstructed attention-output metrics only. No end-to-end perplexity, generation quality, serving latency, cache kernel, RoPE/GQA model, or long-context task validation was performed.

## Claim scope

On GPT-2 small WikiText windows at 512 and 1024 tokens, anchor-delta KV reconstruction reduced per-layer causal attention-output RMSE versus a direct per-block quantization control at the same nominal bit width across tested 4-bit and 8-bit block sizes, while using 1.5% to 15.0% more KV bytes than that direct control.

## Why it stopped

This run closes as a no-paper useful signal because evidence is trace-level and attention-output proxy only, not full validation of an inference cache system.

## Recommended next action

Run a bounded end-to-end decode follow-up that inserts anchor-delta KV into autoregressive generation and measures perplexity, task/generation quality, memory, and latency against dense KV and direct quantized KV controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Anchor-Delta KV Decode Evaluation
- Success threshold: At matched or near-matched KV byte ratio, anchor-delta should reduce perplexity degradation by at least 25% versus direct quantized KV, keep generation/task metric loss within 5% relative of dense KV, and avoid more than 15% decode throughput regression.
- Stop condition: Stop if integrated anchor-delta decoding shows no perplexity or task-quality advantage over direct quantized KV at comparable cache size, or if decode throughput overhead exceeds 25% before quality gains appear.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-delta-kv-compression-for-long-context-9d6611a628c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
