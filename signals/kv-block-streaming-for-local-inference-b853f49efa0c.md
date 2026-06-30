# KV-Block Streaming for Local Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-block-streaming-for-local-inference-b853f49efa0c`
Run ID: `kv-block-streaming-for-local-inference-b853f49efa0c-20260607T194026590701+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fec5ab3734c4

## What looked useful

Resident selected KV blocks were much faster than full resident attention, but host-streamed selected KV was slower than full resident attention at 50% and 25% retention across all tested context lengths. Host streaming only slightly beat full resident attention at 12.5% retention, where relative L2 output error versus full attention was 2.65-2.77 on the synthetic task.

## Boundaries and scale limits

Synthetic KV only; one attention layer; no real transformer logits/perplexity; no learned selector; no multi-layer scheduler; no quantized KV; no prefetch or overlap beyond PyTorch non_blocking copies; not a full serving benchmark.

## Claim scope

Naive per-token host-to-GPU KV-block streaming with contiguous recent-block selection on a synthetic one-layer fp16 decode-attention benchmark for 4096-16384 token contexts on NVIDIA GB10.

## Why it stopped

Proxy microbenchmark showed transfer overhead dominates naive host KV streaming except at an aggressively small retained fraction with very high approximation error, so this is useful no-paper evidence rather than a full validation.

## Recommended next action

Stop this run as an early proxy falsification of naive host-streamed KV blocks; the concrete next bounded test is to repeat with real small-LLM KV traces and a quality-preserving selector.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace KV block selection and streaming benchmark for small local LLM decode
- Success threshold: At 25% or lower KV retention, selected-block decode has relative logit error below 0.1 or perplexity increase below 5%, and host-streamed selected KV improves ms/token by at least 20% versus full resident attention at 8192 or 16384 context.
- Stop condition: Stop if real-trace selection at 25% retention exceeds the quality threshold or if staged host streaming remains slower than full resident attention at 50% retention.

## Evidence references

- Artifact root: `<local-path>/projects/kv-block-streaming-for-local-inference-b853f49efa0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
