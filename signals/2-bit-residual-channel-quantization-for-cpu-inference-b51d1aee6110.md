# 2-bit Residual Channel Quantization for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-residual-channel-quantization-for-cpu-inference-b51d1aee6110`
Run ID: `2-bit-residual-channel-quantization-for-cpu-inference-b51d1aee6110-20260619T093312385960+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/38be93e803b3

## What looked useful

Residual-channel correction improved output relative MSE over plain q2 by 1.26x-1.30x at 2.5 bits/weight and 1.72x-1.85x at a 3.0 bits/weight budget, but it remained 3.06x-4.20x worse than simple q3 at the same 3.0 bits/weight budget.

## Boundaries and scale limits

Synthetic weights/activations only; no real transformer layers, no packed int2 CPU decode kernel, no perplexity/task accuracy, no end-to-end token latency, and no metadata/cache overhead accounting beyond nominal bits per weight.

## Claim scope

Bounded synthetic CPU NumPy mechanism probe of row-wise 2-bit residual-channel weight quantization on 1024x1024 and 2048x2048 dense matrices, comparing output relative MSE and dequantized float32 matmul proxy timing against plain q2 and q3 baselines.

## Why it stopped

Proxy early falsification of the practical viability claim: the mechanism helps versus q2 but fails an equal-bit q3 control on synthetic CPU probes, so it is not paper-positive or deployment-ready from this evidence.

## Recommended next action

Stop this run as a no-paper useful signal; if pursued, run a bounded real-layer follow-up with activation-weighted channel selection and a packed-kernel or decode-cost model before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-weighted residual-channel quantization on real transformer layers
- Success threshold: At equal nominal bits/weight, residual-channel quantization must reduce output relative MSE by at least 20% versus q3 on most tested layers while adding no more than 10% CPU decode/matmul latency.
- Stop condition: Stop if activation-weighted residual channels remain worse than q3 by more than 10% output relative MSE on a majority of real layers or require metadata/decode overhead that removes any storage/latency advantage.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-residual-channel-quantization-for-cpu-inference-b51d1aee6110`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
