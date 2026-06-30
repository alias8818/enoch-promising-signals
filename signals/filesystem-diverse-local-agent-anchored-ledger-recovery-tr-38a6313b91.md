# Filesystem-diverse local-agent anchored ledger recovery trial

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `filesystem-diverse-local-agent-anchored-ledger-recovery-tr-38a6313b91`
Run ID: `filesystem-diverse-local-agent-anchored-ledger-recovery-tr-38a6313b91-20260609T222157470518+0000`

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

- Parent run decision: Hash-chained evidence ledger for small local agents: enoch://control-plane/projects/hash-chained-evidence-ledger-for-small-local-agents-0f380ac31808/runs/hash-chained-evidence-ledger-for-small-local-agents-0f380ac31808-20260609T132655290717+0000
- Parent run decision: Concurrent crash-safe anchored evidence ledger for local agents: enoch://control-plane/projects/concurrent-crash-safe-anchored-evidence-ledger-for-local-a-2e05f5fd60/runs/concurrent-crash-safe-anchored-evidence-ledger-for-local-a-2e05f5fd60-20260609T180107566076+0000

## What looked useful

Anchored manifests are useful for protecting the recovery plan from mutable ledger tampering and for preventing silent restoration of corrupted payloads. Exact recovery still requires redundant verified payload storage; a single local content-addressed object store is insufficient under payload tamper.

## Boundaries and scale limits

Synthetic local workload only: 162 small cases, two local backing filesystems, no real external anchor service, no signatures or key rotation, no crash-consistency testing, no concurrent writers, no large-file or million-file scale, and no redundant remote or erasure-coded payload storage.

## Claim scope

In a deterministic local benchmark across ext4 and tmpfs trees with regular files, directories, symlinks, hardlinks, modes, and fixed seeds, an out-of-band anchored manifest root enabled exact recovery from mutable-manifest tampering and detected payload-store tampering, but did not recover corrupted single-copy payload bytes.

## Why it stopped

Tier 2 local evidence supports the anchored-manifest mechanism but falsifies the stronger single-copy recovery claim under payload-store corruption; this is not publication-grade broad evidence.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up that adds independently verified redundant payload copies and repeats the same manifest and payload tamper matrix.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored ledger recovery with redundant verified payload storage
- Success threshold: Across at least the same 162-case matrix, redundant anchored recovery achieves >=0.95 exact recovery under payload tamper, 1.0 exact recovery under manifest tamper, and 1.0 tamper detection without silently restoring corrupted bytes.
- Stop condition: Stop if redundant payload recovery fails any filesystem/profile class with exact recovery below 0.90 or if storage overhead/latency is not measured well enough to compare against the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/filesystem-diverse-local-agent-anchored-ledger-recovery-tr-38a6313b91`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
