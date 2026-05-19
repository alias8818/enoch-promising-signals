# Real-KV anchors on a competent learned recall model

Status: `useful_signal`
Project ID: `real-kv-anchors-on-a-competent-learned-recall-model-1b68c0de0b`
Run ID: `real-kv-anchors-on-a-competent-learned-recall-model-1b68c0de0b-20260519T104854515322+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Real-KV anchors on a competent learned recall model: internal_generated:real-kv-anchors-on-a-competent-learned-recall-model-1b68c0de0b

## What looked useful

Across three fixed seeds, no-anchor accuracy averaged 0.4017, real non-target anchors averaged 0.3639, shuffled anchors averaged 0.3717, and an oracle target-anchor positive control averaged 0.9999. Real anchors consistently hurt versus baseline with mean delta -0.0378.

## Boundaries and scale limits

Synthetic short-context task only; not a natural-language LLM, not a long-context benchmark, and not an internal KV-cache injection test. The no-anchor model is competent relative to chance but not near-perfect: 40.2% exact recall versus 12.5% chance.

## Claim scope

In a small synthetic episodic learned-recall task with a 0.88M-parameter causal transformer, 32 keys, 8 values, 4 support pairs, 4 anchors, and fixed seeds 0/1/2, truthful non-target prompt-level key-value anchors do not improve exact recall over a no-anchor baseline or shuffled-anchor controls.

## Why it stopped

Tier 2 scoped validation with fixed seeds, a standard transformer baseline, shuffled-anchor control, and oracle positive control found no support for non-target real prompt-level KV anchors; they reduced recall rather than improving it.

## Recommended next action

Stop this branch as a no-paper negative result unless a new follow-up changes the intervention to internal KV-cache anchors or target-containing retrieval anchors with a direct mechanism diagnostic.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Internal KV-cache anchors versus prompt-token anchors on episodic recall
- Success threshold: Internal real KV anchors improve exact recall by at least 5 absolute percentage points over no-anchor and shuffled-internal controls on every fixed seed, while prompt-token non-target anchors remain non-improving.
- Stop condition: Stop if internal real anchors fail to beat both no-anchor and shuffled-internal controls by at least 2 absolute percentage points on two or more seeds, or if the only improvement comes from target leakage.

## Evidence references

- Artifact root: `<local-path>/projects/real-kv-anchors-on-a-competent-learned-recall-model-1b68c0de0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
