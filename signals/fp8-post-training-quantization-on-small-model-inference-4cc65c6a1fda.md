# FP8 post-training quantization on small model inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fp8-post-training-quantization-on-small-model-inference-4cc65c6a1fda`
Run ID: `fp8-post-training-quantization-on-small-model-inference-4cc65c6a1fda-20260610T214451837871+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/9de07b39bdaf

## What looked useful

Simple per-tensor FP8 PTQ with dynamic per-forward activation quantization is quality-tolerable but does not accelerate small-model inference on this GB10 stack. Microbenchmarks show static-input FP8 _scaled_mm can beat BF16 on some OPT-like GEMMs, while dynamic input quantization is slower on every tested shape, explaining the end-to-end loss.

## Boundaries and scale limits

Single small OPT-125M causal LM, WikiText-2 raw test batches, batch-1 prefill only, eager attention, no production serving stack, no decode/KV-cache concurrency test, no fused FP8 activation quantization, and no per-channel or blockwise scale calibration.

## Claim scope

On NVIDIA GB10 with PyTorch 2.12 CUDA 13, cached facebook/opt-125m batch-1 prefill using a naive post-training FP8 wrapper for all nn.Linear layers preserves WikiText perplexity within about 1.3% but is slower than BF16 for sequence lengths 128, 256, 512, and 1024.

## Why it stopped

Bounded direct evidence falsified the practical speedup claim for the tested naive FP8 PTQ implementation: FP8/BF16 latency ratios were 2.156 at seq128, 1.654 at seq256, 1.145 at seq512, and 1.160 at seq1024 despite small perplexity deltas. This is an early scoped falsification, not a full validation of all FP8 inference methods.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next bounded test is a fused/static-activation FP8 path for OPT-125M prefill that removes dynamic quantization from the timed loop and must beat BF16 end-to-end at sequence lengths 512 and 1024 while keeping perplexity ratio below 1.02.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused or static-activation FP8 PTQ path for OPT-125M prefill on GB10
- Success threshold: FP8/BF16 mean latency ratio below 0.90 at both sequence lengths 512 and 1024, replacement coverage at least the same 73 linear layers, and FP8/BF16 perplexity ratio below 1.02 on the same cached WikiText evaluation setup.
- Stop condition: Stop if the fused/static path cannot replace all OPT-125M linear layers, if perplexity ratio is at or above 1.02, or if FP8 latency is not at least 10% faster than BF16 at both target sequence lengths.

## Evidence references

- Artifact root: `<local-path>/projects/fp8-post-training-quantization-on-small-model-inference-4cc65c6a1fda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
