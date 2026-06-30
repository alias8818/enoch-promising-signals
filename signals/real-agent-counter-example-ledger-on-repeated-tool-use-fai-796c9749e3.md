# Real-agent counter-example ledger on repeated tool-use failures

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-counter-example-ledger-on-repeated-tool-use-fai-796c9749e3`
Run ID: `real-agent-counter-example-ledger-on-repeated-tool-use-fai-796c9749e3-20260611T204151375882+0000`

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

- Parent run decision: Counter-Example Ledger: Negative-Memory Layer Reduces Repeated Failures: enoch://control-plane/projects/counter-example-ledger-negative-memory-layer-reduces-repeated-failures-48876d31d9e2/runs/counter-example-ledger-negative-memory-layer-reduces-repeated-failures-48876d31d9e2-20260611T184359910258+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfc61bad5e15

## What looked useful

A real Codex CLI agent repeated a misleading transient-looking failing command three times under control prompts, but stopped after one confirmation attempt when a counter-example ledger named the repeated failure pattern. The mechanism cleared the Tier 1 threshold but is not paper-ready.

## Boundaries and scale limits

Synthetic local fixtures only; hand-written ledger entries; one agent implementation; 3 paired tasks; no automatic ledger retrieval, production traces, cross-model robustness, or retry-eventual-success cases.

## Claim scope

In 3 paired controlled Codex CLI shell-tool tasks with a retryable-looking local command that always failed, a prompt-injected counter-example ledger reduced semantic repeated failed primary-command calls from 6 to 0 while preserving 3/3 task success.

## Why it stopped

Tier 1 controlled direct test met the local mechanism threshold, but evidence remains too small and synthetic for paper readiness.

## Recommended next action

Run a bounded deepen follow-up with automatic ledger generation from first-failure traces on at least 30 randomized retry/fallback tasks, including retry-eventual-success cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Automatic counter-example ledger on randomized retry/fallback tool tasks
- Success threshold: Ledger condition reduces semantic repeated failed invocations by >=50%, preserves task success within 5 percentage points of control, and has <=10% false suppression on retry-eventual-success cases.
- Stop condition: Stop if automatic ledger generation fails to reduce repeated failures by 25% in the first 15 paired tasks or causes more than 10 percentage points task-success loss.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-counter-example-ledger-on-repeated-tool-use-fai-796c9749e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
