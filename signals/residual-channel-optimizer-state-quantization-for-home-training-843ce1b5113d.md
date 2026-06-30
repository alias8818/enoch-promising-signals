# Residual-Channel Optimizer State Quantization for Home Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `residual-channel-optimizer-state-quantization-for-home-training-843ce1b5113d`
Run ID: `residual-channel-optimizer-state-quantization-for-home-training-843ce1b5113d-20260528T044813287825+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4a9b5300cb31

## What looked useful

Plain int8 moment storage reduced optimizer state to 25.6% of AdamW and achieved mean validation loss 1.8971. The residual-channel variant used 31.9% of AdamW state, ran 1.40x slower than plain int8, and had worse mean validation loss at 1.9033. The tested residual-channel addition is not justified unless a future setting first shows plain int8 optimizer state failing.

## Boundaries and scale limits

This run did not test GPT-2-small-class models, long-horizon pretraining, production fused quantized optimizer kernels, memory-pressure training near GB10 capacity, or alternative residual-channel policies and fractions.

## Claim scope

On a 421,697-parameter Tiny Shakespeare character GPT trained for 3000 CUDA steps across three seeds, keeping 6.25% high-second-moment output channels as fp32 residual optimizer state did not improve over plain per-channel int8 Adam moments.

## Why it stopped

Medium local GPU proxy falsified the tested mechanism rather than providing full-scale validation: residual-channel state added memory and runtime overhead and did not beat the simpler int8 baseline.

## Recommended next action

Stop this project as a bounded local negative/useful-signal result; do not scale residual-channel optimizer state quantization until a task is found where plain int8 optimizer states degrade convergence.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-optimizer-state-quantization-for-home-training-843ce1b5113d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
