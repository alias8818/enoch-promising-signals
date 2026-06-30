# Agent Reliability via Cascade Confidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-reliability-via-cascade-confidence-ledger-25d5bc8d4ed6`
Run ID: `agent-reliability-via-cascade-confidence-ledger-25d5bc8d4ed6-20260529T073110875892+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/78abe1b60d0e

## What looked useful

Across 8 seeds and 3 synthetic scenarios, the ledger reduced upstream-blind Brier score versus final-only confidence from 0.1870 to 0.1236 and improved AUROC from 0.7132 to 0.8867, but calibrated min stage confidence was stronger in that same scenario with Brier 0.1201 and AUROC 0.8931.

## Boundaries and scale limits

CPU-only synthetic simulation; no real LLM/tool-use traces, no human evaluation, no production agent telemetry, and no datacenter-scale validation.

## Claim scope

Synthetic four-stage cascade simulations show that retaining calibrated per-stage confidence improves final correctness prediction when the final stage is upstream-blind, but the tested ledger aggregation does not outperform simple calibrated stage-confidence baselines.

## Why it stopped

The local synthetic evidence is useful but mixed: per-stage evidence matters under upstream-blind final confidence, while the proposed ledger aggregation is not better than a simple calibrated min-confidence baseline.

## Recommended next action

Do not write a paper from this run; run a bounded real-trace follow-up comparing final-only, min-stage, product-stage, and learned ledger aggregators on actual cascaded agent/tool tasks with stage correctness labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace cascade confidence ledger benchmark
- Success threshold: Ledger aggregator improves Brier score by at least 10% relative to the best simple stage baseline and improves or matches AUROC and selective accuracy at comparable coverage on held-out real traces.
- Stop condition: Stop if min/product stage-confidence baselines match or beat the learned ledger on Brier and AUROC, or if stage-level labels cannot be obtained reproducibly.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-cascade-confidence-ledger-25d5bc8d4ed6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
