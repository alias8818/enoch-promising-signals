# Cryptographic Evidence Ledger for CPU Agent Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cryptographic-evidence-ledger-for-cpu-agent-tool-calls-5e9b72700233`
Run ID: `cryptographic-evidence-ledger-for-cpu-agent-tool-calls-5e9b72700233-20260527T191941085746+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/eb1767320215

## What looked useful

Local prototype detected payload modification, record deletion, record swap, prefix truncation, and suffix truncation in every trial with anchored-head verification. Median runtime overhead was 6.94x and byte overhead was 2.73x versus plain JSONL.

## Boundaries and scale limits

Only 10,000 synthetic events x 5 repeats were tested. No real agent traces, concurrent writers, crash recovery, remote timestamping, public transparency anchoring, asymmetric signatures, or key-compromise adversary were evaluated.

## Claim scope

A pure-Python canonical JSONL hash-chain ledger with HMAC seals can detect tested retained-log tampering for synthetic CPU agent tool-call records when an external final anchor is available, at about 16k appends/sec and 44k verifies/sec on this worker.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct or broad enough for a publication-grade claim.

## Recommended next action

Stop this run as a no-paper useful signal; next, test the same ledger on real agent tool-call traces with crash and concurrent-writer fault injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace crash and concurrency validation for CPU agent evidence ledgers
- Success threshold: All tamper/crash/concurrency integrity checks pass, no lost accepted records, and median append overhead is below 2x versus JSONL on the selected real trace.
- Stop condition: Stop if concurrent writes lose or reorder accepted records without detection, crash recovery leaves unverifiable accepted records, or optimized overhead remains above 5x on realistic traces.

## Evidence references

- Artifact root: `<local-path>/projects/cryptographic-evidence-ledger-for-cpu-agent-tool-calls-5e9b72700233`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
