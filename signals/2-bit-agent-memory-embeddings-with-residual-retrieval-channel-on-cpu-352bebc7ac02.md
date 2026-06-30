# 2-bit agent memory embeddings with residual retrieval channel on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-agent-memory-embeddings-with-residual-retrieval-channel-on-cpu-352bebc7ac02`
Run ID: `2-bit-agent-memory-embeddings-with-residual-retrieval-channel-on-cpu-352bebc7ac02-20260628T024313350140+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1bcbea3c9b85

## What looked useful

Residual-channel reranking consistently recovers a small amount of ranking quality lost by 2-bit quantization, but the gain is modest and does not close the large float32 quality gap.

## Boundaries and scale limits

Synthetic embeddings only; no live agent replay, no production embedding model, no learned residual code, no downstream task success metric, and no optimized CPU reranker. The 2-bit residual variant remained far below float32 recall@1 and was slower than coarse retrieval due to Python reranking.

## Claim scope

On a deterministic synthetic clustered retrieval benchmark with 24,000 memories, 2,400 queries, 128-dimensional vectors, and three seeds, a compact int8 residual projection reranker improved 2-bit embedding recall@1 by 0.0294 absolute and MRR by 0.0261 while retaining 5.82x estimated memory compression versus float32.

## Why it stopped

Bounded synthetic evidence supports a small mechanism effect but is not direct/full validation and is not paper-ready.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded test should use real agent-memory embeddings and a learned or structured residual channel with optimized CPU reranking.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-embedding residual channel test for 2-bit agent memory retrieval
- Success threshold: Residual-channel 2-bit retrieval improves recall@1 by at least 0.05 absolute over 2-bit-only, retains at least 4x memory compression versus float32, and runs within 2x float32 CPU query latency on the same corpus.
- Stop condition: Stop if residual gain is below 0.03 absolute recall@1 on real embeddings, compression falls below 4x, or optimized CPU latency exceeds 2x float32 retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-agent-memory-embeddings-with-residual-retrieval-channel-on-cpu-352bebc7ac02`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
