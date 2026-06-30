# Real training-loop validation for double-buffered CPU-offloaded AdamW

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-training-loop-validation-for-double-buffered-cpu-offl-6e683142bc`
Run ID: `real-training-loop-validation-for-double-buffered-cpu-offl-6e683142bc-20260614T102344263204+0000`

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

- Parent run decision: Paged AdamW with async CPU-RAM offload and double-buffered prefetch: enoch://control-plane/projects/paged-adamw-with-async-cpu-ram-offload-and-double-buffered-prefetch-b44b7eb0cc1b/runs/paged-adamw-with-async-cpu-ram-offload-and-double-buffered-prefetch-b44b7eb0cc1b-20260614T095313460719+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8e64d1d89fb2

## What looked useful

Double-buffered CPU gradient offload improved CPU-offloaded AdamW mean step time by 1.055x over synchronous CPU offload across three seeds, but double-buffered CPU offload was still 1.587x slower than GPU AdamW at this scale.

## Boundaries and scale limits

Only 60-step synthetic teacher-labeled MLP runs across three seeds were tested. No LLM, transformer, distributed, long-duration, memory-pressure, fused CPU optimizer, or discrete PCIe/NVLink validation was performed.

## Claim scope

On GB10 with a 31.6M-parameter synthetic MLP training loop, hook-based double-buffered CPU-offloaded AdamW modestly improves step time versus synchronous CPU-offloaded AdamW while preserving training behavior, but both CPU-offload variants are slower than GPU AdamW.

## Why it stopped

Tier 1 direct validation completed; result is a useful no-paper signal, not full validation, because the mechanism only yields a modest CPU-offload speedup and remains slower than the GPU AdamW baseline.

## Recommended next action

Run one bounded memory-pressure transformer test where GPU AdamW either OOMs or must reduce batch size, and compare effective tokens/s against double-buffered CPU-offloaded AdamW.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Memory-pressure transformer validation for double-buffered CPU-offloaded AdamW
- Success threshold: Double-buffered CPU-offloaded AdamW must either run a target configuration that GPU AdamW cannot run locally, or achieve at least 1.15x effective tokens/s at matched convergence under a documented memory constraint.
- Stop condition: Stop if GPU AdamW runs the target model/batch without memory pressure and remains faster by more than 10%, or if CPU update/parameter-copy overhead prevents at least 0.9x effective tokens/s versus the best feasible GPU baseline.

## Evidence references

- Artifact root: `<local-path>/projects/real-training-loop-validation-for-double-buffered-cpu-offl-6e683142bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
