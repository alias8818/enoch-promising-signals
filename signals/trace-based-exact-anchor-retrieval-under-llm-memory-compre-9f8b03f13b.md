# Trace-based exact-anchor retrieval under LLM memory compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-based-exact-anchor-retrieval-under-llm-memory-compre-9f8b03f13b`
Run ID: `trace-based-exact-anchor-retrieval-under-llm-memory-compre-9f8b03f13b-20260528T150020990709+0000`

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

- Parent run decision: Exact Anchor Retrieval for Compressed Agent Memory: enoch://control-plane/projects/exact-anchor-retrieval-for-compressed-agent-memory-e480a1d6afcc/runs/exact-anchor-retrieval-for-compressed-agent-memory-e480a1d6afcc-20260528T004413366451+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/93859ccdeb1f

## What looked useful

Exact anchors are easily lost by lossy text memory compression; a compact query-addressable side trace can preserve exact anchor retrieval when the trace budget covers the active subject-anchor mappings. Raw literal trace tables are budget-bound, but compact hash rows fit 24 mappings in 383 characters in this test.

## Boundaries and scale limits

Tier 1 controlled small direct test only: synthetic subjects and anchors, deterministic compression/retrieval, no real LLM-generated summaries, no real chat/tool/citation transcripts, and limited collision/eviction stress.

## Claim scope

In deterministic synthetic transcripts with 24 exact anchors and three distractors per anchor, a compact trace index using a 16-bit subject hash plus anchor payload preserved exact anchor retrieval at 100% across 384/768/1536-character compressed-memory budgets, while text-only compression baselines remained at 0.0% to 11.5%.

## Why it stopped

Mechanism supported in a controlled synthetic direct test, but evidence is not publication-grade because LLM-generated compression and realistic transcript distributions were not tested.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should integrate the compact trace index with an actual LLM summarization memory pipeline on realistic transcripts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compact trace index inside real LLM memory summarization
- Success threshold: At matched budget, compact trace plus LLM summary achieves >= 0.95 exact-hit rate and <= 0.01 false-positive rate, and improves exact-hit rate by at least 50 percentage points over summary-only memory on the high-density condition.
- Stop condition: Stop if compact trace exact-hit rate falls below 0.90 in two realistic datasets at budgets where the trace rows fit, or if collision/false-positive rate exceeds 0.05.

## Evidence references

- Artifact root: `<local-path>/projects/trace-based-exact-anchor-retrieval-under-llm-memory-compre-9f8b03f13b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
