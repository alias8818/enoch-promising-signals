# Concurrent crash-safe anchored evidence ledger for local agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `concurrent-crash-safe-anchored-evidence-ledger-for-local-a-2e05f5fd60`
Run ID: `concurrent-crash-safe-anchored-evidence-ledger-for-local-a-2e05f5fd60-20260609T180107566076+0000`

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

- Parent run decision: Hash-chained evidence ledger for small local agents: enoch://control-plane/projects/hash-chained-evidence-ledger-for-small-local-agents-0f380ac31808/runs/hash-chained-evidence-ledger-for-small-local-agents-0f380ac31808-20260609T132655290717+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a08a821698a2

## What looked useful

The corrected mechanism passed 4/4 Tier 1 direct trials: 557-763 recovered safe records per trial, zero missing acknowledged safe appends, valid post-recovery anchors, tamper detection, and an unsafe split-write control with 12912-17174 corrupt lines plus over 1000 missing/corrupt acknowledged events per trial.

## Boundaries and scale limits

Validated only on local process-kill tests with 6 writer processes, 3-4 seconds per trial, and one host/filesystem context. Not validated for power loss, distributed agents, malicious writers, remote anchoring, long runtime, or filesystem diversity.

## Claim scope

A standard-library local Python reference ledger using advisory file locks, fsynced JSONL hash-chain appends, atomic anchor replacement, and recovery-time anchor rebuild preserved all acknowledged appends under 4 corrected local multi-process SIGKILL trials and detected tampering.

## Why it stopped

Tier 1 mechanism evidence is useful but not publication-grade; the first stale-anchor failure also showed the design needed recovery-time anchor repair before broader validation.

## Recommended next action

Run a bounded deepen follow-up with local-agent workload integration, independent reader verification, and filesystem variants before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Filesystem-diverse local-agent anchored ledger recovery trial
- Success threshold: Across at least 30 trials and at least two filesystem contexts, every acknowledged append is present after recovery, every recovered ledger verifies, every tamper mutation is detected, and the unsafe control fails in a measurable way.
- Stop condition: Stop as unsupported if any acknowledged append is missing, recovery cannot rebuild a valid anchor, or tampering is not detected in a corrected reference run.

## Evidence references

- Artifact root: `<local-path>/projects/concurrent-crash-safe-anchored-evidence-ledger-for-local-a-2e05f5fd60`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
