# Anchor-Gated KV Compression for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-gated-kv-compression-for-long-context-6df55d4444e1`
Run ID: `anchor-gated-kv-compression-for-long-context-6df55d4444e1-20260602T223732726205+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/62cb44e2974e

## What looked useful

Anchor-gated KV compression won all 18 mixed-workload cells versus score-only salience with mean accuracy 0.541 vs 0.381, but lost all 12 old-anchor-only ablation cells to score-only because the recency reserve reduced anchor capacity.

## Boundaries and scale limits

No trained LLM, no natural corpus, no perplexity or generation metric, no layerwise KV dynamics, and no optimized serving-kernel throughput measurement.

## Claim scope

Controlled synthetic attention proxy: fixed-budget KV selection for mixed old-anchor and recent-reference retrieval at sequence lengths 2048-8192 and budgets 64-256 on one GB10 GPU.

## Why it stopped

Proxy evidence is useful but mixed: the mechanism helps mixed old-plus-recent retrieval and hurts pure old-anchor retrieval; no full LLM validation was performed.

## Recommended next action

Run a bounded GPT-2-small-class direct evaluation with the same compression controls on long-context retrieval and perplexity before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2-small Anchor-Gated KV Compression Evaluation
- Success threshold: Anchor-gated improves mixed retrieval accuracy by at least 10 percentage points over the best compressed baseline at the same KV budget while keeping perplexity degradation within 5% of the best compressed baseline and documenting the old-anchor-only tradeoff.
- Stop condition: Stop if anchor-gated fails to beat score-only or sliding-window on mixed retrieval in two matched-budget settings, or if perplexity degradation exceeds 5% without a compensating retrieval gain.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-compression-for-long-context-6df55d4444e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
