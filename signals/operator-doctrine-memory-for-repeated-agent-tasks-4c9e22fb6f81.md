# Operator-Doctrine Memory for Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-for-repeated-agent-tasks-4c9e22fb6f81`
Run ID: `operator-doctrine-memory-for-repeated-agent-tasks-4c9e22fb6f81-20260611T052140925739+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb94e1342f57

## What looked useful

Across 100 seeds x 80 tasks, doctrine memory reduced transfer violations from 0.10000 to 0.02500 versus episodic memory in the clean run, a paired delta of 0.07500 violations/task with bootstrap 95% CI [0.067, 0.0835]. With 10% feedback corruption, doctrine memory reduced transfer violations from 0.11300 to 0.02675 versus episodic memory, delta 0.08625 with 95% CI [0.07775, 0.09525].

## Boundaries and scale limits

Synthetic proxy only; no live LLM agent, real operator feedback, natural-language doctrine extraction, long-horizon multi-session persistence, or production coding-task validation was tested.

## Claim scope

In a synthetic repeated-agent-task harness, feature-level operator-doctrine memory transferred feedback across held-out task variants better than no memory and exact-template episodic memory.

## Why it stopped

No-paper closure: this is a synthetic proxy mechanism result, not direct validation of a real LLM agent or production operator-doctrine memory system.

## Recommended next action

Run a bounded live-agent follow-up that compares no memory, episodic memory, and doctrine memory on real repeated coding/review/frontend/research tasks with held-out variants and human or model-graded doctrine compliance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-Agent Operator-Doctrine Memory Transfer Benchmark
- Success threshold: Doctrine memory reduces held-out doctrine violations by at least 20% versus episodic memory without reducing task success or increasing severe overgeneralization failures.
- Stop condition: Stop if doctrine memory does not beat episodic memory on held-out doctrine violations, or if overgeneralization/stale-doctrine errors offset the correction reduction.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-for-repeated-agent-tasks-4c9e22fb6f81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
