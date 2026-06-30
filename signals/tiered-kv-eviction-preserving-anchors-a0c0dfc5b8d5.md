# Tiered KV Eviction Preserving Anchors

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiered-kv-eviction-preserving-anchors-a0c0dfc5b8d5`
Run ID: `tiered-kv-eviction-preserving-anchors-a0c0dfc5b8d5-20260608T073915238303+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/98a3a9dfd9b2

## What looked useful

Explicit anchor preservation retained anchors slightly more than heavy-hitter eviction, but did not improve attention-output fidelity. Heavy-hitter eviction already retained 92-98% of synthetic anchors, and tiered_anchor failed the preregistered >=20% anchor-query error reduction threshold across the main run and cache sweep.

## Boundaries and scale limits

No real transformer KV-cache implementation, no real text corpus, no multi-layer or multi-head model traces, no latency/kernel measurements, and no downstream perplexity or task accuracy. Results should not be treated as full LLM-serving validation.

## Claim scope

Synthetic causal-attention proxy with known early anchor tokens, sequence length 512, dimension 64, 16 anchors, cache sizes 24-128, and paired trials comparing recency, last-attention, heavy-hitter, and tiered anchor-preserving eviction.

## Why it stopped

Proxy early falsification: in paired synthetic attention trials, tiered_anchor was worse than heavy_hitter by 1.679% on anchor-query error in the main run and only ranged from 0.726% better to 2.240% worse across the cache sweep, far below the 20% success threshold.

## Recommended next action

Stop this paper path unless a real-trace replay shows anchors are missed by heavy-hitter eviction; the current result is a proxy early falsification, not a full validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace replay of anchor preservation versus heavy-hitter KV eviction
- Success threshold: Tiered anchor preservation must reduce anchor-query output error or improve retrieval accuracy by at least 10% relative to heavy_hitter at the same cache size, with no more than 5% degradation in mean output error or perplexity.
- Stop condition: Stop if heavy_hitter retains at least 95% of real anchor tokens or if tiered_anchor improves anchor-specific metrics by less than 5% at two cache budgets.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-eviction-preserving-anchors-a0c0dfc5b8d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
