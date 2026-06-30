# Live sidecar public-key receipt authority for real agent tool-call sessions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `live-sidecar-public-key-receipt-authority-for-real-agent-t-c425929ad8`
Run ID: `live-sidecar-public-key-receipt-authority-for-real-agent-t-c425929ad8-20260520T130910132853+0000`

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

- Parent run decision: Out-of-process receipt authority for real agent tool-call traces: enoch://control-plane/projects/out-of-process-receipt-authority-for-real-agent-tool-call-4422f4519d/runs/out-of-process-receipt-authority-for-real-agent-tool-call-4422f4519d-20260520T125846376516+0000
- Parent run decision: Real agent tool-call ledger with separated receipt authority: enoch://control-plane/projects/real-agent-tool-call-ledger-with-separated-receipt-authori-34e74801fd/runs/real-agent-tool-call-ledger-with-separated-receipt-authori-34e74801fd-20260520T124809584201+0000

## What looked useful

The mechanism worked on 20,000 sequential live sidecar receipts plus an 8,000-receipt concurrent check. All valid receipts verified, event tampering and chain deletion were detected, and same-session crash/restart continuity verified after log replay recovery. The result supports mechanism feasibility but is not broad real-agent publication evidence.

## Boundaries and scale limits

Single host only; deterministic harness rather than captured production LLM/Codex/LangGraph agent sessions; local file/search/json/hash/list tools only; no remote tools, hostile host model, key rotation, multi-authority federation, external transparency log, or independent deployment operators tested.

## Claim scope

A local Python Unix-socket Ed25519 sidecar can issue public-key-verifiable, hash-chained receipts for deterministic agent-like tool-call sessions with about 0.4 ms mean sequential overhead per lightweight local tool call, can detect event mutation and receipt deletion, can recover same-session chain state after restart, and can verify 8,000 receipts from 16 concurrent local clients.

## Why it stopped

No-paper closure: bounded local evidence supports the mechanism, but the validation uses generated agent-like sessions and is not direct production real-agent evidence.

## Recommended next action

Run a bounded integration test inside a real agent runtime such as LangGraph or Codex tool execution, capture at least 100 real multi-tool sessions, and compare sidecar receipts against native runtime logs with an independent verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrate public-key receipt sidecar with real agent runtime tool calls
- Success threshold: >=99.9% receipt/log agreement, 100% offline verification of untampered logs, 100% detection of injected event mutation and receipt deletion/reorder ablations, and <5 ms p95 added latency over no-sidecar baseline on the tested runtime.
- Stop condition: Stop if real runtime integration cannot observe complete tool-call arguments/results, if receipt/log agreement is below 99.9% after fixing instrumentation bugs, or if p95 overhead is >=5 ms for local tools.

## Evidence references

- Artifact root: `<local-path>/projects/live-sidecar-public-key-receipt-authority-for-real-agent-t-c425929ad8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
