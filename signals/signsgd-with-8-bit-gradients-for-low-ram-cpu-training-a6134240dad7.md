# SignSGD with 8-bit Gradients for Low-RAM CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `signsgd-with-8-bit-gradients-for-low-ram-cpu-training-a6134240dad7`
Run ID: `signsgd-with-8-bit-gradients-for-low-ram-cpu-training-a6134240dad7-20260525T132711129632+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ee1b9b06ebf8

## What looked useful

Gradient compression is a real low-RAM mechanism on CPU, but naive 8-bit gradient quantization can be throughput-negative, and sign-only updates require additional tuning before they are a viable replacement for standard gradients.

## Boundaries and scale limits

Synthetic convex objective only; no neural backprop, activation memory, minibatch stochasticity, dataloader memory, validation quality, transformer-scale model, or long training run was tested.

## Claim scope

On a 20M-parameter dense convex CPU proxy, int8 gradient storage reduced gradient-buffer memory by 4x and full-process peak RSS by 24.7% versus fp32 SGD while preserving final loss, but the naive implementation was 5.08x slower. SignSGD removed the gradient buffer and reduced peak RSS by 33.0%, but did not match fp32 convergence in the tested 100-step budget.

## Why it stopped

Proxy evidence supports the memory mechanism but not a publication-grade low-RAM CPU training claim; naive int8 gradients had a 5.08x CPU slowdown and signSGD under-converged in the tested budget.

## Recommended next action

Stop this run as no-paper useful signal; next bounded evidence should be a real small neural training benchmark with fused or blockwise int8-gradient production and measured peak RSS, validation quality, and wall-clock against fp32.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Neural Benchmark for Fused Int8 Gradients and SignSGD
- Success threshold: At least 20% lower peak RSS than fp32 with final validation metric within 2% relative of fp32 and wall-clock no worse than 1.5x fp32 on the same CPU host.
- Stop condition: Stop as negative if the real neural benchmark either loses more than 2% relative validation quality or remains slower than 1.5x fp32 after a fused/blockwise implementation.

## Evidence references

- Artifact root: `<local-path>/projects/signsgd-with-8-bit-gradients-for-low-ram-cpu-training-a6134240dad7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
