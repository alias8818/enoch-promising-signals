# KV-Cache Compression With Real Memory Accounting on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-with-real-memory-accounting-on-gb10-8d07b99f4639`
Run ID: `kv-cache-compression-with-real-memory-accounting-on-gb10-8d07b99f4639-20260629T073332061032+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58869bd8e939

## What looked useful

Real GB10 CUDA memory accounting matched theoretical int8 KV-cache storage savings once measured before decode workspaces. The simple blockwise implementation preserved memory but imposed a large latency penalty, making fused-kernel work the next meaningful bounded test.

## Boundaries and scale limits

Synthetic random tensors only; not an end-to-end transformer serving benchmark; no real prompts, perplexity, task accuracy, fused CUDA/Triton kernel, multi-layer scheduler, or production batching validation. Largest direct cache allocation was 512 MiB fp16 versus 256 MiB int8 for one synthetic layer shape.

## Claim scope

On a GB10 host with CUDA-enabled PyTorch and swap disabled, a synthetic block-quantized int8 KV cache for batch=1, heads=16, head_dim=128, and sequence lengths up to 65,536 tokens produced allocator-measured cache storage reductions of about 2.0x versus fp16. The tested unfused blockwise PyTorch decode path was 6.5-12x slower than fp16 decode.

## Why it stopped

Bounded synthetic evidence supports real memory savings but also shows the tested unfused implementation is too slow and too proxy-only for a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up implementing fused int8 KV decode and require near-fp16 latency while preserving the measured 2x cache allocation reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused int8 KV-cache decode with GB10 allocator accounting
- Success threshold: At 65K tokens, fused int8 cache uses at least 1.9x less CUDA allocated cache memory than fp16 and median decode latency is no more than 2.0x fp16 with p99 absolute output error below 0.001 on the synthetic benchmark.
- Stop condition: Stop as negative if the fused path cannot beat 4x fp16 median latency while preserving at least 1.9x cache memory reduction, or if implementation requires dependencies unavailable on the GB10 worker.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-with-real-memory-accounting-on-gb10-8d07b99f4639`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
