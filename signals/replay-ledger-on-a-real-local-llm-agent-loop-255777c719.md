# Replay ledger on a real local LLM agent loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-ledger-on-a-real-local-llm-agent-loop-255777c719`
Run ID: `replay-ledger-on-a-real-local-llm-agent-loop-255777c719-20260531T225050861117+0000`

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

- Parent run decision: Replay ledger on a real local agent/tool harness: enoch://control-plane/projects/replay-ledger-on-a-real-local-agent-tool-harness-0fd1cbc09c/runs/replay-ledger-on-a-real-local-agent-tool-harness-0fd1cbc09c-20260531T174744160807+0000
- Parent run decision: Deterministic replay ledger for stochastic CPU agents: enoch://control-plane/projects/deterministic-replay-ledger-for-stochastic-cpu-agents-066d978d16a8/runs/deterministic-replay-ledger-for-stochastic-cpu-agents-066d978d16a8-20260531T130733591784+0000

## What looked useful

Tier 2 bounded evidence supports the replay-ledger mechanism at a real local LLM tool boundary: 20/20 episodes produced tool records, full snapshot replay and deterministic rerun were 100%, tamper/mutation/nondeterminism controls were detected, and transcript-only baseline lacked core integrity diagnostics.

## Boundaries and scale limits

One small local model, one tool call per task, prompt-shaped arithmetic/counting workloads, small text workspaces, no production agent framework, no concurrent or streaming tools, no crash persistence, no binary/symlink/permission edge cases, and no evidence that ledgering improves model answer correctness.

## Claim scope

In a bounded 20-task fixed-seed local CPU experiment with Qwen/Qwen2.5-0.5B-Instruct emitting one real shell action per task, a hash-chained replay ledger with initial and after snapshots exactly replayed deterministic local shell/file episodes and detected seeded ledger tampering, workspace mutation, and nondeterministic command output; transcript-only logging failed tamper and workspace-mutation detection.

## Why it stopped

Evidence supports the scoped mechanism but is not paper-ready because it uses one small model, a standalone harness, one tool call per task, and small text workspaces.

## Recommended next action

Stop as no-paper useful signal; the concrete next bounded deepen test is production agent-framework integration with multi-step tasks, crash-persistent writes, and filesystem edge cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production local-agent replay ledger with crash-persistent multi-step tool traces
- Success threshold: >=95% exact deterministic replay, >=99% deterministic rerun agreement, 100% seeded tamper/mutation/crash/nondeterminism detection for the full ledger, and clear diagnostic advantage over transcript-only baseline.
- Stop condition: Stop if the full ledger falls below 95% exact replay on deterministic traces or fails any seeded integrity-control class after one implementation repair pass.

## Evidence references

- Artifact root: `<local-path>/projects/replay-ledger-on-a-real-local-llm-agent-loop-255777c719`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
