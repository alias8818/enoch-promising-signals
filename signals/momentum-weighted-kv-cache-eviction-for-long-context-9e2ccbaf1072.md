# Momentum-weighted KV cache eviction for long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `momentum-weighted-kv-cache-eviction-for-long-context-9e2ccbaf1072`
Run ID: `momentum-weighted-kv-cache-eviction-for-long-context-9e2ccbaf1072-20260530T065953430766+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/561ff17d42d8

## What looked useful

Momentum/recency EMA won retained-attention-mass comparisons for stationary anchors and shifting topics across all tested budgets, and for needle recall at budgets 128 and 256. It was worse than LRU for pure local attention at tight budget and lost total retained mass to LRU on needle recall at budget 64 despite better critical-anchor retention. Decay sensitivity showed shorter EMA memory performed best in these traces.

## Boundaries and scale limits

No real transformer inference, perplexity, downstream task accuracy, multi-layer/head behavior, or GPU serving throughput was measured. Results are bounded to synthetic full-attention traces and should not be treated as a production LLM validation.

## Claim scope

Trace-level synthetic attention evaluation of momentum-weighted KV cache eviction under fixed cache budgets of 64, 128, and 256 tokens over 4096-token traces. The supported mechanism is that EMA attention scores retain useful long-range keys better than LRU and cumulative heavy-hitter scores when important keys are durable or shift over time.

## Why it stopped

Closed as no-paper useful signal: the trace proxy supports the mechanism but is not direct/full validation of long-context LLM quality or serving performance.

## Recommended next action

Run a bounded direct model-quality follow-up by implementing momentum eviction in a small pretrained decoder and measuring perplexity/task accuracy plus decode cost against LRU, H2O-style heavy hitter, and StreamingLLM-style baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-decoder validation of momentum KV eviction
- Success threshold: At matched cache budget, momentum eviction improves real-model quality by at least 5% relative error/perplexity degradation reduction versus the best non-momentum eviction baseline while keeping decode overhead under 5%.
- Stop condition: Stop if momentum does not beat the best baseline on direct model-quality metrics at two cache budgets or if online score maintenance adds more than 5% decode overhead.

## Evidence references

- Artifact root: `<local-path>/projects/momentum-weighted-kv-cache-eviction-for-long-context-9e2ccbaf1072`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
