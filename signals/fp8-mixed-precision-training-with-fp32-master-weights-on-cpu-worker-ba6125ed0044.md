# FP8 mixed-precision training with FP32 master weights on CPU worker

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fp8-mixed-precision-training-with-fp32-master-weights-on-cpu-worker-ba6125ed0044`
Run ID: `fp8-mixed-precision-training-with-fp32-master-weights-on-cpu-worker-ba6125ed0044-20260610T102800436544+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f080886e20ca

## What looked useful

FP32 master weights appear important for preserving training dynamics under FP8 fake quantization, but CPU-emulated FP8 is not a practical speed path: fp8_master reached 0.99349 mean validation accuracy versus 0.99447 for FP32, but only 13.55% of FP32 throughput.

## Boundaries and scale limits

Toy synthetic classification only; FP8 was emulated and dequantized to FP32 for matmul, not packed or natively accelerated. No large model, real dataset, gradient quantization, optimizer-state quantization, native FP8 CPU kernel, or long-run stability evidence was produced.

## Claim scope

On a CPU-only NumPy 2-64-64-3 MLP trained for 50 epochs on a synthetic 3-class spiral task, per-tensor E4M3-style fake FP8 activations and weights with FP32 master weights preserved validation accuracy within 0.001 absolute of FP32, while destructive no-master FP8 rounding degraded loss and accuracy.

## Why it stopped

Bounded CPU proxy supports the FP32-master mechanism but does not validate native FP8 CPU performance or large-model training; emulated FP8 was substantially slower than FP32.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded deepen test should use a real small dataset/model and include gradient/optimizer-state quantization ablations before any scale claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small real-task FP8 master-weight training with gradient quantization ablations
- Success threshold: FP8-master final validation metric within 1% relative of FP32 on all seeds, while no-master or gradient-quantized variants identify a reproducible boundary or failure mode.
- Stop condition: Stop if FP8-master loses more than 3% relative validation quality versus FP32 on two of three seeds, diverges, or remains slower than FP32 with no new stability insight.

## Evidence references

- Artifact root: `<local-path>/projects/fp8-mixed-precision-training-with-fp32-master-weights-on-cpu-worker-ba6125ed0044`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
