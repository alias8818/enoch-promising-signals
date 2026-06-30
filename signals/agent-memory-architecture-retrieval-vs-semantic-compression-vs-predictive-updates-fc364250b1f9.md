# Agent Memory Architecture: Retrieval vs Semantic Compression vs Predictive Updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-architecture-retrieval-vs-semantic-compression-vs-predictive-updates-fc364250b1f9`
Run ID: `agent-memory-architecture-retrieval-vs-semantic-compression-vs-predictive-updates-fc364250b1f9-20260614T055232785707+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/498077bb1909

## What looked useful

Predictive updates reached 1.000 accuracy versus 0.628 for transcript search and 0.632 for semantic compression. Predictive updates used 2,132 final memory tokens versus 27,934 for transcript search, a 0.076 final-memory ratio.

## Boundaries and scale limits

Synthetic parser-addressable task only; no real user transcripts, no LLM extraction errors, no embedding retrieval baseline, no production agent orchestration, and no downstream task-quality evaluation.

## Claim scope

In a deterministic synthetic repeated-agent replay benchmark with 24 streams, 1,920 noisy update events, and 576 latest-fact queries, structured predictive updates preserved mutable state more accurately than lexical transcript search and fixed-slot semantic compression while using much less memory than transcript search.

## Why it stopped

No paper-positive closure because the result is useful but synthetic and architecture-favoring; it supports the mechanism but is not a full validation.

## Recommended next action

Run a bounded direct replay on redacted real or high-fidelity semi-real agent traces with equalized noisy extractors and embedding/LLM summary baselines before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic replay validation for predictive agent memory updates
- Success threshold: Predictive updates improve latest-state accuracy by >=10 percentage points over the best baseline while using no more memory than semantic compression and less than 25% of transcript-search memory.
- Stop condition: Stop if predictive updates fail to beat the best baseline by 5 percentage points on a 100-query pilot or if extraction noise makes structured updates less accurate than semantic compression.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-architecture-retrieval-vs-semantic-compression-vs-predictive-updates-fc364250b1f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
