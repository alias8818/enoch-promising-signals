# Real-Agent Layered Memory Compliance Study

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-layered-memory-compliance-study-447157f57f`
Run ID: `real-agent-layered-memory-compliance-study-447157f57f-20260619T132958412808+0000`

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

- Parent run decision: Operator-Doctrine Layered Memory for Repeated Local Agent Tasks: enoch://control-plane/projects/operator-doctrine-layered-memory-for-repeated-local-agent-tasks-cfb799ce9023/runs/operator-doctrine-layered-memory-for-repeated-local-agent-tasks-cfb799ce9023-20260619T130942112611+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d2902e151206

## What looked useful

Main run: flat memory compliance 0.000, task success 0.000, stale violation 1.000, mean prompt tokens 390.75; layered memory compliance 0.750, task success 0.750, stale violation 0.125, mean prompt tokens 255.00. Layered exceeded the parent +15 percentage point compliance threshold by +75 points while using 34.7% fewer prompt tokens.

## Boundaries and scale limits

Evidence is limited to eight synthetic-but-AGENTS-style tasks, one small instruction model, simulated tool actions, deterministic decoding, and automated scoring. It does not validate actual repository edits, multi-turn agent recovery, blinded human scoring, larger model families, embedding retrievers, or production memory systems.

## Claim scope

In a controlled Tier 1 real-LLM action-selection harness using Qwen/Qwen2.5-1.5B-Instruct across four AGENTS-style local task suites and eight tasks, layered operator/project/procedure/episodic memory with precedence filtering improved instruction compliance and reduced stale-memory violations versus a flat retrieved memory pool.

## Why it stopped

Closed as no-paper useful signal: the controlled real-LLM threshold was met, but the study is too small and simulated-tool based for publication readiness.

## Recommended next action

Run a medium sandboxed real-repository execution study with randomized flat/layered memory conditions, actual safe tool execution, saved traces, and blinded compliance scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sandboxed Real-Repository Layered Memory Execution Study
- Success threshold: Layered memory improves blinded instruction-compliance score by at least 15 percentage points over flat memory, reduces stale-memory violations, does not reduce task success, and keeps mean prompt tokens within 25% of flat memory.
- Stop condition: Stop if the first two repositories show less than 5 percentage point layered compliance improvement or if layered prompt overhead exceeds 50% without fewer stale-memory violations.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-layered-memory-compliance-study-447157f57f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
