# INT4 KV-Cache on CPU with Exact FP16 Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-kv-cache-on-cpu-with-exact-fp16-baseline-3ab3958a0eab`
Run ID: `int4-kv-cache-on-cpu-with-exact-fp16-baseline-3ab3958a0eab-20260628T091455800365+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d2b982979355

## What looked useful

INT4 KV-cache memory savings are real under scale-overhead accounting, but naive CPU unpack/dequantization erases the latency benefit. Future work must fuse packed INT4 consumption into the attention kernel before claiming practical CPU inference benefit.

## Boundaries and scale limits

Synthetic random tensors only; no full language model quality, no fused SIMD kernel, no batching/prefill study, no production serving integration, and sequence length limited to 4096 with heads=8 and head_dim=64.

## Claim scope

On this 8-logical-CPU host, a NumPy one-token decode microbenchmark with synthetic tensors shows packed signed INT4 KV-cache storage with FP16 per-token group scales compresses K/V cache bytes by 3.56x-3.76x versus an exact FP16-cache baseline, but a naive dequantize-then-attend CPU path is 1.72x-2.57x slower and has output relative L2 error of 0.139-0.159.

## Why it stopped

Bounded local evidence is sufficient for an early negative on the naive CPU INT4 KV-cache path, but it is not a full validation of optimized INT4 CPU inference.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should implement a fused/tiled CPU INT4 dequantization-attention kernel and compare it against the same FP16-cache baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU INT4 KV-cache decode kernel versus exact FP16 baseline
- Success threshold: INT4 cache bytes at least 3.5x smaller than FP16, output relative L2 no worse than 0.16, and median INT4 decode latency no more than 1.1x the FP16 baseline at both sequence lengths 2048 and 4096.
- Stop condition: Stop if the fused kernel remains more than 1.5x slower than FP16 at seq_len 2048 after a smoke implementation, or if output relative L2 exceeds 0.20 under the same quantization scheme.

## Evidence references

- Artifact root: `<local-path>/projects/int4-kv-cache-on-cpu-with-exact-fp16-baseline-3ab3958a0eab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
