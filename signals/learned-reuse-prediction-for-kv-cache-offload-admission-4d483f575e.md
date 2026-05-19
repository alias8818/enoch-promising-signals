# Learned Reuse Prediction for KV-Cache Offload Admission

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-reuse-prediction-for-kv-cache-offload-admission-4d483f575e`
Run ID: `learned-reuse-prediction-for-kv-cache-offload-admission-4d483f575e-20260519T034624640799+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4a1d9380147a

## What looked useful

Primary 10-seed Tier 1 test at offload capacity 256 showed learned admission had 6573.37 mean net benefit versus 5712.97 for admit-all LRU (+15.06%) and 3471.94 for matched-rate random (+89.33%). Capacity sensitivity showed +53.54% versus admit-all at capacity 128, but -3.34% at capacity 512, indicating the mechanism is pressure-dependent.

## Boundaries and scale limits

Synthetic traces only; latency costs are parameterized rather than measured from a serving engine; no vLLM/TensorRT-LLM/SGLang integration; no real model attention or production workload traces.

## Claim scope

In a controlled synthetic direct KV cache/offload replay, a small learned reuse predictor improved net offload-admission benefit over admit-all LRU when offload capacity was tight or moderately constrained, but not when offload capacity was ample.

## Why it stopped

Tier 1 controlled direct test supports a bounded mechanism signal but is synthetic and mixed across capacity regimes, so it is not paper-ready.

## Recommended next action

Run a deepen follow-up using real or engine-generated KV block traces with measured restore/recompute costs, and require learned admission to beat admit-all LRU under at least two constrained memory budgets without losing under ample capacity by more than 2%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Driven Learned KV Offload Admission Under Memory Pressure
- Success threshold: Learned admission improves mean net benefit over admit-all LRU by at least 10% in two constrained offload budgets and is no worse than 2% below admit-all in an ample-capacity budget across at least five seeds or trace shards.
- Stop condition: Stop as a negative result if learned admission fails to beat admit-all LRU by 5% in constrained budgets or loses more than 5% in the ample-capacity budget after threshold tuning on held-out training traces.

## Evidence references

- Artifact root: `<local-path>/projects/learned-reuse-prediction-for-kv-cache-offload-admission-4d483f575e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
