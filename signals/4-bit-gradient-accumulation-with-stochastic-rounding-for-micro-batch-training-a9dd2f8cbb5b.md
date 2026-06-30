# 4-bit gradient accumulation with stochastic rounding for micro-batch training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-gradient-accumulation-with-stochastic-rounding-for-micro-batch-training-a9dd2f8cbb5b`
Run ID: `4-bit-gradient-accumulation-with-stochastic-rounding-for-micro-batch-training-a9dd2f8cbb5b-20260531T210920936825+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e8771661c28c

## What looked useful

Stochastic 4-bit accumulation was close to FP32 in the main 5-seed run (validation accuracy delta -0.0048, loss delta +0.0114) and better than deterministic nearest rounding there, but the advantage disappeared under a 32-accumulation-step stress ablation where stochastic had worse validation loss than FP32 and deterministic nearest rounding. This supports a mixed, regime-sensitive mechanism rather than a robust positive result.

## Boundaries and scale limits

No real language-model data, no GPT-2-small-class baseline, no adaptive/blockwise scale sweep, no packed 4-bit accumulator kernel, no optimizer variants beyond SGD, and no multi-GPU or long-run validation. Speed measurements are from an emulation prototype and are not an optimized implementation claim.

## Claim scope

Bounded CUDA toy-training evidence for signed 4-bit gradient accumulation during micro-batch training on a teacher-generated MLP classification task. Stochastic rounding helped versus deterministic rounding at 16 accumulation steps but did not hold up in a 32-step accumulation stress ablation.

## Why it stopped

Bounded direct toy-training evidence is mixed: stochastic rounding improves over deterministic rounding in one micro-batch regime but fails to show robust benefit under a nearby accumulation-depth stress test, so the result is not publication-grade or generally validated.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should add blockwise/adaptive scaling or error feedback and rerun the 16-step and 32-step accumulation regimes before any optimized-kernel or large-model work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise/error-feedback 4-bit stochastic gradient accumulation under accumulation-depth stress
- Success threshold: Across both accumulation regimes, the best low-bit variant must stay within +0.01 validation loss or within 1% relative validation loss of FP32, avoid worse accuracy by more than 0.005 absolute, and improve final accumulator relative L2 error versus the current stochastic variant.
- Stop condition: Stop if blockwise/adaptive/error-feedback variants still miss FP32 by more than +0.03 validation loss in either regime or fail to improve accumulator relative L2 error versus the current stochastic baseline.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-gradient-accumulation-with-stochastic-rounding-for-micro-batch-training-a9dd2f8cbb5b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
