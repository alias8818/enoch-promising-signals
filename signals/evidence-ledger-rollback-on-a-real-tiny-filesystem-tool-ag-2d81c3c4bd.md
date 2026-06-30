# Evidence ledger rollback on a real tiny filesystem tool agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-on-a-real-tiny-filesystem-tool-ag-2d81c3c4bd`
Run ID: `evidence-ledger-rollback-on-a-real-tiny-filesystem-tool-ag-2d81c3c4bd-20260601T042605252857+0000`

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

- Parent run decision: Evidence ledger and rollback for tiny tool agent: enoch://control-plane/projects/evidence-ledger-and-rollback-for-tiny-tool-agent-4d5a52fef59d/runs/evidence-ledger-and-rollback-for-tiny-tool-agent-4d5a52fef59d-20260601T001201722314+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6290d1416720

## What looked useful

The mechanism worked on a real tiny filesystem control: ledger policy achieved 100% fault restoration and 100% valid-change retention, while the no-rollback baseline restored 0/60 fault trials. This is useful as a reproducible local mechanism signal but not a paper-ready validation.

## Boundaries and scale limits

Small Tier 1 direct test only: deterministic scripted agent actions, four tiny files, full-copy snapshots, no live LLM planner, no crash injection, no concurrency, no symlink/permission/special-file handling, no large-tree stress, and no production agent framework integration.

## Claim scope

In a controlled scripted tiny-filesystem tool-agent harness using real ext4 workspace files, a pre-action evidence snapshot plus validation-triggered rollback restored 60/60 corrupting or destructive fault trials to the exact pre-action visible file-content hash tree and kept 20/20 valid edits.

## Why it stopped

Tier 1 controlled direct test completed and supports the local mechanism, but evidence is too small and scripted for publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up with crash injection and randomized multi-step filesystem operations to test whether rollback remains exact under interrupted or interleaved tool execution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-injected evidence ledger rollback on randomized tiny filesystem action sequences
- Success threshold: Ledger restores the exact pre-sequence visible tree in at least 99/100 crash or validation-failure sequences, preserves valid sequences without rollback in at least 99/100 cases, and beats the no-rollback baseline by at least 50 percentage points on failed sequences.
- Stop condition: Stop early if any deterministic seed produces an unrecoverable ledger state that cannot be explained as a harness bug, or after 100 crash/fault sequences and 100 valid sequences complete with aggregate metrics.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-on-a-real-tiny-filesystem-tool-ag-2d81c3c4bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
