# Layered Trace-Derived Semantic Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-trace-derived-semantic-compression-9f1eb72d635e`
Run ID: `layered-trace-derived-semantic-compression-9f1eb72d635e-20260620T064652349003+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/8326b63f3b9a

## What looked useful

Layered summaries reached 1.0 accuracy from the 2048-character budget upward in the primary run and across five replication seeds, while flat retrieval peaked at 0.66 mean accuracy and degraded from stale-fact false recalls as budget increased.

## Boundaries and scale limits

Synthetic/proxy evidence only; semantic extraction from natural language traces was not tested, no real operator corpus was used, and no large-scale serving or model-training validation was attempted.

## Claim scope

On deterministic synthetic repeated-agent traces with generated structured facts, layered trace-derived semantic compression preserved current-state recall under fixed character budgets better than raw transcript search and flat fact retrieval.

## Why it stopped

No-paper closure: the mechanism is supported in a synthetic memory-layout benchmark, but the extraction and real-trace assumptions remain unvalidated.

## Recommended next action

Run a bounded deepen follow-up on real or human-authored repeated-agent traces with a fixed extractor and blinded answer keys; stop here for paper purposes because this run is proxy-only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace layered semantic compression with extractor error analysis
- Success threshold: At least 15 percentage points higher recall accuracy than the best baseline at two or more memory budgets, with no increase in false-recall rate and extractor F1 reported.
- Stop condition: Stop if extractor F1 is below 0.80 or layered recall is not at least 5 percentage points above the best baseline at any tested budget.

## Evidence references

- Artifact root: `<local-path>/projects/layered-trace-derived-semantic-compression-9f1eb72d635e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
