# Checksum Ledger for Local CPU Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `checksum-ledger-for-local-cpu-agents-75f6a291be92`
Run ID: `checksum-ledger-for-local-cpu-agents-75f6a291be92-20260607T052308247296+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4d064f2d90ca

## What looked useful

Clean verification passed and all tested workspace mutations were detected across 0.39 MiB, 7.81 MiB, and 100 MiB synthetic workspaces with sub-second scans. Naive ledger tampering was detected, but a complete local rewrite attack passed without an external anchor.

## Boundaries and scale limits

Synthetic-only test; no real agent-loop integration, no concurrent writer stress, no multi-GB repositories, and no external immutable ledger anchor. A process with write access to both workspace and ledger can rewrite a consistent local history.

## Claim scope

A dependency-free SHA-256 checksum ledger can cheaply detect ordinary local workspace drift for CPU agents on synthetic file trees up to 100 MiB, including same-size edits, renames, additions, and deletions.

## Why it stopped

Bounded local evidence supports drift detection but also exposes a decisive trust-boundary limitation: an unauthenticated ledger in the same writable workspace can be forged by full local rewrite.

## Recommended next action

Stop this run as no-paper useful signal; next test should add an external anchor or signing policy and rerun the mutation suite on a real agent workspace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored Checksum Ledger for Agent Workspaces
- Success threshold: Detect 100% of same-size edit, rename, add, delete, naive ledger tamper, and full local rewrite attempts while keeping p95 append and verify time under 2 seconds for a representative real workspace and under 10 seconds for 1 GiB synthetic data.
- Stop condition: Stop if anchored verification fails to detect any full local rewrite attempt or if checkpoint overhead exceeds the success threshold by more than 2x on the representative workspace.

## Evidence references

- Artifact root: `<local-path>/projects/checksum-ledger-for-local-cpu-agents-75f6a291be92`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
