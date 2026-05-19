# Medium direct confirmation of uncertainty-routed cascades on a harder neural task

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-direct-confirmation-of-uncertainty-routed-cascades-72a499b232`
Run ID: `medium-direct-confirmation-of-uncertainty-routed-cascades-72a499b232-20260516T111453051177+0000`

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

- Internal Enoch project: Medium direct confirmation of uncertainty-routed cascades on a harder neural task: internal_generated:medium-direct-confirmation-of-uncertainty-routed-cascades-72a499b232

## What looked useful

Three fixed-seed full Fashion-MNIST runs showed small-only test accuracy 0.8837 +/- 0.0076, large-only 0.9169 +/- 0.0032, and uncertainty cascade at the 0.35 budget 0.9148 +/- 0.0015 using 0.3499 +/- 0.0045 of large-model MACs. The cascade beat random matched routing by 0.0215 accuracy and high-confidence matched routing by 0.0311 accuracy on average.

## Boundaries and scale limits

Evidence is limited to Fashion-MNIST, small CNNs, MAC estimates rather than measured serving latency, three seeds, and in-distribution classification. It does not validate language-model cascades, production latency, distribution shift, calibration alternatives, or larger architectures.

## Claim scope

On Fashion-MNIST with small and large CNN classifiers, validation-selected max-softmax uncertainty routing recovers nearly all large-model test accuracy at about 35% of large-model MACs and beats small-only, random matched routing, and high-confidence matched routing across three fixed seeds.

## Why it stopped

No-paper closure: the mechanism is supported on a medium local neural task, but the evidence is too narrow for publication-grade claims about uncertainty-routed cascades.

## Recommended next action

Run a bounded CIFAR-10 deepen test with ResNet-style small/large models, five fixed seeds, measured latency plus MACs, and calibration ablations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CIFAR-10 calibrated uncertainty-routed cascades with latency controls
- Success threshold: Mean held-out cascade accuracy at less than 50% of large-model compute or latency beats small-only and matched random routing by at least 1 percentage point, with positive gains in at least four of five seeds and a gap to large-only under 2 percentage points.
- Stop condition: Stop as unsupported if the calibrated uncertainty route fails to beat matched random routing by 1 percentage point at less than 50% large-model compute/latency, or if gains appear only in fewer than four of five seeds.

## Evidence references

- Artifact root: `<local-path>/projects/medium-direct-confirmation-of-uncertainty-routed-cascades-72a499b232`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
