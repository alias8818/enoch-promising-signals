# TinyOpt: 1-bit Adam + Gradient Checkpointing for <1GB VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tinyopt-1-bit-adam-gradient-checkpointing-for-1gb-vram-training-715f2d14fe3d`
Run ID: `tinyopt-1-bit-adam-gradient-checkpointing-for-1gb-vram-training-715f2d14fe3d-20260619T073126441257+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d9c36983d595

## What looked useful

Optimizer-state compression and activation checkpointing can combine to cross a 1 GiB peak-allocation boundary on a small transformer, but the tested TinyOpt optimizer required a much lower learning rate and converged much more slowly than AdamW in the short probe.

## Boundaries and scale limits

Synthetic data only; 64-step boundary confirmation only; no validation perplexity; no real dataset; PyTorch bool state is one byte per element rather than custom bit-packed state; tested optimizer is a local memory-saving proxy and not the published distributed 1-bit Adam algorithm.

## Claim scope

On a synthetic GPT-style causal language-modeling benchmark on one GB10 CUDA host, a local TinyOpt variant storing sign+scale first moment and fp16 second moment plus activation checkpointing reduced peak CUDA allocation for a 54.8M parameter model from 1141.4 MiB with AdamW+checkpointing to 811.1 MiB, while maintaining decreasing training loss for 64 steps.

## Why it stopped

Proxy/local optimizer evidence supports the memory mechanism but not a paper-ready training-quality claim; this is not a full validation of published 1-bit Adam or long-run language-model training.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should run a TinyOpt learning-rate sweep on a real small language-modeling dataset and compare validation perplexity under the same 1 GiB allocation target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: TinyOpt learning-rate sweep under a 1 GiB transformer-training budget
- Success threshold: At least one TinyOpt+checkpointing run remains below 1024 MiB peak CUDA allocation and reaches validation loss within 10% of the best AdamW baseline at the same parameter scale and token budget.
- Stop condition: Stop if TinyOpt cannot avoid divergence across a 10x learning-rate sweep or remains more than 25% worse in validation loss after the fixed sequence-item budget.

## Evidence references

- Artifact root: `<local-path>/projects/tinyopt-1-bit-adam-gradient-checkpointing-for-1gb-vram-training-715f2d14fe3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
