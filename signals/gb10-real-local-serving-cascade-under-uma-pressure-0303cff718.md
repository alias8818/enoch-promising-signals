# GB10 real local-serving cascade under UMA pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gb10-real-local-serving-cascade-under-uma-pressure-0303cff718`
Run ID: `gb10-real-local-serving-cascade-under-uma-pressure-0303cff718-20260613T124650933728+0000`

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

- Parent run decision: VRAM-Pressure Cascade Router for GB10 Local Serving: enoch://control-plane/projects/vram-pressure-cascade-router-for-gb10-local-serving-97bab5e621cf/runs/vram-pressure-cascade-router-for-gb10-local-serving-97bab5e621cf-20260613T122021974941+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e7fc61c5d25f

## What looked useful

Severe UMA pressure down to about 10.2 GiB MemAvailable and 3.2 GiB CUDA-free did not change primary latency materially: 0.2797 s baseline versus 0.2801 s under 100 GiB pressure. A memory-threshold cascade routed to the 0.5B fallback at about 0.1290 s, but this speedup reflects smaller-model serving rather than recovery from primary degradation.

## Boundaries and scale limits

Small request count, short prompts, no concurrent multi-client load, 1.5B primary only, no quality scoring, and synthetic CUDA tensor pressure rather than an organic competing workload.

## Claim scope

On this GB10 host, two real llama-server instances using Qwen2.5 1.5B Q4_K_M primary and Qwen2.5 0.5B Q4_K_M fallback remained healthy under short 70 GiB and 100 GiB CUDA/UMA pressure windows; the smaller fallback was faster, but pressure did not measurably degrade the primary.

## Why it stopped

Controlled direct small-scale test did not show pressure-induced primary serving degradation, so the cascade mechanism is not supported beyond ordinary smaller-model latency routing.

## Recommended next action

Stop this run as no-paper useful signal; if deepening, run a larger-primary concurrent-serving test with explicit p95/error/quality thresholds near the earlyoom margin.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Larger-primary concurrent local-serving cascade near GB10 earlyoom margin
- Success threshold: Under pressure, primary-only p95 latency increases by at least 25% or error rate exceeds 1%, and cascade reduces p95 latency or error rate by at least 15% while keeping quality within a predeclared acceptable delta.
- Stop condition: Stop if the larger primary shows less than 10% p95 latency degradation and zero serving errors under near-margin pressure, or if the pressure setup cannot stay above earlyoom safety margin while running both servers.

## Evidence references

- Artifact root: `<local-path>/projects/gb10-real-local-serving-cascade-under-uma-pressure-0303cff718`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
