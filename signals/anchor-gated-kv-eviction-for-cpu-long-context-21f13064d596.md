# Anchor-Gated KV Eviction for CPU Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-gated-kv-eviction-for-cpu-long-context-21f13064d596`
Run ID: `anchor-gated-kv-eviction-for-cpu-long-context-21f13064d596-20260530T030030961553+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e595c1ffba14

## What looked useful

Anchor-gated retention improved mean hit-rate by +0.089 to +0.143 over the best baseline on anchor_recall at budgets 256/512 and by +0.130 to +0.275 on mixed_shift at budgets 256/512; it tied heavy-hitter at budget 1024 and carried slower Python update overhead than recency.

## Boundaries and scale limits

No real transformer, tokenizer, attention trace, perplexity, generation quality, batching, quantized KV layout, or production CPU serving path was tested. The policy received explicit anchor markers and a synthetic noisy gate signal.

## Claim scope

On deterministic synthetic long-context traces, an anchor-gated KV eviction policy improves retained target hit-rate over recency and often over a simple heavy-hitter baseline at tight and medium cache budgets when old section anchors are recurring targets.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic trace-level mechanism support, not direct model quality or serving evidence.

## Recommended next action

Run a bounded model-backed follow-up using a small local transformer cache modification on needle/retrieval long-context tasks before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-backed anchor-gated KV eviction on small long-context retrieval tasks
- Success threshold: At two or more KV budgets, anchor-gated improves retrieval accuracy by at least 5 percentage points over the best baseline while adding no more than 15% decode latency versus the closest non-recency baseline.
- Stop condition: Stop if anchor-gated does not beat both recency and heavy-hitter on model-backed retrieval accuracy at any tested budget, or if policy overhead exceeds 25% without an accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-eviction-for-cpu-long-context-21f13064d596`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
