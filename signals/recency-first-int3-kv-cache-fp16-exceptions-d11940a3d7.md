# Recency-first INT3 KV-cache FP16 exceptions

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `recency-first-int3-kv-cache-fp16-exceptions-d11940a3d7`
Run ID: `recency-first-int3-kv-cache-fp16-exceptions-d11940a3d7-20260516T145902902711+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Recency-first INT3 KV-cache FP16 exceptions: internal_generated:recency-first-int3-kv-cache-fp16-exceptions-d11940a3d7

## What looked useful

Recency-first quantization is the useful component: distilgpt2 recent=128 averaged +0.0174 NLL vs FP16 with 3.302x theoretical KV compression, compared with +0.2664 NLL for INT3-all at 4.923x. The FP16-exception variant averaged essentially the same NLL (+0.0172), reduced compression to 2.938x, was slower in simulation, and hurt on gpt2.

## Boundaries and scale limits

The run used GPT-2-family models at native 1024-token context and rewrote Hugging Face DynamicCache tensors with dequantized values. It did not implement packed INT3 storage, CUDA attention kernels, allocator integration, long-context models, 7B+ models, or multi-request serving benchmarks.

## Claim scope

On 1024-token WikiText-2 cached decoding with distilgpt2 and gpt2, recency-first INT3 KV-cache simulation preserves perplexity far better than INT3-all at 2.5x-4.0x theoretical KV compression, but 3.125% FP16 exceptions do not provide reliable additional quality benefit over recency-only.

## Why it stopped

Direct bounded evaluation supports the recency-first mechanism but not the FP16-exception addition, and the evidence is a dequantized-cache simulation rather than a packed serving implementation.

## Recommended next action

Stop this FP16-exception line as no-paper evidence; if continuing within the lineage, branch to a packed recency-only INT3 KV-cache implementation and measure real memory and decode throughput.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Packed recency-only INT3 KV cache without FP16 exceptions
- Success threshold: At least 2.5x measured KV memory reduction versus FP16 with <=2% perplexity increase and <=15% decode throughput regression versus FP16 on a real packed implementation.
- Stop condition: Stop if packed recency-only INT3 exceeds 2% perplexity increase at <=2.5x measured KV memory reduction or if decode throughput regresses by more than 15% after basic kernel/packing optimization.

## Evidence references

- Artifact root: `<local-path>/projects/recency-first-int3-kv-cache-fp16-exceptions-d11940a3d7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
