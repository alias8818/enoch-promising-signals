# Real LLM agents on executable capability-graph tool tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-llm-agents-on-executable-capability-graph-tool-tasks-f9868fc36d`
Run ID: `real-llm-agents-on-executable-capability-graph-tool-tasks-f9868fc36d-20260609T181115302657+0000`

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

- Parent run decision: Real-agent capability graph tool-calling benchmark: enoch://control-plane/projects/real-agent-capability-graph-tool-calling-benchmark-f380afa6ca/runs/real-agent-capability-graph-tool-calling-benchmark-f380afa6ca-20260609T125005498914+0000
- Parent run decision: Capability Graph Sandbox for Local Agents: enoch://control-plane/projects/capability-graph-sandbox-for-local-agents-8d12be1ca601/runs/capability-graph-sandbox-for-local-agents-8d12be1ca601-20260609T030551137751+0000

## What looked useful

Executable validation and persistent capability-graph state are strongly supported as the mechanism in this harness: success stayed at 100% across 240 fixed-seed tasks with zero invalid calls, while flat BFS fell to 7.5% on medium and 0% on hard, and the no-exec-validation ablation was 0% on medium/hard.

## Boundaries and scale limits

The Tier 2 result is on generated local tool worlds and deterministic planner policies. A real local Qwen2.5-0.5B-Instruct backend was installed and smoke-tested, but CPU rollout was too slow for a medium fixed-seed LLM-agent comparison; only one corrected partial flat-prompt trial completed and failed.

## Claim scope

In deterministic executable tool worlds with hidden preconditions and misleading advertised affordances, a persistent executable capability-graph planner solved 80/80 easy, 80/80 medium, and 80/80 hard tasks with optimal call counts, while flat BFS and no-execution-validation baselines degraded sharply with task depth and distractors.

## Why it stopped

Mechanism evidence met the Tier 2 structure with fixed seeds, ablations, and baselines, but the central real-LLM-agent claim was not closed because the corrected local LLM rollout was only a CPU smoke test and did not complete a medium comparison.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded deepen test should run completed real-LLM graph-scaffold versus flat-prompt rollouts on the same executable tasks using a faster inference backend or API.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fixed-seed real LLM rollouts on executable capability-graph tasks
- Success threshold: Graph-scaffold real LLM agent achieves at least 70% success on medium tasks and at least a 2x reduction in invalid calls versus flat prompting, with matched fixed-seed repeatability and no parser-only explanation for the gain.
- Stop condition: Stop if graph-scaffold success is below 50% on medium tasks, if gains disappear after parser/malformed-output accounting, or if rollout throughput cannot complete 80 medium seeds within the allocated backend budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-agents-on-executable-capability-graph-tool-tasks-f9868fc36d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
