# Operator-doctrine memory for repeated agent tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-for-repeated-agent-tasks-80536f441c20`
Run ID: `operator-doctrine-memory-for-repeated-agent-tasks-80536f441c20-20260620T200242279327+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/56f71e69a40f

## What looked useful

Compact doctrine memory generalized avoid/require rules across task variants: doctrine_memory reached 0.975 success rate and 0.0476 mean violations versus episodic_exact at 0.500 success and 0.9269 violations over 7,200 episodes per agent.

## Boundaries and scale limits

The result is limited to a toy symbolic simulation with clean feedback, fixed task families, and scripted agents; it does not validate natural-language doctrine extraction, real LLM action selection, repository workflows, noisy operator feedback, or production persistence.

## Claim scope

In a deterministic synthetic repeated-task benchmark with symbolic operator doctrine, generalized family-level doctrine memory improved success and reduced violations versus stateless execution and exact episodic memory.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy evidence, not direct field evidence for real repeated agent tasks.

## Recommended next action

Run a bounded real-agent replay comparing no memory, raw episodic notes, and compact doctrine memory on repeated Codex tasks with held-out variants.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent replay for compact operator-doctrine memory
- Success threshold: Doctrine memory improves held-out variant success by at least 15 percentage points over raw episodic notes while reducing mean violations per task by at least 25%.
- Stop condition: Stop if doctrine memory fails to beat raw episodic notes on held-out variant success or increases violations/task in two independent task-family splits.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-for-repeated-agent-tasks-80536f441c20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
