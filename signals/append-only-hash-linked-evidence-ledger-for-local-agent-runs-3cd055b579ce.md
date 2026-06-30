# Append-Only Hash-Linked Evidence Ledger for Local Agent Runs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `append-only-hash-linked-evidence-ledger-for-local-agent-runs-3cd055b579ce`
Run ID: `append-only-hash-linked-evidence-ledger-for-local-agent-runs-3cd055b579ce-20260629T213421968262+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e34903c05e19

## What looked useful

Hash linking is practical and low-overhead for local JSONL evidence logs under per-record fsync, but it is insufficient as a standalone append-only evidence mechanism because valid-prefix tail truncation and rehashed suffix rewrite pass verification without an external anchor.

## Boundaries and scale limits

Synthetic records only; no multi-writer concurrency, OS append-only enforcement, secret redaction, external notarization, hardware signing, or production agent traces were tested. Tail truncation and suffix rewrite are not detected by the ledger alone and require an external head anchor or stronger signing/checkpoint design.

## Claim scope

A single-process Python prototype of a canonical JSONL SHA-256 hash-linked ledger for synthetic local agent-run evidence records detects interior payload modification, middle deletion, and adjacent reordering, and verifies 20k-record ledgers at roughly 132k records/s on this host.

## Why it stopped

Local bounded evidence produced a mixed useful signal, but the core standalone append-only claim is not paper-ready because tail truncation and suffix rewrite require external anchoring.

## Recommended next action

Stop this no-paper run; a useful next bounded test would add signed periodic anchors plus file-locking and replay the same tamper suite with concurrent local writers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed Anchors and Concurrent Writers for Local Evidence Ledgers
- Success threshold: Detect 100% of tested tamper cases including tail truncation and suffix rewrite with signed anchors, preserve all records in a 4-writer stress test, and keep ledger write overhead under 2x plain JSONL for 20k 512-byte records.
- Stop condition: Stop if signed anchoring still cannot distinguish valid tail loss from legitimate short runs, if concurrent appends corrupt records, or if overhead exceeds 2x plain JSONL under matched durability settings.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-hash-linked-evidence-ledger-for-local-agent-runs-3cd055b579ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
