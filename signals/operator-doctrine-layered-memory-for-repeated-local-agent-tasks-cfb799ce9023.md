# Operator-Doctrine Layered Memory for Repeated Local Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-layered-memory-for-repeated-local-agent-tasks-cfb799ce9023`
Run ID: `operator-doctrine-layered-memory-for-repeated-local-agent-tasks-cfb799ce9023-20260619T130942112611+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d2902e151206

## What looked useful

Layered memory reached 1.000 decision accuracy and 1.000 retrieval hit rate with 0.000 stale retrieved fraction; flat memory reached 0.750 accuracy and 0.750 retrieval hit rate with 0.3475 stale retrieved fraction, failing destructive-safety and resource-calibration tasks because stale shortcuts were retrieved.

## Boundaries and scale limits

Evidence is limited to a deterministic synthetic benchmark: 60 seeds, 8 task templates, 8 repeats per seed, 160 distractor memories per seed, and a rule-based downstream decision policy. It does not validate real LLM agents, real repositories, embedding retrievers, multi-turn execution, or human productivity.

## Claim scope

In a synthetic repeated local-agent doctrine benchmark with stale memories and distractors, a layered memory policy using scope, precedence, recency/staleness penalties, and tag matching improved retrieval and deterministic compliance decisions versus no memory and flat lexical memory.

## Why it stopped

Closed as no-paper useful signal because the positive effect is synthetic and deterministic rather than a full validation with real LLM agents.

## Recommended next action

Run a bounded real-agent follow-up on local repository tasks comparing flat versus layered memory with blinded compliance scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Layered Memory Compliance Study
- Success threshold: Layered memory improves instruction-compliance score by at least 15 percentage points over flat memory while not reducing task success or increasing prompt tokens by more than 25%.
- Stop condition: Stop if layered memory fails to improve compliance by at least 5 percentage points over flat memory on the first two repositories or if prompt overhead exceeds 50% without fewer stale-memory violations.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-layered-memory-for-repeated-local-agent-tasks-cfb799ce9023`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
