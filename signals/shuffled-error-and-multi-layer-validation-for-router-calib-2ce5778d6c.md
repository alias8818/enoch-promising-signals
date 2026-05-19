# Shuffled-error and multi-layer validation for router-calibrated KV adapters

Status: `useful_signal`
Project ID: `shuffled-error-and-multi-layer-validation-for-router-calib-2ce5778d6c`
Run ID: `shuffled-error-and-multi-layer-validation-for-router-calib-2ce5778d6c-20260517T233704200212+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Shuffled-error and multi-layer validation for router-calibrated KV adapters: internal_generated:shuffled-error-and-multi-layer-validation-for-router-calib-2ce5778d6c

## What looked useful

Adapter capacity closed much of the frozen-base held-out-task gap (+0.018 held-out accuracy for multi-layer router KV adapters), but the same gain appeared for global and shuffled-route controls, so the result supports generic KV adapter calibration rather than router-calibrated error alignment.

## Boundaries and scale limits

Evidence is from a small synthetic transformer surrogate with five fixed seeds, not GPT-2-small-class or real pretrained LM router traces; held-out accuracy saturated across adapter controls.

## Claim scope

In a bounded synthetic causal-transformer validation, small KV adapters improved a frozen base model on held-out transition tasks, but correctly routed multi-layer adapters did not materially outperform global adapters or shuffled-route controls.

## Why it stopped

Bounded full local validation produced a useful adapter signal but failed to isolate the router-calibrated mechanism against global and shuffled-route controls.

## Recommended next action

Stop this follow-up as no-paper evidence; only revisit with a real pretrained LM hidden-state/error-trace workload where shuffled-error controls cannot explain the adapter gain.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM hidden-state shuffled-error validation for router-calibrated KV adapters
- Success threshold: Correctly routed KV adapters must beat both global KV adapters and shuffled-error routed adapters by at least 0.01 held-out accuracy or 5% relative held-out loss reduction with consistent direction across seeds, while retaining a meaningful gain over the frozen base.
- Stop condition: Stop if shuffled-error or global controls match the routed adapter within the threshold across three seeds, or if adapter gains vanish relative to the frozen base.

## Evidence references

- Artifact root: `<local-path>/projects/shuffled-error-and-multi-layer-validation-for-router-calib-2ce5778d6c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
