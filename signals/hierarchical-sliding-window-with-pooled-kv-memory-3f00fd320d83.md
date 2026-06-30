# Hierarchical Sliding Window with Pooled KV Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-sliding-window-with-pooled-kv-memory-3f00fd320d83`
Run ID: `hierarchical-sliding-window-with-pooled-kv-memory-3f00fd320d83-20260604T232314765813+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8918b642850a

## What looked useful

Average pooled KV lost almost all distant exact retrieval signal, and static 16-slot exemplars recovered only about 25% of distant old-block targets at 27%-44% of full KV memory. A query-conditioned router upper bound recovered distant targets, suggesting the viable branch is learned or indexed routing rather than naive pooled KV.

## Boundaries and scale limits

No transformer training, no GPT-2-small-class baseline, no perplexity measurement, no learned router, and no real decode throughput measurement. The query-router result is an upper bound because it selects old-block entries after seeing the query.

## Claim scope

Bounded synthetic exact-retrieval probe for hierarchical sliding-window attention with static pooled KV memory at sequence lengths 512-4096, window 128, block 64, and up to 16 retained old-block slots.

## Why it stopped

Proxy early falsification: the directly tested static pooled KV mechanisms do not preserve exact long-range bindings, while the successful query-conditioned upper bound is not the same mechanism and is not full validation.

## Recommended next action

Stop this static pooled-KV claim as no-paper; run a separate bounded learned-router experiment that must recover at least 90% distant exact retrieval without scanning all old keys at query time.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Block Router for Pooled KV Memory
- Success threshold: At sequence lengths 1024-4096, recover at least 90% distant exact retrieval with no more than 25% full-KV memory and router compute below full old-key scan cost.
- Stop condition: Stop if the router either scans all old keys, falls below 75% distant retrieval at 25% memory, or has compute cost comparable to full attention.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-sliding-window-with-pooled-kv-memory-3f00fd320d83`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
