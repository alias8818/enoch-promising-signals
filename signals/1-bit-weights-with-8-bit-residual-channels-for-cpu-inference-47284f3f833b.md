# 1-bit weights with 8-bit residual channels for CPU inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `1-bit-weights-with-8-bit-residual-channels-for-cpu-inference-47284f3f833b`
Run ID: `1-bit-weights-with-8-bit-residual-channels-for-cpu-inference-47284f3f833b-20260608T175935331672+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a8aaff34ff66

## What looked useful

Small residual fractions preserved 3.9x-5.2x compression versus int8 but left relative output RMSE around 0.57. Increasing residual coverage to 50% still left 0.43 RMSE and only 1.58x int8 compression. Full residual coverage recovered int8-like RMSE but was larger than int8 and about 20x slower in this kernel.

## Boundaries and scale limits

No trained transformer weights, learned residual selection, downstream perplexity, end-to-end inference stack, multithread scaling, or hand-optimized AVX512 binary kernel were tested.

## Claim scope

Bounded synthetic CPU linear-layer probe: row-scaled 1-bit weights plus selected int8 residual input channels did not provide a favorable accuracy/latency/storage tradeoff versus dense int8 on deterministic Gaussian matrices up to 2048x2048 and batch sizes 1 and 8.

## Why it stopped

Proxy early falsification rather than full validation: the directly tested synthetic CPU layer economics were unfavorable wherever the format retained useful compression over int8.

## Recommended next action

Stop this run as a proxy early falsification; only revisit with trained transformer layers and an optimized CPU kernel that can meet explicit accuracy and latency thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Test 1-bit plus residual channels on trained transformer weight matrices with optimized CPU kernels
- Success threshold: At no more than 12.5% residual channels, median layer-output relative RMSE below 0.05 or negligible downstream perplexity degradation, at least 2x int8 weight compression, and binary-residual latency no worse than 1.25x dense int8.
- Stop condition: Stop if trained layers still exceed 0.15 relative RMSE at 12.5% residual channels or if the optimized kernel remains slower than 2x dense int8 while using at least 2x less storage.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-weights-with-8-bit-residual-channels-for-cpu-inference-47284f3f833b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
