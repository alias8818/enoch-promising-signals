# Remote-Anchored Real-Agent Crash-Recovery Trace Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `remote-anchored-real-agent-crash-recovery-trace-test-8f9246db19`
Run ID: `remote-anchored-real-agent-crash-recovery-trace-test-8f9246db19-20260524T022333688800+0000`

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

- Parent run decision: Merkle-Ledger Agent Tool-Call Integrity: enoch://control-plane/projects/merkle-ledger-agent-tool-call-integrity-f72fee77b0d4/runs/merkle-ledger-agent-tool-call-integrity-f72fee77b0d4-20260524T010404391720+0000
- Parent run decision: Real-Agent Merkle Ledger Anchoring and Crash-Recovery Test: enoch://control-plane/projects/real-agent-merkle-ledger-anchoring-and-crash-recovery-test-e42c7a0664/runs/real-agent-merkle-ledger-anchoring-and-crash-recovery-test-e42c7a0664-20260524T021323841435+0000

## What looked useful

Across 240 paired trials per strategy, the full remote-anchor/idempotent/verify strategy achieved 240/240 recoveries with no duplicate, missing, or unexpected side effects. The unanchored baseline, local checkpoint, and batched remote anchor each achieved 90/240; no-verify achieved 148/240 and failed on anchored-but-incomplete steps.

## Boundaries and scale limits

This was a local CPU-only harness with real filesystem side effects but not a live LLM/Codex/LangGraph agent, not a networked object store, not concurrent, and not production-scale.

## Claim scope

In a deterministic filesystem-agent crash-recovery harness with fixed crash seeds, per-step remote anchoring plus idempotent replay and local digest/marker verification recovered all tested crash schedules and outperformed unanchored, coarse-checkpoint, batched-anchor, and no-verify controls.

## Why it stopped

Closed as no-paper useful signal because the Tier 2 harness supports the mechanism, but the project title asks for a real-agent crash-recovery trace test and this run used a deterministic local agent harness rather than a live agent stack.

## Recommended next action

Run the same fixed-seed crash matrix against a live LangGraph or Codex-style tool-calling agent with remote anchor writes over a networked store and process SIGKILL injection at tool boundaries.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Tool-Calling Agent Remote-Anchor Crash Recovery
- Success threshold: At least 95% recovery for the full method and at least +30 percentage points paired recovery gain versus the strongest baseline across 50 or more fixed crash seeds, with zero duplicate or corrupt side effects.
- Stop condition: Stop if the full method falls below 90% recovery, produces duplicate/corrupt side effects in more than 1% of trials, or fails to beat the strongest baseline by 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/remote-anchored-real-agent-crash-recovery-trace-test-8f9246db19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
