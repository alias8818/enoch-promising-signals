# Tool-Call Ledger for Small Agent Rollback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tool-call-ledger-for-small-agent-rollback-6fe3e063c81e`
Run ID: `tool-call-ledger-for-small-agent-rollback-6fe3e063c81e-20260524T165917428701+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/43764c537a02

## What looked useful

The ledger achieved 100% exact rollback on reversible traces versus 0% for no rollback, used 43.6% of snapshot rollback storage on the reversible workload, and correctly treated irreversible external sends as non-restorable rather than silently claiming success.

## Boundaries and scale limits

Tested only on synthetic deterministic Python traces with 500 trials per scenario, 200 planned tool calls per trace, single-thread execution, no real LLM planner, no real LangGraph runtime, no process-crash recovery, no concurrency, and mocked external side effects.

## Claim scope

In a single-process synthetic small-agent tool-call trace, a compensation ledger exactly restores workspace/global state after injected failures when all post-checkpoint tools provide correct inverse operations, and it flags traces containing irreversible external sends as unsafe to claim fully rolled back.

## Why it stopped

No-paper useful signal: synthetic evidence supports the mechanism under reversible-tool assumptions, but direct runtime evidence is required before any publication-grade claim.

## Recommended next action

Run a bounded real-runtime follow-up by adding durable ledger persistence and crash-injection rollback tests to a LangGraph-style small-agent harness with filesystem, SQLite, and mocked HTTP/email tools.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Durable Tool-Call Ledger in a Real Small-Agent Runtime
- Success threshold: At least 99% exact restoration over 1000 injected failures for reversible real tools, 100% detection of irreversible post-checkpoint side effects, and ledger storage below 60% of snapshot storage on the tested workload.
- Stop condition: Stop if durable replay cannot recover exact filesystem and SQLite state after crash injection, or if irreversible side effects cannot be reliably detected before reporting rollback success.

## Evidence references

- Artifact root: `<local-path>/projects/tool-call-ledger-for-small-agent-rollback-6fe3e063c81e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
