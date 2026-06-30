# Suffix-Tree Speculative Decoding with Anchor Memory on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-with-anchor-memory-on-cpu-25786257d2e2`
Run ID: `suffix-tree-speculative-decoding-with-anchor-memory-on-cpu-25786257d2e2-20260621T185412205126+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5e9c9627c941

## What looked useful

On non-control scenarios, suffix_anchor reached 2.4535x mean simulated verifier-call speedup ceiling and 0.6579 acceptance, essentially matching ngram4 at 2.4538x and 0.6585, while suffix_anchor lookup averaged 8471 ns/call versus 922 ns/call for ngram4. High-entropy control stayed at 1.0x for all strategies.

## Boundaries and scale limits

Synthetic token traces only; no full LLM verifier, logits, KV-cache, batching, compiled suffix data structure, or end-to-end serving latency. Calibrated run used four 40000-token scenarios with draft length 8 on a single CPU process.

## Claim scope

Bounded CPU token-stream mechanism probe: memory-based drafting reduces simulated verifier calls on repeated synthetic streams, but the suffix-anchor variant does not outperform a simple 4-token n-gram baseline and has substantially higher lookup/update overhead.

## Why it stopped

Proxy mechanism test found no advantage for suffix-anchor memory over a cheap n-gram baseline; this is an early bounded falsification, not a full serving validation.

## Recommended next action

Stop this run as a no-paper useful signal; only revisit with real model token traces and an optimized suffix-anchor implementation that must beat ngram4 on accepted tokens per verifier call and end-to-end latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-token trace suffix-anchor drafting versus n-gram baselines
- Success threshold: suffix-anchor improves accepted tokens per verifier call by at least 15% over ngram4 and keeps total draft lookup/update overhead below 10% of measured verifier time on the trace workload.
- Stop condition: Stop if suffix-anchor fails to beat ngram4 on accepted tokens per verifier call or if lookup/update overhead removes the simulated verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-with-anchor-memory-on-cpu-25786257d2e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
