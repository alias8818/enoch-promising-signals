# Bounded Evidence Ledger Local Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-evidence-ledger-local-validation-637fc81ef17a`
Run ID: `bounded-evidence-ledger-local-validation-637fc81ef17a-20260608T134524472009+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/9a735872710e

## What looked useful

Streaming validation completed 200,000 records in 0.919731 s at 217,455 records/s with 26.45 MiB peak RSS, compared with a load-all baseline at 1.252892 s, 159,631 records/s, and 328.53 MiB peak RSS. All five synthetic tamper classes were rejected.

## Boundaries and scale limits

Tested only on synthetic records up to 200,000 intact records and 5,000-record tamper ledgers. Did not test real evidence semantics, cryptographic signatures, external timestamp anchoring, concurrent writers, crash recovery, distributed replication, adversarial canonicalization edge cases, or million-to-billion-record scale.

## Claim scope

In a deterministic synthetic JSONL ledger with SHA-256 content hashes, append-only hash chaining, and trusted checkpoint anchors, a single-process Python streaming validator can locally validate 200,000 records with bounded memory and detect tested mutation, deletion, insertion, reordering, and checkpoint-mismatch tampering.

## Why it stopped

No-paper closure: the local synthetic experiment supports the bounded streaming validation mechanism, but evidence is not broad or production-realistic enough for publication-grade validation.

## Recommended next action

Run a bounded deepen test that adds signed/external checkpoint anchors plus crash-recovery and concurrent-append cases before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed checkpoint and crash-recovery validation for bounded evidence ledgers
- Success threshold: All crash and concurrency tamper fixtures are rejected or recovered without accepting a corrupted ledger, while streaming validation of 1,000,000 records stays below 128 MiB peak RSS and remains within 2x the current per-record validation time.
- Stop condition: Stop as negative if any common interrupted-write or concurrent-append corruption passes validation, or if checkpoint verification requires memory growing linearly with ledger length.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-evidence-ledger-local-validation-637fc81ef17a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
