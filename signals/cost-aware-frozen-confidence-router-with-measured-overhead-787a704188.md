# Cost-aware frozen confidence router with measured-overhead guard

Status: `useful_signal`
Project ID: `cost-aware-frozen-confidence-router-with-measured-overhead-787a704188`
Run ID: `cost-aware-frozen-confidence-router-with-measured-overhead-787a704188-20260519T010543585574+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Cost-aware frozen confidence router with measured-overhead guard: internal_generated:cost-aware-frozen-confidence-router-with-measured-overhead-787a704188

## What looked useful

Confidence-based routing produced mean accuracy 0.9766 and mean latency 0.002676 ms/sample versus expensive-only 0.9739 and 0.025069 ms/sample across 60 runs, with utility wins over expensive-only in 51/60 splits. However, cheap-only remained the best practical utility baseline on breast cancer and wine, and the measured-overhead guard differed from no-guard thresholding in 0/60 runs.

## Boundaries and scale limits

Small CPU sklearn classifiers only; no LLM, token-generation, GPU serving, batching, RPC, queueing, or distribution-shift validation. Router overhead was measured locally and was too small relative to expensive-model latency to stress the guard.

## Claim scope

On three small real sklearn classification datasets with 20 fixed train/validation/test splits each, a frozen cheap-model confidence router can improve measured cost utility versus expensive-only and random-routing controls, especially on digits, but it does not consistently beat cheap-only and the measured-overhead guard does not change threshold selection versus a no-guard ablation.

## Why it stopped

Moderate direct local evidence supports confidence routing as a useful mechanism but gives mixed support for the full hypothesis and no support for an independent measured-overhead guard effect; this is not a Tier-4 paper-ready result.

## Recommended next action

Stop this follow-up at depth 4: preserve the bounded confidence-router evidence, but do not write a paper because the measured-overhead guard had no independent effect and cheap-only beat the router on two datasets under the chosen utility.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/cost-aware-frozen-confidence-router-with-measured-overhead-787a704188`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
