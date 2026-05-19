# CIFAR-10 calibrated uncertainty-routed cascades with latency controls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `cifar-10-calibrated-uncertainty-routed-cascades-with-laten-e93d3deda8`
Run ID: `cifar-10-calibrated-uncertainty-routed-cascades-with-laten-e93d3deda8-20260516T112302580598+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: CIFAR-10 calibrated uncertainty-routed cascades with latency controls: internal_generated:cifar-10-calibrated-uncertainty-routed-cascades-with-laten-e93d3deda8

## What looked useful

The calibrated cascade achieved mean test accuracy 0.8853 at the 0.70 latency budget versus 0.8868 for the large model, with 1.45x expected speedup. At the 0.50 budget it reached 0.8740 accuracy, above the medium baseline's 0.8710, with about 2.04x speedup versus the large model. Random same-exit controls were much worse, especially at 0.70 where they averaged 0.8548 accuracy.

## Boundaries and scale limits

Evidence is limited to CIFAR-10, 20-epoch simple CNNs, three seeds, temperature scaling, validation-selected thresholds, and expected latency from batched per-stage measurements. It does not include CIFAR-100/ImageNet, ResNet-class models, optimized serving implementation, or established early-exit/BranchyNet/MSDNet baselines.

## Claim scope

On CIFAR-10 with three scratch-trained CNN stages over seeds 0, 1, and 2, validation-calibrated confidence routing can meet explicit expected-latency budgets and nearly match the large CNN accuracy at lower expected latency.

## Why it stopped

The direct CIFAR-10 mechanism test is positive, but the strict paper gate is not met because baselines are simple CNNs and the run lacks comparison to established early-exit/cascade methods and optimized serving latency.

## Recommended next action

Stop this run as no-paper useful evidence; run one bounded deepen follow-up comparing calibrated cascades against a proper early-exit baseline on CIFAR-10/100 with matched latency measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CIFAR-10/100 calibrated cascades versus early-exit baselines under matched latency
- Success threshold: At two or more latency budgets, calibrated cascades match or exceed early-exit baseline accuracy within 0.3 percentage points while maintaining ECE no worse than 0.01 absolute and at least 1.3x speedup versus the dense large baseline.
- Stop condition: Stop if the early-exit baseline dominates calibrated cascades by at least 0.5 percentage points accuracy at matched latency on both datasets or if calibration no longer improves ECE/accuracy tradeoffs.

## Evidence references

- Artifact root: `<local-path>/projects/cifar-10-calibrated-uncertainty-routed-cascades-with-laten-e93d3deda8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
