# Embedding and LLM replay of layered versus flat memory on repeated operator traces

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `embedding-and-llm-replay-of-layered-versus-flat-memory-on-56f432be51`
Run ID: `embedding-and-llm-replay-of-layered-versus-flat-memory-on-56f432be51-20260630T083802063797+0000`

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

- Parent run decision: Layered Memory Architecture vs Flat Retrieval on Repeated Operator Tasks: enoch://control-plane/projects/layered-memory-architecture-vs-flat-retrieval-on-repeated-operator-tasks-52b19a4df1ad/runs/layered-memory-architecture-vs-flat-retrieval-on-repeated-operator-tasks-52b19a4df1ad-20260630T080052947848+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/745fc4966091

## What looked useful

Naive vector retrieval over raw repeated traces becomes stale as operator state drifts, falling to 15.53% exact replay accuracy at drift 0.18 in the main run. Layered state memory reaches 100%, but a simple metadata-filtered latest-event flat baseline also reaches 100%, so the measured advantage is state/metadata structure rather than a novel layered-memory replay effect.

## Boundaries and scale limits

Synthetic traces only; lexical TF-IDF embeddings only; deterministic constrained replay only; no real LLM, neural embedding model, production trace corpus, noisy summarizer, or matched token-budget LLM context experiment.

## Claim scope

On synthetic repeated operator traces with explicit operator/workflow identifiers and four drifting command parameters, layered current-state memory fixes stale-context failures from naive embedding-only flat retrieval, but it does not outperform a flat raw-event memory with operator/workflow metadata filtering and latest-event selection.

## Why it stopped

Bounded synthetic proxy falsified the broad layered-versus-flat advantage: layered beats naive embedding-only flat retrieval but ties an obvious filtered-recency flat baseline.

## Recommended next action

Stop this run as no-paper useful signal; any continuation should test real LLM replay with neural embeddings and a metadata-filtered flat baseline on realistic traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM replay with neural embeddings versus metadata-filtered flat memory
- Success threshold: Layered memory beats the metadata-filtered flat baseline by at least 5 percentage points exact replay accuracy or reduces stale-context errors by at least 25% relative at matched context budget across at least 3 seeds or trace shards.
- Stop condition: Stop if the metadata-filtered flat baseline matches layered memory within 2 percentage points exact accuracy and stale-context error, or if summary noise makes layered memory worse at matched context budget.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-and-llm-replay-of-layered-versus-flat-memory-on-56f432be51`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
