# Real-data comparison of channel-wise versus global 1-bit residual gradients

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-data-comparison-of-channel-wise-versus-global-1-bit-r-66960931c3`
Run ID: `real-data-comparison-of-channel-wise-versus-global-1-bit-r-66960931c3-20260522T083424564210+0000`

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

- Parent run decision: Channel-Wise 1-Bit Gradients with Local Error Residuals: enoch://control-plane/projects/channel-wise-1-bit-gradients-with-local-error-residuals-6f741f8159be/runs/channel-wise-1-bit-gradients-with-local-error-residuals-6f741f8159be-20260522T003143304102+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71b83696c4f4

## What looked useful

Channel-wise 1-bit residual gradients reduced final-epoch relative compressed-update error by 3.84% versus global in the extended run and lowered residual/gradient ratio, but final validation accuracy was slightly lower on average (-0.024 pp) and worse on 3 of 5 seeds. The predefined Tier 1 threshold was not met.

## Boundaries and scale limits

Tested one small CNN, MNIST, single-node PyTorch training, 5 extended seeds, 30k train examples, 5k test examples, 8 epochs. Not tested on CIFAR/ImageNet, transformers, distributed communication, or metadata-overhead-adjusted wall-clock throughput.

## Claim scope

On a controlled MNIST small-CNN training task with error-feedback 1-bit gradients, channel-wise scaling modestly reduces update reconstruction error versus global tensor-wise scaling but does not produce a consistent validation accuracy advantage.

## Why it stopped

Direct small real-data validation did not meet the stated Tier 1 threshold: update-error reduction was below 10% and validation accuracy was not no-worse across seeds.

## Recommended next action

Stop this run as a bounded no-paper useful signal; only pursue a next bounded follow-up if testing a more channel-heterogeneous real model with metadata-overhead-adjusted compression cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Channel-wise 1-bit residual gradients on a channel-heterogeneous CIFAR model with scale-overhead accounting
- Success threshold: Channel-wise achieves >=10% mean relative update-error reduction versus global, is no worse in validation accuracy in at least 4 of 5 seeds, improves mean validation accuracy by >=0.5 percentage points, and preserves a net compression advantage after scale metadata overhead.
- Stop condition: Stop if channel-wise update-error reduction remains below 10% or mean validation accuracy fails to improve after 5 matched seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-comparison-of-channel-wise-versus-global-1-bit-r-66960931c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
