# Checkpointed evidence ledger in a live tool-agent harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `checkpointed-evidence-ledger-in-a-live-tool-agent-harness-2cbd73d3ba`
Run ID: `checkpointed-evidence-ledger-in-a-live-tool-agent-harness-2cbd73d3ba-20260604T020650923378+0000`

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

- Parent run decision: Append-Only Evidence Ledger for Tool-Using CPU Agents: enoch://control-plane/projects/append-only-evidence-ledger-for-tool-using-cpu-agents-c63325ed93f0/runs/append-only-evidence-ledger-for-tool-using-cpu-agents-c63325ed93f0-20260603T235303994081+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/45d77e07dfa2

## What looked useful

Checkpointing every evidence event before cutover points produced 24/24 successful recoveries with zero duplicate completed tool invocations; the volatile in-memory baseline failed in 24/24 matching cutover trials because evidence was lost after restart.

## Boundaries and scale limits

This did not test production LangGraph or Codex runtime integration, concurrent tools, external APIs, long-running tools, distributed workers, OS power-loss durability beyond fsynced local files, tamper evidence, or large multi-step agent workloads.

## Claim scope

In a controlled local subprocess tool-agent harness with three deterministic tool calls and one or two injected hard process cutovers per trial, a fsynced JSONL evidence ledger allowed restarted runs to recover prior evidence, avoid duplicate completed tool calls, and make a correct final digest-backed decision in 24/24 trials.

## Why it stopped

Tier 1 mechanism was supported, but evidence remains a small controlled local harness result rather than production-harness or paper-grade validation.

## Recommended next action

Run a bounded integration follow-up in a real LangGraph or Codex-style tool-agent harness using the same randomized kill/restart schedule and requiring 100% recovery with no duplicate side effects across at least 50 multi-tool episodes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Checkpointed evidence ledger recovery in a real graph-based tool-agent runtime
- Success threshold: Checkpointed runtime achieves 100% recovery and final-answer correctness with zero duplicate completed side effects across at least 50 randomized cutover episodes, and outperforms the volatile/default baseline by at least 50 percentage points in recovery success.
- Stop condition: Stop as negative or mixed if any checkpointed episode loses required evidence, duplicates a completed side-effectful tool, or produces an incorrect final answer after replay under a reproducible cutover schedule.

## Evidence references

- Artifact root: `<local-path>/projects/checkpointed-evidence-ledger-in-a-live-tool-agent-harness-2cbd73d3ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
