# Layered Memory for Multi-Step Household Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-for-multi-step-household-tasks-b5f963b0da1a`
Run ID: `layered-memory-for-multi-step-household-tasks-b5f963b0da1a-20260629T221302309776+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fa338371aaca

## What looked useful

Layered memory achieved 1.000 task success and 1.000 fact accuracy with 0.000 conflict violations; transcript_search achieved 0.126 task success and 0.451 fact accuracy with 0.391 conflict violations; flat_retrieval achieved 0.014 task success and 0.167 fact accuracy with 0.673 conflict violations.

## Boundaries and scale limits

Evidence is symbolic and synthetic: 10 seeds, 4,800 task instances, 36,000 generated memory facts. It does not validate LLM planning, natural-language extraction, embodied execution, real user preferences, or long-horizon deployment.

## Claim scope

In a deterministic synthetic replay benchmark for multi-step household tasks, layered active key/layer memory resolved current profile, environment, procedure, and episodic facts under distractors better than no-memory, transcript-search, and flat-retrieval baselines.

## Why it stopped

Closed as no-paper useful signal because the evidence is a symbolic mechanism probe, not direct validation of a real household-task agent.

## Recommended next action

Run a bounded LLM-agent follow-up on held-out natural-language household traces using the same baselines and success metrics before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-agent layered memory replay on natural-language household traces
- Success threshold: Layered memory improves task success by at least 20 percentage points over transcript_search and reduces conflict violations by at least 50 percent, with no increase in default/missing-fact errors.
- Stop condition: Stop if layered memory fails to beat transcript_search by 10 percentage points task success or if gains come only from oracle labels unavailable to the LLM-agent runtime.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-for-multi-step-household-tasks-b5f963b0da1a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
