# GaLore vs 8-bit AdamW vs Adafactor: optimizer memory under 6GB VRAM GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `galore-vs-8-bit-adamw-vs-adafactor-optimizer-memory-under-6gb-vram-gpt-2-small-54940e31da88`
Run ID: `galore-vs-8-bit-adamw-vs-adafactor-optimizer-memory-under-6gb-vram-gpt-2-small-54940e31da88-20260621T005732138813+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b61001e528d9

## What looked useful

For GPT-2 small with tied LM head, estimated persistent optimizer state is 237.814 MiB for 8-bit AdamW, 1.227 MiB for Adafactor without first moment, 308.150-409.400 MiB for GaLore ranks 8-128 targeting non-embedding matrices, and 10.806-159.005 MiB for GaLore ranks 8-128 targeting all matrices. Optimizer state alone is far below 6 GiB in all tested profiles.

## Boundaries and scale limits

No CUDA-visible GPU, no PyTorch runtime, no training-step peak memory telemetry, and no activation/gradient/checkpointing/allocator-fragmentation measurement.

## Claim scope

Analytical persistent optimizer-state memory for GPT-2 small parameter shapes under a 6 GiB threshold; not measured CUDA VRAM.

## Why it stopped

Bounded analytical proxy supports the optimizer-state-only mechanism but cannot validate the broader VRAM claim without a CUDA-visible training run.

## Recommended next action

Stop this run as no-paper useful signal; run a CUDA follow-up measuring peak allocated/reserved VRAM over real GPT-2-small training steps for the three optimizers if direct VRAM validation is required.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measured CUDA peak VRAM for GPT-2 small optimizer comparison
- Success threshold: Each optimizer completes the same calibrated GPT-2-small training step workload with peak reserved VRAM below 6 GiB and no optimizer-specific OOM.
- Stop condition: Stop after any optimizer repeatedly OOMs below the common workload target or after all three produce peak VRAM metrics for the calibrated workload.

## Evidence references

- Artifact root: `<local-path>/projects/galore-vs-8-bit-adamw-vs-adafactor-optimizer-memory-under-6gb-vram-gpt-2-small-54940e31da88`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
