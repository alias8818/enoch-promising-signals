# Hierarchical KV Budget for Long-Context CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-kv-budget-for-long-context-cpu-inference-0566b7d629bb`
Run ID: `hierarchical-kv-budget-for-long-context-cpu-inference-0566b7d629bb-20260609T044804150707+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/47ec9868743a

## What looked useful

Retaining 512 KV entries instead of full context reduced estimated fp16 KV memory by 75.00%-98.44% and measured proxy attention time by about 4.1x-121.8x across 2k-32k contexts, but hierarchical old retrieval hit rate was consistently below strided anchors: at 8k tokens across five seeds, hierarchical averaged 0.0156 versus strided 0.0605.

## Boundaries and scale limits

No real language model, no perplexity/downstream task measurement, no multi-layer KV implementation, no learned/content-aware salience, contexts limited to 32,768 synthetic keys with 128-dimensional vectors.

## Claim scope

Small CPU-only synthetic KV-cache proxy: fixed-size KV budgets reduce dot-product attention time and estimated KV memory, but the tested hierarchical exact-anchor retention policy underperforms a uniform strided baseline for uniformly old exact-token retrieval.

## Why it stopped

Proxy evidence supports CPU cost reduction but early-falsifies the tested hierarchical exact-anchor policy as an old-token retrieval improvement over a simpler strided baseline; this is not a full validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should implement a real-model KV eviction harness comparing recent, strided, hierarchical, and content-aware promotion on long-context retrieval plus perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV eviction benchmark for content-aware hierarchical retention
- Success threshold: Content-aware hierarchical retention matches or exceeds strided old-needle retrieval by at least 5 percentage points at equal budget, keeps perplexity degradation within 5% relative to strided, and preserves at least 4x CPU attention-time speedup versus full attention at 8k context.
- Stop condition: Stop if content-aware hierarchical retention does not beat strided retrieval at any tested budget or if perplexity degradation exceeds 10% while latency/memory are equal-budget comparable.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-kv-budget-for-long-context-cpu-inference-0566b7d629bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
