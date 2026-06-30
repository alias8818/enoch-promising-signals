# Real-embedding QuantMem anchor preservation benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-embedding-quantmem-anchor-preservation-benchmark-59f46580df`
Run ID: `real-embedding-quantmem-anchor-preservation-benchmark-59f46580df-20260620T043552827774+0000`

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

- Parent run decision: QuantMem: 4-bit memory embeddings with exact-anchor preservation: enoch://control-plane/projects/quantmem-4-bit-memory-embeddings-with-exact-anchor-preservation-ea024ca97a85/runs/quantmem-4-bit-memory-embeddings-with-exact-anchor-preservation-ea024ca97a85-20260620T042442122382+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cc79cf7494ed

## What looked useful

Tier 1 direct test passed the preservation threshold: int4_anchor_sidecar had 0.0000 recall@1 drop and 0.0000 mean-rank delta versus float32 on 96 real-embedding anchor queries. Plain int4 also preserved recall@1, while int2/binary compression degraded retrieval, especially in the 96-anchor stress check.

## Boundaries and scale limits

Synthetic controlled corpus, one embedding model, no end-to-end agent loop, no production memory traces, and low absolute float32 recall@1. Results are mechanism-level and not a full QuantMem validation.

## Claim scope

Controlled CPU-local benchmark using sentence-transformers/all-MiniLM-L6-v2 embeddings on 48 synthetic anchor memories with 5 distractors each. Int8, int4, and int4 anchor-sidecar storage preserved float32 anchor retrieval rankings under this setup; int2/binary compression showed degradation.

## Why it stopped

No-paper closure: the benchmark produced a useful direct mechanism signal, but float32 recall@1 was only 0.4167 on the primary corpus, so the result is not strong enough for a paper or broad QuantMem claim.

## Recommended next action

Run a bounded deepen follow-up with a high-baseline corpus and stronger compression pressure to test whether explicit anchor preservation recovers lost recall when plain quantization actually damages retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: High-baseline anchor-sidecar recovery under stronger QuantMem compression
- Success threshold: Across the high-baseline corpus, anchor-sidecar variants recover at least 75% of recall@1 lost by the strongest damaging quantization setting and keep mean-rank delta <= 0.25 versus float32.
- Stop condition: Stop as negative if float32 recall@1 is below 0.80 after corpus cleanup, or if anchor-sidecar recovery is below 0.05 absolute recall@1 over the corresponding plain quantized baseline.

## Evidence references

- Artifact root: `<local-path>/projects/real-embedding-quantmem-anchor-preservation-benchmark-59f46580df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
