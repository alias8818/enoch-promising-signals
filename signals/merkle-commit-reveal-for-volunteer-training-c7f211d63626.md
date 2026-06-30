# Merkle Commit-Reveal for Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `merkle-commit-reveal-for-volunteer-training-c7f211d63626`
Run ID: `merkle-commit-reveal-for-volunteer-training-c7f211d63626-20260524T215634139562+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e971ea2dbc86

## What looked useful

Across 200 synthetic trials, honest reveals were accepted at 1.000 and tested post-commit mutations were detected at 1.000, while the no-commit baseline accepted tampered payloads by construction. Commit throughput ranged from 251.3 to 341.9 MB/s and verify throughput from 246.4 to 341.1 MB/s on one CPU process.

## Boundaries and scale limits

Synthetic float32 update bytes only; no real volunteer network, no real neural training loop, no semantic poisoning defense, no dropout/straggler modeling, no Sybil resistance, and no full federated-learning quality metrics.

## Claim scope

In a local deterministic simulation, Merkle roots over SHA-256-hashed update shards bind volunteer update bytes and metadata before reveal, detecting post-commit bit flips, truncation, and shard reordering with low CPU overhead for 4 KiB to 4 MiB payloads.

## Why it stopped

No-paper useful signal only: the result validates byte-level commit-reveal mechanics and local overhead, but it is synthetic/proxy evidence rather than direct volunteer-training validation.

## Recommended next action

Stop paper path for this run; next run should wrap the protocol around a small real federated-learning task with multiple local volunteer processes and semantic adversarial updates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Merkle Commit-Reveal on a Small Real Federated Training Task
- Success threshold: Commit-reveal detects 100% of post-commit byte changes, keeps final validation accuracy within 1 percentage point of the no-commit baseline on honest clients, and adds less than 5% per-round coordinator overhead for the tested small workload.
- Stop condition: Stop if commit-reveal overhead exceeds 10% on the small workload, honest training quality degrades by more than 2 percentage points, or the implementation cannot distinguish byte tampering from semantic poisoning in logs.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-commit-reveal-for-volunteer-training-c7f211d63626`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
