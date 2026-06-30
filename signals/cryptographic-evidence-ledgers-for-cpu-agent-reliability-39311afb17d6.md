# Cryptographic Evidence Ledgers for CPU Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cryptographic-evidence-ledgers-for-cpu-agent-reliability-39311afb17d6`
Run ID: `cryptographic-evidence-ledgers-for-cpu-agent-reliability-39311afb17d6-20260621T063246012892+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/7933f37160e7

## What looked useful

The ledger mechanism adds practical tamper evidence over plain claim/evidence schemas with about 9.10x verification overhead but only 162.19 ms mean absolute verification time and 1.33x storage overhead for 5,000-record ledgers.

## Boundaries and scale limits

Synthetic local traces only; no live agent harness, no production key custody, no distributed transparency log, no malicious signing-key compromise model, and no measurement of downstream task correctness or operator trust decisions.

## Claim scope

In a deterministic synthetic CPU-agent artifact workload, a canonical JSON SHA-256 hash-chain plus Merkle root plus HMAC evidence ledger detected all tested post-hoc claim/evidence drift cases across 5 trials of 5,000 records, while plain schema validation missed observation tampering, entry deletion, adjacent reorder, and content edits that recomputed only unkeyed hashes.

## Why it stopped

Closed as no-paper useful signal because the result supports artifact-integrity mechanics only; it is not full validation that cryptographic ledgers improve real CPU agent reliability.

## Recommended next action

Run a bounded deepen test in a real tool-using CPU-agent harness with hidden drift tasks, false-reject measurement on clean runs, and explicit key-custody assumptions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger Drift Detection in a Real Tool-Agent Harness
- Success threshold: Ledger detects at least 95% of injected post-hoc drift cases that plain schemas miss, clean-run false reject rate stays below 1%, and median verification overhead stays below 500 ms per 5,000 records.
- Stop condition: Stop if ledger detection does not exceed the plain-schema baseline on hidden drift cases, false rejects exceed 1% on clean runs, or overhead exceeds the threshold after straightforward implementation fixes.

## Evidence references

- Artifact root: `<local-path>/projects/cryptographic-evidence-ledgers-for-cpu-agent-reliability-39311afb17d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
