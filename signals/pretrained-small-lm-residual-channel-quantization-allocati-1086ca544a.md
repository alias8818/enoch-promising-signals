# Pretrained Small-LM Residual Channel Quantization Allocation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `pretrained-small-lm-residual-channel-quantization-allocati-1086ca544a`
Run ID: `pretrained-small-lm-residual-channel-quantization-allocati-1086ca544a-20260613T214335339720+0000`

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

- Parent run decision: Residual Channel Importance Ranking for Quantization Allocation: enoch://control-plane/projects/residual-channel-importance-ranking-for-quantization-allocation-383771481245/runs/residual-channel-importance-ranking-for-quantization-allocation-383771481245-20260613T212800259728+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fdc72ec0d6bc

## What looked useful

The calibration-weighted residual/channel allocator beat random mixed 2/4/6 allocation at the same average bit budget, but lost badly to the practical uniform 4-bit baseline: uniform4 loss 4.817347 versus rcq_alloc_2_4_6 loss 6.328887. The ranking signal is non-random, but the aggressive 2-bit tail appears to erase any benefit.

## Boundaries and scale limits

Small direct validation only: distilgpt2, 24 eval batches of size 2 at sequence length 128, GPT-2 projection weights only, no fine-tuning, no activation quantization, no Hessian correction, no broader model-family or long validation sweep.

## Claim scope

Tier 1 direct post-training quantization test on distilgpt2 projection weights using WikiText-2 validation chunks: the tested residual/channel calibration allocator with 2/4/6-bit channels at 4.0 average bits does not improve validation LM loss over uniform 4-bit per-channel quantization.

## Why it stopped

Early direct falsification of the stated Tier 1 success threshold, not full validation: rcq_alloc_2_4_6 failed to beat uniform 4-bit by 0.005 loss and was 1.511540 loss worse on the calibrated pretrained-LM test.

## Recommended next action

Do not write a paper from this formulation; run one bounded deepen test with a floor-preserving 3/4/5-bit or layer-wise budget allocator only if continuing this line.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Floor-preserving residual channel allocation for pretrained LM quantization
- Success threshold: Floor-preserving allocation loss <= uniform4 loss - 0.005 and lower than random mixed at exactly 4.0 average bits on the same pretrained-LM setup.
- Stop condition: Stop if the floor-preserving allocator is not better than uniform4 by at least 0.005 loss on distilgpt2, or if it only wins against random mixed but not uniform same-budget quantization.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-small-lm-residual-channel-quantization-allocati-1086ca544a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
