# Dynamic 8-bit Optimizer with Variance Tracking

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-8-bit-optimizer-with-variance-tracking-fa86d64b4e72`
Run ID: `dynamic-8-bit-optimizer-with-variance-tracking-fa86d64b4e72-20260522T164831072671+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/93f4f84942ac

## What looked useful

Variance range tracking changes the failure mode and can keep training finite where absmax explodes at lr=1e-4, but second-moment quantization error remains large enough that both 8-bit variants diverge at lr=1e-3 even without outlier injection.

## Boundaries and scale limits

Toy synthetic regression only; no language-model training, no blockwise quantization, no nonlinear second-moment quantization, no production 8-bit kernels, and runs were seconds rather than long training.

## Claim scope

On a bounded CUDA synthetic MLP regression benchmark, a simple tensor-wise variance-tracked int8 Adam state scheme reduced estimated optimizer-state bytes by about 4x and was more stable than tensor-wise absmax at a reduced learning rate, but it failed as a drop-in fp32 Adam replacement and diverged at the fp32 learning rate.

## Why it stopped

Proxy/toy early falsification: variance tracking alone did not preserve fp32 Adam behavior on the direct local benchmark, although it outperformed absmax in a lower-learning-rate rescue setting.

## Recommended next action

Stop this variant as a no-paper useful signal; only revisit with a bounded follow-up that changes second-moment quantization rather than merely tuning the variance range.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise nonlinear second-moment quantization for variance-tracked 8-bit Adam
- Success threshold: No NaN/divergence in all seeds, final loss within 2x fp32 for outlier magnitudes 0 and 10, and estimated optimizer-state storage at least 3x smaller than fp32 Adam state.
- Stop condition: Stop if the modified second-moment quantizer still diverges at lr=1e-3 on outlier magnitude 0 or if final loss remains more than 10x fp32 after 500 steps.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-8-bit-optimizer-with-variance-tracking-fa86d64b4e72`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
