# Replay real local-agent traces with crash-injected rollback ledger commits

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-real-local-agent-traces-with-crash-injected-rollbac-81dbb9f5e9`
Run ID: `replay-real-local-agent-traces-with-crash-injected-rollbac-81dbb9f5e9-20260520T052008294008+0000`

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

- Parent run decision: Rollback Evidence Ledger for Local Tool Agents: enoch://control-plane/projects/rollback-evidence-ledger-for-local-tool-agents-8d0906640758/runs/rollback-evidence-ledger-for-local-tool-agents-8d0906640758-20260520T051301386101+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d99004ef738a

## What looked useful

Strict delimiter-framed commit recovery passed 7,200/7,200 checks; the unframed JSON-parseable control failed 13/7,200 checks by accepting one extra event after a torn final commit record.

## Boundaries and scale limits

Test used 1,198 real trace events and 7,200 recovery checks with simulated file-prefix and torn-record crashes. It did not kill live writer processes, test power-loss behavior, or compare filesystems/storage stacks.

## Claim scope

In a controlled durable-prefix simulation over 12 real local Codex/Enoch agent traces, a hash-checked append ledger recovers exactly the committed prefix across crash boundaries only when commit records require strict newline record framing.

## Why it stopped

Tier 1 controlled direct trace replay supports the mechanism and exposes a framing counterexample, but it is not full process/filesystem crash validation.

## Recommended next action

Stop this run as a no-paper useful signal; next validate the same strict-framing ledger with process-kill injection at write/fsync points on a real filesystem.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-kill validation of strict-framed rollback ledger recovery
- Success threshold: At least 1,000 process-kill recovery trials over real trace payloads with zero over-recovery, zero hash mismatches, and all under-recovery matching the last externally recorded durable commit.
- Stop condition: Stop early if any recovered prefix includes an event beyond the external durable commit counter or if filesystem semantics make the commit boundary unobservable without privileged/power-loss tooling.

## Evidence references

- Artifact root: `<local-path>/projects/replay-real-local-agent-traces-with-crash-injected-rollbac-81dbb9f5e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
