# CPU-native KV cache eviction via per-block importance scoring

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-native-kv-cache-eviction-via-per-block-importance-scoring-5ea83792fc8c`
Run ID: `cpu-native-kv-cache-eviction-via-per-block-importance-scoring-5ea83792fc8c-20260622T003931992310+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f2f77c424514

## What looked useful

Importance scoring beat FIFO/random on persistent-anchor traces but matched LRU overall: 0/15 wins vs LRU, 0.0% mean retained-attention gain, 1.23x Python policy CPU overhead, and a 0.216 mean retained-mass gap to oracle.

## Boundaries and scale limits

No real transformer, serving stack, hardware KV path, perplexity/task-quality measurement, memory-bandwidth profile, or production attention trace was evaluated. The run is a proxy early falsification, not full validation.

## Claim scope

In a bounded synthetic CPU simulator of block-level KV cache pressure, a simple exponentially decayed observed-attention importance score did not improve retained attention mass over LRU.

## Why it stopped

Proxy early falsification: the tested per-block observed-importance policy did not beat LRU under the bounded success threshold, though direct full evidence would require real transformer serving replay.

## Recommended next action

Stop this simple-policy line unless a follow-up implements a predictive or phase-aware block score and tests it against LRU on real model-serving traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Predictive phase-aware KV block eviction against LRU on real decode traces
- Success threshold: At least 5% retained-attention or task-quality improvement over LRU across most tested capacity regimes, with no more than 2x eviction bookkeeping CPU overhead in the serving path.
- Stop condition: Stop if predictive scoring fails to beat LRU by 5% on real traces or exceeds 2x CPU overhead after a small-model replay.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-native-kv-cache-eviction-via-per-block-importance-scoring-5ea83792fc8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
