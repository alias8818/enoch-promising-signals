# Quantized Agent Memory Stores for Long-Home Sessions

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-agent-memory-stores-for-long-home-sessions-350754abeb07`
Run ID: `quantized-agent-memory-stores-for-long-home-sessions-350754abeb07-20260629T030931977286+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/34fc6b6ab6e3

## What looked useful

Int8 is the strongest implementation candidate for quantized agent memory stores: at 100k memories/noise=0.16 it used 38.8 MB vs 153.6 MB fp32 with identical recall@1 and recall@5; at harder noise=0.24 it retained recall@5 0.5795 vs fp32 0.5815. Int4 reached 7.84x compression but top-1 agreement degraded under ambiguity, and binary sign lost too much recall.

## Boundaries and scale limits

Synthetic latent-topic vectors and target-known noisy queries only; no real home-session corpus, production ANN/packed-kernel implementation, persistence workload, or end-to-end agent task evaluation. Maximum tested store size was 100k memories and 2,000 queries per condition.

## Claim scope

In a bounded synthetic long-home-session vector retrieval benchmark up to 100k 384-dimensional memories, per-vector int8 quantized storage preserved fp32 recall@5/top-1 behavior while reducing vector bytes by about 4x; int4 was useful only in easier retrieval settings; binary sign quantization was not viable.

## Why it stopped

No-paper closure: this is useful bounded synthetic evidence for the memory-store mechanism, not direct real-home-session or production-index validation.

## Recommended next action

Run a bounded deepen test on real or high-fidelity home-session memory text embedded with a fixed model, comparing fp32/int8/int4/binary stores with labeled retrieval targets and a production-style persisted index.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Embedding Quantized Memory Store Retrieval for Home Sessions
- Success threshold: int8 achieves >=98% of fp32 recall@5 and >=0.98 top-1 agreement while using <=27% of fp32 vector bytes; int4 is considered promising only if recall@5 is within 0.02 absolute of fp32 after reranking.
- Stop condition: Stop if int8 recall@5 falls below 95% of fp32 or top-1 agreement below 0.95 on real embeddings, or if persistence/update overhead eliminates the memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-agent-memory-stores-for-long-home-sessions-350754abeb07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
