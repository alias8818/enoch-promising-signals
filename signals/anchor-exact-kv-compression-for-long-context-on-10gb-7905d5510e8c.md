# Anchor-Exact KV Compression for Long Context on 10GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-exact-kv-compression-for-long-context-on-10gb-7905d5510e8c`
Run ID: `anchor-exact-kv-compression-for-long-context-on-10gb-7905d5510e8c-20260603T201043739748+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c067134b618a

## What looked useful

Exact anchors are useful only when the anchor policy covers salient tokens. In anchor-aligned traces, anchor-exact counted compression reached mean cosine 0.99985 to dense attention and mean relative L2 0.0178 at mean KV-entry ratio 0.0602. In off-anchor needle traces, anchor-exact was effectively unchanged from no-anchor compression, showing static anchors do not solve arbitrary needle retention.

## Boundaries and scale limits

Evidence is synthetic only: no real transformer perplexity, retrieval QA, production decode kernel, or actual 10GB memory-pressure serving test was run. Sequence lengths were 4096 to 16384 with dim 128 and 64 queries.

## Claim scope

Synthetic CUDA attention probes show that count-corrected block KV compression with exact static anchors can closely match dense attention when salient tokens are on anchor positions, while using about 2.7% to 10.0% of dense KV entries in the tested configurations.

## Why it stopped

No-paper closure: the result is a synthetic mechanism signal with a clear off-anchor failure mode, not direct model-quality or serving evidence.

## Recommended next action

Run a bounded real-model deepen test with dynamic anchor promotion on long-context retrieval/perplexity tasks, comparing dense KV, static periodic anchors, and dynamic anchor-exact compression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dynamic Anchor Promotion for Anchor-Exact KV Compression
- Success threshold: At a matched KV-entry ratio below 0.15, dynamic anchor promotion recovers at least 95% of dense retrieval accuracy or keeps perplexity within 5% of dense while outperforming static anchors on off-anchor needle cases.
- Stop condition: Stop if dynamic promotion cannot beat static anchors on off-anchor retrieval at matched KV budget, or if the required metadata/selection overhead erases the memory or decode benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-exact-kv-compression-for-long-context-on-10gb-7905d5510e8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
