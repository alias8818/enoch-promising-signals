# Counterexample-Mining Pipeline for Small CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-mining-pipeline-for-small-cpu-agents-3fd2d6741fba`
Run ID: `counterexample-mining-pipeline-for-small-cpu-agents-3fd2d6741fba-20260620T150812130028+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8478ec7cb8b7

## What looked useful

On 120 seed-173 replay tasks, best simple baseline accuracy was 0.1667, layered_doctrine_memory accuracy was 1.0, and 100 cases were strong counterexamples where all simple baselines failed while layered memory succeeded.

## Boundaries and scale limits

Synthetic template-generated tasks only; deterministic policy evaluator only; no LLM-in-the-loop agents, no external replay corpus, no public benchmark comparison, and one fixed seed/task distribution.

## Claim scope

A deterministic synthetic 120-task replay benchmark shows that a small CPU counterexample-mining pipeline can generate memory/retrieval failure cases where layered doctrine memory solves correction, revocation, alias, noisy metadata, and cross-thread conflict cases that naive baselines miss.

## Why it stopped

Bounded synthetic/proxy evidence is useful but not sufficient for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with at least 3 seeds, live small LLM/tool-agent replay, and a non-template held-out corpus before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Small-Agent Counterexample Mining on Held-Out Replay Tasks
- Success threshold: Layered memory improves accuracy by at least 25 percentage points over the best simple baseline and produces at least 50 all-baselines-failed counterexamples across held-out live-agent replay tasks.
- Stop condition: Stop if layered memory advantage is below 10 percentage points on two seeds/splits or if mined counterexamples collapse to template/parser artifacts.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-mining-pipeline-for-small-cpu-agents-3fd2d6741fba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
