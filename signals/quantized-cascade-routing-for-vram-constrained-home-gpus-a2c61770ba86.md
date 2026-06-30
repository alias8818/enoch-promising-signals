# Quantized cascade routing for VRAM-constrained home GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-cascade-routing-for-vram-constrained-home-gpus-a2c61770ba86`
Run ID: `quantized-cascade-routing-for-vram-constrained-home-gpus-a2c61770ba86-20260614T085101396345+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c4452a202ca9

## What looked useful

Quantized expert storage is a real resident-memory lever, but the simple home-GPU implementation tested here is a poor latency tradeoff: in the memory-pressure run, resident weights fell from 1024.3 MiB to 512.6 MiB while top-k 1 latency rose from 6.85 ms routed fp16 to 19.73 ms routed int8 and peak allocation rose by 81.2 MiB.

## Boundaries and scale limits

Synthetic MLP experts only; no real language-model quality metric, no KV-cache behavior, no production serving stack, and no fused int8 GEMM or optimized quantized inference kernel.

## Claim scope

On NVIDIA GB10 with PyTorch 2.12 CUDA, synthetic routed expert MLPs stored as int8+scale cut resident expert weight memory by about 2x versus fp16 storage, but naive dequantize-on-use routing was slower than routed fp16 and increased transient peak allocation.

## Why it stopped

Proxy systems benchmark found a mixed mechanism: memory savings were confirmed, but naive quantized cascade routing failed the practical latency and transient-memory test; this is not full LLM validation.

## Recommended next action

Stop this run as a useful-signal negative; the next bounded test should replace dequantize-on-use with fused or cached quantized expert execution and require latency parity with routed fp16 while preserving about 2x resident memory savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused or cached quantized expert execution for routed home-GPU cascades
- Success threshold: For the 16-expert memory-pressure case, quantized routed top-k 1 mean latency <= 1.10x routed fp16, resident expert memory <= 0.55x fp16, peak allocation <= 1.10x routed fp16, and MAE versus routed fp16 <= 0.01.
- Stop condition: Stop if fused/cached quantized execution still exceeds routed fp16 latency by more than 25% or raises peak allocation above routed fp16 by more than 25% on the calibrated memory-pressure benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-cascade-routing-for-vram-constrained-home-gpus-a2c61770ba86`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
