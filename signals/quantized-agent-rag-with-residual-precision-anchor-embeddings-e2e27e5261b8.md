# Quantized agent RAG with residual-precision anchor embeddings

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-agent-rag-with-residual-precision-anchor-embeddings-e2e27e5261b8`
Run ID: `quantized-agent-rag-with-residual-precision-anchor-embeddings-e2e27e5261b8-20260621T001300926660+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43b672c7910d

## What looked useful

Anchor-residual int4 improved mean recall@10 over per-vector int4 by +0.0066 to +0.0184 and over global int4 by +0.0715 to +0.0959 across scenarios; anchor-residual int3 improved over per-vector int3 by +0.0095 to +0.0395 and over global int3 by +0.1383 to +0.1743, winning all 30 scenario/seed/bit comparisons.

## Boundaries and scale limits

Synthetic retrieval-fidelity proxy only; no real text encoder, labeled RAG benchmark, approximate ANN index, query quantization, agent workflow, answer-quality metric, production latency, or update-cost validation was tested.

## Claim scope

On synthetic normalized embedding corpora with 10,000 corpus vectors, 800 queries, 256 dimensions, 192 fp16 anchors, three retrieval geometries, and five seeds, fp16 anchor plus low-bit residual corpus representations preserve float32 top-10 nearest-neighbor recall better than direct per-vector or global low-bit quantization.

## Why it stopped

Closed as no-paper useful signal because the result is a synthetic retrieval proxy, not direct full agent RAG validation.

## Recommended next action

Run a bounded real-embedding follow-up on a public retrieval dataset with storage-normalized baselines, ANN latency, and recall or nDCG against labeled relevance judgments.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real text RAG benchmark for anchor-residual embedding quantization
- Success threshold: Anchor-residual quantization improves recall@10 or nDCG@10 by at least 1 percentage point over the best storage-comparable direct low-bit baseline while keeping p95 query latency within 10% of that baseline.
- Stop condition: Stop if anchor-residual quantization fails to beat the best storage-comparable direct low-bit baseline on two public retrieval datasets or if ANN latency/build cost exceeds the baseline by more than 25% without a quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-agent-rag-with-residual-precision-anchor-embeddings-e2e27e5261b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
