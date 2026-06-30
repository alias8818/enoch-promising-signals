# Real agent tool-call ledger with separated receipt authority

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-tool-call-ledger-with-separated-receipt-authori-34e74801fd`
Run ID: `real-agent-tool-call-ledger-with-separated-receipt-authori-34e74801fd-20260520T124809584201+0000`

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

- Parent run decision: Hash-Chained Evidence Ledger for Small Agent Action Verification: enoch://control-plane/projects/hash-chained-evidence-ledger-for-small-agent-action-verification-807a3647150d/runs/hash-chained-evidence-ledger-for-small-agent-action-verification-807a3647150d-20260520T123721896821+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b11c7497bb69

## What looked useful

Separated receipt authority materially improved tamper evidence versus a no-authority self-report baseline: authority-backed verifier reached 100% detection on all six tamper classes with 0% honest false rejects; baseline missed fabricated, argument/result-modified, replayed, and naive-forged ledgers.

## Boundaries and scale limits

Small synthetic Tier 1 test only: 200 trials per adversarial scenario, one process, toy tools, no real LLM agent framework, no OS-level authority isolation test, no concurrency, no crash/restart persistence, no hostile filesystem model, no production API integration.

## Claim scope

In a controlled local Python agent/tool loop with deterministic toy tools, a separated keyed hash-chain receipt authority at the tool execution boundary detected tested ledger omission, fabrication, argument/result modification, reorder, receipt replay, and naive MAC forgery attacks while accepting honest ledgers.

## Why it stopped

Tier 1 mechanism evidence is useful but not paper-ready because the run is local, synthetic, and does not validate process isolation or real agent integration.

## Recommended next action

Run a bounded real-framework follow-up with an out-of-process receipt sidecar for LangGraph/OpenAI-style tool calls and adversarial transcript editing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Out-of-process receipt authority for real agent tool-call traces
- Success threshold: >=99% detection for omission, fabrication, argument/result modification, reorder, replay, and naive forgery attacks; <=1% honest false rejects; receipt overhead below 10 ms per local tool call in the tested framework.
- Stop condition: Stop as unsupported if any core tamper class falls below 95% detection, honest false rejects exceed 5%, or the sidecar cannot be isolated from agent-controlled transcript writes in the local framework.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-tool-call-ledger-with-separated-receipt-authori-34e74801fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
