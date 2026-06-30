# CRouter: Calibrated Cascade Router for Single-GPU Local Serving

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `crouter-calibrated-cascade-router-for-single-gpu-local-serving-6c64662bd187`
Run ID: `crouter-calibrated-cascade-router-for-single-gpu-local-serving-6c64662bd187-20260628T230601917433+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f09155c847f9

## What looked useful

The final proxy found no viable cascade. The expert did not beat the router at full proxy scale, calibration did not improve final ECE, and the fastest nonzero calibrated cascade routed 0.67% of requests but was 112.3% slower than expert-only serving.

## Boundaries and scale limits

Synthetic classification only; no real LLMs, token generation, KV-cache pressure, production serving scheduler, or real request distribution were tested.

## Claim scope

Bounded synthetic single-GPU proxy: a temperature-calibrated small MLP router escalating to a larger MLP expert did not produce a viable nonzero-routing cascade on GB10.

## Why it stopped

Proxy/early falsification: under the bounded synthetic GB10 benchmark, nonzero cascade routing was slower than expert-only and the assumed large-over-small quality hierarchy was not stable.

## Recommended next action

Stop this run as a no-paper negative proxy; only revisit with a real local LLM serving benchmark that first proves the expert model has a stable quality advantage over the router.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CRouter Real Local-LLM Serving Probe
- Success threshold: At least one nonzero-routing calibrated cascade must stay within 1 percentage point or task-equivalent quality tolerance of expert-only while reducing median end-to-end latency or measured GPU work by at least 15%.
- Stop condition: Stop if the expert does not beat the router on the request metric, or if every nonzero-routing cascade is slower or more GPU-expensive than expert-only after scheduler-aware batching is enabled.

## Evidence references

- Artifact root: `<local-path>/projects/crouter-calibrated-cascade-router-for-single-gpu-local-serving-6c64662bd187`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
