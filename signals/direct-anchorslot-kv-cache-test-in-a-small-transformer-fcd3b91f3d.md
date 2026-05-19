# Direct AnchorSlot KV Cache Test in a Small Transformer

Status: `useful_signal`
Project ID: `direct-anchorslot-kv-cache-test-in-a-small-transformer-fcd3b91f3d`
Run ID: `direct-anchorslot-kv-cache-test-in-a-small-transformer-fcd3b91f3d-20260518T035237356747+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/27b55e4499f7

## What looked useful

Actual incremental KV-cache filtering showed a sharp split: generic anchors failed at chance-level recall, but key-addressed anchor slots with anchor-compatible training reached 1.0000 anchor-slot accuracy while retaining 36% of prefix cache and beating recent-only by 71.8 percentage points.

## Boundaries and scale limits

Tested only on a tiny synthetic transformer, 8 facts, 32 keys, 32 values, one main seed, and one task family. No natural language pretraining, GPT-2-small-class baseline, long-context serving benchmark, multi-seed robustness, or wall-clock memory-bandwidth validation was performed. Generic single-token anchors failed.

## Claim scope

In a single-seed synthetic associative-recall task with an explicitly anchor-forced tiny causal transformer, key-addressed post-fact anchor tokens can be retained as 9 KV-cache slots instead of the 25-token full pre-query prefix while matching full-cache answer accuracy.

## Why it stopped

Tier 1 produced direct useful mechanism evidence but also a generic-anchor failure and lacks robustness or real-model validation, so this run is no-paper.

## Recommended next action

Run a medium multi-seed confirmation with key-addressed anchors on harder associative-recall settings, longer prefixes, parameter-matched baselines, and measured cache memory/latency savings before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Multi-Seed Key-Addressed AnchorSlot KV Cache Confirmation
- Success threshold: Across at least 5 seeds, key-addressed anchor-slot accuracy is within 5 percentage points of full-cache accuracy, at least 30 percentage points above recent-only, and retains no more than 50% of full-prefix KV tokens on the harder settings.
- Stop condition: Stop if anchor-slot accuracy falls more than 10 percentage points below full-cache accuracy on 3 or more seeds, or if savings disappear once prefixes and distractors are increased.

## Evidence references

- Artifact root: `<local-path>/projects/direct-anchorslot-kv-cache-test-in-a-small-transformer-fcd3b91f3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
