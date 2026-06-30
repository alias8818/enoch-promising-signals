# Mandatory Evidence Ledger vs Free-form Agent on Repeated Task Suite

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `mandatory-evidence-ledger-vs-free-form-agent-on-repeated-task-suite-27eaed3c5558`
Run ID: `mandatory-evidence-ledger-vs-free-form-agent-on-repeated-task-suite-27eaed3c5558-20260629T114521120383+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/44e2a0250434

## What looked useful

Across 50,000 main tasks per agent, compressed free-form notes reached 0.62414 accuracy with 0.91688 unsupported decision rate, while the mandatory ledger and full-history control both reached 1.0 accuracy and 0.0 unsupported rate. A 20-configuration sweep found ledger accuracy advantage over compressed free-form from +0.21653 to +0.47.

## Boundaries and scale limits

Synthetic proxy only; no live LLM agent, no human summaries, no real operational task traces, and no measured token or latency overhead from enforcing ledger writes in a production agent loop.

## Claim scope

In a deterministic synthetic repeated-task suite with six required source-backed facts per task, a mandatory evidence ledger eliminated drift and unsupported decisions that appeared in a lossy compressed free-form-note baseline, while matching a full-history control.

## Why it stopped

Closed as no-paper useful signal because the evidence is a deterministic synthetic proxy rather than direct live-agent validation.

## Recommended next action

Run a bounded live LLM-agent follow-up on the same repeated-task suite with equal token budgets, ledger-overhead accounting, and unsupported-decision auditing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM Evidence Ledger vs Free-form Notes on Repeated Task Suite
- Success threshold: Ledger condition improves accuracy by at least 10 percentage points or cuts unsupported decisions by at least 50% versus free-form notes without more than 25% token or latency overhead.
- Stop condition: Stop if ledger advantage is below 5 percentage points and unsupported-decision reduction is below 20% across at least 1,000 evaluated tasks, or if ledger overhead exceeds 50% without a commensurate accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/mandatory-evidence-ledger-vs-free-form-agent-on-repeated-task-suite-27eaed3c5558`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
