# Agent-Trace Validation of Falsifiable Memory Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-trace-validation-of-falsifiable-memory-ledger-bf24cb1ba8`
Run ID: `agent-trace-validation-of-falsifiable-memory-ledger-bf24cb1ba8-20260528T140832921513+0000`

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

- Parent run decision: Falsifiable Memory Ledger for Long-Context CPU Agents: enoch://control-plane/projects/falsifiable-memory-ledger-for-long-context-cpu-agents-7b7d543c25bf/runs/falsifiable-memory-ledger-for-long-context-cpu-agents-7b7d543c25bf-20260528T001723246961+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/eb1767320215

## What looked useful

Tier 1 controlled direct test passed: 80 TP, 80 TN, 0 FP, 0 FN; precision 1.0, true-entry recall 1.0, false-entry rejection recall 1.0 against threshold >=0.95 for each.

## Boundaries and scale limits

Single local trace snapshot, controlled mutations, generated ledger entries, no naturally occurring memory drift, no human-authored ledger, no cross-agent or cross-schema validation, and no downstream task-success measurement.

## Claim scope

A deterministic falsifiable memory ledger verifier accepted all true machine-checkable ledger entries and rejected all seeded false or non-falsifiable entries on one frozen local Codex agent-trace snapshot with 160 controlled entries.

## Why it stopped

No-paper closure: the mechanism passed a Tier 1 controlled direct test, but evidence is too narrow and mutation-controlled for publication readiness.

## Recommended next action

Run a bounded multi-trace deepen test on at least 20 independent agent traces with a mix of human-authored and model-authored ledger entries before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Trace Validation of Falsifiable Memory Ledger Entries
- Success threshold: Aggregate and per-trace lower-bound metrics should satisfy precision >=0.95, true-entry recall >=0.95, and false-entry rejection recall >=0.95, with no unclassified false positives.
- Stop condition: Stop as unsupported if any metric falls below 0.90 on aggregate or if false memories pass verification due to predicate weakness in more than one trace.

## Evidence references

- Artifact root: `<local-path>/projects/agent-trace-validation-of-falsifiable-memory-ledger-bf24cb1ba8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
