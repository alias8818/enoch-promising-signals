# Hybrid Exact-Compressed Agent Memory

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `hybrid-exact-compressed-agent-memory-692191c444ae`
Run ID: `hybrid-exact-compressed-agent-memory-692191c444ae-20260608T072907298513+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/98a3a9dfd9b2

## What looked useful

At equal 64-slot capacity, recent_exact reached 0.4029 mean accuracy, compressed_only reached 0.3927, and the best hybrid split reached 0.3914. All bounded policies scored 0.0 on arbitrary old-event recall, while the unbounded exact oracle scored 1.0, showing that latest-state compression is insufficient for episodic recall.

## Boundaries and scale limits

Synthetic key-value fact streams only; no natural conversations, LLM-generated summaries, embeddings, semantic retrieval, tool-use traces, or downstream agent task success. The tested compression is a bounded latest-state table, not a full language-summary memory.

## Claim scope

A dependency-free synthetic agent-memory benchmark with 50 trials, 500 fact writes per trial, 300 recall queries per trial, and 64 storage slots found that a naive hybrid of exact recent FIFO memory plus older latest-state compression did not outperform exact-only FIFO or compressed-only latest-state baselines.

## Why it stopped

Proxy/early falsification: the tested slot-budgeted hybrid mechanism failed to beat storage-matched exact-only and compressed-only baselines; this is not a full real-agent validation.

## Recommended next action

Stop this simple hybrid allocation as an early synthetic falsification; the next bounded test should replace latest-state-only compression with an episodic reservoir or provenance-bearing compressed summaries and compare against the same baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Exact Memory with Episodic Reservoir Compression
- Success threshold: Best hybrid mean accuracy exceeds both 64-slot baselines by at least 3 percentage points and old_recall is at least 0.20 while recent_exact remains at least 0.98.
- Stop condition: Stop if the improved hybrid still has old_recall below 0.10 or mean accuracy does not exceed the best simple baseline after a split sweep.

## Evidence references

- Artifact root: `<local-path>/projects/hybrid-exact-compressed-agent-memory-692191c444ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
