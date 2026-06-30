# KV-Cache Eviction via Attention Sinks for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-eviction-via-attention-sinks-for-long-context-08cd7eed97ca`
Run ID: `kv-cache-eviction-via-attention-sinks-for-long-context-08cd7eed97ca-20260528T225120911448+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4b7f37f21ef6

## What looked useful

Fixed sink+sliding was worse than sliding across all tested budgets and sink strengths, increasing output MSE by 46.99% on average and lowering target probability by 10.45% on average. Sink-aware H2O-style retention improved output MSE versus calibrated H2O by 10.74% on average, but target probability was mixed.

## Boundaries and scale limits

No real transformer model, perplexity benchmark, long-context QA benchmark, production KV cache implementation, latency measurement, or memory-throughput measurement was run. Dynamic controls use full-attention calibration and are not deployable algorithms as written.

## Claim scope

Synthetic attention probe with 4096-token caches, 4 initial sink tokens, budgets of 64/128/256, eight seeds, and target tokens distributed across far/mid/recent context. The result supports only a proxy claim: fixed sink+recent eviction can over-amplify sink mass and hurt target retention, while sink-aware dynamic retention can modestly improve attention-output fidelity over a dynamic attention-score control.

## Why it stopped

Proxy evidence does not support a paper-ready KV-cache eviction method; the simplest fixed attention-sink policy is early-falsified in the synthetic setting, while the dynamic sink-aware signal requires direct model validation.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded real-model deepen comparing full cache, sliding, sink+sliding, H2O-style retention, and sink-aware dynamic retention on a small long-context retrieval/perplexity benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model validation of sink-aware dynamic KV eviction
- Success threshold: At equal cache budget, sink-aware dynamic retention improves the primary task metric by at least 5% relative to sliding and fixed sink+sliding, stays within 10% latency overhead of the best eviction baseline, and avoids materially higher sink-mass error.
- Stop condition: Stop if fixed sink+sliding and sink-aware dynamic retention both fail to beat sliding on the primary task metric at matched cache budget, or if sink-mass over-amplification persists in real model traces.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-eviction-via-attention-sinks-for-long-context-08cd7eed97ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
