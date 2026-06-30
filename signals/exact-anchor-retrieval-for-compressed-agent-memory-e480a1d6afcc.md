# Exact Anchor Retrieval for Compressed Agent Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-retrieval-for-compressed-agent-memory-e480a1d6afcc`
Run ID: `exact-anchor-retrieval-for-compressed-agent-memory-e480a1d6afcc-20260528T004413366451+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/93859ccdeb1f

## What looked useful

Lossy compressed-text retrieval reached only about 9.4% top-1, while an exact-anchor sidecar reached 100% candidate recall and 100% top-1 for globally unique anchors, at 25.3% to 56.8% of raw-token footprint depending on compression budget.

## Boundaries and scale limits

2,000 synthetic records per seed, 20 seeds, 240,000 total exact-anchor queries; no real agent traces, LLM-generated summaries, embedding retrievers, or production latency measurements.

## Claim scope

Synthetic benchmark of exact-anchor queries over compressed operational agent-memory records with ticket IDs, commit hashes, file paths, and handles.

## Why it stopped

Proxy/synthetic evidence supports the mechanism but is not direct/full validation and is not paper-ready.

## Recommended next action

Stop this run as synthetic useful-signal evidence; next run should test the same sidecar mechanism on trace-like or real agent memories with LLM compression and embedding/hybrid retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-based exact-anchor retrieval under LLM memory compression
- Success threshold: Anchor sidecar candidate recall >= 0.95, unique-anchor top-1 >= 0.95, and at least 25 percentage-point top-1 improvement over the best non-sidecar compressed-memory baseline.
- Stop condition: Stop if sidecar candidate recall falls below 0.90 on trace-like data or if non-sidecar hybrid retrieval matches sidecar top-1 within 5 percentage points at comparable storage.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-retrieval-for-compressed-agent-memory-e480a1d6afcc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
