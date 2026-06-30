# Semantic Operator Doctrine vs Flat Vector Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `semantic-operator-doctrine-vs-flat-vector-memory-300142d613e8`
Run ID: `semantic-operator-doctrine-vs-flat-vector-memory-300142d613e8-20260620T073742135582+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/8326b63f3b9a

## What looked useful

Layered doctrine memory reached 3840/3840 accuracy versus 636/3840 for flat retrieval in the main run, and retained a roughly 0.83-0.85 accuracy advantage across the noise sweep. The mechanism signal is useful, but it is not paper-ready because the structured memory receives idealized fields.

## Boundaries and scale limits

Synthetic rule-ID scoring only; no real operator traces, no LLM answer generation, no production embedding model, and no noisy extraction into structured doctrine fields.

## Claim scope

In a deterministic synthetic repeated-agent replay benchmark with clean operator/domain/current-doctrine structure, layered doctrine memory avoids superseded-doctrine and transcript-noise conflicts that cause flat lexical vector retrieval to fail.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy and gives the layered strategy clean structured fields; it supports the mechanism but not a full validation.

## Recommended next action

Run a bounded deepen follow-up on real or realistic repeated-agent traces with production embeddings, metadata-filtered flat retrieval, noisy doctrine extraction, and LLM-backed answer scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic Trace Doctrine Memory vs Filtered Vector Retrieval
- Success threshold: Layered doctrine memory improves action accuracy by at least 10 percentage points over the strongest flat-vector baseline while not increasing latency by more than 2x on the bounded corpus.
- Stop condition: Stop if the filtered flat-vector baseline matches layered accuracy within 5 percentage points or if extraction errors erase the layered advantage.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-operator-doctrine-vs-flat-vector-memory-300142d613e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
