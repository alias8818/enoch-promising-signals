# Live Transparency Service Validation for Agent Tool-Call Ledger Anchors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `live-transparency-service-validation-for-agent-tool-call-l-5c24f24188`
Run ID: `live-transparency-service-validation-for-agent-tool-call-l-5c24f24188-20260610T193528651612+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real Agent Tool-Call Ledger Integration With External Anchors: enoch://control-plane/projects/real-agent-tool-call-ledger-integration-with-external-anch-59ccac4e2d/runs/real-agent-tool-call-ledger-integration-with-external-anch-59ccac4e2d-20260610T174121244278+0000
- Parent run decision: Remote Transparency Anchor Test for Agent Tool-Call Ledgers: enoch://control-plane/projects/remote-transparency-anchor-test-for-agent-tool-call-ledger-a1e9c53df4/runs/remote-transparency-anchor-test-for-agent-tool-call-ledger-a1e9c53df4-20260610T183401270122+0000

## What looked useful

Incremental Merkle maintenance enabled a local live transparency service to sustain mean 1,587 anchors/s across 150,000 total anchors, with mean p95 append latency 5.85 ms, sampled proof verification success 1.0, persistence replay matches, and tampered-record/wrong-index controls detected. Naive recomputation failed the throughput target at 5,000 anchors.

## Boundaries and scale limits

No production agent traces, no public witness/gossip layer, no multi-node deployment, no adversarial operator equivocation test, no crash fault injection, and no datacenter-scale or multi-tenant validation. The hash-chain baseline is in-process and not service-equivalent.

## Claim scope

Local single-operator HTTP Merkle transparency service for synthetic structured agent tool-call ledger anchors, tested at 50,000 anchors per run across three fixed seeds with inclusion proof, persistence replay, tampered-record, wrong-index, latency, throughput, baseline, and ablation metrics.

## Why it stopped

Bounded local validation supports the mechanism but lacks external witnesses, real traces, crash fault injection, and adversarial operator tests required for publication-grade live transparency claims.

## Recommended next action

Run one depth-4 bounded follow-up with witnessed checkpoints, crash/corruption fault injection, and equivocation controls on the same service before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Witnessed Crash and Equivocation Validation for Agent Tool-Call Ledger Anchors
- Success threshold: At 50000 anchors, p95 append latency remains below 25 ms, throughput remains above 750 anchors/s, proof verification success is 1.0, persistence recovery reproduces the last witnessed root, and all injected corruption/equivocation cases are detected.
- Stop condition: Stop if witness overhead drops throughput below 750 anchors/s, any valid proof fails verification, persistence recovery cannot reproduce the witnessed root, or any injected equivocation/corruption case is not detected.

## Evidence references

- Artifact root: `<local-path>/projects/live-transparency-service-validation-for-agent-tool-call-l-5c24f24188`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
