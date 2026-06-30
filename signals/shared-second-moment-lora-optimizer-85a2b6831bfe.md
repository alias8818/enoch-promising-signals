# Shared Second-Moment LoRA Optimizer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `shared-second-moment-lora-optimizer-85a2b6831bfe`
Run ID: `shared-second-moment-lora-optimizer-85a2b6831bfe-20260529T121320205522+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c79b9e0aa0fd

## What looked useful

Shared second moments can converge on isotropic synthetic LoRA tasks and save optimizer state, but anisotropic tasks show higher validation loss instability and substantially worse target-delta recovery than Adam. A naive shared-v optimizer is not paper-ready as a robust Adam replacement.

## Boundaries and scale limits

Evidence is CPU-only NumPy synthetic regression: 64x64 and 128x64 linear maps, rank 4 adapters, 6 seeds, 900 full-batch steps. It does not validate LLM LoRA fine-tuning, minibatch stochasticity, transformer layers, quantization, or real memory-pressure throughput.

## Claim scope

In synthetic frozen-linear LoRA adaptation with known low-rank target deltas, naive rank- or layer-shared second-moment accumulators reduce optimizer-state scalars by about half but are less robust than Adam under anisotropic feature distributions.

## Why it stopped

Early/proxy synthetic evidence found a useful memory-saving mechanism but also falsified robustness of naive shared second moments under anisotropic inputs; this is not full LLM validation.

## Recommended next action

Stop this naive shared-second-moment variant as no-paper; next bounded work should test a structured factored/grouped second-moment LoRA optimizer on a small transformer LoRA task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Structured shared second moments for small-transformer LoRA
- Success threshold: Across at least 3 seeds, structured shared-v reaches within 2% of AdamW validation loss or task metric while reducing optimizer-state memory by at least 25% and avoiding the anisotropic delta-recovery failures seen here.
- Stop condition: Stop if structured shared-v remains more than 5% worse than AdamW on validation metric or shows repeated instability after a small learning-rate sweep.

## Evidence references

- Artifact root: `<local-path>/projects/shared-second-moment-lora-optimizer-85a2b6831bfe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
