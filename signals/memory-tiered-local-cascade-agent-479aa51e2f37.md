# Memory-Tiered Local Cascade Agent

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `memory-tiered-local-cascade-agent-479aa51e2f37`
Run ID: `memory-tiered-local-cascade-agent-479aa51e2f37-20260611T212913881800+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3da898a765a2

## What looked useful

At 16,384 memories, flat search reached recall@8=1.000 with 16,384 vector scores/query. The tiered cascade with top_chunks=4 reduced scoring by 21.45x but reached only recall@8=0.126. A sensitivity sweep up to top_chunks=128 improved recall@8 to 0.736 but dropped reduction below the 4x success threshold.

## Boundaries and scale limits

Synthetic vectors only; no real agent traces, natural-language embeddings, LLM answer evaluation, learned routing, semantic clustering, or large-scale serving benchmark. CPU-only local run with 1,000 queries per condition.

## Claim scope

A naive local memory cascade with a 128-item working tier and chronological fixed-size archival chunks represented by simple centroids did not preserve target-fact retrieval recall on a synthetic 16,384-memory benchmark.

## Why it stopped

Proxy early falsification rather than full validation: the tested cascade missed the recall target by a wide margin under synthetic retrieval, and increasing chunk fanout did not recover near-flat recall while preserving the required 4x reduction.

## Recommended next action

Stop this run as a proxy early falsification of the naive chronological-centroid cascade; a bounded follow-up should test semantic clustering or a learned router against the same recall and vector-score thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semantic-clustered memory tiers for local cascade retrieval
- Success threshold: At 16,384 or more memories, semantic or learned-router cascade reaches recall@8 >= 0.95 while using at least 4x fewer vector scores/query than flat_all, and beats the chronological centroid cascade by at least 20 recall points.
- Stop condition: Stop if recall@8 remains below 0.90 at 16k memories under any configuration that preserves at least 4x vector-score reduction.

## Evidence references

- Artifact root: `<local-path>/projects/memory-tiered-local-cascade-agent-479aa51e2f37`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
