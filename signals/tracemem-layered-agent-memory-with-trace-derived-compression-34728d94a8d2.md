# TraceMem: layered agent memory with trace-derived compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tracemem-layered-agent-memory-with-trace-derived-compression-34728d94a8d2`
Run ID: `tracemem-layered-agent-memory-with-trace-derived-compression-34728d94a8d2-20260620T041043356459+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cc79cf7494ed

## What looked useful

Layering trace-derived memory into current-state and doctrine entries can remove stale facts and reduce retrieval/storage burden in repeated-agent memory workloads, but this run only validates the mechanism on synthetic structured traces.

## Boundaries and scale limits

Synthetic traces only; structured oracle extraction from generated event fields; no live agent runtime, real operator traces, LLM summarization, learned compression, adversarial trace corruption, or end-to-end task completion measurement.

## Claim scope

In a deterministic synthetic repeated-session trace benchmark with 14,880 events and 840 current-state queries, a layered current-state/doctrine memory preserved all queried durable facts under an 80-token retrieval budget while using 8,505 storage tokens, compared with 57.1% accuracy and 142,269 storage tokens for transcript search and 55.2% accuracy and 32,774 storage tokens for flat retrieval.

## Why it stopped

No-paper closure: the mechanism is supported in a bounded synthetic probe, but publication-grade evidence would require real/raw traces and non-oracle compression.

## Recommended next action

Run a bounded deepen follow-up on real or realistic raw agent traces using an LLM or heuristic compressor, measuring both memory-answer accuracy and end-to-end replay task success against transcript and flat retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: TraceMem on raw replay traces with non-oracle compression
- Success threshold: Layered memory reaches at least 0.90 current-fact accuracy, reduces storage by at least 50% versus transcript search, and does not reduce end-to-end replay-task success versus the strongest baseline.
- Stop condition: Stop if non-oracle compression falls below 0.75 current-fact accuracy or has a stale-fact error rate within 5 percentage points of flat retrieval on a 100+ query validation set.

## Evidence references

- Artifact root: `<local-path>/projects/tracemem-layered-agent-memory-with-trace-derived-compression-34728d94a8d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
