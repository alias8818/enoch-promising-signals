# Real-trace validation of norm-preserving 1-bit memory retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-validation-of-norm-preserving-1-bit-memory-retr-79cad8e9d2`
Run ID: `real-trace-validation-of-norm-preserving-1-bit-memory-retr-79cad8e9d2-20260613T170444729639+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Norm-preserving extreme quantization for agent memory traces: enoch://control-plane/projects/norm-preserving-extreme-quantization-for-agent-memory-traces-44142d3ca50d/runs/norm-preserving-extreme-quantization-for-agent-memory-traces-44142d3ca50d-20260613T164527337666+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b2e9f148a6b9

## What looked useful

Across six 512-dimensional runs, norm-preserving 1-bit retrieval had mean recall@10 0.5790 (min 0.5699) and mean NDCG@10 0.9098; recall gain over unit sign-only averaged 0.1373 with min 0.1260. Random-sign recall stayed near chance and int8 stayed near exact.

## Boundaries and scale limits

6000 memory keys, 1000 queries, AG News only, deterministic text-derived embeddings rather than learned transformer or production traces; no packed-bit latency/bandwidth kernel and no million-scale memory store tested.

## Claim scope

On a small AG News real text-derived retrieval trace using hashed TF-IDF plus dense random projection, storing key sign bits plus original key norm preserved useful top-10 dense-retrieval structure at d=512 and consistently outperformed unit sign-only memory.

## Why it stopped

Tier 1 controlled direct test completed and produced a useful mechanism signal, but evidence is no-paper because traces are small text-derived projections rather than learned transformer or production memory traces.

## Recommended next action

Run the same exact dense-vs-norm-preserving-1bit-vs-unit-sign-vs-int8 retrieval test on frozen transformer embeddings from at least two public corpora before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-trace validation of norm-preserving 1-bit memory retrieval
- Success threshold: For each corpus, norm-preserving 1-bit recall@10 >= 0.50, NDCG@10 >= 0.85, and recall@10 gain over unit sign-only >= 0.05 at d>=512.
- Stop condition: Stop as negative if either corpus falls below 0.45 recall@10 or the norm-preserving gain over unit sign-only is below 0.03 after three reproducible shards/seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-validation-of-norm-preserving-1-bit-memory-retr-79cad8e9d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
