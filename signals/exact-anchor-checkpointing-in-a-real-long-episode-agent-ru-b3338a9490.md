# Exact-Anchor Checkpointing in a Real Long-Episode Agent Runtime

Status: `useful_signal`
Project ID: `exact-anchor-checkpointing-in-a-real-long-episode-agent-ru-b3338a9490`
Run ID: `exact-anchor-checkpointing-in-a-real-long-episode-agent-ru-b3338a9490-20260515T150156508169+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8f955958c14a

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 direct local LangGraph evidence supports the exact-anchor mechanism, but this is not publication-grade validation because it uses deterministic mock tools, local SQLite, and runtime rebuild inside one Python process rather than production crash/restart conditions.

## Recommended next action

Run a medium direct confirmation with OS process kill/restart, durable checkpoint storage, real or API-faithful tool side effects, 1000+ step episodes, and overhead/control metrics before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-Level Exact-Anchor Resume in a 1000-Step Tool-Using LangGraph Agent
- Success threshold: Across at least 9 process-level cutover trials, exact-anchor resume must start at the selected anchor, finish all episodes, produce zero duplicate side-effect keys, and add less than 25% mean elapsed-time overhead versus a checkpointed no-cutover baseline; controls must duplicate the replayed prefix.
- Stop condition: Stop if any exact-anchor process-level trial resumes before the anchor, skips required work, duplicates a prefix side effect, or exceeds 25% mean overhead without a clear implementation bug.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-checkpointing-in-a-real-long-episode-agent-ru-b3338a9490`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
