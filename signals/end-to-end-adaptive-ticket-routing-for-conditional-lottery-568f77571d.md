# End-to-End Adaptive Ticket Routing for Conditional Lottery Aggregation

Status: `useful_signal`
Project ID: `end-to-end-adaptive-ticket-routing-for-conditional-lottery-568f77571d`
Run ID: `end-to-end-adaptive-ticket-routing-for-conditional-lottery-568f77571d-20260518T083307176250+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: End-to-End Adaptive Ticket Routing for Conditional Lottery Aggregation: internal_generated:end-to-end-adaptive-ticket-routing-for-conditional-lottery-568f77571d

## What looked useful

Router diversity contains recoverable signal according to the oracle top-3 bound, but the implemented conditional reliability gate plus lottery/beta adaptation fails to recover it: adaptive_context_lottery_k3 loses 1.07 accuracy points vs single_global and increases misroute cost while using 2.84x router cost; the validation-tuned selective variant only ties the single baseline within uncertainty while using more compute.

## Boundaries and scale limits

Evidence is synthetic and local CPU-scale; routers are classical probabilistic classifiers rather than production LLM routers, and labels are revealed immediately for online adaptation. No private production trace or external deployment was tested.

## Claim scope

In a synthetic shifted support-ticket routing benchmark with six logistic/specialist routers and one million test-stream tickets across 20 fixed seeds, the tested conditional/adaptive lottery aggregation policies do not improve direct routing quality over a single global router or all-router ensemble.

## Why it stopped

Bounded direct synthetic validation falsified the stated mechanism threshold: adaptive lottery aggregation saved router cost versus the full ensemble but did not match or beat real baselines on direct routing quality.

## Recommended next action

Stop this follow-up as a no-paper useful negative; only revisit with a materially different gating objective or real ticket trace that can beat the single-global and all-router baselines on paired misroute cost and accuracy.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-adaptive-ticket-routing-for-conditional-lottery-568f77571d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
