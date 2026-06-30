# Counterexample Ledger in a Real CPU Coding-Agent Harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-ledger-in-a-real-cpu-coding-agent-harness-6843af2ce7`
Run ID: `counterexample-ledger-in-a-real-cpu-coding-agent-harness-6843af2ce7-20260529T000123236434+0000`

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

- Parent run decision: Counterexample Ledger for Self-Correction in CPU Agents: enoch://control-plane/projects/counterexample-ledger-for-self-correction-in-cpu-agents-0c8555cc37c8/runs/counterexample-ledger-for-self-correction-in-cpu-agents-0c8555cc37c8-20260528T193631124988+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57b4ce2850fe

## What looked useful

The counterexample ledger mechanism produced a clear bounded efficiency signal in a real CPU coding harness: it avoided retrying failed repair families and selected structurally relevant alternatives from observed pytest counterexamples.

## Boundaries and scale limits

Small synthetic task set; scripted repair candidates; no live LLM patch generation; single sequential CPU worker; no randomized benchmark or large held-out corpus.

## Claim scope

In a four-task controlled Python file-edit-plus-pytest harness with scripted candidate repairs and a two-attempt budget, a structured counterexample ledger improved solve rate from 1/4 to 4/4 and reduced repeated failed patch-family attempts from 3 to 0 versus a bounded transcript-only baseline.

## Why it stopped

Tier 1 controlled direct threshold was met, but evidence remains no-paper because tasks and repair candidates are scripted rather than produced by a live coding agent.

## Recommended next action

Run a bounded live-agent follow-up that attaches this ledger interface to an LLM coding agent on at least 30 held-out CPU tasks and compares against transcript-only memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-agent counterexample ledger on held-out CPU coding tasks
- Success threshold: At least +10 percentage points solve-rate improvement or at least 20% fewer attempts-to-solve at equal solve rate, with at least 50% fewer repeated failed repair-family attempts than baseline.
- Stop condition: Stop if ledger overhead increases wall clock or token cost by more than 25% without improving solve rate, attempts-to-solve, or repeated-failure rate.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-ledger-in-a-real-cpu-coding-agent-harness-6843af2ce7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
