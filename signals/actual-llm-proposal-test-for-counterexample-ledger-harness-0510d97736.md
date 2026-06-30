# Actual LLM proposal test for counterexample ledger harness

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `48`
Project ID: `actual-llm-proposal-test-for-counterexample-ledger-harness-0510d97736`
Run ID: `actual-llm-proposal-test-for-counterexample-ledger-harness-0510d97736-20260607T001406652492+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `48`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Bounded LLM-agent replication of counterexample ledger harness: enoch://control-plane/projects/bounded-llm-agent-replication-of-counterexample-ledger-har-fc2805fbd6/runs/bounded-llm-agent-replication-of-counterexample-ledger-har-fc2805fbd6-20260605T232445224387+0000
- Parent run decision: Natural-language LLM-agent counterexample ledger harness: enoch://control-plane/projects/natural-language-llm-agent-counterexample-ledger-harness-572c981a56/runs/natural-language-llm-agent-counterexample-ledger-harness-572c981a56-20260605T211255185218+0000

## What looked useful

The corrected direct run failed all success thresholds: ledger solve rate equaled baseline at 0.375, hidden failures were worse by 0.25 on average, and prior-counterexample regressions were worse by 0.125 on average. Representative traces show the model often ignored or regressed accumulated counterexamples.

## Boundaries and scale limits

One small local model, eight local synthesis tasks, deterministic greedy decoding, three attempts per condition, CPU-only run under the resource envelope; not a public benchmark, larger model study, or 24-hour full validation.

## Claim scope

On eight local oracle-checkable Python proposal tasks with Qwen/Qwen2.5-0.5B-Instruct, an accumulated counterexample-ledger prompt did not improve proposal repair over a matched latest-failure baseline.

## Why it stopped

Corrected bounded direct actual-LLM test failed the predeclared threshold: no ledger solve-rate improvement and worse hidden-failure/regression metrics, so the prompt-only counterexample ledger harness is not paper-ready.

## Recommended next action

Stop this run as a bounded negative/useful-signal result; only pursue one final depth-4 follow-up if testing a stronger counterexample replay gate rather than the same prompt-only ledger.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Counterexample replay gate for LLM proposal repair
- Success threshold: Replay-gated ledger solve rate >= baseline + 0.10 absolute, mean prior-counterexample regressions <= baseline, and invalid-code rate not more than 0.10 absolute above baseline on at least eight tasks.
- Stop condition: Stop if replay-gated ledger fails to improve solve rate or still increases prior-counterexample regressions on the corrected harness.

## Evidence references

- Artifact root: `<local-path>/projects/actual-llm-proposal-test-for-counterexample-ledger-harness-0510d97736`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
