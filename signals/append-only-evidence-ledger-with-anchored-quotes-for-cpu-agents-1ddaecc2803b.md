# Append-Only Evidence Ledger with Anchored Quotes for CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `append-only-evidence-ledger-with-anchored-quotes-for-cpu-agents-1ddaecc2803b`
Run ID: `append-only-evidence-ledger-with-anchored-quotes-for-cpu-agents-1ddaecc2803b-20260610T003542330990+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb42f9c0ae34

## What looked useful

Prototype and tests show a practical evidence-ledger mechanism for CPU agents: anchored quotes can be verified against source bytes, local tampering is detected by hash-chain checks, and 1000-record synthetic append/verify overhead is small enough for ordinary agent logging.

## Boundaries and scale limits

Synthetic single-process local-filesystem workload only; no real agent traces, concurrent writers, cryptographic signatures, remote storage, adversarial checkpoint custody, binary/non-text sources, or long-duration operation were tested. Valid-prefix truncation is not detectable without an external checkpoint/head publication.

## Claim scope

A dependency-free local JSONL ledger with byte-offset quote anchors, source hashes, per-record hashes, and previous-hash chaining can verify 1000 synthetic CPU-agent evidence records, detect simple record/source/reorder tampering, and append with p95 latency below 4 ms on this CPU worker.

## Why it stopped

No-paper closure: local synthetic evidence supports the mechanism, but broader utility and adversarial durability require real traces and concurrency/checkpoint tests.

## Recommended next action

Run a bounded deepen study on real CPU-agent transcripts with concurrent append attempts and externally published checkpoints; stop here for this run because current evidence is useful but not paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace and Concurrency Validation for Anchored Evidence Ledgers
- Success threshold: Verification detects 100% of non-prefix tamper injections and all truncations after an externally published checkpoint, with p95 append latency below 10 ms on at least 10000 real-trace records.
- Stop condition: Stop if concurrent append cannot preserve an unambiguous total order without a database/lock service, or if real-trace append p95 latency exceeds 25 ms after removing obvious prototype bottlenecks.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledger-with-anchored-quotes-for-cpu-agents-1ddaecc2803b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
