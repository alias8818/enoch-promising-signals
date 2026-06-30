# Replay ledger on a real local agent/tool harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-ledger-on-a-real-local-agent-tool-harness-0fd1cbc09c`
Run ID: `replay-ledger-on-a-real-local-agent-tool-harness-0fd1cbc09c-20260531T174744160807+0000`

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

- Parent run decision: Deterministic replay ledger for stochastic CPU agents: enoch://control-plane/projects/deterministic-replay-ledger-for-stochastic-cpu-agents-066d978d16a8/runs/deterministic-replay-ledger-for-stochastic-cpu-agents-066d978d16a8-20260531T130733591784+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8408ff0055b8

## What looked useful

The Tier 1 direct test supports the mechanism for small local agent/tool debugging: deterministic local subprocess/filesystem episodes replayed with 0/30 failures, deterministic reruns had 0/30 failures, and all seeded integrity/nondeterminism controls were detected.

## Boundaries and scale limits

One dependency-free local harness; 120 deterministic tool records; short text-file filesystem tasks; no real LLM planner, concurrent tools, remote APIs, binary-heavy workspaces, crash recovery, or large repository state.

## Claim scope

In a 30-episode local CPU harness with real bash/python3/filesystem tool calls, a hash-chained append-only replay ledger with workspace digests and snapshots exactly replayed deterministic episodes and detected seeded ledger tampering, workspace mutation, and nondeterministic command output.

## Why it stopped

Tier 1 direct validation passed and produced a useful mechanism signal, but the evidence is too small and harness-specific for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on a real local LLM agent loop with at least 100 multi-tool tasks and a no-ledger baseline/control before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay ledger on a real local LLM agent loop
- Success threshold: At least 99% exact deterministic replay, 100% detection of seeded tamper/mutation/nondeterminism controls, and less than 2x wall-clock overhead versus the baseline on the tested task suite.
- Stop condition: Stop if exact replay falls below 95% on deterministic tasks, any seeded tamper/mutation control is missed, or overhead exceeds 3x without a clear optimization path.

## Evidence references

- Artifact root: `<local-path>/projects/replay-ledger-on-a-real-local-agent-tool-harness-0fd1cbc09c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
