# Process-kill filesystem validation for atomic hashed evidence manifests

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `78`
Project ID: `process-kill-filesystem-validation-for-atomic-hashed-evide-a7e4915bb4`
Run ID: `process-kill-filesystem-validation-for-atomic-hashed-evide-a7e4915bb4-20260528T164353347654+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-trace crash and concurrency validation for CPU agent evidence ledgers: enoch://control-plane/projects/real-trace-crash-and-concurrency-validation-for-cpu-agent-e4a8419480/runs/real-trace-crash-and-concurrency-validation-for-cpu-agent-e4a8419480-20260527T221053264063+0000
- Parent run decision: Restart recovery and manifest validation for atomic evidence ledgers: enoch://control-plane/projects/restart-recovery-and-manifest-validation-for-atomic-eviden-8c8d8fecc9/runs/restart-recovery-and-manifest-validation-for-atomic-eviden-8c8d8fecc9-20260528T010013221711+0000

## What looked useful

Process-kill safety for hashed evidence manifests appears to come from immutable/content-addressed payload paths plus temp-file atomic rename of the published manifest. In-place overwrite is unsafe because a killed writer can leave a stale readable manifest pointing at partially overwritten evidence bytes.

## Boundaries and scale limits

Single host, single ext4 mount, process-kill only. No power-loss, kernel-panic, block-device fault, network filesystem, concurrent writer, or multi-filesystem validation. The no-fsync atomic ablation also passed, so this run does not prove fsync is necessary for process-kill safety.

## Claim scope

On the local ext4 filesystem, a content-addressed evidence layout using temp files plus atomic rename preserved a readable, SHA-256-consistent published manifest across 400 SIGKILL update trials; an in-place overwrite baseline failed in 380 of 400 killed trials.

## Why it stopped

Bounded validation supports the local process-kill mechanism but does not establish broad filesystem or crash/power-loss durability, and the fsync ablation did not separate from rename-only behavior under SIGKILL.

## Recommended next action

Stop as no-paper useful signal; use the harness and metrics as scoped engineering evidence, and require a filesystem/crash-durability matrix before making publication-grade claims.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/process-kill-filesystem-validation-for-atomic-hashed-evide-a7e4915bb4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
