# Small transformer adapter validation for residual-preserving gated 1-bit bottlenecks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-transformer-adapter-validation-for-residual-preservi-dfbb836955`
Run ID: `small-transformer-adapter-validation-for-residual-preservi-dfbb836955-20260518T110256382159+0000`

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

- Internal Enoch project: Small transformer adapter validation for residual-preserving gated 1-bit bottlenecks: internal_generated:small-transformer-adapter-validation-for-residual-preservi-dfbb836955

## What looked useful

Residual preservation is supported by the strong failure of the non-residual binary ablation, but the learned gate is not supported as beneficial because the gated binary residual variant was slightly worse than dense gated residual and worse than the no-gate binary residual ablation.

## Boundaries and scale limits

Small character-level LM, 800-step pretrain, 800-step adapter runs, same-corpus continued adaptation, straight-through binary estimator; not GPT-2-small-class tokenization, not large pretrained-model fine-tuning, and not downstream transfer.

## Claim scope

In a 0.81M-parameter character-level WikiText-2 causal transformer with a frozen pretrained backbone and 3 fixed seeds, residual binary bottleneck adapters improved over a frozen control, but the residual-preserving gated 1-bit bottleneck did not outperform a dense gated adapter baseline or a no-gate binary residual ablation.

## Why it stopped

Tier 2 medium local evidence supports residual preservation but falsifies the stronger claim that the gated 1-bit residual bottleneck is better than real dense and no-gate adapter baselines in the tested setting.

## Recommended next action

Stop paper pursuit for this exact claim; if continuing, run a bounded gate initialization/schedule ablation to test whether the gate is suppressing useful binary residual updates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gate initialization and schedule ablation for binary residual bottleneck adapters
- Success threshold: A scheduled or reinitialized gated binary residual variant must beat the no-gate binary residual mean validation loss by at least 0.01 CE over 3 seeds while staying within 0.01 CE of the dense gated residual baseline or better.
- Stop condition: Stop if all gated variants remain worse than no-gate binary residual by 0.005 CE or more over 3 fixed seeds, or if gate trajectories show no meaningful movement from initialization.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-adapter-validation-for-residual-preservi-dfbb836955`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
