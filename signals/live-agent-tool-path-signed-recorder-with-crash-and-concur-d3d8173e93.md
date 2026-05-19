# Live Agent Tool-Path Signed Recorder With Crash and Concurrency Checks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `live-agent-tool-path-signed-recorder-with-crash-and-concur-d3d8173e93`
Run ID: `live-agent-tool-path-signed-recorder-with-crash-and-concur-d3d8173e93-20260518T121433475428+0000`

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

- Internal Enoch project: Live Agent Tool-Path Signed Recorder With Crash and Concurrency Checks: internal_generated:live-agent-tool-path-signed-recorder-with-crash-and-concur-d3d8173e93

## What looked useful

Direct bounded evidence supports the core mechanism: signed hash-chain recording did not break concurrent durable appends or process-crash recovery, detected two tamper classes, and added little throughput cost relative to durable SQLite transactions.

## Boundaries and scale limits

Tested only as a local standalone harness with synthetic tool events; not integrated into a live agent runtime, not tested under host power loss or filesystem corruption, not distributed across hosts, and not evaluated for production key rotation, rollback prevention, privacy controls, or replay ergonomics.

## Claim scope

A standalone SQLite WAL recorder using per-event durable transactions, SHA-256 previous-digest chaining, and HMAC-SHA256 signatures preserved and verified 320,000 synthetic fixed-seed tool events under 16 concurrent writer processes, survived 10 process-level SIGKILL crash trials with clean post-crash verification, detected payload mutation and row deletion, and ran at 96.8% of a matched unsigned durable SQLite baseline.

## Why it stopped

No-paper closure: bounded local evidence is useful and directly supports the prototype mechanism, but it is not paper-positive because live-agent integration, host-level crash testing, and key-management adversary coverage remain untested.

## Recommended next action

Run one depth-4 live-agent integration follow-up that records real tool calls across forced agent restarts and verifies replay completeness, then stop the chain unless that direct integration falsifies the current mechanism.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Agent Integration Replay Test For Signed Tool-Path Recorder
- Success threshold: Across at least 1000 real tool invocations and 20 forced restarts, signed recording verifies cleanly, loses zero completed invocations, creates zero duplicate invocation IDs, replays the complete recorded path, and maintains at least 90% of unsigned baseline task throughput.
- Stop condition: Stop as negative if any completed invocation is missing, any duplicate invocation ID appears, any post-restart verification fails, replay cannot reconstruct the tool path, or signed task throughput falls below 90% of the unsigned durable baseline.

## Evidence references

- Artifact root: `<local-path>/projects/live-agent-tool-path-signed-recorder-with-crash-and-concur-d3d8173e93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
