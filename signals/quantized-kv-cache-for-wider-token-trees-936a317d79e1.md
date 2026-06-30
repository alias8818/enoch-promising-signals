# Quantized KV Cache for Wider Token Trees

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-kv-cache-for-wider-token-trees-936a317d79e1`
Run ID: `quantized-kv-cache-for-wider-token-trees-936a317d79e1-20260604T002524386644+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f1841f57fa90

## What looked useful

Branch-only int8 KV nearly doubled modeled width under an fp16 width-64 budget with max relative L2 error 0.000873 and max p95 abs error 0.0000916, while all-int8 reached median 4.875x width gain with max relative L2 error 0.00949. The naive PyTorch path was slower than fp16, with branch-only median runtime ratio 2.295x.

## Boundaries and scale limits

No real transformer, no trained-model KV distribution, no acceptance-rate or perplexity measurement, no end-to-end speculative decoding, and no fused int8 attention kernel. Results are a bounded synthetic mechanism test, not a full validation.

## Claim scope

Synthetic GB10 PyTorch token-tree attention benchmark with random fp16 K/V/Q tensors, 24 modeled layers, 16 heads, head dimension 128, prefix length 1024, widths 16-256, and branch depths 4/8. Int8 per-token/per-head KV quantization preserves attention outputs with low relative L2 error and increases modeled tree width under a fixed KV budget, but naive dequantize-then-attend execution is slower than fp16.

## Why it stopped

No-paper useful signal: synthetic evidence supports memory/error viability but naive runtime is slower and direct real-model speculative decoding evidence is missing.

## Recommended next action

Run a bounded real-model follow-up on GPT-2-small-class speculative decoding that measures acceptance, quality/perplexity, memory, and throughput for fp16 versus branch-only int8 KV; stop if quantized KV does not preserve acceptance within 2 percentage points or if optimized throughput fails to exceed fp16 at equal memory budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model branch-int8 KV cache for speculative token trees
- Success threshold: At equal KV memory budget, branch-only int8 KV supports at least 1.8x tree width, keeps acceptance within 2 percentage points or perplexity delta within 0.1 versus fp16, and improves end-to-end decode throughput by at least 10%.
- Stop condition: Stop as negative if real-model acceptance drops by more than 2 percentage points, perplexity increases by more than 0.1, or optimized quantized throughput remains at or below fp16 throughput at equal memory budget.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-kv-cache-for-wider-token-trees-936a317d79e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
