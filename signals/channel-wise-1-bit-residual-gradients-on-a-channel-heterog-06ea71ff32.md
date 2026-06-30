# Channel-wise 1-bit residual gradients on a channel-heterogeneous CIFAR model with scale-overhead accounting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `channel-wise-1-bit-residual-gradients-on-a-channel-heterog-06ea71ff32`
Run ID: `channel-wise-1-bit-residual-gradients-on-a-channel-heterog-06ea71ff32-20260522T104424331693+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-data comparison of channel-wise versus global 1-bit residual gradients: enoch://control-plane/projects/real-data-comparison-of-channel-wise-versus-global-1-bit-r-66960931c3/runs/real-data-comparison-of-channel-wise-versus-global-1-bit-r-66960931c3-20260522T083424564210+0000
- Parent run decision: Channel-Wise 1-Bit Gradients with Local Error Residuals: enoch://control-plane/projects/channel-wise-1-bit-gradients-with-local-error-residuals-6f741f8159be/runs/channel-wise-1-bit-gradients-with-local-error-residuals-6f741f8159be-20260522T003143304102+0000

## What looked useful

Channel granularity and residual error feedback both mattered: channel-wise residual averaged 78.29% validation accuracy, dense averaged 79.71%, tensor-wise residual averaged 75.83%, and channel-wise no-residual averaged 75.00%. This supports the mechanism but not publication readiness.

## Boundaries and scale limits

Single compact CIFAR-10 CNN, 10 epochs, simulated single-worker gradient compression, no real distributed network, no pack/unpack kernel benchmark, no ResNet/transformer/large-scale validation.

## Claim scope

On one 61,790-parameter channel-heterogeneous CIFAR-10 CNN trained for 10 epochs with SGD across seeds 11, 22, and 33, channel-wise 1-bit gradients with error-feedback residuals retained validation accuracy within 1.4 percentage points of dense SGD while reducing scale-overhead-accounted gradient bits by 28.7x, and outperformed tensor-wise residual and channel-wise no-residual controls.

## Why it stopped

Tier 2 evidence supports the mechanism as a useful scoped signal, but the validation is too narrow for a paper: one compact model, one dataset, one schedule, and simulated communication only.

## Recommended next action

Run a bounded deepening test on a stronger CIFAR baseline, such as a small ResNet for 30-50 epochs with the same four variants, retaining scale-overhead bit accounting and adding pack/unpack wall-clock timing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Channel-wise residual 1-bit gradients on a stronger CIFAR baseline with timing overhead
- Success threshold: Channel-wise residual is no more than 2.0 validation-accuracy points below dense and at least 1.5 points above both controls, while preserving at least 20x scale-overhead-accounted gradient-bit reduction.
- Stop condition: Stop if channel-wise residual is more than 2.0 points below dense at convergence or does not beat both controls by at least 1.5 points under the same schedule.

## Evidence references

- Artifact root: `<local-path>/projects/channel-wise-1-bit-residual-gradients-on-a-channel-heterog-06ea71ff32`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
