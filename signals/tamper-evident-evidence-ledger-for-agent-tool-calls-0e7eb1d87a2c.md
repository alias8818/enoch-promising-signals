# Tamper-Evident Evidence Ledger for Agent Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tamper-evident-evidence-ledger-for-agent-tool-calls-0e7eb1d87a2c`
Run ID: `tamper-evident-evidence-ledger-for-agent-tool-calls-0e7eb1d87a2c-20260610T170322432710+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/74bbef087b46

## What looked useful

The mechanism is mechanically viable for the tested post-hoc file-tampering threat model and has overhead likely acceptable for interactive tool-call streams: 5.95x write overhead, 8.54x verify overhead, and 1.429x storage overhead versus plain JSONL parsing/writing.

## Boundaries and scale limits

Synthetic records only; no production agent integration, external transparency service, key rotation, distributed writers, signer compromise, crash consistency, or long-running audit workflow was tested.

## Claim scope

A local, single-writer HMAC-SHA256 hash-chain ledger with an independently preserved final anchor detected payload modification, middle deletion, adjacent reordering, duplicate-shaped insertion, and tail truncation in synthetic agent tool-call logs across 5 trials of 50000 records each, while sustaining about 61423 appends/s and 65319 verifies/s on one CPU process.

## Why it stopped

Synthetic/local evidence supports the mechanism but is insufficient for a paper or broad deployment claim.

## Recommended next action

Stop this run as no-paper useful evidence; next, integrate the ledger into a real agent tool-call wrapper and test external anchoring plus crash recovery on real traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Tool-Call Ledger Integration With External Anchors
- Success threshold: Detect 100% of the same five tamper classes plus partial-write corruption on real traces across at least 10 runs, with p95 append overhead below 10 ms per tool call and successful recovery/audit replay after forced process termination.
- Stop condition: Stop if real integration cannot preserve anchors independently, if crash recovery produces ambiguous verifier states, or if append overhead exceeds 10 ms p95 per tool call under representative local workloads.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-evidence-ledger-for-agent-tool-calls-0e7eb1d87a2c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
