# Bounded LLM-agent replication of counterexample ledger harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-llm-agent-replication-of-counterexample-ledger-har-fc2805fbd6`
Run ID: `bounded-llm-agent-replication-of-counterexample-ledger-har-fc2805fbd6-20260605T232445224387+0000`

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

- Parent run decision: Agent reliability via evidence ledger with counterexamples: enoch://control-plane/projects/agent-reliability-via-evidence-ledger-with-counterexamples-891798f8cbe2/runs/agent-reliability-via-evidence-ledger-with-counterexamples-891798f8cbe2-20260605T153409056113+0000
- Parent run decision: Natural-language LLM-agent counterexample ledger harness: enoch://control-plane/projects/natural-language-llm-agent-counterexample-ledger-harness-572c981a56/runs/natural-language-llm-agent-counterexample-ledger-harness-572c981a56-20260605T211255185218+0000

## What looked useful

Across 800 paired task/seed episodes per strategy, the full ledger reached 100% exact recovery with mean 7.77 steps, versus 23.0% for no-ledger and 39.25% for last-counterexample context; truncated and corrupted-ledger ablations support the counterexample-retention mechanism.

## Boundaries and scale limits

Evidence is limited to a finite symbolic DSL, 8 Boolean features, 160 tasks, 5 fixed seeds, and a stochastic proposal-policy surrogate rather than an actual LLM agent or natural benchmark.

## Claim scope

In a bounded synthetic Boolean-rule recovery harness with exhaustive oracle counterexamples, a persistent correct counterexample ledger improves exact recovery and efficiency over no-ledger and last-counterexample baselines.

## Why it stopped

Medium synthetic validation supports the mechanism but remains proxy evidence for LLM-agent behavior, so it is not paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded deepen test should replace the surrogate proposal policy with an actual local or API LLM while preserving paired ledger/no-ledger controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual LLM proposal test for counterexample ledger harness
- Success threshold: Full-ledger LLM agent improves exact-recovery success by at least 20 percentage points over both no-ledger and last-counterexample baselines, with paired budgeted-step wins on at least 65% of non-tied task/seed pairs.
- Stop condition: Stop as negative if the full ledger fails to beat either real baseline by 10 percentage points or if gains disappear under a correct-vs-corrupted ledger control.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-llm-agent-replication-of-counterexample-ledger-har-fc2805fbd6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
