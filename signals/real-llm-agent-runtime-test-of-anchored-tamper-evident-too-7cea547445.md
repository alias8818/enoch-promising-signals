# Real LLM-agent runtime test of anchored tamper-evident tool-call receipts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-llm-agent-runtime-test-of-anchored-tamper-evident-too-7cea547445`
Run ID: `real-llm-agent-runtime-test-of-anchored-tamper-evident-too-7cea547445-20260529T162110992771+0000`

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

- Parent run decision: Tamper-evident tool-call ledger for 1B agent: enoch://control-plane/projects/tamper-evident-tool-call-ledger-for-1b-agent-6efd279d5234/runs/tamper-evident-tool-call-ledger-for-1b-agent-6efd279d5234-20260528T210950930918+0000
- Parent run decision: Real-agent integration test for tamper-evident tool-call ledger: enoch://control-plane/projects/real-agent-integration-test-for-tamper-evident-tool-call-l-756bd20643/runs/real-agent-integration-test-for-tamper-evident-tool-call-l-756bd20643-20260529T080133891282+0000

## What looked useful

Across 7,500 fixed-seed tamper trials, anchored receipts achieved 1.0 detection and 1.0 within-anchor localization for all tested attack classes. Raw JSONL achieved 0.0 detection. Co-located hash-chain receipts achieved 0.6 overall detection, failing adaptive rewrite and truncation. Anchored receipt generation cost averaged 10.67 us/event and 823.0 bytes/event.

## Boundaries and scale limits

The medium corpus augmented 18 real tool-call templates into fixed-seed streams rather than running a long live multi-agent workload. Anchoring used a local HMAC-signed manifest rather than an independent transparency log, blockchain timestamp, WORM store, or remote notary. Concurrent emitters, delayed anchors, crash recovery, key rotation, and production tracing baselines were not tested.

## Claim scope

In a deterministic local audit-log experiment using real Codex tool-call event templates, canonical hash-chain receipts with independently held periodic signed Merkle anchors detected modify, delete, reorder, truncate, and adaptive-rewrite attacks that raw JSONL logs and co-located unanchored hash chains missed.

## Why it stopped

Mechanism supported in a bounded local Tier 2 experiment, but publication readiness requires live dispatcher integration and independent external anchoring rather than deterministic augmentation plus a local signed anchor manifest.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next, integrate receipt emission into a live tool dispatcher and publish anchors to an independent append-only transparency or timestamp service.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live dispatcher integration for externally anchored LLM-agent tool-call receipts
- Success threshold: At least 0.99 tamper detection across all attack classes, 1.0 detection for adaptive rewrite and truncation, p95 added latency below 5 ms/tool call excluding remote anchor batching delay, and successful verification after crash/restart recovery.
- Stop condition: Stop as negative if external anchoring introduces more than 25 ms p95 dispatcher latency under batching, if crash recovery creates unverifiable gaps in more than 1% of sessions, or if any adaptive rewrite/truncation class falls below 0.99 detection.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-agent-runtime-test-of-anchored-tamper-evident-too-7cea547445`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
