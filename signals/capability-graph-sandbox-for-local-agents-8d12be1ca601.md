# Capability Graph Sandbox for Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `capability-graph-sandbox-for-local-agents-8d12be1ca601`
Run ID: `capability-graph-sandbox-for-local-agents-8d12be1ca601-20260609T030551137751+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0b02e3d6188e

## What looked useful

A typed capability graph is a viable sandbox primitive for local agents: reachability search eliminated invalid tool calls and recovered optimal chains, while a stronger precondition-filtered greedy baseline still failed 36.7% of generated tasks.

## Boundaries and scale limits

Proxy-only CPU simulation; no real LLM agent, no real local OS/tool APIs, no security isolation evaluation, no adversarial or natural-language benchmark, and no full multi-agent runtime.

## Claim scope

In a synthetic typed local-tool sandbox with 60 generated worlds and 600 start-goal tasks, explicit capability-graph BFS solved all tasks with zero invalid attempts and optimal path length, outperforming flat and locally-valid greedy tool selection baselines.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only rather than direct validation with real local agents or realistic tool runtimes.

## Recommended next action

Run a bounded real-agent follow-up where the same generated capability worlds are exposed as callable tools and compare LLM/tool-policy success with graph-state access versus schema text only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent capability graph tool-calling benchmark
- Success threshold: Graph-state agents improve success by at least 20 percentage points or reduce invalid calls by at least 50% against the strongest flat schema-text baseline on at least 300 held-out tasks.
- Stop condition: Stop if graph-state access does not improve success by 10 percentage points and does not reduce invalid calls by 25% on the first 100 held-out tasks.

## Evidence references

- Artifact root: `<local-path>/projects/capability-graph-sandbox-for-local-agents-8d12be1ca601`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
