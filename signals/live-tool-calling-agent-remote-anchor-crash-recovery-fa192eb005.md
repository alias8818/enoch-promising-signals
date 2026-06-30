# Live Tool-Calling Agent Remote-Anchor Crash Recovery

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `live-tool-calling-agent-remote-anchor-crash-recovery-fa192eb005`
Run ID: `live-tool-calling-agent-remote-anchor-crash-recovery-fa192eb005-20260524T023343909395+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Remote-Anchored Real-Agent Crash-Recovery Trace Test: enoch://control-plane/projects/remote-anchored-real-agent-crash-recovery-trace-test-8f9246db19/runs/remote-anchored-real-agent-crash-recovery-trace-test-8f9246db19-20260524T022333688800+0000
- Parent run decision: Real-Agent Merkle Ledger Anchoring and Crash-Recovery Test: enoch://control-plane/projects/real-agent-merkle-ledger-anchoring-and-crash-recovery-test-e42c7a0664/runs/real-agent-merkle-ledger-anchoring-and-crash-recovery-test-e42c7a0664-20260524T021323841435+0000

## What looked useful

Across 50k primary episodes per condition and 30k stress episodes per condition, remote result anchoring held idempotent logical success at 1.0 and reduced non-idempotent duplicate executions versus no-anchor/lost-local baselines, but exactly-once success remained only 0.5427 at crash_rate 0.03 and 0.1873 at crash_rate 0.08 because crashes after external execution but before durable result recording still duplicate side effects. Intent-only anchoring matched no-anchor failure behavior, and intent-plus-result added writes without improving target metrics over result-only.

## Boundaries and scale limits

Evidence is local simulator evidence, not a real LangGraph/OpenAI/live HTTP deployment. It does not include real database/network latency, process SIGKILL orchestration, provider-side idempotency contracts, or production tool APIs.

## Claim scope

In a deterministic crash-window simulator for 20-step live tool-calling agents, remote result anchoring improves hard-cutover recovery and logical completion for idempotent tools, but remote intent-plus-result anchoring does not outperform result-only anchoring and does not guarantee exactly-once side effects for non-idempotent tools.

## Why it stopped

Moderate bounded evidence supports a practical recovery mechanism for idempotent tools but falsifies the broad exactly-once remote-anchor claim for non-idempotent side effects; simulator-only evidence and a result-only ablation prevent paper readiness.

## Recommended next action

Stop this branch as no-paper simulator evidence; the concrete next bounded test is a real runtime crash harness with transactional outbox/idempotency-key tools to test whether the after-execute/before-record window can be closed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Runtime Transactional Outbox Crash Harness for Tool-Calling Agents
- Success threshold: Across at least 1000 real process-kill episodes per condition, the transactional/idempotent outbox variant achieves 0 externally visible duplicate effects and >=0.99 logical success on idempotency-key tools, and clearly beats result-only anchoring on crash-after-execute cases.
- Stop condition: Stop if result-only anchoring matches the transactional outbox on duplicate-effect and logical-success metrics, or if non-idempotent tools still duplicate without provider-side idempotency; that would confirm the simulator boundary.

## Evidence references

- Artifact root: `<local-path>/projects/live-tool-calling-agent-remote-anchor-crash-recovery-fa192eb005`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
