# Live-agent counterexample ledger on held-out CPU coding tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-agent-counterexample-ledger-on-held-out-cpu-coding-ta-ca3aacb431`
Run ID: `live-agent-counterexample-ledger-on-held-out-cpu-coding-ta-ca3aacb431-20260529T050243324921+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Counterexample Ledger in a Real CPU Coding-Agent Harness: enoch://control-plane/projects/counterexample-ledger-in-a-real-cpu-coding-agent-harness-6843af2ce7/runs/counterexample-ledger-in-a-real-cpu-coding-agent-harness-6843af2ce7-20260529T000123236434+0000
- Parent run decision: Counterexample Ledger for Self-Correction in CPU Agents: enoch://control-plane/projects/counterexample-ledger-for-self-correction-in-cpu-agents-0c8555cc37c8/runs/counterexample-ledger-for-self-correction-in-cpu-agents-0c8555cc37c8-20260528T193631124988+0000

## What looked useful

Ledger retention reduced repeated regressions to zero and improved sparse-public solve rate from 88.36% to 94.05% at a 3-hidden-submission budget, beating latest-only and random-matched controls there; at 4 submissions it beat latest-only but not random-matched, and at 2 submissions it had no latest-only advantage.

## Boundaries and scale limits

Synthetic hand-authored tasks and repair candidates; no LLM-generated code, no standard HumanEval/MBPP benchmark, and no live external judge. Authored public tests saturated all methods, and a random matched-test control matched or exceeded the ledger in the 4-submission sparse-public setting.

## Claim scope

In a deterministic Python repair-agent harness over 13 held-out CPU coding tasks, persistent task-local counterexample ledgers improved solve rate over a latest-only feedback baseline when public tests were sparse and hidden-submission budget was moderately tight.

## Why it stopped

Tier-2 synthetic harness produced mixed mechanism support but not publication-grade live-agent evidence.

## Recommended next action

Stop this run as no-paper useful signal; next direct test should run the same ledger/latest-only/random-matched comparison with an actual coding agent on standard HumanEval/MBPP-style held-out tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual coding-agent counterexample ledger on HumanEval/MBPP-style held-out tasks
- Success threshold: Ledger improves paired pass rate by at least 5 percentage points over latest-only and at least 2 points over random/control memory with no increase in judge submissions, across at least 100 task-seed trials.
- Stop condition: Stop if the ledger fails to beat latest-only by 2 percentage points or fails to reduce repeated regressions on the first 100 paired task-seed trials.

## Evidence references

- Artifact root: `<local-path>/projects/live-agent-counterexample-ledger-on-held-out-cpu-coding-ta-ca3aacb431`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
