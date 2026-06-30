# Crash-consistent evidence ledger under concurrent home-worker writes

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `crash-consistent-evidence-ledger-under-concurrent-home-wor-00ab05c0fa`
Run ID: `crash-consistent-evidence-ledger-under-concurrent-home-wor-00ab05c0fa-20260611T051609883848+0000`

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

- Parent run decision: Lightweight Evidence Ledger for Home GPU Workers: enoch://control-plane/projects/lightweight-evidence-ledger-for-home-gpu-workers-b9da40e1e11d/runs/lightweight-evidence-ledger-for-home-gpu-workers-b9da40e1e11d-20260611T022906027415+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eb27cdc59ebe

## What looked useful

Across the primary run and five repeats, safe ledger runs had 3,199 valid committed records, 0 invalid committed records, 0 duplicate event ids, and 16 leftover temp files from interrupted writes; unsafe shared append controls produced 3,416 invalid records.

## Boundaries and scale limits

Validated only on the local project filesystem with short CPU-only runs. Not validated on real shared home directories, network filesystems, power loss, disk-cache failure modes, long-duration churn, or controller-integrated recovery.

## Claim scope

A local one-file-per-event ledger using temp writes, file fsync, atomic rename, and committed-directory fsync preserved parseable checksummed committed evidence records under 12 concurrent Python worker processes with injected SIGKILL.

## Why it stopped

Tier 1 direct local evidence supports the mechanism but is not sufficient for a paper or production claim.

## Recommended next action

Run a medium confirmation on the actual shared home-worker filesystem or a faithful NFS/SMB mount with recovery replay after repeated worker kills and at least one remount or host-crash-style interruption.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium shared-filesystem crash-recovery confirmation for the evidence ledger
- Success threshold: Zero invalid committed records, zero duplicate committed ids, deterministic recovery replay in all trials, and less than 2x throughput overhead versus a locked append baseline.
- Stop condition: Stop early if any checksummed committed record is invalid, replay is nondeterministic after recovery, or filesystem semantics make directory fsync/atomic rename unavailable.

## Evidence references

- Artifact root: `<local-path>/projects/crash-consistent-evidence-ledger-under-concurrent-home-wor-00ab05c0fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
