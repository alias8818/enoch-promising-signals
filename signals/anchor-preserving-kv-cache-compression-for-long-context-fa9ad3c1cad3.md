# Anchor-Preserving KV-Cache Compression for Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-preserving-kv-cache-compression-for-long-context-fa9ad3c1cad3`
Run ID: `anchor-preserving-kv-cache-compression-for-long-context-fa9ad3c1cad3-20260628T020555034161+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/795ee7683651

## What looked useful

Observation heavy-hitter retention often kept the target anchor but dropped the adjacent target value, while anchor-neighborhood retention kept the target value in 98.75-100% of medium trials and improved output-cosine similarity versus heavy-hitter by 0.30-0.48 across tested lengths and budgets.

## Boundaries and scale limits

No real transformer inference path, real dataset, real tokenization, multi-layer KV behavior, latency, or memory measurement was tested. The anchor-preserving policy uses known record structure and adjacent value positions in the proxy.

## Claim scope

Synthetic associative-recall proxy with known structural record anchors, sequence lengths 1024-4096, retained-token budgets 64-256, and equal-budget comparisons against recency, sink+recent, and observation heavy-hitter retention.

## Why it stopped

No-paper useful signal only: the positive mechanism evidence is synthetic/proxy evidence, not direct full validation.

## Recommended next action

Run a bounded real-model follow-up implementing anchor-neighborhood retention in a small transformer inference path and evaluate LongBench/Needle-style retrieval at fixed KV budgets against SnapKV/H2O/StreamingLLM controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model anchor-neighborhood KV retention on long-context retrieval
- Success threshold: At least 10 percentage-point retrieval accuracy gain over the best non-full-cache baseline at the same KV budget on a bounded real-model retrieval task, with no worse than 5% decode throughput regression versus that baseline.
- Stop condition: Stop if anchor-neighborhood retention fails to beat heavy-hitter retention by at least 3 percentage points on a smoke real-model retrieval task or if implementation overhead prevents matched-budget evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserving-kv-cache-compression-for-long-context-fa9ad3c1cad3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
