# KV Cache Quantization for Long Context Inference: INT8 vs FP16 Tradeoffs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-quantization-for-long-context-inference-int8-vs-fp16-tradeoffs-784789f6ac65`
Run ID: `kv-cache-quantization-for-long-context-inference-int8-vs-fp16-tradeoffs-784789f6ac65-20260614T082202058416+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/498077bb1909

## What looked useful

INT8 KV-cache storage nearly halved cache bytes. Granular layouts, especially per-channel keys with per-token values, kept max synthetic output relative L2 near 0.01, while naive global INT8 reached 0.0796 under mixed outliers. Latency was implementation-dependent once dequantization was included.

## Boundaries and scale limits

No real LLM task quality, perplexity, tokenizer path, multi-layer model, batch serving, CUDA kernel, paged attention, or contexts above 8192 tokens were tested. CPU NumPy timing is not representative of GPU serving throughput.

## Claim scope

Synthetic single-step decode attention with 8 heads, head dimension 64, sequence lengths up to 8192, and controlled normal/outlier KV-cache distributions. INT8 cache layouts were compared against FP16 storage for memory footprint, attention-output error, and CPU NumPy decode timing with read-time dequantization.

## Why it stopped

Closed as no-paper useful signal because this run is synthetic/proxy evidence rather than direct model-serving validation.

## Recommended next action

Run a bounded real-transformer follow-up that injects FP16, global INT8, per-token INT8, and K-channel/V-token INT8 KV-cache layouts into an actual decode path and measures perplexity/task delta plus GPU throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer validation of granular INT8 KV-cache layouts
- Success threshold: K-channel/V-token INT8 achieves about 2x KV-cache memory reduction with less than 1% relative quality degradation versus FP16 and better quality than global INT8 at matched context length, while throughput is neutral or positive after fused dequantization.
- Stop condition: Stop if granular INT8 quality degradation is not materially better than global INT8, or if unfused/fused dequantization overhead prevents any memory-throughput benefit at the tested context lengths.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-quantization-for-long-context-inference-int8-vs-fp16-tradeoffs-784789f6ac65`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
