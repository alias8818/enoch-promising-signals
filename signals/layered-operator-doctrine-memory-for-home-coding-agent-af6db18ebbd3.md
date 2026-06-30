# Layered operator-doctrine memory for home coding agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-operator-doctrine-memory-for-home-coding-agent-af6db18ebbd3`
Run ID: `layered-operator-doctrine-memory-for-home-coding-agent-af6db18ebbd3-20260610T032758570552+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8a2ca7664871

## What looked useful

Across 50,000 synthetic tasks, layered resolution achieved 1.00000 exact-memory accuracy and 0.00000 violation rate, versus the best flat baseline at 0.37732 accuracy and 0.43446 violation rate. This supports explicit doctrine layering as a cheap control mechanism for conflict-heavy coding-agent memory.

## Boundaries and scale limits

No LLM-in-the-loop agent was evaluated. The benchmark is synthetic and gives the layered method the intended precedence model by design; it does not measure real coding task success, prompt sensitivity, persistence failures, human satisfaction, or production memory-store behavior.

## Claim scope

In a deterministic synthetic memory-selection benchmark with explicit operator/project/repo doctrine conflicts, a layered scope-and-precedence resolver selected the intended governing doctrine more reliably than flat lexical, flat recency, or operator-only retrieval baselines.

## Why it stopped

Closed as no-paper useful signal: the result supports the mechanism in a synthetic proxy, but it is not direct/full validation of a home coding agent.

## Recommended next action

Run a bounded LLM-in-the-loop trace benchmark that compares layered doctrine memory against flat retrieval on persistent coding-agent tasks with conflicting operator, project, and repo instructions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM trace benchmark for layered coding-agent doctrine memory
- Success threshold: Layered memory reduces instruction violations by at least 30% relative to the best flat-memory baseline while keeping task success within 5 percentage points and token overhead below 15%.
- Stop condition: Stop if layered memory does not reduce instruction violations by at least 10% on a 30-task pilot or if token overhead exceeds 25% without a compensating reduction in violations.

## Evidence references

- Artifact root: `<local-path>/projects/layered-operator-doctrine-memory-for-home-coding-agent-af6db18ebbd3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
