# Pure PyTorch 8-bit Block-wise AdamW for CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pure-pytorch-8-bit-block-wise-adamw-for-cpu-250ea26310ba`
Run ID: `pure-pytorch-8-bit-block-wise-adamw-for-cpu-250ea26310ba-20260525T015641074514+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/dc70f9f6e915

## What looked useful

The memory mechanism works and small-block quantization can preserve training behavior on a bounded task, but large blocks diverged and the pure PyTorch update path was about 3.6x slower than AdamW on a 1M-parameter vector.

## Boundaries and scale limits

Evidence is limited to synthetic CPU regression, random-gradient vector fidelity, and 1M-parameter optimizer-step probes under 10 seconds; no real model, large model, memory-pressure, robustness, or fused-kernel validation was run.

## Claim scope

A pure PyTorch CPU 8-bit block-wise AdamW implementation with 256-value blocks reduced measured optimizer-state memory to about 25.4% of PyTorch AdamW and matched AdamW final loss on a small synthetic 33k-parameter regression MLP across three seeds, but was slower than AdamW in optimizer-step throughput.

## Why it stopped

No-paper closure: this worker produced a bounded useful signal, but evidence remains synthetic/small-scale and pure PyTorch speed is not competitive.

## Recommended next action

Run a bounded direct small-transformer or real-dataset CPU training comparison with block sizes 64/128/256, AdamW, and a mechanism diagnostic for second-moment quantization underflow before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small real-model validation of pure PyTorch 8-bit block AdamW
- Success threshold: At least one 8-bit block size reaches validation loss within 2% of AdamW over three seeds, reduces optimizer-state bytes by at least 3.5x, and has no repeated loss spikes attributable to quantization underflow.
- Stop condition: Stop if all 8-bit block sizes miss AdamW validation loss by more than 5%, show repeated divergence/loss spikes, or remain slower by more than 3x without a memory-pressure benefit.

## Evidence references

- Artifact root: `<local-path>/projects/pure-pytorch-8-bit-block-wise-adamw-for-cpu-250ea26310ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
