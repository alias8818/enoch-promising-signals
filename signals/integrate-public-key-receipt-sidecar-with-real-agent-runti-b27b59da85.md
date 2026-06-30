# Integrate public-key receipt sidecar with real agent runtime tool calls

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `integrate-public-key-receipt-sidecar-with-real-agent-runti-b27b59da85`
Run ID: `integrate-public-key-receipt-sidecar-with-real-agent-runti-b27b59da85-20260520T131632646118+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Out-of-process receipt authority for real agent tool-call traces: enoch://control-plane/projects/out-of-process-receipt-authority-for-real-agent-tool-call-4422f4519d/runs/out-of-process-receipt-authority-for-real-agent-tool-call-4422f4519d-20260520T125846376516+0000
- Parent run decision: Live sidecar public-key receipt authority for real agent tool-call sessions: enoch://control-plane/projects/live-sidecar-public-key-receipt-authority-for-real-agent-t-c425929ad8/runs/live-sidecar-public-key-receipt-authority-for-real-agent-t-c425929ad8-20260520T130910132853+0000

## What looked useful

Signed receipts reached 100% coverage on 15,000 real LangGraph ToolNode invocations, verified cleanly in all seeds, detected naive mutation and full journal rewrite, and added about 0.049 ms per call / 6.96% mean overhead versus no-sidecar baseline. The unsigned ablation failed the full-rewrite adversary, supporting the public-key mechanism.

## Boundaries and scale limits

Validated on 3 fixed seeds with 5,000 tool calls per seed across no-sidecar, unsigned, and signed conditions. Not validated for live LLM planning, multi-process sidecar IPC, high-concurrency serving, production key custody, runtime compromise isolation, or non-LangGraph frameworks.

## Claim scope

A public-key Ed25519 receipt sidecar can wrap real LangGraph compiled StateGraph ToolNode calls and produce complete, publicly verifiable, tamper-evident receipts with low local overhead in a single-process CPU harness.

## Why it stopped

The Tier 4 paper-readiness threshold was not met: the run used real LangGraph tool calls with baseline and ablation, but did not validate production agent traffic, sidecar isolation, key custody, concurrency, or cross-runtime robustness.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful mechanism evidence; do not chain another follow-up from this run because the remaining work is production-grade validation beyond this bounded local harness.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/integrate-public-key-receipt-sidecar-with-real-agent-runti-b27b59da85`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
