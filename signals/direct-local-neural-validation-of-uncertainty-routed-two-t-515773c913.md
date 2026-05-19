# Direct local neural validation of uncertainty-routed two-tier cascades

Status: `useful_signal`
Project ID: `direct-local-neural-validation-of-uncertainty-routed-two-t-515773c913`
Run ID: `direct-local-neural-validation-of-uncertainty-routed-two-t-515773c913-20260516T110923491355+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bf84e6e5d49a

## What looked useful

Entropy-routed cascades met the predefined Tier 1 threshold: at 30% tier-2 routing, aggregate test accuracy was 0.8954 versus tier-2 0.9049 mean, using 0.317x tier-2 MACs and beating random routing by 0.0358 accuracy; 40-50% routing essentially recovered tier-2 accuracy under the 0.60x compute cap.

## Boundaries and scale limits

Small image-classification task only; no language-model cascade, no distribution-shift test, no production serving stack, and compute cost is primarily analytical MAC accounting rather than full deployment latency.

## Claim scope

In a three-seed Fashion-MNIST CNN test, tier-1 entropy routing to a larger tier-2 CNN recovered near-tier-2 accuracy at substantially lower average analytical MAC cost and outperformed matched random escalation.

## Why it stopped

Tier 1 direct neural mechanism threshold was met, but the evidence remains a small controlled image-classification result and is not publication-grade validation.

## Recommended next action

Run a medium direct confirmation on CIFAR-10 or a small language-model classification task with calibrated uncertainty, real latency/throughput measurement, and a compute-matched baseline before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium direct confirmation of uncertainty-routed cascades on a harder neural task
- Success threshold: Mean cascade accuracy within 1.0 percentage point of tier 2 while using <=60% of tier-2 measured cost and beating random routing by at least 1.0 accuracy point at the selected route fraction.
- Stop condition: Stop if calibrated uncertainty routing cannot beat matched random routing by 1.0 accuracy point at any route fraction under the 60% measured-cost cap, or if it requires more than 60% measured cost to get within 1.0 percentage point of tier 2.

## Evidence references

- Artifact root: `<local-path>/projects/direct-local-neural-validation-of-uncertainty-routed-two-t-515773c913`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
