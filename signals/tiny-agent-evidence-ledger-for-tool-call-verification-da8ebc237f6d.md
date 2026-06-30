# Tiny Agent Evidence Ledger for Tool Call Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-for-tool-call-verification-da8ebc237f6d`
Run ID: `tiny-agent-evidence-ledger-for-tool-call-verification-da8ebc237f6d-20260607T212551272846+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/faf98fc6ffd0

## What looked useful

The prototype detected 100% of tested synthetic attacks versus 40% for a transcript-only presence baseline, with 94.016 microseconds median ledger verification time per 24-record trace over a 6,000-trace run.

## Boundaries and scale limits

Synthetic traces only; 8 tool calls per trace; single-process CPU verification; no real agent framework integration, concurrent tool calls, streaming outputs, compromised ledger writer, or key-management trust boundary tested.

## Claim scope

In a dependency-free synthetic calculator-tool harness, a tiny append-only hash-chained evidence ledger verified tool request/result/assistant-claim consistency and detected five tested trace tamper modes across 5,000 attacked traces.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct real-agent evidence and is insufficient for paper-positive closure.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the ledger with a real tool-calling agent runtime and compare against a stronger structured-log baseline on real plus tampered traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Integration Test for Evidence Ledger Tool-Call Verification
- Success threshold: At least 95% attack detection, less than 1% false positives on clean traces, and median verification overhead below 5 ms per trace against a stronger structured-log baseline.
- Stop condition: Stop if real clean traces exceed 5% false positives after minimal schema adaptation, or if the structured-log baseline matches ledger detection and latency without requiring the ledger mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-for-tool-call-verification-da8ebc237f6d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
