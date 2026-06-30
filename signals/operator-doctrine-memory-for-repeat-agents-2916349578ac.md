# Operator-Doctrine Memory for Repeat Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-for-repeat-agents-2916349578ac`
Run ID: `operator-doctrine-memory-for-repeat-agents-2916349578ac-20260620T082302653028+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a49c4c28f6c4

## What looked useful

Doctrine memory reached 0.89125 held-out success and 0.08625 safety violation rate in the main benchmark, versus raw-log 0.195 success and 0.3825 safety violation, and no-memory 0.03156 success and 0.79219 safety violation. The doctrine advantage over raw recall persisted in context-budget sweeps, though raw recall improved with larger budgets.

## Boundaries and scale limits

Synthetic proxy only; no real LLM agent calls, no real repositories, no human-generated memory, no production traces, and no long-horizon deployment test. Main run used 40 seeds and 3200 held-out test episodes per variant; sensitivity used 30 seeds across context budgets 3, 6, 12, and 24.

## Claim scope

In a local synthetic repeated-agent decision benchmark, compact operator-doctrine memory improved held-out task success and reduced safety/process violations compared with no memory and raw episodic recall under matched context budgets.

## Why it stopped

Stopped because the local evidence is synthetic-only useful signal, not direct/full validation of repeat production agents.

## Recommended next action

Run a bounded real-agent follow-up using the same three memory conditions on repeated coding or research tasks with observable success, validation, and safety metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent doctrine memory benchmark for repeated coding tasks
- Success threshold: Doctrine memory improves task success by at least 10 percentage points over raw retrieval while reducing safety/process violations by at least 20 percent relative on held-out repeated tasks.
- Stop condition: Stop if doctrine memory fails to beat raw retrieval on either success or safety metrics across two independent task suites, or if gains disappear under stale-memory ablation.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-for-repeat-agents-2916349578ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
