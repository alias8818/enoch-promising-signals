# KV-Cache Compression Under Agent Trace Pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-under-agent-trace-pressure-c37450a70e2e`
Run ID: `kv-cache-compression-under-agent-trace-pressure-c37450a70e2e-20260628T211232169454+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/34fc6b6ab6e3

## What looked useful

Agent trace pressure creates a concrete failure mode for sliding and sink-plus-recent KV-cache compression: long-gap middle-context revisits had 0.000 target retention in the main run. Static prompt selection retained only 0.071 of long-gap revisit targets at budget 256. Optimistic heavy-hitter retention kept 1.000 of long-gap revisit targets and reached 0.928 mean output cosine against full attention.

## Boundaries and scale limits

No real language model, tokenizer, layer/head diversity, paged-attention runtime, latency measurement, or real agent trace task success was tested. H2O-style scoring is optimistic because cumulative importance is updated from full attention.

## Claim scope

Synthetic NumPy attention traces with 2,048 prompt tokens, 768 decode steps, sparse phase-local and long-gap revisit targets, and cache budgets from 128 to 512 slots show that recency/static KV retention fails under agent-style revisit pressure while optimistic cumulative-attention heavy-hitter retention preserves target tokens.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only; it supports a mechanism but cannot validate real model quality or serving performance.

## Recommended next action

Run a bounded real-model follow-up using a small decoder and recorded or generated agent traces, comparing decode-time heavy-hitter retention against sliding, sink-recent, and static prompt selection on task success plus memory/latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV retention under agent trace revisits
- Success threshold: At the same cache budget, decode-time heavy-hitter retention should improve long-gap fact retrieval by at least 20 percentage points over sliding/sink-recent while keeping task accuracy within 5 percentage points of full cache and reducing KV memory by at least 50%.
- Stop condition: Stop if heavy-hitter retention fails to beat sliding/sink-recent by at least 10 percentage points on long-gap fact retrieval or causes more than a 10 percentage point task-accuracy drop versus full cache.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-under-agent-trace-pressure-c37450a70e2e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
