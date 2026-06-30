# Tiny LoRA with Frozen Optimizer State for CPU Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-lora-with-frozen-optimizer-state-for-cpu-workers-8cee8392aead`
Run ID: `tiny-lora-with-frozen-optimizer-state-for-cpu-workers-8cee8392aead-20260611T214859499757+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1e9ada20720b

## What looked useful

Frozen optimizer state is mechanically viable for tiny LoRA in a controlled low-rank adapter problem and can sharply reduce optimizer-state footprint/write traffic, but it did not improve wall-clock speed in the NumPy harness and is warmup-sensitive.

## Boundaries and scale limits

Synthetic linear task only; no transformer, language-model loss, real dataset, hardware counter, or production CPU-worker throughput measurement. The method diverged when the variance preconditioner was frozen after only 10 warmup steps.

## Claim scope

In a CPU-only NumPy low-rank teacher/student linear adaptation with frozen base weights, a LoRA adapter trained with a warmed then frozen Adam variance preconditioner reached low validation error while using half the optimizer-state bytes of LoRA AdamW and no post-warmup optimizer-state writes.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is insufficient for a paper or practical CPU-worker speedup claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a CPU tiny-transformer LoRA validation-loss experiment with measured wall-clock and memory/write-profile counters.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer LoRA with Frozen Adam Variance on CPU
- Success threshold: Frozen-variance LoRA reaches validation loss within 5% of AdamW, uses at most 60% of AdamW optimizer-state memory, and shows a measurable reduction in optimizer-state write traffic without divergence across three seeds.
- Stop condition: Stop if frozen-variance LoRA diverges or exceeds AdamW validation loss by more than 20% under two reasonable warmup/learning-rate settings.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-lora-with-frozen-optimizer-state-for-cpu-workers-8cee8392aead`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
