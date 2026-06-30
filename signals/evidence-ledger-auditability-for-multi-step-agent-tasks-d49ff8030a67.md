# Evidence-Ledger Auditability for Multi-Step Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-auditability-for-multi-step-agent-tasks-d49ff8030a67`
Run ID: `evidence-ledger-auditability-for-multi-step-agent-tasks-d49ff8030a67-20260612T233921925346+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ce43259ae602

## What looked useful

The implemented verifier achieved 3/3 true accepts and 4/4 true rejects on the seeded corpus; an accept-all baseline false-accepted all 4 trap claims.

## Boundaries and scale limits

Synthetic corpus only: 3 tasks, 9 evidence items, 7 claims, 4 traps. No live LLM agents, real tool traces, independent claim generation, adversarial paraphrase, or human audit workflow were tested.

## Claim scope

A deterministic evidence-ledger verifier can reject seeded missing-reference, unsupported-predicate, cross-task-drift, and missing-step failures on this 3-task synthetic multi-step corpus while preserving valid claims.

## Why it stopped

Closed as a useful synthetic mechanism signal, not a full validation or paper-ready result.

## Recommended next action

Run a bounded direct-evidence follow-up on replayed real or realistic tool-agent traces with independent labels and a non-ledger auditing baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger auditability on replayed tool-agent traces
- Success threshold: Ledger verifier reduces trap false accept rate by at least 50% relative to the baseline while keeping valid-claim false reject rate at or below 10%.
- Stop condition: Stop if the verifier cannot parse the trace format reproducibly, if false rejects exceed 20% in the first 10 labeled traces, or if no independently labeled traces are available.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-auditability-for-multi-step-agent-tasks-d49ff8030a67`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
