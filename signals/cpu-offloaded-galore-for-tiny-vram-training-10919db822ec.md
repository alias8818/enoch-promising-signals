# CPU-Offloaded GaLore for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-galore-for-tiny-vram-training-10919db822ec`
Run ID: `cpu-offloaded-galore-for-tiny-vram-training-10919db822ec-20260531T170213644309+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4916619d362f

## What looked useful

Stable low-rank CPU moments reduced optimizer-state storage by 87-97% at ranks 16-64 but recovered only 13-42% of AdamW's validation-loss improvement; rank 128 recovered 80% but reduced state by only 50%. A changing projection basis with stale moments was clearly poor.

## Boundaries and scale limits

No GPU/GB10 run, no real accelerator memory telemetry, no CPU-GPU transfer measurement, no external dataset, no GPT-2-small-class baseline, and only 48-step toy training runs.

## Claim scope

CPU-only synthetic tiny-token benchmark of CPU-resident low-rank GaLore-style Adam moments versus AdamW, with optimizer-state memory accounting and fixed validation batches.

## Why it stopped

This run is a CPU/proxy useful signal, not direct validation; low-rank settings that preserve the strongest memory savings underperform AdamW too much on the toy task.

## Recommended next action

Run a bounded GB10/GPU follow-up with real memory telemetry on a GPT-2-small-class or parameter-matched language-model task before making any tiny-VRAM training claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 tiny-VRAM CPU-offloaded GaLore validation
- Success threshold: At least 90% of AdamW validation-loss improvement at equal steps, at least 50% reduction in accelerator-resident optimizer state, and no more than 25% throughput slowdown on a configuration where memory pressure matters.
- Stop condition: Stop if no rank/projection-gap setting reaches 75% of AdamW validation-loss improvement within the bounded run or if CPU-offload overhead exceeds 2x step time before achieving a memory-fit advantage.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-galore-for-tiny-vram-training-10919db822ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
