# Append-Only Evidence Ledger for CPU Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `append-only-evidence-ledger-for-cpu-agent-reliability-8aaa751f4128`
Run ID: `append-only-evidence-ledger-for-cpu-agent-reliability-8aaa751f4128-20260521T225920908709+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ba50c91d1226

## What looked useful

The ledger mechanism is practical enough for a CPU-agent audit harness: 5/5 clean ledger verifications passed, 5/5 artifact tamper injections were detected, 5/5 ledger-record tamper injections were detected, and 5/5 false metric claims were rejected in the medium run.

## Boundaries and scale limits

Synthetic single-process CPU harness only; no real autonomous agent trajectories, concurrent writers, crash recovery, external anchoring, adversarial runtime compromise, or production-scale log volume were tested.

## Claim scope

In a deterministic local CPU workload, an append-only hash-chained evidence ledger detected post-run artifact tampering, detected ledger-record mutation, and rejected unsupported metric claims with about 4.8% measured runtime overhead.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy-only; it supports the auditability mechanism but not a publication-grade claim about broad CPU-agent reliability.

## Recommended next action

Run a bounded real-agent follow-up where the ledger wraps actual CPU-agent command execution and final reports are automatically checked against captured command, artifact, and metric evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ledger-Enforced Claim Checking for Real CPU-Agent Runs
- Success threshold: Detect at least 90% of injected or naturally occurring unsupported metric/artifact claims with no more than 10% median runtime overhead and no lost ledger events across crash/restart tests.
- Stop condition: Stop if ledger enforcement misses more than 10% of unsupported claims, loses events during crash/restart, or exceeds 10% median runtime overhead on the real-agent task set.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledger-for-cpu-agent-reliability-8aaa751f4128`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
