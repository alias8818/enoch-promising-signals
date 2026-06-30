# Replay Real Agent Workspace Traces Through a Checksum Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-real-agent-workspace-traces-through-a-checksum-ledg-92bd44098e`
Run ID: `replay-real-agent-workspace-traces-through-a-checksum-ledg-92bd44098e-20260529T061647418654+0000`

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

- Parent run decision: Local Checksum Ledger for CPU Agent Reliability: enoch://control-plane/projects/local-checksum-ledger-for-cpu-agent-reliability-9e0b3745af8e/runs/local-checksum-ledger-for-cpu-agent-reliability-9e0b3745af8e-20260529T015143383309+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e8a03bd370e8

## What looked useful

The checksum-ledger mechanism worked on the controlled trace: baseline replay passed 6/6 events with zero mismatches, output tamper produced one output-hash mismatch, and workspace tamper produced one before/after tree-hash mismatch. A stale pre-existing Codex log did not cleanly replay after workspace changes, showing that historical replay needs snapshot binding.

## Boundaries and scale limits

Validation used a small mostly read-only trace from this workspace. It did not validate long multi-turn agent sessions, intentional file mutation replay, nondeterministic commands, interactive tools, or historical traces without a captured workspace snapshot.

## Claim scope

A six-command controlled real workspace trace can be replayed in an isolated workspace through a chained checksum ledger, with clean replay passing and injected output/workspace tampering detected at the affected command.

## Why it stopped

Tier 1 mechanism support only; this is a small controlled trace result, not broad or publication-grade validation.

## Recommended next action

Run a bounded deepen test on a captured 50+ command agent trace with a pre-trace workspace snapshot and intentional write operations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay a snapshot-bound multi-step agent trace with write operations
- Success threshold: Clean replay must pass all expected checks for at least 50 command events, including at least 10 intentional workspace mutations, and each injected tamper class must produce exactly localized ledger mismatches without masking later ledger-chain divergence.
- Stop condition: Stop if snapshot-bound clean replay has more than 2% unexpected mismatches after classifying nondeterministic commands, or if write-operation replay cannot distinguish intended mutations from tampering.

## Evidence references

- Artifact root: `<local-path>/projects/replay-real-agent-workspace-traces-through-a-checksum-ledg-92bd44098e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
