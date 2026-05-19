# Anchored HMAC Checkpoints in a Real Agent Runtime

Status: `useful_signal`
Project ID: `anchored-hmac-checkpoints-in-a-real-agent-runtime-91aa182911`
Run ID: `anchored-hmac-checkpoints-in-a-real-agent-runtime-91aa182911-20260515T212743940500+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/49b2b878513b

## What looked useful

A real installed LangGraph runtime accepted an anchored HMAC checkpointer and passed the Tier 1 direct test: 600 anchored checkpoints, 23.731% mean overhead versus baseline, and all four direct tamper/replay/fork scenarios detected before resume.

## Boundaries and scale limits

Only 120 invocations, 600 checkpoints, single thread namespace, in-memory storage, no process restart, no durable SQL/Redis/Postgres saver, no concurrent agents, no real LLM/tool side effects, and no attacker with access to both checkpoint storage and the independent anchor log.

## Claim scope

In a controlled single-process LangGraph StateGraph run using an InMemorySaver-compatible custom checkpointer, external chained HMAC anchors over raw checkpoint bytes, metadata, parent ids, and channel blobs detected blob tampering, metadata tampering, rollback, and parent-fork attacks before resume while preserving checkpoint count and staying under 25% mean overhead.

## Why it stopped

No-paper useful signal: the Tier 1 mechanism is supported, but the evidence is single-process in-memory validation rather than durable production-runtime validation.

## Recommended next action

Run a durable-storage follow-up with a file-backed or SQL-backed LangGraph saver, preserve the independent anchor log across process restart, then repeat the same four attacks after restart with at least 5 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Durable Restart Validation for Anchored LangGraph Checkpoints
- Success threshold: Across at least 5 seeds, all post-restart tamper/replay/fork cases are detected before resume, no clean resumes fail integrity checks, and mean invocation overhead remains under 30% or under 2 ms absolute overhead.
- Stop condition: Stop if durable integration cannot preserve/verifiably reload the anchor chain, if any attack resumes without detection in two independent seeds, or if clean resumes fail integrity validation.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-hmac-checkpoints-in-a-real-agent-runtime-91aa182911`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
