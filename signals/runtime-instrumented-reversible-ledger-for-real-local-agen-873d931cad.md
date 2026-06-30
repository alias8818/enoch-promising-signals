# Runtime-instrumented reversible ledger for real local-agent file tool calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `runtime-instrumented-reversible-ledger-for-real-local-agen-873d931cad`
Run ID: `runtime-instrumented-reversible-ledger-for-real-local-agen-873d931cad-20260528T155113203010+0000`

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

- Parent run decision: Reversible tool-call ledger for home CPU agents: enoch://control-plane/projects/reversible-tool-call-ledger-for-home-cpu-agents-c9003b79fdcc/runs/reversible-tool-call-ledger-for-home-cpu-agents-c9003b79fdcc-20260527T201030942256+0000
- Parent run decision: Merkleized reversible ledger on real local-agent tool traces: enoch://control-plane/projects/merkleized-reversible-ledger-on-real-local-agent-tool-trac-7bd3117bb4/runs/merkleized-reversible-ledger-on-real-local-agent-tool-trac-7bd3117bb4-20260528T014530988576+0000

## What looked useful

Directory state is necessary for exact reversible ledgers: the file-only ledger failed all 10 medium seeds by leaking newly-created directories, while the directory-aware ledger and Git baseline both achieved 100% exact rollback. The directory-aware ledger averaged 0.0000965 seconds/op versus Git checkpointing at 0.0234409 seconds/op and used about 50.6% of Git artifact bytes.

## Boundaries and scale limits

Synthetic agent-like workload only; no live local-agent trace replay, no crash-recovery persistence, no concurrent writers, no symlink/device edge cases, and no large binary-file workload.

## Claim scope

In a deterministic local filesystem harness with 10 fixed seeds and 500 operations per seed, a directory-aware preimage ledger exactly reverted all tested write, append, replace, delete, rename, and chmod operations while using lower apply-time overhead and smaller artifacts than per-operation Git checkpointing.

## Why it stopped

Tier 2 harness evidence supports the mechanism but remains a bounded synthetic confirmation rather than direct production-agent validation.

## Recommended next action

Stop short of paper writing; replay real local-agent file-tool traces with persistent directory-aware ledger logging and injected crash/restart points.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent directory-aware ledger replay on real local-agent tool traces
- Success threshold: 100% exact rollback and crash-recovery correctness across all replayed traces, less than 5x Git checkpoint apply overhead, and artifact bytes no more than Git checkpoint bytes on median.
- Stop condition: Stop if any non-environmental exact rollback failure occurs in the persistent ledger or if overhead exceeds Git checkpointing on median.

## Evidence references

- Artifact root: `<local-path>/projects/runtime-instrumented-reversible-ledger-for-real-local-agen-873d931cad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
