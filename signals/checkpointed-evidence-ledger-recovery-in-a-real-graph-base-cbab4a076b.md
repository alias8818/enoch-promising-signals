# Checkpointed evidence ledger recovery in a real graph-based tool-agent runtime

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `checkpointed-evidence-ledger-recovery-in-a-real-graph-base-cbab4a076b`
Run ID: `checkpointed-evidence-ledger-recovery-in-a-real-graph-base-cbab4a076b-20260604T052513926744+0000`

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

- Parent run decision: Checkpointed evidence ledger in a live tool-agent harness: enoch://control-plane/projects/checkpointed-evidence-ledger-in-a-live-tool-agent-harness-2cbd73d3ba/runs/checkpointed-evidence-ledger-in-a-live-tool-agent-harness-2cbd73d3ba-20260604T020650923378+0000
- Parent run decision: Append-Only Evidence Ledger for Tool-Using CPU Agents: enoch://control-plane/projects/append-only-evidence-ledger-for-tool-using-cpu-agents-c63325ed93f0/runs/append-only-evidence-ledger-for-tool-using-cpu-agents-c63325ed93f0-20260603T235303994081+0000

## What looked useful

The ledger variant achieved 30/30 completion, 30/30 planned crashes, 0 duplicate calls, and 0 mean tool-call overhead. The checkpoint-only ablation achieved completion but incurred 81 duplicate/overhead calls across 30 trials. The restart baseline incurred 233 duplicate/overhead calls. A key mechanism finding is that LangGraph checkpoint resume can expose stale checkpoint state after hard death, so supervisor reinvocation and ledger-state reconciliation are required for robust completion.

## Boundaries and scale limits

Synthetic deterministic tool tasks only; 5 fixed seeds, 6 trials per seed, 8 to 18 tool steps per task, one planned hard cutover per trial. No real LLM/tool APIs, concurrent graph threads, multiple cutovers per task, remote checkpoint store, network filesystem, or production traces were tested.

## Claim scope

In a local LangGraph StateGraph runtime using SQLite graph checkpoints and a SQLite evidence ledger, a supervisor-reconciled checkpointed evidence ledger recovered from single hard process cutovers after external tool observation writes and avoided duplicate external tool calls across 30 fixed-seed ledger trials.

## Why it stopped

Medium local validation supports the recovery mechanism but is not broad or production-real enough for publication readiness.

## Recommended next action

Stop this run as no-paper useful evidence; next implement the same supervisor reconciliation in a concurrent real-tool LangGraph harness with multiple cutovers per task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent multi-cutover LangGraph evidence-ledger recovery on real tool traces
- Success threshold: Across at least 100 paired real-tool or trace-replay tasks, ledger recovery completes at least 99% of tasks, has zero duplicate non-idempotent tool calls, and reduces duplicate/overhead calls by at least 90% versus checkpoint-only and restart baselines.
- Stop condition: Stop if ledger recovery produces any duplicate non-idempotent tool call, completion falls below 95%, or reconciliation requires manual intervention in more than 1% of tasks.

## Evidence references

- Artifact root: `<local-path>/projects/checkpointed-evidence-ledger-recovery-in-a-real-graph-base-cbab4a076b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
