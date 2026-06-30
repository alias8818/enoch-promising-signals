# LangGraph Tool-Call Ledger Replay Under SIGKILL

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `langgraph-tool-call-ledger-replay-under-sigkill-4cb6d8df45`
Run ID: `langgraph-tool-call-ledger-replay-under-sigkill-4cb6d8df45-20260529T014552789302+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real Agent Trace and Crash Test for Tiny Tool-Call Evidence Ledger: enoch://control-plane/projects/real-agent-trace-and-crash-test-for-tiny-tool-call-evidenc-9c95dffea8/runs/real-agent-trace-and-crash-test-for-tiny-tool-call-evidenc-9c95dffea8-20260528T200344160080+0000
- Parent run decision: Live SIGKILL Crash-Recovery Test for Tiny Tool-Call Evidence Ledger: enoch://control-plane/projects/live-sigkill-crash-recovery-test-for-tiny-tool-call-eviden-29d6d47eac/runs/live-sigkill-crash-recovery-test-for-tiny-tool-call-eviden-29d6d47eac-20260528T231343367586+0000

## What looked useful

Across 1400 completed trials with 1000 induced SIGKILLs and 60000 expected external effects, plain LangGraph replay duplicated side effects in 400/400 killed baseline trials with 3076 excess duplicate effect rows, while the ledger treatment had 0 duplicate trials, 0 duplicate effect ops, and 0 missing effects across 600 killed treatment trials plus 200 no-crash controls.

## Boundaries and scale limits

Synthetic deterministic graph rather than production LLM ToolNode traffic; local SQLite checkpointer and external-effect database only; single worker with deterministic one-kill retries; no distributed/concurrent tool execution, production Postgres/Redis saver, or real external API idempotency integration.

## Claim scope

In a deterministic local Python LangGraph StateGraph using SQLite checkpointing and SQLite-modeled external effects, hard SIGKILL between tool-side external commits and durable graph progress causes duplicate visible side effects on replay; an external operation-id ledger prevents duplicates across the tested cutpoints.

## Why it stopped

Bounded local validation supports the mechanism but remains synthetic and single-worker, so it is useful engineering evidence rather than publication-grade proof.

## Recommended next action

Stop this run as no-paper useful evidence; deepen with a bounded production-shape test using LangGraph prebuilt ToolNode message traffic, a production-style checkpointer/store, and concurrent multi-tool side effects.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-Shape LangGraph ToolNode Ledger Replay Under SIGKILL
- Success threshold: Ledger arm has zero duplicate visible effects and zero missing effects across all killed trials, while the no-ledger baseline reproduces at least one duplicate-effect failure under the same crash schedule.
- Stop condition: Stop if the production-shape ledger arm shows any duplicate or missing external effect after replay, or if the baseline no longer reproduces duplicate effects under a verified crash between external commit and durable graph progress.

## Evidence references

- Artifact root: `<local-path>/projects/langgraph-tool-call-ledger-replay-under-sigkill-4cb6d8df45`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
