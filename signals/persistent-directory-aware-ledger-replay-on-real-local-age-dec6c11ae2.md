# Persistent directory-aware ledger replay on real local-agent tool traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `persistent-directory-aware-ledger-replay-on-real-local-age-dec6c11ae2`
Run ID: `persistent-directory-aware-ledger-replay-on-real-local-age-dec6c11ae2-20260528T222050996547+0000`

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

- Parent run decision: Runtime-instrumented reversible ledger for real local-agent file tool calls: enoch://control-plane/projects/runtime-instrumented-reversible-ledger-for-real-local-agen-873d931cad/runs/runtime-instrumented-reversible-ledger-for-real-local-agen-873d931cad-20260528T155113203010+0000
- Parent run decision: Merkleized reversible ledger on real local-agent tool traces: enoch://control-plane/projects/merkleized-reversible-ledger-on-real-local-agent-tool-trac-7bd3117bb4/runs/merkleized-reversible-ledger-on-real-local-agent-tool-trac-7bd3117bb4-20260528T014530988576+0000

## What looked useful

Directory preimages are necessary for exact persistent rollback on real trace-shaped local-agent filesystem workloads. The mechanism is faster than Git per-operation checkpointing, but naive ledger artifacts are larger than Git, even with gzip in the fixed-seed aggregate.

## Boundaries and scale limits

Replay uses real local-agent JSONL trace payloads but maps them into deterministic filesystem mutations; it does not re-execute original shell commands or instrument a live production file-tool boundary. Crash kill points, symlinks, permissions, binary artifacts, and concurrent live writers were not fully covered.

## Claim scope

On three fixed-seed replays over real local Codex/Enoch agent trace payloads, totaling 6,492 trace-derived filesystem operations, a persistent directory-aware preimage ledger exactly rolled back after reopening from disk; file-only and hash-only controls failed; Git was exact and smaller but much slower.

## Why it stopped

Useful bounded mechanism signal but no paper: trace-derived replay is not the same as live tool-boundary evidence, and artifact size loses to Git in the aggregate.

## Recommended next action

Run one final depth-4 live tool-boundary replay where the ledger wraps actual file edits during local-agent tasks, with process-kill injection and artifact-size mitigation as explicit success criteria.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live tool-boundary persistent directory-aware ledger replay with crash injection
- Success threshold: Across at least 20 live local-agent tasks and at least 2,000 actual file mutations, compressed directory-aware ledger rollback exact rate is 1.0 after injected kills, file-only/hash-only controls are below 0.5 exact rate, apply-time overhead is at least 10x faster than Git, and artifact bytes are no more than 1.25x Git.
- Stop condition: Stop if live tool-boundary exact rollback is below 0.95, if any acknowledged mutation is unrecoverable after a kill, or if compressed artifact bytes remain above 1.25x Git after one bounded compaction attempt.

## Evidence references

- Artifact root: `<local-path>/projects/persistent-directory-aware-ledger-replay-on-real-local-age-dec6c11ae2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
