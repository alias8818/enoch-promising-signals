# Runtime-integrated anchored tool-call ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `runtime-integrated-anchored-tool-call-ledger-6e04a98f51`
Run ID: `runtime-integrated-anchored-tool-call-ledger-6e04a98f51-20260526T130857146414+0000`

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

- Parent run decision: Append-Only Ledger for Tool Call Verification: enoch://control-plane/projects/append-only-ledger-for-tool-call-verification-67c714c7c256/runs/append-only-ledger-for-tool-call-verification-67c714c7c256-20260526T043111662260+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7cc8b96039e4

## What looked useful

Anchored ledger verification passed on clean traces and detected 1000/1000 tamper trials for modify_args, modify_result, delete_entry, swap_adjacent, truncate_tail, and replay_entry. The plaintext baseline detected structural count/order faults but missed content edits. Anchored logging averaged 7.408 microseconds per call versus 0.218 for no logging and 0.541 for plaintext logging.

## Boundaries and scale limits

Tested only deterministic local tool calls, one process, 128-call traces for detection, and 50,000-call local overhead repetitions. Not tested in a real LangGraph or hosted model runtime, with concurrency, streaming outputs, crash recovery, independent external anchoring, key compromise, or colluding runtime compromise.

## Claim scope

In a controlled local Python runtime harness, a tool-call wrapper that writes HMAC-tagged hash-chain entries with periodic anchors made persisted tool-call transcripts tamper-evident for six tested post-hoc fault classes while adding about 7.19 microseconds per simple tool call.

## Why it stopped

No-paper useful signal: the mechanism met the Tier 1 controlled direct-test threshold, but evidence is local-harness only and not publication-grade runtime validation.

## Recommended next action

Run a bounded deepen follow-up that integrates the ledger into an actual LangGraph-style tool execution path with concurrent calls, crash/restart persistence, and an independent append-only anchor store.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-runtime anchored tool-call ledger with crash and concurrency faults
- Success threshold: Clean verification false-positive rate is 0%; all tested post-hoc tamper classes are detected in at least 99.5% of trials; crash/restart leaves either a verifiable complete prefix or an explicit incomplete-tail marker; overhead is below 5 ms median per real tool call or below 2% wall-clock on IO-bound workflows.
- Stop condition: Stop if clean verification has any unexplained false positives, if any non-key-compromise post-hoc tamper class falls below 99.5% detection, or if median overhead exceeds 5 ms per real tool call without a clear optimization path.

## Evidence references

- Artifact root: `<local-path>/projects/runtime-integrated-anchored-tool-call-ledger-6e04a98f51`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
