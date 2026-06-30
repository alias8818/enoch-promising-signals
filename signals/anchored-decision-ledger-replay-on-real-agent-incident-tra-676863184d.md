# Anchored decision ledger replay on real agent incident traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchored-decision-ledger-replay-on-real-agent-incident-tra-676863184d`
Run ID: `anchored-decision-ledger-replay-on-real-agent-incident-tra-676863184d-20260529T071051130048+0000`

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

- Parent run decision: Hash-Chained Decision Ledger for Agent Reliability Drift Detection: enoch://control-plane/projects/hash-chained-decision-ledger-for-agent-reliability-drift-detection-f425985636ea/runs/hash-chained-decision-ledger-for-agent-reliability-drift-detection-f425985636ea-20260529T032721019597+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/87997efde574

## What looked useful

Anchored replay validated all clean ledgers and rejected all recomputed-chain incident mutations, while the no-anchor control accepted all recomputed attacks and allowed failure rewrite or omission to erase incident evidence.

## Boundaries and scale limits

Local trace corpus only; ledger rows were reconstructed from command execution events rather than natively emitted live; incident labels used command exit codes and error-like output; anchors were local snapshots, not an external immutable witness.

## Claim scope

Periodic external anchors over reconstructed command-decision ledgers rejected targeted incident-evidence rewrites, omissions, and reorders on 80 real local Codex/Enoch traces with observed command-level incidents.

## Why it stopped

No-paper useful signal: Tier 1 direct replay supports the mechanism on reconstructed real incident traces, but lacks native live ledgers, external anchoring infrastructure, and independent incident labels.

## Recommended next action

Run a bounded live-agent follow-up with native decision-ledger emission, independent incident labels, and an external immutable anchor witness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live native decision-ledger anchoring on labeled agent incident runs
- Success threshold: Clean replay valid rate >= 0.99; anchored rejection rate >= 0.99 for each attack family; no-anchor or final-only baseline false-accept rate >= 0.50 on at least two attack families; incident-label preservation >= 0.95 after replay.
- Stop condition: Stop if fewer than 20 labeled live incident runs can be produced locally, if the external anchor backend cannot be made append-only/verifiable, or if anchored replay rejects clean ledgers below 0.99.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-decision-ledger-replay-on-real-agent-incident-tra-676863184d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
