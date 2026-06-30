# Reversible Action Ledger for Small Safe Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `reversible-action-ledger-for-small-safe-agents-661f78ab79f6`
Run ID: `reversible-action-ledger-for-small-safe-agents-661f78ab79f6-20260530T001811288410+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b0a71578baf5

## What looked useful

Across 100000 main trials, direct and audit-only execution each produced unsafe notifications in 37.122% of trials with 43039 unsafe notifications total, while the reversible ledger produced 0 unsafe notifications, preserved workspace validity in 100% of trials, and ran with about 2.1x executor runtime overhead. A 30k-trial mutation sweep at rates 0.02, 0.08, and 0.16 also produced 0 ledger unsafe notifications while direct unsafe rates rose from 22.303% to 50.447%.

## Boundaries and scale limits

Synthetic single-process CPU simulation only; no real LLM planner, real tool API, concurrent execution, human approval loop, long-horizon task graph, or production compensating-action adapter was tested.

## Claim scope

In a deterministic synthetic small-agent benchmark with reversible workspace edits, invariant checks, crashes, corrupt actions, action reordering, and deferred external notifications, a reversible action ledger eliminated unsafe notifications compared with direct and audit-only execution.

## Why it stopped

Mechanism is supported only by synthetic evidence, which is insufficient for a paper-positive claim about real safe agents.

## Recommended next action

Stop this run as a no-paper useful signal; next run should validate the same ledger contract on real LLM tool-call traces with mocked irreversible APIs and concurrency/retry faults.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reversible ledger on real tool-calling agent traces
- Success threshold: At least 1000 realistic tool-call episodes with a statistically lower unsafe-side-effect rate than both baselines, zero unrolled-back invariant violations after handled failures, and no more than 10% relative loss in valid task completion.
- Stop condition: Stop if the ledger cannot model inverses/commit barriers for at least 80% of the selected tool actions, or if valid task completion drops by more than 10% while unsafe side effects are not reduced by at least 50%.

## Evidence references

- Artifact root: `<local-path>/projects/reversible-action-ledger-for-small-safe-agents-661f78ab79f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
