# Trace-derived semantic compression vs flat retrieval for CPU agent memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-derived-semantic-compression-vs-flat-retrieval-for-cpu-agent-memory-d9043ef4e0d2`
Run ID: `trace-derived-semantic-compression-vs-flat-retrieval-for-cpu-agent-memory-d9043ef4e0d2-20260619T174452193123+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e4e06b2a7886

## What looked useful

Compressed latest-state memory achieved 1.000 mean accuracy versus 0.585 for flat retrieval, with +0.415 mean accuracy delta, 0.9956 mean stored-character reduction, and 0.0040 mean compressed/flat latency ratio.

## Boundaries and scale limits

Synthetic benchmark only; 8 projects, 5 slots, 1640 events and 40 queries per seed, 10 seeds. Does not validate learned compression, embedding retrieval, real operator traces, natural-language parser errors, or production memory workloads.

## Claim scope

On deterministic synthetic repeated-agent traces with explicit typed updates, stale superseded facts, and distractor events, trace-derived latest-state semantic compression outperformed flat lexical retrieval for current-fact queries across 10 seeds.

## Why it stopped

No-paper closure: this is a synthetic/proxy mechanism signal, not full validation on real agent traces or robust memory baselines.

## Recommended next action

Run a bounded natural-language trace extraction follow-up against recency-aware flat retrieval and embedding retrieval baselines before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy natural-language trace compression versus recency-aware and embedding retrieval baselines
- Success threshold: Compression beats the best non-compressed baseline by at least 10 absolute accuracy points while reducing stored memory by at least 80%, with extractor F1 at or above 0.90 on the evaluated trace distribution.
- Stop condition: Stop if extraction F1 is below 0.80 or if recency-aware/embedding baselines match compression accuracy within 5 points while staying within 2x memory and latency.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-semantic-compression-vs-flat-retrieval-for-cpu-agent-memory-d9043ef4e0d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
