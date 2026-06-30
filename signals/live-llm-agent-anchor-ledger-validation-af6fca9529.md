# Live LLM Agent Anchor Ledger Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-llm-agent-anchor-ledger-validation-af6fca9529`
Run ID: `live-llm-agent-anchor-ledger-validation-af6fca9529-20260529T011414465612+0000`

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

- Parent run decision: Agent Ledger: Exact Anchor Buffer plus Compressed Summary: enoch://control-plane/projects/agent-ledger-exact-anchor-buffer-plus-compressed-summary-00d19bdc6bfa/runs/agent-ledger-exact-anchor-buffer-plus-compressed-summary-00d19bdc6bfa-20260528T222053649038+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/dcdcd6c75d7c

## What looked useful

Anchor roots stored outside the mutable ledger caught rollback and suffix-fork attacks that local hash recomputation could otherwise hide; local hash-chain validation caught edits, deletion, and reorder. Clean false-positive rate was 0/120 and tamper detection was 600/600, while a naive JSONL baseline detected 0/600.

## Boundaries and scale limits

120 synthetic sessions, 40 events per session, 600 tamper trials total; synthetic deterministic agent events; local modeled external anchor store; no real LLM inference, real tool execution, concurrent writers, crash recovery, remote service, key compromise, or production storage backend.

## Claim scope

In a deterministic Tier 1 harness using live-agent-shaped event streams, a canonical JSON hash-chain ledger with periodic external anchors accepted clean sessions and detected all tested post-hoc tampering modes: payload edit, event deletion, reorder, rollback/truncation, and suffix fork rewrite.

## Why it stopped

Tier 1 mechanism evidence is positive but not paper-ready because the LLM agent and external anchor service were modeled locally rather than validated in a real agent runtime.

## Recommended next action

Run a bounded deepen test by integrating the ledger into a real local LLM tool-calling agent with persistent external anchors, crash injection, and overhead measurement; do not write a paper from the current synthetic/local evidence alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Local LLM Agent Anchor Ledger Crash and Tamper Validation
- Success threshold: Detection rate 100% for each tamper class, clean false-positive rate 0%, successful validation after crash/restart, and median runtime overhead below 5% versus unledgered baseline.
- Stop condition: Stop if any tamper class has detection below 100%, any clean session fails validation without an identified implementation bug, crash recovery loses anchor consistency, or overhead is at least 5% after one straightforward optimization pass.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-agent-anchor-ledger-validation-af6fca9529`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
