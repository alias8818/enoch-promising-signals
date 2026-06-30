# Exact-anchor hybrid memory in an LLM-driven small-agent loop

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-hybrid-memory-in-an-llm-driven-small-agent-lo-434603d682`
Run ID: `exact-anchor-hybrid-memory-in-an-llm-driven-small-agent-lo-434603d682-20260526T215731355835+0000`

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

- Parent run decision: Exact-anchor hybrid memory in a real small-agent trace loop: enoch://control-plane/projects/exact-anchor-hybrid-memory-in-a-real-small-agent-trace-loo-81b679c6d2/runs/exact-anchor-hybrid-memory-in-a-real-small-agent-trace-loo-81b679c6d2-20260525T064101485724+0000
- Parent run decision: Exact-Anchor Episodic Memory for Small Agents: enoch://control-plane/projects/exact-anchor-episodic-memory-for-small-agents-38b3219c09d4/runs/exact-anchor-episodic-memory-for-small-agents-38b3219c09d4-20260525T035831395822+0000

## What looked useful

Exact anchor lookup is a strong practical control for dense/vector memory failures on arbitrary ids, but exact-token-capable lexical retrieval is a necessary baseline and was more accurate under anchor corruption.

## Boundaries and scale limits

CPU-only synthetic/template benchmark; no live LLM trajectories, no standard external agent benchmark, no natural model-generated memory writes or anchor-copy errors, and no large-scale serving or training validation.

## Claim scope

In a deterministic small-agent episodic-memory benchmark with 54,000 queries per policy, exact-anchor hybrid memory substantially outperformed normalized vector-like retrieval and exact-only ablations when exact anchors were present, but it did not outperform a raw lexical TF-IDF baseline that preserved anchor tokens.

## Why it stopped

Medium confirmation produced a mixed result: the mechanism beats normalized vector memory but fails to beat the stronger raw lexical exact-token baseline, so the current claim is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; if continuing this line, test fuzzy/checksummed anchor repair against the raw lexical baseline on real small-LLM agent traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fuzzy exact-anchor repair against raw lexical memory on small-LLM traces
- Success threshold: Hybrid with fuzzy/checksummed anchor repair is within 1 percentage point of raw lexical TF-IDF answer accuracy overall, is not worse on corrupted-anchor queries by more than 2 points, and is at least 5x faster in mean query latency across three or more seeds.
- Stop condition: Stop if raw lexical remains more than 2 percentage points more accurate overall or if real LLM traces rarely preserve enough anchor structure for repair to work.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-hybrid-memory-in-an-llm-driven-small-agent-lo-434603d682`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
