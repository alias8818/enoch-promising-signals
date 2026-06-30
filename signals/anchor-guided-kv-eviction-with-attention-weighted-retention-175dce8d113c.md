# Anchor-Guided KV Eviction with Attention-Weighted Retention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-guided-kv-eviction-with-attention-weighted-retention-175dce8d113c`
Run ID: `anchor-guided-kv-eviction-with-attention-weighted-retention-175dce8d113c-20260528T164353295896+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ad0d66fa7103

## What looked useful

Anchor-weighted retention achieved near-perfect output cosine on anchor-dominant traces and beat recency by +0.278 to +0.931 cosine on many-anchor traces, but failed under tight recency-dominant budget and depended strongly on an anchor prior.

## Boundaries and scale limits

No trained LLM, no real tokenizer/prompt anchor detection, no multi-layer KV serving, no perplexity/task-accuracy measurement, and no latency or memory-bandwidth validation. Results are 1024-token synthetic traces with 180 sequences per scenario.

## Claim scope

Synthetic causal-attention proxy over generated long-context traces: anchor-guided attention-weighted KV retention can preserve full-attention outputs much better than recency, uniform, and attention-only policies when future queries depend on identifiable old anchors and cache budget is sufficient.

## Why it stopped

Proxy evidence is mixed: it supports the anchor-retention mechanism in scoped synthetic settings but early-falsifies a fixed universal anchor-weighted policy under recency-dominant tight budgets.

## Recommended next action

Stop this run as a proxy useful signal; next run should test adaptive anchor/recency gating with non-oracle anchor detection on a small open transformer long-context retrieval benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Anchor-Recency KV Eviction on a Small Transformer
- Success threshold: Adaptive anchor/recency-gated eviction improves long-context retrieval accuracy by at least 10% relative over recency or heavy-hitter baselines at the same cache budget while degrading local recency tasks by less than 2% absolute.
- Stop condition: Stop if adaptive gating cannot beat both recency and heavy-hitter baselines on retrieval, or if local-task degradation exceeds 2% absolute at budgets where retrieval improves.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-guided-kv-eviction-with-attention-weighted-retention-175dce8d113c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
