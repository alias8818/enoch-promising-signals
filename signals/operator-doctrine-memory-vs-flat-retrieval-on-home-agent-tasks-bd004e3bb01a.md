# Operator-doctrine memory vs flat retrieval on home agent tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-on-home-agent-tasks-bd004e3bb01a`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-on-home-agent-tasks-bd004e3bb01a-20260621T173003838262+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8c1f51c1f150

## What looked useful

Flat retrieval handled simple episodic facts but had 16.9% unsafe rate on doctrine-governed tasks at 8 conflicting snippets per rule; doctrine memory had 0% unsafe rate and used fewer context tokens in the same benchmark.

## Boundaries and scale limits

Synthetic tasks only; no real LLM planner, no real household traces, no human-authored task suite, no embedding retrieval baseline, and no long-horizon memory updates. Main evidence is 20 seeds and 5,600 task decisions per policy.

## Claim scope

In a deterministic synthetic home-agent benchmark, separating stable operator doctrine into a priority-bearing memory layer eliminated unsafe action choices caused by noisy/conflicting flat episodic retrieval while preserving episodic-fact accuracy.

## Why it stopped

No-paper useful signal: the result supports the mechanism in a synthetic deterministic surrogate, but does not provide direct real-agent evidence.

## Recommended next action

Run a bounded LLM-in-the-loop confirmation on a fixed hand-authored home-agent task set comparing the same doctrine-layer policy against flat retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop doctrine memory confirmation for home-agent safety tasks
- Success threshold: Doctrine-layer LLM planner reduces unsafe-action rate by at least 50% relative to flat retrieval without reducing episodic-fact accuracy by more than 2 percentage points.
- Stop condition: Stop as unsupported if doctrine-layer unsafe-action rate is not lower than flat retrieval on two independent task/prompt seeds or if task-router/rule-matching errors dominate the observed failures.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-on-home-agent-tasks-bd004e3bb01a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
