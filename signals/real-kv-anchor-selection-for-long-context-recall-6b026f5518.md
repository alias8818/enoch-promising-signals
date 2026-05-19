# Real-KV Anchor Selection for Long-Context Recall

Status: `useful_signal`
Project ID: `real-kv-anchor-selection-for-long-context-recall-6b026f5518`
Run ID: `real-kv-anchor-selection-for-long-context-recall-6b026f5518-20260519T103304934966+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6c11686cef8e

## What looked useful

Across 5,000-example synthetic KV recall and a 9-point budget/noise sweep, real-KV score-selected anchors matched full-cache accuracy while random, recency, and uniform controls stayed near budget-fraction accuracy. A learned-transformer control failed to learn the task, limiting direct model claims.

## Boundaries and scale limits

No paper-scale validation; successful evidence is synthetic. The attempted small learned-transformer recall model did not learn full-context recall, so pretrained or successfully trained model-level evidence remains missing.

## Claim scope

Controlled synthetic KV-cache recall only: real query-to-key score anchors preserve full-cache recall under small fixed budgets when the recall-relevant key is identifiable in the KV geometry.

## Why it stopped

No-paper useful signal: synthetic KV evidence supports the mechanism, but the direct learned-transformer evaluation was not competent enough to validate model-level long-context recall.

## Recommended next action

Run a deeper direct test on a capable recall model with full-cache accuracy at least 80%, comparing real-KV anchors against random, recency, uniform, and score-aware ablations at matched budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-KV anchors on a competent learned recall model
- Success threshold: Full-cache accuracy >= 80%; real-KV anchor accuracy within 10 percentage points of full cache; real-KV anchors exceed the best random/recency/uniform baseline by >= 20 percentage points over at least 3 seeds or equivalent bootstrap confidence.
- Stop condition: Stop as negative if no competent full-cache recall model is obtained within the allocated run, or if real-KV anchors fail to beat the best position/random control by 20 percentage points once full-cache recall is >= 80%.

## Evidence references

- Artifact root: `<local-path>/projects/real-kv-anchor-selection-for-long-context-recall-6b026f5518`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
