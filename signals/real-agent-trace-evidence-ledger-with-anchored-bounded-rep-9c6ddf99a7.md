# Real Agent Trace Evidence Ledger with Anchored Bounded Replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-trace-evidence-ledger-with-anchored-bounded-rep-9c6ddf99a7`
Run ID: `real-agent-trace-evidence-ledger-with-anchored-bounded-rep-9c6ddf99a7-20260605T141735240647+0000`

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

- Parent run decision: CPU-Only Agent Evidence Ledger with Bounded Replay: enoch://control-plane/projects/cpu-only-agent-evidence-ledger-with-bounded-replay-7b5fe4c8178e/runs/cpu-only-agent-evidence-ledger-with-bounded-replay-7b5fe4c8178e-20260605T102444602388+0000
- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/92a46d25a542

## What looked useful

The core mechanism works in a controlled small direct test: clean bounded replay verified indices 20..26 for a requested 21..26 window, all 3 tamper classes were rejected, ledger build median was 1.032 ms, and bounded verification median was 0.191 ms over 100 repeats.

## Boundaries and scale limits

Single local trace, 27 events, one schema family, no external timestamping, no cross-process persistence test, no large-trace storage or latency validation, and no human audit study.

## Claim scope

On one 27-event real Codex/Enoch JSONL trace, an append-only evidence ledger with 4-event Merkle anchors verified a bounded replay window from the nearest prior anchor and rejected content edit, deletion-with-padding, and adjacent reorder mutations.

## Why it stopped

No-paper closure: this is a small direct mechanism test with useful signal, not broad or publication-grade validation.

## Recommended next action

Run a bounded deepen test on a heterogeneous corpus of real agent traces with persisted anchors, restart replay, and at least 8 mutation classes before considering paper framing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heterogeneous Real Agent Trace Ledger Replay with Restart Persistence
- Success threshold: Clean restart replay succeeds on all tested windows, all mutation classes are rejected, and median bounded verification recomputes no more than anchor_interval + window_size events per window.
- Stop condition: Stop as negative if any clean persisted replay fails, if any mutation class is accepted, or if verifier requires full-history replay for tail windows.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-trace-evidence-ledger-with-anchored-bounded-rep-9c6ddf99a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
