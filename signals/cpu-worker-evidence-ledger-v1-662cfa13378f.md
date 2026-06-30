# CPU Worker Evidence Ledger v1

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-worker-evidence-ledger-v1-662cfa13378f`
Run ID: `cpu-worker-evidence-ledger-v1-662cfa13378f-20260609T122441510740+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/11af1c80a1bf

## What looked useful

Stateful ledger writing reached 50,596.71 entries/s without fsync for 1000 entries and 972.80 entries/s with fsync for 200 entries; full validation of 1000 entries took about 0.009 s. Hash-chain validation detected payload edits, middle deletion, and reordering, but a truncated ledger remained internally valid.

## Boundaries and scale limits

Single-process local benchmark only; no controller-side head anchoring, signatures, crash-recovery stress, concurrent writers, remote receipts, or multi-run production integration were tested. File-local validation does not detect pure truncation without an external expected head hash.

## Claim scope

On this CPU worker, a standard-library SHA-256 hash-chained JSONL ledger can validate command, metric, artifact, and decision entries; detect payload edits, middle deletion, and reorder mutations; and write quickly when using a stateful writer that validates once before appending.

## Why it stopped

No-paper useful signal: local mechanism works with a stateful writer, but append-only integrity is incomplete because truncation is only detectable with external anchoring that was not implemented in this run.

## Recommended next action

Build a controller-anchored ledger receipt prototype that records expected head hashes outside the worker ledger, then rerun truncation, crash-recovery, and real worker-run validation tests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Controller-Anchored Evidence Ledger Receipts
- Success threshold: Detect all tested mutation classes including truncation and rollback while sustaining at least 500 non-fsync local entries/s or at least 50 fsync local entries/s for 1000 evidence entries, with successful recovery from a partial trailing record.
- Stop condition: Stop if external receipt anchoring cannot detect truncation/rollback, if crash recovery loses committed entries, or if receipt overhead drops below 50 fsync entries/s in the 1000-entry test.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-worker-evidence-ledger-v1-662cfa13378f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
