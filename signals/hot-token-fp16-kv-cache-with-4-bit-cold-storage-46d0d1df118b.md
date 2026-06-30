# Hot-Token FP16 KV Cache with 4-bit Cold Storage

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hot-token-fp16-kv-cache-with-4-bit-cold-storage-46d0d1df118b`
Run ID: `hot-token-fp16-kv-cache-with-4-bit-cold-storage-46d0d1df118b-20260604T233002223079+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8918b642850a

## What looked useful

The mixed cache reduced estimated KV bytes by about 55% to 73%, but the naive decode path was 7.1x to 16.8x slower than FP16 in the medium sweep and 13.7x to 17.5x slower in representative 5-seed repeats, with roughly 0.105 to 0.162 relative L2 output error.

## Boundaries and scale limits

No trained model, perplexity, generation-quality, concurrent serving, production paged attention, or fused int4 attention kernel was tested. Sequence lengths were 1024 to 8192 tokens with 8 to 16 heads and head dimension 64.

## Claim scope

Synthetic CUDA decode microbenchmark on NVIDIA GB10 comparing full FP16 KV attention against hot FP16 plus packed int4 cold KV that is unpacked and dequantized on every decode step.

## Why it stopped

Proxy early falsification of the naive hot-FP16/cold-int4 design: storage savings were real, but per-token unpack/dequantize made decode much slower than FP16, so this is not a practical result without a different kernel or access policy.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should implement or use a fused/page-aware int4 cold-KV attention path that avoids unpacking the full cold cache per token.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused or page-aware int4 cold-KV decode for hot-token FP16 cache
- Success threshold: At sequence lengths of 4096 and 8192, show at least 50% estimated or measured KV-memory reduction, mixed decode latency no worse than 1.25x FP16, and relative output error below 0.05 or no material quality degradation on a small real transformer.
- Stop condition: Stop if the fused/page-aware implementation remains above 2x FP16 decode latency or cannot reduce relative output error below 0.10 at 4096 and 8192 tokens.

## Evidence references

- Artifact root: `<local-path>/projects/hot-token-fp16-kv-cache-with-4-bit-cold-storage-46d0d1df118b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
