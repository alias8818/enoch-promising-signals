# Collusive-corruption and stronger-baseline audit benchmark for blinded multi-trace evidence ledgers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `33`
Project ID: `collusive-corruption-and-stronger-baseline-audit-benchmark-48d3b67390`
Run ID: `collusive-corruption-and-stronger-baseline-audit-benchmark-48d3b67390-20260531T185720884914+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `33`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Blinded multi-trace audit benchmark for an agent evidence ledger: enoch://control-plane/projects/blinded-multi-trace-audit-benchmark-for-an-agent-evidence-da89e39e19/runs/blinded-multi-trace-audit-benchmark-for-an-agent-evidence-da89e39e19-20260531T150311180651+0000
- Parent run decision: Real-trace audit study for an agent evidence ledger: enoch://control-plane/projects/real-trace-audit-study-for-an-agent-evidence-ledger-3bec48a1f9/runs/real-trace-audit-study-for-an-agent-evidence-ledger-3bec48a1f9-20260531T114810950760+0000

## What looked useful

The proposed blinded multitrace rule had lower false positives but substantially worse attack detection than stronger baselines. Scenario attack detection means were 0.602-0.652 for blinded_multitrace versus 0.931-0.969 for pair_random, 0.990-1.000 for risk_weighted_pair, and 0.960-0.981 for single_trace_random. Matched-run attack detection deltas for blinded_multitrace were -0.317 versus pair_random, -0.368 versus risk_weighted_pair, and -0.344 versus single_trace_random across 1,440 matched conditions.

## Boundaries and scale limits

Synthetic data only; no real institutional evidence logs, no deployed cryptographic ledger, no adaptive human red team, and no datacenter-scale operational audit workload. The result tests the audit mechanism and budget tradeoff, not real-world governance or legal admissibility.

## Claim scope

Bounded synthetic benchmark of binary multi-trace evidence ledgers with 20,000 cases per run, 8 traces, 40 fixed seeds, 2% honest trace noise, static collusive corruption across 1/2/4/6 traces, 0.5%/1%/3% corrupted-case fractions, and a fixed 2,000-trace audit budget. In this scoped setting, the calibrated blinded four-trace audit underperforms stronger deployable baselines on campaign detection.

## Why it stopped

Bounded synthetic validation found the proposed blinded four-trace audit consistently worse than stronger deployable baselines on direct attack detection under a fixed trace-inspection budget, so the hypothesis is unsupported and not paper-positive.

## Recommended next action

Stop this follow-up as a no-paper useful negative; do not pursue the tested blinded four-trace audit rule unless a new design explicitly fixes calibrated one-mismatch suppression or proves value on real audit logs.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/collusive-corruption-and-stronger-baseline-audit-benchmark-48d3b67390`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
