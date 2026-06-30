# INT4 weight-only quantization for CPU inference with quality ceiling test

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-weight-only-quantization-for-cpu-inference-with-quality-ceiling-test-2b2987752033`
Run ID: `int4-weight-only-quantization-for-cpu-inference-with-quality-ceiling-test-2b2987752033-20260611T192055851647+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ee1613732b9e

## What looked useful

Naive CPU INT4 weight-only inference should not be expected to speed up inference merely from packed weights; without a fused low-bit matmul kernel, unpack/dequant overhead dominated and produced only 0.253x-0.304x of FP32 speed in the medium grid, while storage improved to 0.133x-0.156x of FP32 and median logit NRMSE was 0.117.

## Boundaries and scale limits

Synthetic projection-only NumPy test; no pretrained LLM checkpoint, no text-corpus perplexity, no fused low-bit CPU kernel, no end-to-end serving stack, and no 7B+ model validation.

## Claim scope

For 2048x2048 synthetic model-like linear projections on CPU, packed symmetric INT4 groupwise weight-only storage reduced weight memory to about 13.3-15.6% of FP32 and preserved coarse FP32 teacher logits, but a naive unpack/dequantize-to-float32-then-BLAS-matmul inference path was consistently slower than FP32 matmul.

## Why it stopped

Proxy/early falsification: the tested dequantize-then-matmul INT4 weight-only CPU path was slower than FP32 in every medium trial, so it is not a viable speed path without a fused low-bit kernel.

## Recommended next action

Stop this run as a proxy/early falsification of the naive CPU path; the next bounded direct test should use a fused INT4 CPU kernel on a small pretrained language model and compare tokens/sec plus perplexity against FP32/BF16.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused INT4 CPU kernel quality-speed test on a small pretrained language model
- Success threshold: INT4 fused CPU path is at least 1.25x faster than FP32/BF16 at equal batch/sequence settings while perplexity or NLL is no more than 5% worse and memory is at least 3x lower.
- Stop condition: Stop if the fused path is not faster than FP32/BF16 on the small model or if perplexity/NLL degradation exceeds 5% on the corpus slice.

## Evidence references

- Artifact root: `<local-path>/projects/int4-weight-only-quantization-for-cpu-inference-with-quality-ceiling-test-2b2987752033`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
