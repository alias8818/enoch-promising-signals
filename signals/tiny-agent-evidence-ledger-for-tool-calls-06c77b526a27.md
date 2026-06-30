# Tiny Agent Evidence Ledger for Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-for-tool-calls-06c77b526a27`
Run ID: `tiny-agent-evidence-ledger-for-tool-calls-06c77b526a27-20260528T162823992974+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9ad70054129c

## What looked useful

The local benchmark supports the practical mechanism: canonical body digests, sequence numbers, previous-record hashes, final manifest head/count, and HMACs can provide tamper evidence for small agent tool-call traces with moderate overhead. The 20,000-event benchmark detected body mutation, unkeyed hash recomputation, deletion, reordering, old-record insertion, and tail truncation; mean write overhead was 4.771x and byte overhead was 2.477x versus plain JSONL.

## Boundaries and scale limits

Synthetic events only; no real agent framework integration, no crash-consistency test, no concurrent writers, no log rotation, no remote attestation, no production key-management design, and no adversary with HMAC key compromise or pre-write process control.

## Claim scope

A single-process Python prototype of an append-only hash-chain plus HMAC ledger detected six common post-hoc tampering modes on synthetic 100-event and 20,000-event agent tool-call traces while staying below predefined overhead thresholds of 5x write time and 3x bytes per event versus plain JSONL.

## Why it stopped

Useful synthetic/local signal, but not direct or robust enough for a publication-grade claim.

## Recommended next action

Run a bounded deepen follow-up that integrates the ledger with a real agent trace harness and adds crash-consistency plus concurrent-writer tests; stop paper work for this synthetic-only run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Trace and Crash Test for Tiny Tool-Call Evidence Ledger
- Success threshold: All tamper cases detected; crash tests produce an explainable last-valid-prefix or manifest mismatch; mean write overhead stays below 5x and byte overhead below 3x versus plain JSONL on at least 10,000 real/framework-generated events.
- Stop condition: Stop if real-framework integration fails to preserve ordering/identity semantics, any required tamper class is not detected under the stated adversary model, or overhead exceeds either threshold after removing avoidable implementation overhead.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-for-tool-calls-06c77b526a27`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
