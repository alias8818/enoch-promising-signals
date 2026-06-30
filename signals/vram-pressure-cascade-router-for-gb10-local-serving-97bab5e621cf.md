# VRAM-Pressure Cascade Router for GB10 Local Serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `vram-pressure-cascade-router-for-gb10-local-serving-97bab5e621cf`
Run ID: `vram-pressure-cascade-router-for-gb10-local-serving-97bab5e621cf-20260613T122021974941+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e7fc61c5d25f

## What looked useful

GB10 unified-memory pressure can push greedy local-serving allocation into earlyoom SIGTERM territory, while a simple MemAvailable/CUDA-free cascade can preserve service by selecting smaller tiers under pressure.

## Boundaries and scale limits

Synthetic CUDA scratch/GEMM tiers only; no real LLM server, no real token generation, no concurrent request trace, no production KV-cache allocator, and no measured answer quality.

## Claim scope

On this GB10 host, a telemetry-based cascade router over synthetic CUDA serving tiers completed all requests across 0, 80, and 100 GiB resident CUDA pressure, while a greedy always-large policy was terminated by earlyoom entering the high-pressure phase.

## Why it stopped

No-paper useful signal from a bounded synthetic GB10 pressure test; direct serving evidence is still required before a paper claim.

## Recommended next action

Stop this worker run; next bounded action is a real local-serving reproduction with small/medium/large model tiers and concurrent token-generation traffic on GB10.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 real local-serving cascade under UMA pressure
- Success threshold: Pressure-aware routing completes at least 95% of requests without OOM/earlyoom at high pressure and retains at least 80% of greedy-low-pressure quality or task score with lower failure rate than greedy-largest.
- Stop condition: Stop if production-serving integration cannot expose reliable memory telemetry/routing hooks locally, or if pressure-aware routing has no lower failure rate than baselines in two repeated runs.

## Evidence references

- Artifact root: `<local-path>/projects/vram-pressure-cascade-router-for-gb10-local-serving-97bab5e621cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
