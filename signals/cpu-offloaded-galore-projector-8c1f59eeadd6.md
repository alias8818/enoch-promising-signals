# CPU-Offloaded GaLore Projector

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-galore-projector-8c1f59eeadd6`
Run ID: `cpu-offloaded-galore-projector-8c1f59eeadd6-20260601T101050867863+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1969124219c8

## What looked useful

Randomized CPU projector construction appears cheap enough to justify a bounded direct single-GPU/GB10 follow-up for GPT-2-small-class training, but exact SVD is substantially slower and the current run cannot validate end-to-end optimizer viability.

## Boundaries and scale limits

CPU-only synthetic-gradient benchmark; no GPU transfer/overlap measurement, no PyTorch optimizer integration, no real training loss or convergence evidence, and no large-model validation.

## Claim scope

On a CPU worker, NumPy randomized GaLore-style right-projector construction for synthetic transformer-like gradient matrices up to 4096x1024 took 0.021-0.427 s per refresh and amortized to 0.21-4.27 ms/step at refresh period 100, while estimated low-rank optimizer-state savings were 58.3-92.2%.

## Why it stopped

Stopped after a bounded proxy/mechanism benchmark; the result is useful but not direct training validation and not paper-ready.

## Recommended next action

Run a bounded single-GPU PyTorch follow-up that compares dense AdamW, GPU-resident GaLore, and CPU-offloaded randomized-projector GaLore on GPT-2-small-class training with measured step time, memory, transfer stalls, and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Single-GPU direct validation of CPU-offloaded randomized GaLore projectors
- Success threshold: CPU-offloaded GaLore must retain at least 80% of the dense-to-GaLore memory reduction, stay within 10% of GPU-resident GaLore throughput, and match GPU-resident GaLore validation loss within run-to-run noise over the bounded training budget.
- Stop condition: Stop if transfer/synchronization stalls exceed 10% of step time for two tested ranks or validation loss degrades clearly versus GPU-resident GaLore at matched settings.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-galore-projector-8c1f59eeadd6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
