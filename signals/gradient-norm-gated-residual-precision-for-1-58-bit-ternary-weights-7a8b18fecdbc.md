# Gradient-Norm Gated Residual Precision for 1.58-bit Ternary Weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-norm-gated-residual-precision-for-1-58-bit-ternary-weights-7a8b18fecdbc`
Run ID: `gradient-norm-gated-residual-precision-for-1-58-bit-ternary-weights-7a8b18fecdbc-20260525T105501444932+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ff62eb26f6d5

## What looked useful

Gated residual precision improved final test accuracy over plain ternary by +0.00725 mean across 10 paired seeds and best accuracy by +0.00364, but underperformed static residual by -0.00251 final accuracy and -0.00171 best accuracy.

## Boundaries and scale limits

Small synthetic MLP only; no transformer, language-model, real dataset, 7B-scale, inference kernel, memory-saving implementation, or long training validation was tested.

## Claim scope

On a 10-seed synthetic teacher-student MLP classification task, gradient-norm gated residual precision for ternary STE weights produced a small paired accuracy gain over plain ternary STE while activating about one of three residual layers after warmup, but it did not beat a simpler static residual precision control.

## Why it stopped

Closed as a no-paper useful signal because the local direct test was synthetic/proxy-scale and the proposed gradient-norm gate did not outperform the simpler static residual control.

## Recommended next action

Run a bounded tiny-transformer language-model deepen test with budget-matched static and random residual gates before spending larger compute.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Budget-Matched Gradient Gates in a Tiny Ternary Transformer
- Success threshold: Gradient-gated residual must beat plain ternary by at least 1% relative validation loss and beat budget-matched static and random residual controls on at least 3 of 5 paired seeds.
- Stop condition: Stop if gradient gating fails to beat either budget-matched control after 5 paired seeds or if the apparent gain is below 0.5% relative validation loss.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-gated-residual-precision-for-1-58-bit-ternary-weights-7a8b18fecdbc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
