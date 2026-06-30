# Bounded Evidence Ledger for CPU Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-evidence-ledger-for-cpu-agent-reliability-3eceafe52906`
Run ID: `bounded-evidence-ledger-for-cpu-agent-reliability-3eceafe52906-20260607T131558546167+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/143d4d45374d

## What looked useful

Stress benchmark with 8 required facts and context capacity 4 changed success from 0/1000 for recent-context baseline to 1000/1000 for ledger fact caps 8 and 12, reducing mean steps from 80.000 to 10.706 and repeated invalid actions from 6.163 to 0.000. Ledger fact caps 4 and 6 still had 0/1000 success but cut repeated invalid actions to about 3.0. Easy-control condition with 4 required facts and context capacity 4 had 1000/1000 success for both baseline and ledger, showing no completion gain when context was already sufficient.

## Boundaries and scale limits

Tested only on randomized synthetic fact-gathering tasks with deterministic policy logic, 1000 paired seeds per main condition, single-process Python, and no real LLM, repository, shell, tool-output, or long-horizon agent tasks.

## Claim scope

In a synthetic CPU-only bounded-context agent loop, a fixed-size evidence ledger that can retain all required task facts improves completion and reduces repeated invalid actions; ledger capacity below the required fact count does not rescue completion.

## Why it stopped

Synthetic mechanism evidence is positive but insufficient for a paper or real agent reliability claim; this is not a full validation.

## Recommended next action

Stop this run as no-paper useful synthetic evidence; next run should test the ledger in a real CPU agent harness on paired repository or shell-repair tasks with fixed model, bounded context, and repeated-failure metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded Evidence Ledger in a Real CPU Agent Harness
- Success threshold: Ledger condition reduces repeated failed commands by at least 30% with no more than a 5 percentage point completion-rate drop and less than 10% wall-clock overhead on paired tasks.
- Stop condition: Stop if ledger overhead exceeds 10%, completion drops by more than 5 percentage points, or fewer than 30 paired real tasks can be executed reproducibly in the local harness.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-evidence-ledger-for-cpu-agent-reliability-3eceafe52906`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
