# Real Agent Trace Evidence Ledger Versus Strong Audit Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-agent-trace-evidence-ledger-versus-strong-audit-basel-19bdb11168`
Run ID: `real-agent-trace-evidence-ledger-versus-strong-audit-basel-19bdb11168-20260527T110641042863+0000`

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

- Parent run decision: Live Agent Evidence Ledger With Baseline Audit Log Comparison: enoch://control-plane/projects/live-agent-evidence-ledger-with-baseline-audit-log-compari-e45756c51b/runs/live-agent-evidence-ledger-with-baseline-audit-log-compari-e45756c51b-20260525T224551026043+0000
- Parent run decision: Tamper-Evident Evidence Ledger for Small Tool-Using Agents: enoch://control-plane/projects/tamper-evident-evidence-ledger-for-small-tool-using-agents-f9477609b74b/runs/tamper-evident-evidence-ledger-for-small-tool-using-agents-f9477609b74b-20260525T214530501498+0000

## What looked useful

Full ledger recall was 1.00 versus 0.60 for the strong audit-log baseline, a +0.40 lift over the +0.25 threshold; ledger false-positive rate was 0.00 versus the <=0.05 threshold; max serialized storage overhead was 1.417x versus the <5x threshold. Ablations showed hash removal loses tamper detection, provenance removal loses stale-evidence detection, and claim-link removal loses provenance-mismatch detection.

## Boundaries and scale limits

360 local mini-agent traces, 2160 claims, 300 seeded defective claims, 5 fixed seeds. The run did not use real LLM-generated agent traces, production traces, independent human labels, or broad external tool-use diversity.

## Claim scope

In deterministic local mini-agent traces with seeded unsupported-claim, stale-evidence, provenance-mismatch, tamper, and missing-evidence faults, a full explicit evidence ledger improved defect recall over a strong post-hoc audit-log baseline while preserving zero false positives and low storage overhead.

## Why it stopped

Tier 2 local evidence supports the mechanism and threshold within the harness, but the claim is not paper-positive because real LLM agent trace evidence remains untested.

## Recommended next action

Run the same ledger, baseline, and ablation protocol on real LLM agent execution traces or production-like replay traces with independently labeled seeded faults before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger Audit on Real LLM Agent Trace Replays
- Success threshold: Full ledger recall lift >=0.25 over the strong audit-log baseline, full ledger false-positive rate <=0.05, max serialized storage overhead <5x, and at least two ablations showing class-specific recall loss.
- Stop condition: Stop as no-paper if recall lift is <0.10, false-positive rate exceeds 0.05, storage overhead exceeds 5x, or ablations do not show class-specific mechanism support on real trace replays.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-trace-evidence-ledger-versus-strong-audit-basel-19bdb11168`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
