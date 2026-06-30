# INT8 Activation-Only Training Pass

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-activation-only-training-pass-49adfc9d0ae5`
Run ID: `int8-activation-only-training-pass-49adfc9d0ae5-20260603T232613648951+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/71331c498ab7

## What looked useful

INT8 activation-only storage produced near-identical small-model training metrics to FP32 and high initial gradient cosine (0.999686 mean), while cutting measured activation-cache bytes from 1,572,864 to 393,224 per batch. Naive NumPy quantize/dequantize overhead slowed training to 0.708x FP32 steps/sec.

## Boundaries and scale limits

CPU-only toy MLP proxy; no CUDA/GB10 kernels, no transformer or GPT-2-small-class baseline, no true INT8 matmul, no large-corpus pretraining, and no GPU peak-memory or throughput measurement.

## Claim scope

On a 5-seed NumPy synthetic teacher-student MLP, signed symmetric INT8 activation-only storage with FP32 weights and optimizer preserved validation loss/accuracy within run-to-run noise and reduced activation-cache bytes to about 25% of FP32, but did not improve CPU throughput.

## Why it stopped

Proxy-only useful signal: the mechanism passed a small optimization-tolerance check, but practical claims require direct GPU/transformer evidence.

## Recommended next action

Do not write a paper from this proxy; run a bounded GPU transformer follow-up that measures perplexity, peak activation memory, and throughput against a FP32 baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: INT8 activation-only storage in a bounded transformer training run
- Success threshold: INT8 activation-only final validation perplexity within 2% of FP32, peak activation memory at least 2x lower, and throughput no worse than 10% below FP32 on the same hardware.
- Stop condition: Stop if INT8 activation-only diverges, exceeds 2% validation perplexity degradation after matched compute, fails to reduce measured peak activation memory by at least 2x, or remains more than 10% slower after using an implementation designed to benefit from reduced activation storage.

## Evidence references

- Artifact root: `<local-path>/projects/int8-activation-only-training-pass-49adfc9d0ae5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
