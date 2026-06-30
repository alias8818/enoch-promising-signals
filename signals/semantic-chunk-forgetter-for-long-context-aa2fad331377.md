# Semantic Chunk Forgetter for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `semantic-chunk-forgetter-for-long-context-aa2fad331377`
Run ID: `semantic-chunk-forgetter-for-long-context-aa2fad331377-20260610T112028239406+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/65bbe62591f0

## What looked useful

Semantic chunk forgetting is promising as a context-budget mechanism when semantic coverage is good, but static coverage is brittle: unseen aliases reduced recall to 0.144 at an 8/64 budget, near lexical/random controls. Future tests should prioritize OOD/paraphrase robustness before scale claims.

## Boundaries and scale limits

Synthetic data only; no pretrained embeddings, no natural long-context QA dataset, no transformer reader, no training-time validation, and no deployment latency measurement. Primary run was 3,000 CPU-only episodes with 64 chunks and an 8-chunk retention budget.

## Claim scope

In a controlled synthetic long-context benchmark with 64 chunks and known alias mappings, query-aware semantic chunk forgetting retained answer evidence substantially better than lexical, recency, and random chunk selection under 4-16 chunk budgets; the effect collapsed on intentionally unseen aliases.

## Why it stopped

No-paper useful signal: the bounded synthetic evidence supports the mechanism under covered aliases but also early-falsifies robust static semantic forgetting under unseen alias shift; this is not full validation.

## Recommended next action

Run a bounded real-data deepen test using pretrained embeddings on a long-context QA dataset with an explicit paraphrase/OOD split and fixed reader model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data semantic chunk forgetting with paraphrase/OOD robustness split
- Success threshold: At least +10 percentage points answer accuracy over lexical overlap at the same retained-token budget on in-domain data, with paraphrase/OOD degradation no worse than 50% of the in-domain gain and no regression versus random retention.
- Stop condition: Stop if embedding-based semantic forgetting fails to beat lexical overlap by 5 percentage points on in-domain real-data answer accuracy or if paraphrase/OOD recall falls to random-retention levels.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-chunk-forgetter-for-long-context-aa2fad331377`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
