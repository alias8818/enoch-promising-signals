# 1-bit Adam with CPU offload for GPT-2-small on 10GB GPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `1-bit-adam-with-cpu-offload-for-gpt-2-small-on-10gb-gpu-e4bc6406eda7`
Run ID: `1-bit-adam-with-cpu-offload-for-gpt-2-small-on-10gb-gpu-e4bc6406eda7-20260529T112033312940+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e8d22261cc54

## What looked useful

Standard GPU AdamW already fit tested GPT-2-small batch 1 seq 64 and batch 4 seq 512 cases below 10 GB peak CUDA allocation. At batch 8 seq 1024, all optimizers peaked at about 12.020 GB CUDA allocation, so activation/logit memory, not optimizer state, set the 10 GB boundary. 1-bit-style state reduced logical CPU optimizer state to about 0.016 GB but did not reduce the stress-point CUDA allocation.

## Boundaries and scale limits

Synthetic data only; short step counts only; no validation loss; no real corpus; no hard 10 GB device cap; 1-bit state uses a concrete proxy optimizer and PyTorch bool storage rather than a packed/fused production implementation.

## Claim scope

Bounded synthetic GPT-2-small-class CUDA step benchmarks on GB10 show that CPU optimizer-state offload and a sign/scale 1-bit-style moment state reduce optimizer-state memory, but do not provide a standalone path to fit larger GPT-2-small training configurations under a 10 GB CUDA allocated-memory budget.

## Why it stopped

Proxy synthetic evidence falsifies the standalone memory claim: optimizer-state offload helps small/moderate settings that already fit under 10 GB, while the larger 10 GB stress point remains activation/logit dominated and above budget for every optimizer.

## Recommended next action

Stop this standalone optimizer-offload idea as no-paper useful signal; any next investigation should target activation/logit memory first, then retest packed optimizer state only as a secondary lever.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-adam-with-cpu-offload-for-gpt-2-small-on-10gb-gpu-e4bc6406eda7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
