# CPU-Offloaded GaLore for GPT-2 Small Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-galore-for-gpt-2-small-pretraining-a434b9c79dbb`
Run ID: `cpu-offloaded-galore-for-gpt-2-small-pretraining-a434b9c79dbb-20260603T164914213575+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/613211601a03

## What looked useful

Dense AdamW moments for the covered GPT-2-small matrices require 948.475 MiB, while GaLore projected state plus basis requires 4.823 MiB at rank 4, 9.646 MiB at rank 8, 19.291 MiB at rank 16, and 38.582 MiB at rank 32. Random-gradient reconstruction error remains high, so the memory result is useful but not enough for a pretraining claim.

## Boundaries and scale limits

No GPU offload path, no actual GPT-2-small pretraining, no language-model loss or perplexity, and no real-gradient spectra were measured. Random-gradient reconstruction error is a pessimistic proxy and cannot validate convergence quality.

## Claim scope

CPU-only proxy measurements for GPT-2-small-shaped matrices show large optimizer-state memory savings for GaLore-style low-rank projected Adam moments, with ranks 4-16 faster than dense CPU Adam update in this benchmark and rank 32 slower.

## Why it stopped

This run is a CPU proxy/useful-signal result rather than full validation; it supports memory feasibility but does not establish GPT-2-small pretraining quality.

## Recommended next action

Run a bounded real-gradient mini-GPT or GPT-2-small subset experiment with dense AdamW versus CPU-offloaded GaLore, recording loss/perplexity, gradient spectra, tokens/sec, memory, and transfer overlap on a GPU-capable worker.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-gradient CPU-offloaded GaLore test for mini-GPT/GPT-2-small
- Success threshold: At rank 8 or 16, GaLore reaches within 5% of dense AdamW validation loss/perplexity over the bounded run while reducing optimizer-state memory by at least 40x and avoiding more than 25% throughput loss.
- Stop condition: Stop if rank 16 captures less than 80% gradient spectral energy in core projection layers for repeated checkpoints or if bounded loss diverges by more than 10% versus dense AdamW after the warmup window.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-galore-for-gpt-2-small-pretraining-a434b9c79dbb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
