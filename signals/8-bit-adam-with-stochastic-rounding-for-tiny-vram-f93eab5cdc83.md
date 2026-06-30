# 8-bit Adam with Stochastic Rounding for Tiny VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adam-with-stochastic-rounding-for-tiny-vram-f93eab5cdc83`
Run ID: `8-bit-adam-with-stochastic-rounding-for-tiny-vram-f93eab5cdc83-20260612T214535283743+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/8016a2027f8b

## What looked useful

Naive per-tensor 8-bit Adam state is memory-efficient on paper but unstable at FP32 Adam's useful learning rate and at 3e-4 on this task. At 1e-4, deterministic and stochastic 8-bit variants train similarly to FP32, but stochastic rounding provides no measured advantage.

## Boundaries and scale limits

Toy MLP regression only; 3 seeds; 350 steps; non-fused Python/PyTorch optimizer; no language-model run; no production tiny-VRAM fused memory trace; per-tensor scales only.

## Claim scope

A local CUDA PyTorch prototype of per-tensor 8-bit Adam moment storage achieved about 4x theoretical optimizer-state memory reduction and matched FP32 Adam only at a reduced 1e-4 learning rate on a 336,912-parameter teacher-regression task; stochastic rounding did not improve this prototype over deterministic rounding.

## Why it stopped

Bounded proxy evidence shows the naive per-tensor stochastic-rounding 8-bit Adam idea is unstable at useful learning rates and not paper-ready; this is not a full language-model validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement blockwise moment scales plus denominator protection and require zero NaNs across seeds at the FP32 Adam baseline learning rate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise 8-bit Adam state with second-moment protection
- Success threshold: No NaNs across seeds at the FP32 Adam baseline learning rate and final loss within 10% of FP32 Adam while preserving at least 3x optimizer-state byte reduction.
- Stop condition: Stop if any blockwise/protected 8-bit variant diverges in more than 1 of 5 seeds or requires more than a 3x lower learning rate to remain stable.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adam-with-stochastic-rounding-for-tiny-vram-f93eab5cdc83`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
