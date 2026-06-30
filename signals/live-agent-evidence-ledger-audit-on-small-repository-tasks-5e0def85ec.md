# Live-Agent Evidence Ledger Audit on Small Repository Tasks

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `live-agent-evidence-ledger-audit-on-small-repository-tasks-5e0def85ec`
Run ID: `live-agent-evidence-ledger-audit-on-small-repository-tasks-5e0def85ec-20260610T212431887034+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-Agent Strict Evidence Ledger Audit Benchmark: enoch://control-plane/projects/real-agent-strict-evidence-ledger-audit-benchmark-e0579a535c/runs/real-agent-strict-evidence-ledger-audit-benchmark-e0579a535c-20260610T194531942641+0000
- Parent run decision: Evidence Ledger Falsifiability Protocol for Agent Reliability: enoch://control-plane/projects/evidence-ledger-falsifiability-protocol-for-agent-reliability-297fd8b4eb2d/runs/evidence-ledger-falsifiability-protocol-for-agent-reliability-297fd8b4eb2d-20260610T133944366191+0000

## What looked useful

Ledger content ablations showed mechanism value even though the broad improvement claim was unsupported: removing snippets missed 60 false behavioral claims and reduced recall to 0.667, while removing command evidence caused 60 false positives on true test-pass claims and raised FPR to 0.333.

## Boundaries and scale limits

Synthetic generated repositories and templated claims only; no naturalistic live-agent transcripts, human auditors, large repositories, or LLM-based audit variability were tested.

## Claim scope

On 60 deterministic small Python repository repair tasks with explicit final reports and 360 labeled true/false claims, a structured evidence ledger did not improve seeded false-claim detection over a regex-backed unstructured-report baseline; both achieved precision 1.000, recall 1.000, and F1 1.000.

## Why it stopped

Bounded Tier 2 benchmark produced a negative result for the direct improvement claim: full ledger and real baseline tied on false-claim detection, so the evidence supports only a mechanism note about required ledger fields.

## Recommended next action

Stop this branch as no-paper evidence; if continued, run a live-agent transcript study where claims are naturally produced rather than templated.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Naturalistic Live-Agent Evidence Ledger Audit
- Success threshold: Ledger condition improves false-claim F1 by at least 0.10 or reduces median audit time by at least 25% with false-positive rate no higher than the transcript-only baseline.
- Stop condition: Stop if the ledger condition fails to improve F1 or audit time after the fixed live-agent transcript set, or if naturalistic transcripts do not contain enough auditable claims for a valid comparison.

## Evidence references

- Artifact root: `<local-path>/projects/live-agent-evidence-ledger-audit-on-small-repository-tasks-5e0def85ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
