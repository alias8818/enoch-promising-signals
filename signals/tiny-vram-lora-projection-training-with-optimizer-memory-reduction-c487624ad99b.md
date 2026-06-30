# Tiny-VRAM LoRA Projection Training with Optimizer Memory Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-vram-lora-projection-training-with-optimizer-memory-reduction-c487624ad99b`
Run ID: `tiny-vram-lora-projection-training-with-optimizer-memory-reduction-c487624ad99b-20260611T152329791013+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/cad2ec9c2531

## What looked useful

Naive global random projection of LoRA factors is not a promising tiny-VRAM optimizer-state reduction mechanism: 50% latent width halves Adam state but produced validation MSE 0.59677 versus 0.0000664 for standard LoRA at 360 steps, and the best 720-step projected learning-rate sweep remained 75.6x worse than standard.

## Boundaries and scale limits

CPU-only NumPy toy benchmark; no transformer stack, no real dataset, no GPU/VRAM allocator telemetry, no mixed precision or quantized base model, and no comparison to production memory-saving optimizers such as 8-bit Adam.

## Claim scope

On a synthetic low-rank linear adaptation task with 384x384 weights and LoRA rank 12, an implicit signed-hash projection of the full LoRA parameter vector reduces Adam optimizer-state floats linearly with latent width but fails to preserve standard LoRA training quality.

## Why it stopped

Proxy early falsification: optimizer-state memory reduction was directly accounted for, but trainability failed badly on a synthetic task that standard LoRA solved; this is not full transformer validation.

## Recommended next action

Stop this naive global projection path; if continuing locally, test a structured projection that preserves separate A/B factor geometry and compare it against standard LoRA plus 8-bit Adam on a small transformer task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Structured LoRA-Factor Projection Versus Naive Global Projection
- Success threshold: At least 25% optimizer-state reduction with validation loss within 10% of standard LoRA on the synthetic task and no worse than 20% degradation on a small real fine-tuning task.
- Stop condition: Stop if structured projection remains more than 2x worse than standard LoRA validation loss on the synthetic task after a small LR sweep.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-vram-lora-projection-training-with-optimizer-memory-reduction-c487624ad99b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
