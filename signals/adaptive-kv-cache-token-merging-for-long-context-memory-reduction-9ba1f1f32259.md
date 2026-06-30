# Adaptive KV-Cache Token Merging for Long-Context Memory Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-kv-cache-token-merging-for-long-context-memory-reduction-9ba1f1f32259`
Run ID: `adaptive-kv-cache-token-merging-for-long-context-memory-reduction-9ba1f1f32259-20260524T234243434006+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/95c5fb3a129e

## What looked useful

KV merging is a strong mechanism versus dropping tokens in this probe, with adaptive_kv relative MSE at 0.125 cache ratio of 0.000266 clustered, 0.000196 mixed, 0.000333 random, and 0.04946 adversarial, compared with recent_only from 0.188 to 7.256. However, uniform block merging was usually equal or better, weakening the adaptive novelty claim.

## Boundaries and scale limits

No pretrained LLM was served or evaluated; no perplexity, retrieval, real KV trace, or 7B+ throughput evidence was produced. Sequence length was 768, hidden dimension 64, 96 query vectors, 6 trials, synthetic clustered/mixed/random/adversarial regimes.

## Claim scope

Synthetic attention-level probe only: merging KV tokens preserves full-attention outputs far better than recency-only truncation at 0.125-0.5 cache ratios, but the tested adaptive KV merge rule does not consistently outperform simple uniform block merging.

## Why it stopped

No-paper useful signal: synthetic attention-level evidence supports merge-over-drop but not a distinct adaptive-merging advantage over a simple merge baseline.

## Recommended next action

Stop paper path for this run; run one bounded real-model deepen test on GPT-2-small-class KV traces comparing adaptive_kv, uniform_blocks, and recency/eviction baselines on perplexity or retrieval at matched cache budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real GPT-2 KV Trace Test for Adaptive Token Merging
- Success threshold: Adaptive_kv must reduce task degradation by at least 20% relative to uniform_blocks at one or more aggressive cache ratios without exceeding 10% compression-time overhead relative to attention compute for the tested setup.
- Stop condition: Stop if adaptive_kv is not better than uniform_blocks on the primary task metric at 0.25 cache ratio, or if compression overhead dominates any memory benefit in the bounded setup.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-kv-cache-token-merging-for-long-context-memory-reduction-9ba1f1f32259`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
