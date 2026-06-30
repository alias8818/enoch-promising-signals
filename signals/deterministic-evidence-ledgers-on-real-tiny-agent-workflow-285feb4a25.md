# Deterministic evidence ledgers on real tiny-agent workflows with replay drift

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-evidence-ledgers-on-real-tiny-agent-workflow-285feb4a25`
Run ID: `deterministic-evidence-ledgers-on-real-tiny-agent-workflow-285feb4a25-20260528T180510922843+0000`

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

- Parent run decision: Deterministic evidence ledger for tiny agent reliability: enoch://control-plane/projects/deterministic-evidence-ledger-for-tiny-agent-reliability-9329e525f021/runs/deterministic-evidence-ledger-for-tiny-agent-reliability-9329e525f021-20260528T154250896752+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0c44e0cde6a7

## What looked useful

Per-node deterministic evidence ledgers detected 20/20 injected replay drift cases with 0/4 clean replay false positives, while a final-output-only baseline missed 4/20 hidden-policy drift cases.

## Boundaries and scale limits

Uses local deterministic policy code rather than API-backed LLM agents; drift is injected rather than naturally observed; no concurrent, long-running, persisted, or production workflow validation.

## Claim scope

Controlled local Tier-1 test on four real LangGraph tiny-agent workflows with deterministic plan-tool-summarize execution and injected replay drift.

## Why it stopped

Tier-1 controlled direct test met the mechanism threshold, but evidence is not broad or production-grade enough for paper readiness.

## Recommended next action

Run a bounded deepen test on API-backed tiny agents with persisted checkpoints and naturally induced replay drift, requiring zero clean false positives and materially better recall than final-output-only replay.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: API-backed tiny-agent replay drift ledger validation
- Success threshold: Ledger detects at least 95% of induced or naturally observed drift cases with 0 clean replay false positives and beats final-output-only recall by at least 15 percentage points.
- Stop condition: Stop as negative if clean replay false positives exceed 0 or if ledger recall does not exceed the final-output-only baseline by at least 15 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-evidence-ledgers-on-real-tiny-agent-workflow-285feb4a25`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
