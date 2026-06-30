# Extreme INT4 Quantization with Residual Channel Preservation for KV Compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `extreme-int4-quantization-with-residual-channel-preservation-for-kv-compression-cc43f6e4ec9b`
Run ID: `extreme-int4-quantization-with-residual-channel-preservation-for-kv-compression-cc43f6e4ec9b-20260607T135205940058+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/faa7021da4ce

## What looked useful

Residual channel preservation produced a consistent mechanism signal: mean GPT-2 attention rel MSE fell from 0.03258 for pure INT4 to 0.01412 with 4 preserved channels/head, and synthetic controls showed the benefit is much larger when a few channels carry outlier energy.

## Boundaries and scale limits

This run tested GPT-2 tensor-level attention fidelity and synthetic controls only. It did not test end-to-end perplexity, generation quality, long-context caches, 7B-class models, grouped-query attention, packed INT4 kernels, serving throughput, bandwidth, or byte-matched INT5/INT6 baselines.

## Claim scope

On GPT-2 attention tensors for 8 fixed 128-token prompts, preserving 1-8 high-energy K/V channels per head in FP16 while quantizing the remaining channels to symmetric INT4 reduced causal attention-output relative MSE versus pure INT4 in all 12 layers; four residual channels per 64-dimensional head reduced mean attention rel MSE by 56.7% while retaining 3.20x compression versus FP16 KV.

## Why it stopped

No-paper closure: the local result is a useful bounded mechanism signal, but it is proxy evidence based on attention-output error rather than full end-to-end KV-cache validation.

## Recommended next action

Run a bounded end-to-end autoregressive cache-decoding evaluation on GPT-2-small or a small Llama-family model with perplexity, generation agreement, and byte-matched all-quantized baselines before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end byte-matched residual-channel KV cache decoding test
- Success threshold: Residual-channel KV compression must reduce perplexity or next-token KL degradation by at least 25% versus the best byte-matched all-quantized baseline while preserving at least 3x KV memory compression versus FP16 on the tested model.
- Stop condition: Stop if residual preservation fails to beat the best byte-matched baseline on perplexity/KL, or if cache update overhead removes the practical memory-bandwidth advantage.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int4-quantization-with-residual-channel-preservation-for-kv-compression-cc43f6e4ec9b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
