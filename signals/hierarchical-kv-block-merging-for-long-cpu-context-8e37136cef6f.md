# Hierarchical KV Block Merging for Long CPU Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-kv-block-merging-for-long-cpu-context-8e37136cef6f`
Run ID: `hierarchical-kv-block-merging-for-long-cpu-context-8e37136cef6f-20260602T195820685533+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6d97d8ae3df8

## What looked useful

Multiplicity-aware block-mean KV compression can give roughly 9-10x CPU attention speedups with low relative L2 error on smooth redundant context, but naive age-tiered hierarchy is not better than flat pooling and both merging approaches destroy needle retrieval.

## Boundaries and scale limits

No real transformer integration, no perplexity or downstream tasks, no layer-wise accumulation, no multi-head analysis, no tokenizer/corpus validation, and no production serving overhead measurement. Evidence is local CPU synthetic/proxy only.

## Claim scope

CPU proxy benchmark of single-step attention reads over synthetic 16k-token KV caches: age-tiered hierarchical block-mean merging approximates smooth redundant context at 6.25-12.5 percent cache but does not outperform flat weighted block means and fails isolated old-token retrieval.

## Why it stopped

Moderate CPU proxy evidence shows mixed behavior: useful redundant-context compression signal, but no hierarchical advantage over flat pooling and near-total failure on isolated retrieval; this is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should add salience-preserving retention to block merging and compare against flat pooling on the same smooth and needle probes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Salience-preserving KV block merging for redundant and needle contexts
- Success threshold: At 12.5 percent cache, keep smooth_recency relative L2 error within 25 percent of flat pooling while reducing needle_retrieval relative L2 error below 0.30 and retaining at least 5x CPU attention speedup.
- Stop condition: Stop if salience retention cannot reduce needle_retrieval relative L2 error below 0.50 at 12.5 percent cache or if CPU attention speedup falls below 3x.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-kv-block-merging-for-long-cpu-context-8e37136cef6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
