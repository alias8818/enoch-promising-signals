# Real-agent integration test for tamper-evident tool-call ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-integration-test-for-tamper-evident-tool-call-l-756bd20643`
Run ID: `real-agent-integration-test-for-tamper-evident-tool-call-l-756bd20643-20260529T080133891282+0000`

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
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57ea2dc6f7d8

## What looked useful

Anchored tamper-evident tool-call ledgers worked in the Tier 1 direct harness: 0/5000 honest traces rejected, 35000/35000 anchored tamper cases detected, naive baseline detected 0/35000. Unanchored chains missed clean suffix truncations, detecting only 2679/5000 truncation cases.

## Boundaries and scale limits

Tested only local deterministic Python tools, single-process sequential calls, post-hoc log mutations, and an in-process signing key. Not tested: production LLM agents, streaming/concurrent tool calls, remote tools, live omission/equivocation, trusted timestamp publication, or hardware/key-isolated signing.

## Claim scope

In a controlled local Python agent/tool gateway, canonical HMAC-signed hash-chain logging of tool request/result events detected 100% of seven post-hoc tamper classes across 35,000 cases when verification included an external event-count and final-hash receipt.

## Why it stopped

Tier 1 controlled direct test met the bounded mechanism threshold but remains no-paper evidence because it lacks production agent runtime integration, external receipt publication, and key-isolation/adversarial live-omission tests.

## Recommended next action

Run a bounded deepen follow-up inside a real LLM-agent/tool runtime with concurrent or streamed tool calls and periodic externally persisted receipts; stop paper consideration until that direct integration evidence exists.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM-agent runtime test of anchored tamper-evident tool-call receipts
- Success threshold: At least 100 honest agent runs with zero false rejections and 100% detection across all injected post-hoc mutation families, including suffix truncation, with receipts persisted outside the mutable ledger file.
- Stop condition: Stop if honest false rejection exceeds 1%, any mutation family has detection below 99%, or receipt persistence cannot be made independent of the mutable ledger artifact.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-integration-test-for-tamper-evident-tool-call-l-756bd20643`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
