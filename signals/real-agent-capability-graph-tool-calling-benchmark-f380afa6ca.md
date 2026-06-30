# Real-agent capability graph tool-calling benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-capability-graph-tool-calling-benchmark-f380afa6ca`
Run ID: `real-agent-capability-graph-tool-calling-benchmark-f380afa6ca-20260609T125005498914+0000`

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

- Parent run decision: Capability Graph Sandbox for Local Agents: enoch://control-plane/projects/capability-graph-sandbox-for-local-agents-8d12be1ca601/runs/capability-graph-sandbox-for-local-agents-8d12be1ca601-20260609T030551137751+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0b02e3d6188e

## What looked useful

Graph-aware planning achieved 100% success and 0 invalid calls, versus 10.83% for random-applicable, 0% for flat-name, 0% for local greedy, and 5.83% for 30% edge-dropout graph planning.

## Boundaries and scale limits

No real LLM agents, real-world APIs, natural-language ambiguity, or long-running workflows were tested; this is a Tier 1 mechanism sanity check, not external validation.

## Claim scope

In a controlled synthetic typed-tool benchmark, an executable capability graph discriminated a graph-aware shortest-path planner from flat, local, random, and corrupted-graph controls across 240 generated tasks.

## Why it stopped

Tier 1 controlled direct mechanism test passed, but it used deterministic synthetic planners and therefore is useful no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded real-agent follow-up using the saved executable task format, comparing flat tool lists versus capability-graph annotations with at least two LLM agent loops.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM agents on executable capability-graph tool tasks
- Success threshold: Graph-annotated condition improves success by at least 20 percentage points over flat-list condition while reducing invalid calls by at least 25% relative on 100 or more tasks per agent.
- Stop condition: Stop if both tested real agents fail to improve by 10 percentage points or if invalid-call rates do not decrease under graph annotations.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-capability-graph-tool-calling-benchmark-f380afa6ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
