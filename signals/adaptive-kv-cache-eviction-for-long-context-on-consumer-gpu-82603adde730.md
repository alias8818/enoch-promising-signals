# Adaptive KV-Cache Eviction for Long Context on Consumer GPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-kv-cache-eviction-for-long-context-on-consumer-gpu-82603adde730`
Run ID: `adaptive-kv-cache-eviction-for-long-context-on-consumer-gpu-82603adde730-20260619T231001995973+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7fe93baac7cb

## What looked useful

Adaptive retained attention mass beat fixed H2O-style by 0.0080-0.0222 mean mass and 0.0203-0.0312 tail mass across six model/budget combinations; it beat sliding window by 0.2322-0.3383 mean mass and 0.3262-0.3538 tail mass.

## Boundaries and scale limits

No production KV-cache kernel was modified; no autoregressive generation cache, perplexity, next-token KL, latency, fragmentation, or natural benchmark quality was measured. Inputs were controlled repeated prose on GPT-2-family models only.

## Claim scope

Trace-level evidence on distilgpt2 at 768 tokens and gpt2 at 1024 tokens shows an adaptive recent/heavy-hitter KV retention policy preserves more full-attention probability mass than fixed H2O-style and sliding-window policies at budgets 64, 128, and 256.

## Why it stopped

The result is a bounded trace-level useful signal, not direct/full validation of adaptive KV-cache eviction in serving.

## Recommended next action

Stop paper path for this run; deepen with an actual generation-cache implementation that measures quality, memory, and throughput under the same budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Generation-cache validation for adaptive KV eviction
- Success threshold: At equal KV budget, adaptive reduces quality degradation by at least 10% relative to fixed H2O-style without more than 5% tokens/sec overhead, and remains clearly better than sliding window.
- Stop condition: Stop if adaptive does not improve next-token KL/perplexity versus fixed H2O-style at two or more budgets, or if cache bookkeeping overhead exceeds 10% tokens/sec without quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-kv-cache-eviction-for-long-context-on-consumer-gpu-82603adde730`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
