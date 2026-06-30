# Intercepted Evidence Ledger on Real Local-Agent Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `intercepted-evidence-ledger-on-real-local-agent-tool-calls-3b9d879c0b`
Run ID: `intercepted-evidence-ledger-on-real-local-agent-tool-calls-3b9d879c0b-20260526T150041318082+0000`

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

- Parent run decision: Evidence Ledger and Rollback for Local Agents: enoch://control-plane/projects/evidence-ledger-and-rollback-for-local-agents-df9522eeec1b/runs/evidence-ledger-and-rollback-for-local-agents-df9522eeec1b-20260526T001711499660+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b4b0386b97fe

## What looked useful

The ledger parser recovered all expected sentinel outputs from real local-agent shell tool calls, captured an intentional exit 7 failure, found zero JSON parse errors, found zero missing start events, and produced ledger rows with required audit fields for all 12 completed command calls.

## Boundaries and scale limits

Tested on 12 completed command_execution events from one local run, including three controlled sentinels and one intentional nonzero exit. Not tested across other agent tools, controller implementations, large/binary outputs, independent ground-truth capture, tamper resistance, or stdout/stderr stream separation.

## Claim scope

A Codex controller JSONL trace from one Enoch worker run can be transformed into an auditable ledger for real local shell command tool calls, preserving order, command text, completion status, exit code, and output hashes/excerpts.

## Why it stopped

Tier 1 direct mechanism support was achieved, but evidence remains a single-run shell-command trace and is insufficient for publication-grade claims.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded deepening test should compare the JSONL-derived ledger against an independent wrapper transcript across a larger heterogeneous tool-call workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Independent Ground-Truth Completeness Check for Local-Agent Evidence Ledgers
- Success threshold: At least 95% exact match for command text, ordering, exit status, and output hash against independent ground truth, with all mismatches explained and no silent dropped failures.
- Stop condition: Stop as negative if more than 5% of records are missing/mismatched, any failed command is silently dropped, or stream/channel loss prevents the intended audit claim.

## Evidence references

- Artifact root: `<local-path>/projects/intercepted-evidence-ledger-on-real-local-agent-tool-calls-3b9d879c0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
