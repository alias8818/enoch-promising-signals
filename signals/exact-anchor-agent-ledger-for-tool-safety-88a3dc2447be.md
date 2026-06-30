# Exact-Anchor Agent Ledger for Tool Safety

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-agent-ledger-for-tool-safety-88a3dc2447be`
Run ID: `exact-anchor-agent-ledger-for-tool-safety-88a3dc2447be-20260529T221326602280+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9cb0c1dbbdea

## What looked useful

Exact byte offsets, exact quote checks, document hashes, local context hashes, and hash-chained ledger entries provide a concrete audit mechanism for detecting anchor drift and transcript tampering in a bounded local harness. Local append overhead was low in the prototype: median 23.309 us, p95 35.17335 us over 5000 entries.

## Boundaries and scale limits

Synthetic documents and hand-seeded attacks only; no real agent runtime, no concurrent tool calls, no external append-only storage, no adversarial LLM behavior, and no production persistence or network latency measurements.

## Claim scope

A stdlib Python exact-anchor ledger prototype detected 11/11 seeded synthetic provenance and transcript-tamper failures for small local policy/tool-output documents, while a naive transcript detected 0/11 and a document-hash-only baseline detected 3/11.

## Why it stopped

Closed as no-paper useful signal because the evidence is a local synthetic mechanism test, not a full validation of real agent tool safety.

## Recommended next action

Run a bounded real-agent follow-up that integrates exact anchors into a tool-calling harness and injects the same tamper classes across hundreds of traces; do not write a paper from the synthetic-only result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor ledger in a real tool-calling agent harness
- Success threshold: Detect at least 95% of injected failures overall, detect at least 90% in every named tamper class, keep false positives below 2%, and keep median per-step overhead below 10 ms.
- Stop condition: Stop if valid trace false positives exceed 5%, any core tamper class has detection below 80%, or median overhead exceeds 25 ms after basic implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-agent-ledger-for-tool-safety-88a3dc2447be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
