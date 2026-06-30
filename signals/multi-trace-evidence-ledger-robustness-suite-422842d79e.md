# Multi-trace Evidence Ledger Robustness Suite

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `multi-trace-evidence-ledger-robustness-suite-422842d79e`
Run ID: `multi-trace-evidence-ledger-robustness-suite-422842d79e-20260610T054500030140+0000`

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

- Parent run decision: Evidence Ledger on Real Tool-Use Agent Traces: enoch://control-plane/projects/evidence-ledger-on-real-tool-use-agent-traces-2fb2a6080f/runs/evidence-ledger-on-real-tool-use-agent-traces-2fb2a6080f-20260609T214333532634+0000
- Parent run decision: Evidence Ledger for Tool-Use Agent Reliability: enoch://control-plane/projects/evidence-ledger-for-tool-use-agent-reliability-1d8b149bc7bf/runs/evidence-ledger-for-tool-use-agent-reliability-1d8b149bc7bf-20260609T171317283126+0000

## What looked useful

The full ledger reached 1.0 attack recall but had 0.9971 macro false-positive rate and 0.1273 macro F1 across attack scenarios. The no-cross-anchor ablation improved macro F1 to 0.5064, identifying transitive row-hash anchoring as the likely failure mode. A simple any-disagreement baseline had 0.8571 macro F1 and 0 false-positive rate across the same attacks.

## Boundaries and scale limits

Synthetic traces only; no production audit logs, no real sensor failure correlations, no human-review cost study, and no large-scale operational deployment. CPU-only local validation completed in 31.48 seconds.

## Claim scope

On a fixed-seed synthetic multi-trace evidence-ledger robustness suite with 5,000 events, 5 traces, 30 seeds, and controlled modification/deletion/replay/insertion/collusion/anchor-forgery attacks, the tested row-hash cross-anchor ledger design did not outperform simpler baselines for event-level tamper detection.

## Why it stopped

Medium synthetic validation with fixed seeds, ablations, and real baselines falsified the tested full-ledger mechanism; cross anchors over transitive row hashes caused near-total false positives under attack.

## Recommended next action

Stop this ledger variant as no-paper; if continuing, test a locality-preserving payload-anchor design against the same fixed-seed suite before considering real trace data.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Locality-preserving payload anchors for multi-trace evidence ledgers
- Success threshold: Macro F1 across attack scenarios at least 0.90, false-positive rate at most 0.02, and per-scenario F1 no worse than any_disagreement by more than 0.03.
- Stop condition: Stop if payload/interval anchoring still produces false-positive rate above 0.05 or fails to beat any_disagreement macro F1 on the fixed-seed suite.

## Evidence references

- Artifact root: `<local-path>/projects/multi-trace-evidence-ledger-robustness-suite-422842d79e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
