# Quantization cascade: input-difficulty router over fp16/int8/int4 8B on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantization-cascade-input-difficulty-router-over-fp16-int8-int4-8b-on-gb10-d3c35105c3c2`
Run ID: `quantization-cascade-input-difficulty-router-over-fp16-int8-int4-8b-on-gb10-d3c35105c3c2-20260621T165223337094+0000`

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

Direct low-precision 7B Q4 inference on GB10 is viable, but a naive input-difficulty cascade is not supported: int8/int4 dequantization paths were about 0.22x fp16 speed in the proxy, int4 relative RMSE stayed near 15.7% across easy/medium/hard inputs, and the score-threshold router was only 0.285x all-fp16 speed.

## Boundaries and scale limits

The full matched Q4/Q8/f16 7B GGUF quality router suite did not run because Q8/f16 downloads did not complete. The fp16/int8/int4 cascade evidence is projection-level and synthetic, not full LLM answer quality.

## Claim scope

On this GB10 host, Qwen2.5-7B Q4_K_M runs through a locally built CUDA llama.cpp at 2548.5 prompt tok/s and 44.85 generation tok/s. A transformer-sized PyTorch CUDA proxy for fp16/int8/int4 routing showed that naive dequantize-then-matmul int8/int4 branches were slower than fp16 and that the tested input outlier score did not make int4 error acceptable on easy cases.

## Why it stopped

Early proxy falsification of the naive cascade economics plus incomplete matched Q8/f16 direct evidence; this is not a full validation of all possible optimized routers.

## Recommended next action

Stop this run as a no-paper useful signal; only revisit with matched Q4/Q8/f16 7B variants already cached and optimized fused quantized kernels available.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched GGUF Q4/Q8/f16 difficulty-router quality and latency suite on GB10
- Success threshold: Router accuracy within 1 percentage point of all-f16 on the scoped known-answer suite and at least 20% lower mean latency or 20% higher throughput after switching overhead.
- Stop condition: Stop if Q4/Q8 accuracy is not difficulty-separable, if model switching overhead erases latency gains, or if optimized quantized kernels do not outperform f16 on GB10.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-cascade-input-difficulty-router-over-fp16-int8-int4-8b-on-gb10-d3c35105c3c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
