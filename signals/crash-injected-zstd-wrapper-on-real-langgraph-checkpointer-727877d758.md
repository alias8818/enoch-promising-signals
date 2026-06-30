# Crash-injected zstd wrapper on real LangGraph checkpointer replay traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `crash-injected-zstd-wrapper-on-real-langgraph-checkpointer-727877d758`
Run ID: `crash-injected-zstd-wrapper-on-real-langgraph-checkpointer-727877d758-20260604T023715068489+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Crash-injected LangGraph checkpoint compression for home-agent traces: enoch://control-plane/projects/crash-injected-langgraph-checkpoint-compression-for-home-a-e76bcd709c/runs/crash-injected-langgraph-checkpoint-compression-for-home-a-e76bcd709c-20260604T004535801389+0000
- Parent run decision: Compressed State Checkpoints for Fault-Tolerant Home Agents: enoch://control-plane/projects/compressed-state-checkpoints-for-fault-tolerant-home-agents-450d8026609d/runs/compressed-state-checkpoints-for-fault-tolerant-home-agents-450d8026609d-20260603T213953830612+0000

## What looked useful

zstd frame checksums are useful as a compact byte-corruption detection wrapper for LangGraph checkpoint payloads, but zstd alone is not a complete crash-consistency mechanism because valid serialized payloads can be replayed silently from the wrong logical checkpoint row.

## Boundaries and scale limits

Validated only on local SQLite checkpointer traces with 3 fixed seeds, 24 threads, 32 graph steps per thread, 4 serializer variants, and 12 replicates per corrupting crash mode. Not validated on production traces, distributed stores, filesystem power-loss campaigns, or long-running agents.

## Claim scope

On deterministic local LangGraph StateGraph traces using the real SQLite checkpointer serializer hook, a zstd serializer with frame checksum reduced checkpoint payload bytes to about 48% of raw JsonPlus and detected all tested latest-checkpoint byte flip, zero-window, and truncation corruptions, but did not detect valid checkpoint row substitution.

## Why it stopped

Medium direct validation produced a mixed result: zstd frame checksums strongly improved byte-corruption detection and compression versus raw JsonPlus, but all variants silently accepted valid row-swap corruption, so the zstd-only wrapper is not paper-positive as a crash-consistency mechanism.

## Recommended next action

Stop this zstd-only run as no-paper useful signal; the concrete next bounded test is an authenticated serializer/checkpointer wrapper that binds thread_id, checkpoint_ns, checkpoint_id, and parent_checkpoint_id into the protected payload so row substitution is detectable.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Authenticated zstd LangGraph checkpoint wrapper with row-identity binding
- Success threshold: Across at least the same 3 seeds, 24 threads, 32 steps, and 12 replicates per corrupting mode, authenticated zstd must show 0 clean failures, 0 silent wrong replays for row swaps and byte corruptions, checkpoint payload bytes no worse than 55% of raw JsonPlus, and clean replay/write overhead under 2x raw.
- Stop condition: Stop if identity-bound authentication still permits any silent wrong latest-state replay in targeted row-swap trials or if overhead exceeds 2x raw while compression is worse than 55% of raw.

## Evidence references

- Artifact root: `<local-path>/projects/crash-injected-zstd-wrapper-on-real-langgraph-checkpointer-727877d758`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
