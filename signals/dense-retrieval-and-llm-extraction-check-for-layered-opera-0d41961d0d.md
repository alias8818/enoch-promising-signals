# Dense-retrieval and LLM-extraction check for layered operator memory

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `dense-retrieval-and-llm-extraction-check-for-layered-opera-0d41961d0d`
Run ID: `dense-retrieval-and-llm-extraction-check-for-layered-opera-0d41961d0d-20260630T180642968092+0000`

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

- Parent run decision: Layered agent memory with operator-model updates vs flat retrieval baseline: enoch://control-plane/projects/layered-agent-memory-with-operator-model-updates-vs-flat-retrieval-baseline-4d42271b1d70/runs/layered-agent-memory-with-operator-model-updates-vs-flat-retrieval-baseline-4d42271b1d70-20260630T173353857188+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3a52a3160c0f

## What looked useful

Dense retrieval missed the latest layer in top-5 for most symbolic operator-ID queries (0.0833 recall@5 in the primary run), while BM25 reached 1.0 recall@5 and deterministic exact extraction. FLAN-small/base produced 0.0 exact structured extraction even when BM25 supplied sufficient context.

## Boundaries and scale limits

Synthetic corpus only; 80-operator primary run and 40-operator FLAN-base cross-check; only MiniLM mean-pooled dense embeddings and FLAN-small/base extractors were tested; no production traces, trained retriever, hybrid search, constrained decoder, or larger LLM was evaluated.

## Claim scope

On a synthetic layered operator-memory benchmark with symbolic operator IDs, four overwrite layers, and distractor notes, MiniLM dense retrieval plus FLAN-small/base extraction does not reliably recover current operator state; BM25 plus a deterministic latest-layer extractor solves the same contexts.

## Why it stopped

Proxy early falsification: the synthetic task directly tested layered symbolic memory mechanics but not production traces or larger LLMs; dense retrieval and small-LLM extraction both failed clear local success checks.

## Recommended next action

Stop this dense-only plus small-LLM route; next bounded test should evaluate ID-aware hybrid retrieval with constrained structured extraction on the same benchmark before using larger or real operator-memory data.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid ID-aware retrieval and constrained extraction for layered operator memory
- Success threshold: Hybrid or ID-prefiltered retrieval recall@5 >= 0.98 and full-record extraction exact match >= 0.95 across at least 200 queries and two random seeds.
- Stop condition: Stop if retrieval recall@5 remains below 0.9 or constrained extraction remains below 0.85 exact match when gold latest-layer context is present.

## Evidence references

- Artifact root: `<local-path>/projects/dense-retrieval-and-llm-extraction-check-for-layered-opera-0d41961d0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
