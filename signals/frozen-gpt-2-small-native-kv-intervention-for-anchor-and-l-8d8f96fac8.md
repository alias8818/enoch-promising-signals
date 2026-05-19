# Frozen GPT-2-small Native KV Intervention for Anchor and Log-Count Recall

Status: `useful_signal`
Project ID: `frozen-gpt-2-small-native-kv-intervention-for-anchor-and-l-8d8f96fac8`
Run ID: `frozen-gpt-2-small-native-kv-intervention-for-anchor-and-l-8d8f96fac8-20260518T195004131961+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Frozen GPT-2-small Native KV Intervention for Anchor and Log-Count Recall: internal_generated:frozen-gpt-2-small-native-kv-intervention-for-anchor-and-l-8d8f96fac8

## What looked useful

Late-layer key-side native KV intervention robustly rescued anchor recall from 0% baseline accuracy to 100% with key-only true-anchor boosting, while wrong-anchor and value-only controls failed. Log-count recall did not improve from raw mark evidence K/V; only externally computed correct count-token slot injection improved count accuracy to 70.8%.

## Boundaries and scale limits

Synthetic prompts only; one model size; one late-layer/gain configuration for the main medium run; count slot intervention injects an externally computed answer token and is not autonomous counting from evidence K/V; no natural-language benchmark or multi-token target validation.

## Claim scope

Frozen GPT-2-small on synthetic single-token anchor and count prompts with 36 distractor ledger entries, late-layer native K/V interventions, fixed seeds 11/23/37, and 120 examples per task.

## Why it stopped

Medium fixed-seed evidence supports native KV anchor rescue but does not support native evidence-token KV log-count recall; the count-positive condition is an answer-token slot injection control, not a direct counting mechanism.

## Recommended next action

Stop this run as no-paper mixed evidence; if continuing the campaign, run a bounded deepen test that separates learned/evidence-derived count KV construction from answer-token transport.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-Derived KV Count Controller Versus Answer-Token KV Transport
- Success threshold: On at least 120 held-out count examples, evidence-derived count-KV treatment improves top-1 count accuracy by at least 40 percentage points over baseline and by at least 30 points over wrong-evidence control, with no direct target digit KV copied into the prompt.
- Stop condition: Stop as unsupported if evidence-derived count-KV fails to beat baseline by 15 percentage points on two fixed seeds or if improvements disappear under wrong-evidence controls.

## Evidence references

- Artifact root: `<local-path>/projects/frozen-gpt-2-small-native-kv-intervention-for-anchor-and-l-8d8f96fac8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
