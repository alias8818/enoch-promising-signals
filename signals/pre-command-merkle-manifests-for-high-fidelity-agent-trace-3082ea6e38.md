# Pre-command Merkle manifests for high-fidelity agent trace replay

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `pre-command-merkle-manifests-for-high-fidelity-agent-trace-3082ea6e38`
Run ID: `pre-command-merkle-manifests-for-high-fidelity-agent-trace-3082ea6e38-20260530T011631603851+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Replay real captured agent traces with repository-scale snapshot binding: enoch://control-plane/projects/replay-real-captured-agent-traces-with-repository-scale-sn-bc687ec734/runs/replay-real-captured-agent-traces-with-repository-scale-sn-bc687ec734-20260529T211520945643+0000
- Parent run decision: Replay a snapshot-bound multi-step agent trace with write operations: enoch://control-plane/projects/replay-a-snapshot-bound-multi-step-agent-trace-with-write-4f56cfe9d1/runs/replay-a-snapshot-bound-multi-step-agent-trace-with-write-4f56cfe9d1-20260529T164113306347+0000

## What looked useful

Pre+post manifests achieved 100% drift detection, 100% exact localization, 100% pre-execution detection, and 0% unsafe destructive execution in 240 drift cases per guard. Post-only detected 86.67% but had 0% pre-execution detection and executed destructive drift cases at 20%; 30 paired mutate/delete cases showed post-only masking where pre-command checks caught drift that post-command checks missed.

## Boundaries and scale limits

Validated on 16 fixed-seed synthetic traces with 50 initial files, 30 recorded commands, 48 clean controls, and 720 injected drift replay cases. Not validated on real agent trace corpora, package manager/network/container workflows, large binary workspaces, nondeterministic clocks, permissions, symlinks, or optimized incremental Merkle implementations.

## Claim scope

In deterministic synthetic local file-system traces, adding pre-command Merkle manifests to post-command manifests detects injected replay drift before command execution, localizes the divergent command exactly, and prevents destructive commands from running on drifted state better than command-only logs or post-command-only manifests.

## Why it stopped

Tier 4 paper-readiness was not met: the evidence is synthetic/local mechanism support rather than robust replication on real high-fidelity agent trace replay workloads.

## Recommended next action

Stop this follow-up at depth 4 and preserve the reproducible useful signal; do not claim paper readiness without a real agent-trace corpus and production-style incremental manifest overhead study.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/pre-command-merkle-manifests-for-high-fidelity-agent-trace-3082ea6e38`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
