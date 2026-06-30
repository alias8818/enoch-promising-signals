# Trainable Residual Gates for Extreme Quantized MLPs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trainable-residual-gates-for-extreme-quantized-mlps-d84216a6488d`
Run ID: `trainable-residual-gates-for-extreme-quantized-mlps-d84216a6488d-20260523T223933461152+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71075af61b6a

## What looked useful

Scalar trainable residual gates stayed low around 0.12-0.15. They improved depth-8 test loss versus fixed residuals on 5/5 seeds but did not beat fixed residual accuracy, and at depth 16 they lost accuracy to fixed residuals on 3/3 seeds.

## Boundaries and scale limits

No real language-model training, no GPT-2-small-class baseline, no large dataset, no hardware quantized kernel measurement, and only 5 seeds at depth 8 plus 3 seeds at depth 16.

## Claim scope

Small synthetic teacher-student classification probes for 1-bit-weight, 2-bit-activation MLPs with scalar trainable residual gates at depths 8 and 16.

## Why it stopped

Proxy evidence is mixed and does not support a robust positive claim for scalar trainable residual gates; this is an early bounded falsification of the broad hypothesis, not a full validation.

## Recommended next action

Stop this run as no-paper evidence; the next bounded test should ablate per-channel gates and high-carry initialization against the same fixed-residual controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Per-channel and high-carry residual gate ablation for quantized MLPs
- Success threshold: Beat fixed residual mean validation loss while losing no more than 0.005 absolute accuracy on both depth-8 and depth-16 sweeps.
- Stop condition: Stop if gated variants again underperform fixed residual accuracy by more than 0.005 absolute or fail to improve mean validation loss in either depth setting.

## Evidence references

- Artifact root: `<local-path>/projects/trainable-residual-gates-for-extreme-quantized-mlps-d84216a6488d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
