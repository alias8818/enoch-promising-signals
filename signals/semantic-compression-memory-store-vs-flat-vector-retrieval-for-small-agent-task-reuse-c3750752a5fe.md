# Semantic compression memory store vs flat vector retrieval for small agent task reuse

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `semantic-compression-memory-store-vs-flat-vector-retrieval-for-small-agent-task-reuse-c3750752a5fe`
Run ID: `semantic-compression-memory-store-vs-flat-vector-retrieval-for-small-agent-task-reuse-c3750752a5fe-20260612T210901664344+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5ed6553a91ed

## What looked useful

Across 60 condition rows, compressed retrieval achieved 0.9968 mean top-1 accuracy versus 0.9933 for flat retrieval, reduced retrieved context by 59.4% on average, and reduced mean query latency from 4.364 ms to 0.553 ms. The useful signal is memory/context efficiency, not a paper-grade accuracy breakthrough.

## Boundaries and scale limits

Synthetic structured traces only; no real agent corpus, no LLM summarizer, no dense embedding/vector database baseline, no downstream task-completion evaluation, and memory sizes capped at 144 procedures with 8 traces per procedure.

## Claim scope

On a bounded synthetic benchmark of structured recurring agent task traces, semantic compression into one invariant procedure summary per task preserved near-ceiling top-1 procedure retrieval, slightly improved accuracy versus flat TF-IDF retrieval over raw traces, and substantially reduced retrieved context and lookup latency.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy and the accuracy gain over a simple flat baseline is small despite strong context and latency reductions.

## Recommended next action

Run a bounded follow-up on real or semi-real agent traces using LLM or learned compression, dense embedding retrieval, and downstream task-reuse success as the primary metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semantic Compression Memory on Real Agent Task Reuse Traces
- Success threshold: Compressed memory must be within 2 percentage points of the best flat/hybrid baseline on downstream reuse success while reducing retrieved context tokens by at least 40% and not increasing p95 retrieval latency.
- Stop condition: Stop if compressed memory loses more than 5 percentage points downstream success versus flat dense retrieval or fails to reduce retrieved context by at least 25%.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-compression-memory-store-vs-flat-vector-retrieval-for-small-agent-task-reuse-c3750752a5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
