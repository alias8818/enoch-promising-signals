# Crash-safe and bypass-hardened evidence-ledger rollback for recorded CPU-agent edit sessions

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `crash-safe-and-bypass-hardened-evidence-ledger-rollback-fo-9fb9f2be06`
Run ID: `crash-safe-and-bypass-hardened-evidence-ledger-rollback-fo-9fb9f2be06-20260527T051113189631+0000`

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

- Parent run decision: Evidence-Ledger Rollback for Safer CPU Agents: enoch://control-plane/projects/evidence-ledger-rollback-for-safer-cpu-agents-dd0fef2a67f7/runs/evidence-ledger-rollback-for-safer-cpu-agents-dd0fef2a67f7-20260525T061031013499+0000
- Parent run decision: Evidence-ledger rollback on real file-system CPU-agent tasks: enoch://control-plane/projects/evidence-ledger-rollback-on-real-file-system-cpu-agent-tas-b975726856/runs/evidence-ledger-rollback-on-real-file-system-cpu-agent-tas-b975726856-20260525T063051455691+0000

## What looked useful

Across 1,250 small-workspace Tier 2 trials and 750 sparse-edit sensitivity trials, the evidence ledger achieved 100% crash rollback and 100% bypass/tamper detection. No protection achieved 0% on both metrics. The snapshot-manifest baseline achieved 100% crash rollback but only 50% detection on the mixed workspace-bypass/journal-tamper attack set. Removing fsync reduced crash rollback to 57.3% in the small run and 35.6% in the sparse run; removing hash chaining reduced bypass/tamper detection to 50%. Ledger storage was worse than snapshots on tiny workspaces but about 12.7x smaller for crash metadata and 7.1x smaller for bypass metadata in the sparse-edit condition.

## Boundaries and scale limits

The experiment used synthetic sessions, logical crash cutpoints and partial-write injection, Python os.fsync semantics, and local filesystem execution. It did not replay live Codex logs, perform kernel/power-loss fault injection, test multiple filesystems, or protect against an attacker able to rewrite both workspace and trusted roots.

## Claim scope

In a deterministic local Python harness with synthetic recorded CPU-agent edit sessions, a hash-chained fsync-backed pre-image evidence ledger restored the exact pre-session manifest after all injected crash cutpoints and detected all tested workspace-bypass and journal-tamper attacks. Storage overhead was lower than full-tree snapshots only when edits were sparse relative to workspace size.

## Why it stopped

No-paper useful signal: mechanism support is moderate, but the current evidence is synthetic and logical-fault injected rather than real recorded sessions with process-level crash recovery.

## Recommended next action

Stop short of paper writing; run a bounded deepen follow-up that replays real recorded agent edit sessions in subprocesses killed with SIGKILL and recovers in a fresh process on ext4/xfs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-session process-kill validation for evidence-ledger rollback
- Success threshold: Evidence ledger achieves at least 99% crash rollback and bypass/tamper detection, no-fsync and no-hashchain ablations each fail their target mechanism by at least 20 percentage points, and ledger metadata is under 25% of snapshot metadata for sparse real sessions.
- Stop condition: Stop as negative if process-kill recovery falls below 95%, if journal tamper detection is not better than the snapshot baseline, or if real sessions are not sparse enough for any storage advantage.

## Evidence references

- Artifact root: `<local-path>/projects/crash-safe-and-bypass-hardened-evidence-ledger-rollback-fo-9fb9f2be06`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
