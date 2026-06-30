# Single-GPU ZeRO-1 with unified memory tiering on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `single-gpu-zero-1-with-unified-memory-tiering-on-gb10-3a9e931c23f7`
Run ID: `single-gpu-zero-1-with-unified-memory-tiering-on-gb10-3a9e931c23f7-20260612T030942386119+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b166d9d7a0eb

## What looked useful

Tiered AdamW matched CUDA AdamW within 3.73e-09 max absolute parameter difference in correctness checks. At 268,435,456 fp32 elements, CUDA peak allocation dropped from 5.0 GiB to 2.125 GiB while steady optimizer-step time slowed from 0.1008 s to 0.1853 s. At 1,073,741,824 fp32 elements, CUDA peak allocation dropped from 20.0 GiB to 8.25 GiB while the second optimizer step slowed from 0.4241 s to 0.6980 s.

## Boundaries and scale limits

Evidence is synthetic optimizer-state-only. It does not include transformer training, activation memory, data loading, checkpointing, convergence, gradient accumulation, or distributed ZeRO behavior. Largest tested point was 1,073,741,824 fp32 parameter elements for 2 optimizer steps.

## Claim scope

On a single NVIDIA GB10 using PyTorch 2.12 CUDA 13, a CPU/UMA-resident AdamW moment-state optimizer that stages chunks to CUDA can match torch.optim.AdamW parameter updates on synthetic CUDA tensors while reducing CUDA allocator peak memory for optimizer-state-heavy workloads.

## Why it stopped

This run produced a useful proxy/mechanism result, but it is not full training validation and should not be treated as paper-ready evidence.

## Recommended next action

Run a bounded real transformer training follow-up on GB10 that compares CUDA AdamW versus CPU/UMA-tiered AdamW at matched sequence length, token budget, and loss target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 transformer training with CPU/UMA-tiered AdamW state
- Success threshold: Tiered AdamW trains a real transformer at equal loss quality while either enabling at least 1.5x larger model/batch within GB10 memory or reducing CUDA peak allocation by at least 35%, with end-to-end step time no worse than 2x CUDA AdamW.
- Stop condition: Stop if tiered AdamW cannot run the same transformer workload correctly, if loss diverges relative to CUDA AdamW, or if end-to-end step time exceeds 2x without enabling a larger model or batch.

## Evidence references

- Artifact root: `<local-path>/projects/single-gpu-zero-1-with-unified-memory-tiering-on-gb10-3a9e931c23f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
