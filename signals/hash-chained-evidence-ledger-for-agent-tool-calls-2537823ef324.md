# Hash-Chained Evidence Ledger for Agent Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hash-chained-evidence-ledger-for-agent-tool-calls-2537823ef324`
Run ID: `hash-chained-evidence-ledger-for-agent-tool-calls-2537823ef324-20260619T181522075593+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/99835663199a

## What looked useful

The mechanism is viable for bounded tamper evidence but must be paired with trusted head anchoring. Without anchoring, full recompute and tail truncation attacks pass verification. Full-payload ledgers had 1.50x median byte overhead, 5.79x median append-time overhead in unoptimized Python, and 53k entries/sec median verification throughput.

## Boundaries and scale limits

Synthetic single-process Python harness only; no real agent runner, concurrent appenders, crash recovery, external transparency log, hardware root, or production storage system was tested.

## Claim scope

On local synthetic agent tool-call traces up to 50k entries, a hash-chained JSONL ledger detects local modification, deletion, and reordering, and detects tail truncation or full-ledger recomputation only when verification includes an independently trusted signed head checkpoint.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal, but it is not direct production or publication-grade evidence.

## Recommended next action

Run a bounded deepen test inside a real agent tool-call runner with out-of-process checkpoint anchoring, crash/restart scenarios, and a signed-record baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Runner Ledger With External Head Anchoring
- Success threshold: Detect 100% of local edit, delete, reorder, truncate, and full-recompute attacks after restart; full-payload storage overhead below 2x plain JSONL; verification throughput above 10k entries/sec on at least 100k real or replayed tool calls.
- Stop condition: Stop if trusted head anchoring cannot be made crash-safe, if any attack class passes anchored verification, or if overhead exceeds 2x storage or verification falls below 10k entries/sec in the bounded real-runner test.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-evidence-ledger-for-agent-tool-calls-2537823ef324`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
