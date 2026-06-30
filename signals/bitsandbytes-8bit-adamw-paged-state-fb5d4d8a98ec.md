# bitsandbytes-8bit-AdamW-paged-state

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bitsandbytes-8bit-adamw-paged-state-fb5d4d8a98ec`
Run ID: `bitsandbytes-8bit-adamw-paged-state-fb5d4d8a98ec-20260619T143043838444+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f8d67d49d54

## What looked useful

PagedAdamW8bit reproduced the expected mechanism: 33,554,432 fp32 parameters used 65.00 MiB of 8-bit optimizer state, with large state1/state2 tensors on CPU and only quantization metadata on CUDA; Torch allocated after step was 129.00 MiB versus 193.00 MiB for non-paged AdamW8bit and 384.00 MiB for torch AdamW.

## Boundaries and scale limits

Synthetic optimizer-state/update probe only; no end-to-end model training, convergence, checkpoint/reload, distributed, dataloader, activation-memory, or long-run memory-pressure validation. GB10 nvidia-smi does not expose memory usage, so evidence relies on Torch allocator counters and tensor device/dtype inspection.

## Claim scope

On this GB10 worker with torch 2.12.0+cu130 and bitsandbytes 0.49.2, synthetic one-parameter CUDA optimizer probes show PagedAdamW8bit stores AdamW moment state at about 2.03 bytes per parameter and moves the large quantized moment tensors off CUDA allocation, reducing persistent Torch CUDA allocation versus non-paged AdamW8bit and torch AdamW.

## Why it stopped

The run produced a reproducible synthetic mechanism signal, but the feature already exists publicly in bitsandbytes/QLoRA practice and the evidence is not direct model-training validation.

## Recommended next action

Stop this run as no-paper useful evidence; the bounded next test is a real GPT-2-small-class or LoRA training comparison with peak memory, throughput, validation loss, and checkpoint/reload checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PagedAdamW8bit real-training memory and convergence check
- Success threshold: PagedAdamW8bit reduces peak/persistent CUDA allocation by at least 20% versus AdamW8bit or enables a batch/sequence setting that torch AdamW cannot run, while final validation loss remains within 2% of the best baseline over the bounded run and checkpoint resume succeeds.
- Stop condition: Stop if PagedAdamW8bit fails to train/resume, is slower by more than 50% without enabling a larger feasible setting, or validation loss diverges by more than 2% versus AdamW8bit in the bounded task.

## Evidence references

- Artifact root: `<local-path>/projects/bitsandbytes-8bit-adamw-paged-state-fb5d4d8a98ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
