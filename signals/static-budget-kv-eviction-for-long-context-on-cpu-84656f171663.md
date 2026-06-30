# Static Budget KV Eviction for Long Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `static-budget-kv-eviction-for-long-context-on-cpu-84656f171663`
Run ID: `static-budget-kv-eviction-for-long-context-on-cpu-84656f171663-20260528T194641125365+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57b4ce2850fe

## What looked useful

Static KV budgets gave 11.96x to 18.05x mean CPU attention speedup across lengths and 64.25x KV memory reduction at length 32768 when budget was 512. Fidelity stayed near exact for local dependencies and for prefix dependencies only when sink slots were retained. Middle-context needle dependencies failed: target hit rate was 0.002 for recent and 0.0 for sink_recent, with mean cosine 0.0234 and 0.0953 versus full attention.

## Boundaries and scale limits

Not a real language-model evaluation; does not measure perplexity, QA accuracy, multi-layer effects, tokenizer behavior, or integration overhead in a production inference runtime. Evidence is bounded to controlled attention dependencies on one CPU worker.

## Claim scope

Synthetic NumPy CPU attention benchmark for fixed-budget KV eviction at prompt lengths 1024 to 32768, decode length 128, dimension 64, comparing full KV attention to recent-only and sink-plus-recent static retention.

## Why it stopped

No-paper mixed result: the synthetic benchmark supports the speed/memory mechanism but early-falsifies any broad claim that static-budget eviction preserves arbitrary long-context dependencies.

## Recommended next action

Stop this run as a synthetic useful signal; next, implement the same recent and sink_recent policies in a real small decoder runtime and evaluate CPU latency, memory, perplexity, and needle retrieval at 4k-32k context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU validation of static KV eviction policies
- Success threshold: At 16k or 32k context, show at least 3x CPU decode attention speedup and at least 4x KV memory reduction while retaining at least 95% of full-KV performance on local and prefix tasks, with explicit degradation quantified on middle-needle tasks.
- Stop condition: Stop if real-model local or prefix quality drops below 90% of full KV at budgets that provide at least 4x memory reduction, or if implementation overhead eliminates the measured CPU speedup.

## Evidence references

- Artifact root: `<local-path>/projects/static-budget-kv-eviction-for-long-context-on-cpu-84656f171663`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
