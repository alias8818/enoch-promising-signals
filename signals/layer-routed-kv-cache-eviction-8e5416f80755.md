# Layer-Routed KV Cache Eviction

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `layer-routed-kv-cache-eviction-8e5416f80755`
Run ID: `layer-routed-kv-cache-eviction-8e5416f80755-20260526T005752416986+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8aaed54ce305

## What looked useful

Across 9 scenario/cache-size means and 72 seed-scenario trials, layer_routed_ewma never beat global_lru on scenario means and beat global_lru in only 2 individual trials. The largest mean deficit was -0.02730 weighted hit rate in heterogeneous 2% cache; heterogeneous 5% and 10% cache deficits were -0.00604 and -0.00394.

## Boundaries and scale limits

No real transformer was run. The experiment does not measure perplexity, task quality, GPU memory bandwidth, paged KV behavior, batching, GQA/MQA effects, or production serving latency. The result should be treated as an early proxy falsification of this simple routing mechanism, not all layer-aware eviction methods.

## Claim scope

Synthetic/proxy cache-policy evaluation: an online layer-routed EWMA per-layer capacity allocator did not improve weighted KV hit rate over layer-blind global LRU on 12-layer, 2048-token synthetic attention traces across heterogeneous, homogeneous, and inverted layer age-profile regimes at 2%, 5%, and 10% cache fractions.

## Why it stopped

Early synthetic/proxy falsification: the tested EWMA layer-router underperformed simple global LRU, so current evidence does not justify paper writing or a longer GB10 run.

## Recommended next action

Stop this run as a no-paper proxy negative; a separate bounded follow-up should replay real pretrained-transformer attention traces and test a marginal-utility estimator against global LRU.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Layer-Aware KV Eviction Replay
- Success threshold: At least 1% absolute weighted-hit-rate improvement over global LRU and no worse direct model metric at two or more KV budgets on real traces.
- Stop condition: Stop if the marginal-utility layer-aware policy fails to beat global LRU on weighted trace retention or worsens direct model metrics at matched KV memory.

## Evidence references

- Artifact root: `<local-path>/projects/layer-routed-kv-cache-eviction-8e5416f80755`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
