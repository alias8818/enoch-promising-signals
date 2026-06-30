# Evidence-ledger rollback in a real tool-using LLM agent harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-in-a-real-tool-using-llm-agent-ha-200d93d7b9`
Run ID: `evidence-ledger-rollback-in-a-real-tool-using-llm-agent-ha-200d93d7b9-20260524T202539682932+0000`

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

- Parent run decision: Evidence-ledger agent rollback on CPU: enoch://control-plane/projects/evidence-ledger-agent-rollback-on-cpu-ed2c60140495/runs/evidence-ledger-agent-rollback-on-cpu-ed2c60140495-20260524T194945257712+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5cef9dde20c1

## What looked useful

Rollback rescued 54/54 poisoned tasks relative to no rollback, improving poisoned-task accuracy from 0.0 to 1.0 while keeping clean-task accuracy at 1.0. An answer-time failed-evidence filter also rescued 54/54, showing rollback is one viable mitigation rather than the only viable mitigation.

## Boundaries and scale limits

Tier 1 controlled direct test only: 96 synthetic tasks, deterministic agent policy, no external LLM, no production LangGraph integration, no realistic web/database tools, and no long-horizon memory.

## Claim scope

In a deterministic local tool-using agent harness with synthetic lookup tools, rolling back evidence written during failed tool transactions prevented stale failed evidence from contaminating final ledger-grounded answers.

## Why it stopped

No-paper closure: Tier 1 mechanism support was obtained, but the harness used a deterministic policy and synthetic tools, so it is not publication-grade direct LLM-agent evidence.

## Recommended next action

Run a bounded deepen test in a LangGraph or equivalent real LLM agent loop with actual model calls, persisted ledger state, and naturally occurring or injected tool failures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger rollback in a real LLM LangGraph agent loop
- Success threshold: On at least 50 poisoned LLM-agent episodes, rollback improves poisoned-task accuracy by at least 30 percentage points over no rollback and does not reduce clean-task accuracy by more than 2 percentage points.
- Stop condition: Stop if rollback improves poisoned-task accuracy by less than 10 percentage points, if failed evidence never reaches final answer context, or if LLM/tool nondeterminism prevents paired evaluation after three fixed-seed attempts.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-in-a-real-tool-using-llm-agent-ha-200d93d7b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
