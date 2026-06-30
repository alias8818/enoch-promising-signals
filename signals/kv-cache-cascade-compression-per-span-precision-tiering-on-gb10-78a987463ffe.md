# KV-cache cascade compression: per-span precision tiering on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-cascade-compression-per-span-precision-tiering-on-gb10-78a987463ffe`
Run ID: `kv-cache-cascade-compression-per-span-precision-tiering-on-gb10-78a987463ffe-20260621T163212442501+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/02abaca87fa0

## What looked useful

The memory-side mechanism is plausible, but the latency path is not viable without a fused segmented attention kernel or a serving design that avoids full per-step materialization of quantized spans.

## Boundaries and scale limits

Synthetic random KV tensors only; one-token decode only; no full transformer, no perplexity/generation quality, no paged serving workload, no batching study, no fused dequant-attention kernel, and no multi-seed statistical robustness beyond repeated timing reps.

## Claim scope

On a GB10 PyTorch synthetic single-token decode benchmark with 16 heads, head_dim 128, and contexts up to 65536 tokens, fp16/int8/int4 per-span KV tiering can reduce estimated KV storage by 36.9-72.9% while preserving attention output cosine similarity of 0.978-0.9999, but a naive unpack/dequantize/materialize implementation is 6.3-10.7x slower than fp16 KV attention.

## Why it stopped

Proxy GPU microbenchmark produced a useful early falsification of the naive implementation path: memory savings are real in the tested representation, but per-step materialization makes decode latency far worse than fp16.

## Recommended next action

Do not write a paper from this run; run one bounded follow-up that implements segmented/fused dequantized attention for the int8/int4 spans and requires at least 50% KV memory reduction with tiered decode latency no worse than 1.25x fp16 at 32768 tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Segmented fused dequant-attention for per-span KV precision tiering
- Success threshold: At 32768 tokens, tiered KV storage at least 50% below fp16, output cosine at least 0.98, and decode latency ratio no worse than 1.25x fp16 over repeated timed reps.
- Stop condition: Stop if segmented/fused tiered attention remains slower than 2x fp16 at 32768 tokens or output cosine falls below 0.98 under the same quantization scheme.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-cascade-compression-per-span-precision-tiering-on-gb10-78a987463ffe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
