# Real-Agent Evidence Ledger Trace Benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-evidence-ledger-trace-benchmark-fe07925f79`
Run ID: `real-agent-evidence-ledger-trace-benchmark-fe07925f79-20260524T211351445492+0000`

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

- Parent run decision: Low-Memory Agent Evidence Ledger: enoch://control-plane/projects/low-memory-agent-evidence-ledger-521c7369895f/runs/low-memory-agent-evidence-ledger-521c7369895f-20260524T205907430216+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/784630b0ac91

## What looked useful

A reproducible CPU-only harness shows that evidence ledgers can preserve auditability without reducing task correctness on small real file/command tasks.

## Boundaries and scale limits

Small local fixtures only; deterministic policy; no LLM-sampled traces, web tasks, human audit labels, long-horizon repositories, or multi-agent workflows.

## Claim scope

In a five-task controlled local benchmark with deterministic tool-using agents, structured evidence ledgers provided complete machine-checkable claim-to-evidence coverage and digest replay verification, while plain traces did not.

## Why it stopped

Tier 1 controlled direct test supports the auditability mechanism but is insufficient for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on naturally generated LLM-agent traces with independent audit labels before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger Auditability on Natural LLM Agent Traces
- Success threshold: Ledgered traces achieve at least +30 percentage points verified claim-support coverage versus plain traces, with task correctness within 5 percentage points and no increase in unsupported cited claims.
- Stop condition: Stop if ledgered traces fail to improve verified claim-support coverage by at least 10 percentage points on the first 10 natural traces or if ledger overhead prevents task completion in more than 20% of tasks.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evidence-ledger-trace-benchmark-fe07925f79`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
