# Block-wise 8-bit AdamW for GPT-2-small CPU pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `block-wise-8-bit-adamw-for-gpt-2-small-cpu-pretraining-878786035154`
Run ID: `block-wise-8-bit-adamw-for-gpt-2-small-cpu-pretraining-878786035154-20260604T014503683402+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/91e01e9fca96

## What looked useful

The memory-saving mechanism works, but the simple block-wise 8-bit AdamW formulation fails an early fidelity/performance screen: full GPT-2-small-shaped two-step proxy saw 3.94x-4.00x state-memory reduction, 2.26x-2.76x slower optimizer updates, and 3.24-4.43 max relative RMS update error after quantized state reuse.

## Boundaries and scale limits

No end-to-end GPT-2-small pretraining, real-token loss curve, perplexity, or real-gradient distribution was tested. Evidence is direct for optimizer-state memory, update fidelity, and CPU update time on GPT-2-small-shaped tensors only.

## Claim scope

On a NumPy CPU optimizer proxy using GPT-2-small parameter shapes and deterministic synthetic gradients, simple block-wise 8-bit quantization of both AdamW moment buffers yields about 4x optimizer-state memory reduction but is not viable as a drop-in CPU pretraining optimizer because quantized moment reuse causes large update error and CPU optimizer updates are slower than fp32 AdamW.

## Why it stopped

Proxy early falsification: the tested block-wise 8-bit AdamW state design saves memory but immediately produces large second-step update error and slower CPU optimizer updates on GPT-2-small-shaped tensors, so it is not worth scaling as-is.

## Recommended next action

Stop this simple variant as a proxy early falsification; only continue with a bounded follow-up that tests stabilized second-moment quantization or mixed-precision moment state before any full pretraining run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized second-moment quantization for CPU AdamW
- Success threshold: At least 2x optimizer-state memory reduction versus fp32 AdamW, no more than 1.25x CPU optimizer-step slowdown, and max relative RMS update error below 0.05 across 10 GPT-2-small-shaped proxy steps.
- Stop condition: Stop if relative RMS update error remains above 0.1 after stabilized second-moment quantization, or if CPU optimizer-step time remains above 1.5x fp32 AdamW.

## Evidence references

- Artifact root: `<local-path>/projects/block-wise-8-bit-adamw-for-gpt-2-small-cpu-pretraining-878786035154`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
