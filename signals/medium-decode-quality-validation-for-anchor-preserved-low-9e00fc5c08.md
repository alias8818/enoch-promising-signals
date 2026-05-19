# Medium decode-quality validation for anchor-preserved low-rank KV compression

Status: `useful_signal`
Project ID: `medium-decode-quality-validation-for-anchor-preserved-low-9e00fc5c08`
Run ID: `medium-decode-quality-validation-for-anchor-preserved-low-9e00fc5c08-20260517T221914410928+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/979f0a9871af

## What looked useful

Anchor preservation consistently improved greedy-token agreement versus plain low-rank KV reconstruction and reduced NLL damage by 32.8% at rank 16 with 32 anchors, but no tested configuration satisfied both the relative NLL-damage reduction and absolute NLL quality thresholds.

## Boundaries and scale limits

24 WikiText-2 validation spans, 192-token prefixes, 48-token continuations, 1152 target tokens; GPT-2-small only; no packed compressed-kernel memory or latency validation; no long-context or 7B+ model validation.

## Claim scope

Tier 1 direct GPT-2-small WikiText-2 decode-quality test of simulated dense-reconstructed low-rank KV cache with first-token plus recent-token anchor preservation.

## Why it stopped

Tier 1 direct evidence is mixed and no-paper: the mechanism improves greedy agreement and some NLL deltas, but does not simultaneously meet the preset decode-quality thresholds.

## Recommended next action

Run a bounded deepen test over at least 100 real-text prompts with longer prefixes and an effective-storage constraint to determine whether anchor selection can satisfy both NLL thresholds at <=50% exact-KV storage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rank-anchor frontier for quality-bounded low-rank KV compression
- Success threshold: At <=50% exact-KV effective storage, anchor_lowrank_delta_nll <= 0.10, anchor_delta_reduction_vs_lowrank >= 0.25, and anchor_lowrank_greedy_agreement >= 0.90 on at least 100 prompts.
- Stop condition: Stop if no rank-anchor setting under the <=50% storage bound meets both NLL thresholds and >=0.90 greedy agreement, or if anchor preservation fails to improve both NLL delta and greedy agreement over plain low-rank in aggregate.

## Evidence references

- Artifact root: `<local-path>/projects/medium-decode-quality-validation-for-anchor-preserved-low-9e00fc5c08`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
