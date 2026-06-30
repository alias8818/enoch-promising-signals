# Residual-Channel-Preserving 1.58-bit Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-preserving-1-58-bit-quantization-b885d12338f3`
Run ID: `residual-channel-preserving-1-58-bit-quantization-b885d12338f3-20260529T191413670488+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9f4ef5372376

## What looked useful

Top-error residual/output-channel preservation reduced 5% preserved layer relative MSE from 0.9515 for random to 0.6818 and improved mean GPT-2-small NLL from 13.9429 random to 10.7963, but full precision NLL was 5.2751.

## Boundaries and scale limits

Single GPT-2-small model, projection-only post-training dequantized simulation, 4,096-token local synthetic text evaluation per seed, three random seeds for preservation selection, no packed kernel, no standard benchmark corpus, no training-aware quantization.

## Claim scope

On GPT-2-small projection and MLP modules, preserving the top 5% output rows by ternary weight reconstruction error improves layer reconstruction and small-corpus NLL versus random row preservation at the same effective bit budget, but remains far worse than full precision.

## Why it stopped

No-paper useful signal: the mechanism beats random preservation, but this is a small post-training probe and the quantized model quality remains catastrophically below full precision.

## Recommended next action

Run one bounded follow-up using activation-calibrated channel ranking and a standard validation corpus for GPT-2-small; stop if NLL remains more than 2.0 above a matched low-bit PTQ baseline or full precision.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-calibrated residual-channel preservation for GPT-2-small ternary PTQ
- Success threshold: Activation-calibrated preservation must beat random preservation by at least 1.0 NLL and reduce the gap to full precision or a matched PTQ baseline by at least 50% at 5% preserved rows.
- Stop condition: Stop if activation-calibrated preservation fails to beat random preservation by 1.0 NLL or if all preserved-channel variants remain more than 2.0 NLL worse than a matched low-bit PTQ baseline.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-preserving-1-58-bit-quantization-b885d12338f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
