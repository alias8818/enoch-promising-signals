# Bounded Evidence Ledger in a Real CPU Agent Harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-evidence-ledger-in-a-real-cpu-agent-harness-b28ab5d548`
Run ID: `bounded-evidence-ledger-in-a-real-cpu-agent-harness-b28ab5d548-20260607T220340447896+0000`

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

- Parent run decision: Bounded Evidence Ledger for CPU Agent Reliability: enoch://control-plane/projects/bounded-evidence-ledger-for-cpu-agent-reliability-3eceafe52906/runs/bounded-evidence-ledger-for-cpu-agent-reliability-3eceafe52906-20260607T131558546167+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/143d4d45374d

## What looked useful

A bounded ledger can work under tight memory only when retention is task-aware. A query-agnostic ledger diagnostic failed by evicting target evidence, while the corrected task-aware ledger reached 1.0 answer accuracy, evidence coverage, and digest verification at 512-4096 byte budgets against a rolling transcript baseline at 0.0.

## Boundaries and scale limits

Tier 1 controlled small direct test only: 36 generated scenarios, deterministic regex extraction, deterministic policy, local text and subprocess tools, no LLM sampling, no natural long-horizon traces, and no human audit labels.

## Claim scope

In a deterministic CPU tool harness with generated local fixtures, known active queries, and byte-bounded memory, a task-aware structured evidence ledger preserved query-relevant digest-linked facts under distractor pressure where an equal-budget rolling transcript lost them.

## Why it stopped

Closed as no-paper useful signal: the controlled CPU harness directly supports the task-aware retention mechanism but is deterministic and too small for publication-grade agent reliability claims.

## Recommended next action

Run a bounded deepen test with a small local LLM or noisy extractor on natural agent traces, preserving the same byte budgets and scoring extraction errors end-to-end.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy Extraction Test for Task-Aware Bounded Evidence Ledgers
- Success threshold: Across at least 50 paired natural/noisy traces and three matched budgets, the ledger must improve answer accuracy by at least 10 percentage points over both baselines while maintaining at least 0.90 evidence coverage and digest verification, with less than 5x latency overhead.
- Stop condition: Stop if ledger accuracy is not above the best baseline at two or more budgets, if evidence coverage falls below 0.80, or if extraction noise makes the support links unverifiable.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-evidence-ledger-in-a-real-cpu-agent-harness-b28ab5d548`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
