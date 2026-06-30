# Persistent-checkpoint replay validation for evidence-ledger tool mismatch halts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `persistent-checkpoint-replay-validation-for-evidence-ledge-d2a7b34684`
Run ID: `persistent-checkpoint-replay-validation-for-evidence-ledge-d2a7b34684-20260523T182155240236+0000`

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

- Parent run decision: Evidence-ledger agent halts on tool mismatch: enoch://control-plane/projects/evidence-ledger-agent-halts-on-tool-mismatch-f41accfaf76d/runs/evidence-ledger-agent-halts-on-tool-mismatch-f41accfaf76d-20260523T171727295488+0000
- Parent run decision: LangGraph replay validation for evidence-ledger tool mismatch halts: enoch://control-plane/projects/langgraph-replay-validation-for-evidence-ledger-tool-misma-b61b0d0118/runs/langgraph-replay-validation-for-evidence-ledger-tool-misma-b61b0d0118-20260523T181114672411+0000

## What looked useful

Replay from persisted checkpoints drove completion to 1.0000 across all tested mismatch rates, compared with restart-baseline completion of 0.8976-0.9016 at 2% mismatch, 0.4152-0.4464 at 5%, and 0.0472-0.0544 at 10%. Replay without ledger validation also completed, but had 0.0000 ledger-verified completion versus 1.0000 for replay with ledger validation, isolating auditability as the ledger mechanism's contribution in this model.

## Boundaries and scale limits

Synthetic harness only; no live LangGraph controller, no live tool APIs, no concurrent writers, no OS process-kill fault injection, and no validation of crash consistency beyond SQLite checkpoint replay semantics. The tested mismatch occurs before step commit, so results do not cover corrupt committed evidence or post-commit tool drift.

## Claim scope

In a deterministic SQLite-backed synthetic agent harness with 40-step tool workflows, fixed mismatch rates of 0.02, 0.05, and 0.10, five fixed seeds, restart/checkpoint/replay ablations, and 30,000 total policy episodes, persistent checkpoint replay with evidence-ledger prefix validation recovered all injected mismatch-before-commit halts while preserving ledger-verified completion.

## Why it stopped

Medium synthetic Tier 2 evidence supports the mechanism but is not publication-grade because it does not exercise the real controller/checkpointer/tool stack or OS-level hard cutovers.

## Recommended next action

Run a live LangGraph/evidence-ledger integration fault-injection test that kills and resumes the process at tool-mismatch boundaries, and require replay-with-ledger to retain at least 0.99 verified completion while restart remains materially worse.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LangGraph process-kill replay validation for evidence-ledger mismatch halts
- Success threshold: Replay-with-ledger achieves at least 0.99 ledger-verified completion with duplicate side effects at least 80% lower than restart-only recovery across all fixed mismatch-rate conditions.
- Stop condition: Stop if live replay-with-ledger falls below 0.95 verified completion, if ledger validation fails on any successful completion, or if duplicate side effects are not materially lower than restart-only recovery.

## Evidence references

- Artifact root: `<local-path>/projects/persistent-checkpoint-replay-validation-for-evidence-ledge-d2a7b34684`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
