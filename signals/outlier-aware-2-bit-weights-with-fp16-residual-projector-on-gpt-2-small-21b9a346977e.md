# Outlier-aware 2-bit weights with FP16 residual projector on GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `outlier-aware-2-bit-weights-with-fp16-residual-projector-on-gpt-2-small-21b9a346977e`
Run ID: `outlier-aware-2-bit-weights-with-fp16-residual-projector-on-gpt-2-small-21b9a346977e-20260629T032717197341+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b3da86e28ed9

## What looked useful

Plain 2-bit replacement degraded GPT-2-small from PPL 43.48 to 30,397.04. FP16 residual projectors improved over plain 2-bit at some budgets, best observed PPL 6,146.86 at 2.467 effective bits per quantized non-embedding weight, but remained far from dense quality and was not monotonic with rank budget.

## Boundaries and scale limits

No packed 2-bit kernels, latency, memory-bandwidth, full-validation-set, training, activation-aware calibration, or downstream-task evidence. Evaluation is a bounded early falsification, not a full-scale model-compression study.

## Claim scope

Dense-simulation accuracy test on GPT-2-small non-embedding 2D weights: per-row affine 2-bit quantization plus FP16 SVD residual projectors evaluated on 1,024 WikiText-2 validation tokens.

## Why it stopped

Direct bounded GPT-2-small proxy showed the tested 2-bit plus FP16 SVD residual projector does not recover acceptable perplexity; this is an early falsification rather than full validation.

## Recommended next action

Stop this run as a bounded no-paper early falsification; only pursue a follow-up if testing an activation-aware residual projector with the same effective-bit accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware FP16 residual projector for 2-bit GPT-2-small weights
- Success threshold: At <=2.25 effective bits per quantized non-embedding weight, activation-aware residual reduces at least 50% of the dense-to-plain-2bit NLL gap and beats the SVD residual by at least 10% relative NLL-gap recovery on >=8k validation tokens.
- Stop condition: Stop if activation-aware residual does not outperform SVD residual on the matched token slice and bit budget, or if it requires >2.25 effective bits to recover half the NLL gap.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-aware-2-bit-weights-with-fp16-residual-projector-on-gpt-2-small-21b9a346977e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
