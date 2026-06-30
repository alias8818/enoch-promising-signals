# Task-Bound Evidence Ledger on Real Local-Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `task-bound-evidence-ledger-on-real-local-agent-traces-6d9b417660`
Run ID: `task-bound-evidence-ledger-on-real-local-agent-traces-6d9b417660-20260604T142710901649+0000`

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

- Parent run decision: Evidence Ledger for Small Local Agent Tool-Use: enoch://control-plane/projects/evidence-ledger-for-small-local-agent-tool-use-42122f1b997a/runs/evidence-ledger-for-small-local-agent-tool-use-42122f1b997a-20260604T065814075277+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8ecf6cd3b5fd

## What looked useful

The controlled direct test produced 24 ledger entries with 24/24 source line and SHA-256 provenance, 12/12 completed command exit codes, 0 invalid JSON lines, 5/8 task obligations covered from action text, and all required artifact existence checks true. A first-pass hazard was found and fixed: matching command output can falsely count prompt text as evidence.

## Boundaries and scale limits

Validated on one 35-line live local-agent trace only; no multi-run corpus, hand-labeled precision/recall, adversarial traces, or cross-agent trace formats were tested.

## Claim scope

A deterministic ledger can extract source-line, hash-bound evidence entries from one real local Codex JSONL trace and cover task obligations from action text without using prompt-output contamination.

## Why it stopped

Tier 1 direct local trace test passed but remains single-trace, no-paper evidence; mechanism support is not publication readiness.

## Recommended next action

Run a bounded deepen follow-up on at least 20 completed real local-agent traces with independent obligation labels and report obligation-level precision/recall before considering any paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hand-Labeled Multi-Trace Evaluation for Task-Bound Evidence Ledgers
- Success threshold: At least 0.85 precision, at least 0.75 recall on labeled obligation fulfillment, 100% source-line/hash coverage for completed ledger entries, and no prompt-output contamination false positives in the audited sample.
- Stop condition: Stop if precision falls below 0.70 after prompt-output contamination controls, or if completed trace events lack source/hash/exit-code fields often enough to prevent auditability.

## Evidence references

- Artifact root: `<local-path>/projects/task-bound-evidence-ledger-on-real-local-agent-traces-6d9b417660`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
