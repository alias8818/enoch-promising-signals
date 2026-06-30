# Counterexample-Ledger Driven Self-Correction in Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-ledger-driven-self-correction-in-agents-bdd68db20906`
Run ID: `counterexample-ledger-driven-self-correction-in-agents-bdd68db20906-20260528T000138417802+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ca1df01e51ec

## What looked useful

Typed counterexample persistence improved first-attempt solved rate from 0.000 to 0.875 versus per-task correction while preserving 1.000 final solved rate; hidden failures per episode fell from 1.000 to 0.125. Untyped retrieval was harmful, with mean final solved rate 0.128 and 55.804 unsatisfiable retrieval events per seed.

## Boundaries and scale limits

No LLM, natural-language agent, real coding benchmark, noisy retrieval, or long-horizon planning was tested. The benchmark has eight hand-built task families and ranked candidate programs, so it validates a mechanism rather than a full agent system.

## Claim scope

In a deterministic synthetic program-repair proxy with repeated task families, a typed persistent counterexample ledger reduced repeated hidden-test failures and first-attempt errors compared with per-task-only correction.

## Why it stopped

Closed as no-paper useful signal: the current result is synthetic/proxy evidence for the mechanism, not direct publication-grade agent evidence.

## Recommended next action

Run a bounded deepen test on real LLM coding or tool-use agent tasks with recurring failure motifs, comparing typed ledger retrieval against per-task memory and no-memory baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Typed Counterexample Ledgers on Real LLM Agent Repair Tasks
- Success threshold: Typed ledger improves first-attempt success or repeat-failure rate by at least 20% relative to per-task correction while final success is no worse by more than 3 percentage points across at least two model families or task domains.
- Stop condition: Stop if typed retrieval fails to improve repeat-failure rate by 10% on a pilot of at least 100 tasks, or if retrieval contamination reduces final success by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-ledger-driven-self-correction-in-agents-bdd68db20906`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
