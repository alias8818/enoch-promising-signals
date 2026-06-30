# Local Checksum Ledger for CPU Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `local-checksum-ledger-for-cpu-agent-reliability-9e0b3745af8e`
Run ID: `local-checksum-ledger-for-cpu-agent-reliability-9e0b3745af8e-20260529T015143383309+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e8a03bd370e8

## What looked useful

Checksum content tracking caught 3/3 same-size mtime-preserved corruptions where stat tracking caught 0/3, and caught 3/3 for single-byte corruption, truncate, delete, and rename. Clean checksum overhead was 1.22x versus no tracking and 1.07x versus stat tracking in the reduced bounded run.

## Boundaries and scale limits

Synthetic workload only; 3 seeds per injected fault; one clean seed per detector for false-positive and overhead comparison; no real agent traces, concurrent writers, crash recovery, symlink behavior, permission failures, hostile ledger tampering, or large workspaces tested.

## Claim scope

In a synthetic local CPU workspace with 100 initial files, 500 intended file operations per trial, periodic audits, and five injected filesystem fault classes, a content-checksum ledger detected metadata-preserving content corruption that stat-only tracking missed, and detected all injected tested faults.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not a full validation of CPU agent reliability or a paper-ready result.

## Recommended next action

Stop this run as a no-paper useful signal; next, replay real or recorded agent file-operation traces with clean-run false-positive measurement before considering any reliability claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Real Agent Workspace Traces Through a Checksum Ledger
- Success threshold: Checksum detects at least 95% of injected metadata-preserving content faults and at least matches stat tracking on structural faults, with clean false positives under 1% and mean runtime overhead under 2x.
- Stop condition: Stop if checksum false positives exceed 5% on clean traces, overhead exceeds 3x after reasonable audit-cadence tuning, or stat tracking detects the target fault class equally well on real traces.

## Evidence references

- Artifact root: `<local-path>/projects/local-checksum-ledger-for-cpu-agent-reliability-9e0b3745af8e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
