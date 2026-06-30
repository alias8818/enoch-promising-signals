# CPU-Offloaded Adam with Async Prefetch Pipeline for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-adam-with-async-prefetch-pipeline-for-tiny-vram-training-2cc1a4d37c54`
Run ID: `cpu-offloaded-adam-with-async-prefetch-pipeline-for-tiny-vram-training-2cc1a4d37c54-20260529T121521004697+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4f1f5c340728

## What looked useful

Async prefetch is a small real win for streamed weights, but by itself is insufficient to make CPU-offloaded Adam practical; CPU Adam bandwidth is the main risk and must be overlapped with backward compute or reduced with a lower-traffic optimizer.

## Boundaries and scale limits

No full autograd training, no convergence measurement, no explicit discrete VRAM OOM test because GB10 exposes large UMA memory and nvidia-smi reports memory as not supported. Results cover synthetic layer streaming and optimizer update bandwidth up to 134M streamed fp16 weights and 64M fp32 Adam parameters.

## Claim scope

Bounded GB10 synthetic mechanism benchmark: two-slot async CPU-to-GPU streamed-weight prefetch improved medium tensor forward proxies by 3.3-4.2%, but CPU-resident Adam updates for 32M-64M parameters were 1.6-2.3x slower than the same vectorized update on CUDA and dominated the measured proxy step cost.

## Why it stopped

Proxy evidence is mixed and insufficient for a paper-positive claim: async prefetch helps only 3-4%, while non-overlapped CPU Adam dominates step cost.

## Recommended next action

Stop this project as a no-paper useful signal; only continue via a bounded follow-up that implements real layerwise backward hooks and measures whether CPU Adam plus gradient transfer can be hidden under GPU backward compute.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layerwise Backward Overlap for CPU-Offloaded Adam
- Success threshold: At 32M-100M parameters, CPU-offloaded Adam with overlapped backward is within 15% of GPU Adam step time while reducing GPU optimizer-state residency by at least 2x and matching loss over a short controlled run.
- Stop condition: Stop if overlapped CPU Adam remains more than 30% slower than GPU Adam after eliminating obvious synchronization bugs, or if memory accounting shows the method cannot keep optimizer state off GPU.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-adam-with-async-prefetch-pipeline-for-tiny-vram-training-2cc1a4d37c54`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
