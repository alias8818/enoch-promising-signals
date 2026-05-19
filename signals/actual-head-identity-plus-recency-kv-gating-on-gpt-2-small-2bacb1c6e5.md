# Actual-head identity-plus-recency KV gating on GPT-2-small attention traces

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `actual-head-identity-plus-recency-kv-gating-on-gpt-2-small-2bacb1c6e5`
Run ID: `actual-head-identity-plus-recency-kv-gating-on-gpt-2-small-2bacb1c6e5-20260519T164136455482+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Actual-head identity-plus-recency KV gating on GPT-2-small attention traces: internal_generated:actual-head-identity-plus-recency-kv-gating-on-gpt-2-small-2bacb1c6e5

## What looked useful

Main seq_len=128 run over fixed seeds 17,29,43 found attention-mass recall deltas for head identity+recency vs recency of +0.02809 at 12.5% KV, +0.04918 at 25%, and +0.19273 at 50%; seq_len=256 robustness over seeds 17,29 found +0.02452, +0.04542, and +0.19500. Deltas vs global identity+recency were only +0.00026/+0.00114/+0.01030 for seq_len=128 and +0.00013/+0.00098/+0.01003 for seq_len=256.

## Boundaries and scale limits

Evidence is offline dense-attention trace retention only. No end-to-end KV-pruned inference, perplexity, generation quality, latency, memory, larger-model, multi-dataset, or long-context serving validation was run.

## Claim scope

On GPT-2-small WikiText attention traces, a per-layer/per-head token-identity-plus-recency gate improves held-out past-key attention-mass recall over recency-only and identity-only controls at 12.5%, 25%, and 50% KV budgets. The actual-head-specific component adds only tiny gains over a global identity-plus-recency control at 12.5% and 25% budgets, with a larger but still trace-only gain at 50%.

## Why it stopped

The mechanism is supported on direct GPT-2-small attention traces, but Tier 4 paper readiness is not met because the result is trace-only and actual-head specificity barely improves over a global identity-plus-recency control at tight KV budgets.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful trace evidence; do not launch another deepen/retry follow-up from this worker run unless the controller explicitly overrides the depth cap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/actual-head-identity-plus-recency-kv-gating-on-gpt-2-small-2bacb1c6e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
