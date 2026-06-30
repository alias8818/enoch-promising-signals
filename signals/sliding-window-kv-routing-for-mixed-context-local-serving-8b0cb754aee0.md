# Sliding-Window KV Routing for Mixed-Context Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-window-kv-routing-for-mixed-context-local-serving-8b0cb754aee0`
Run ID: `sliding-window-kv-routing-for-mixed-context-local-serving-8b0cb754aee0-20260524T232302781418+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/cd361cc01529

## What looked useful

Across 12 seeds, the router reduced peak KV from 72,129 to 58,547 tokens versus full KV (18.8% lower) with adequacy 0.991. Under a 50,000-token budget it reduced over-budget proxy exposure from 0.334 to 0.063 (81.2% lower) but still exceeded budget; all-sliding fit memory but adequacy fell to 0.251.

## Boundaries and scale limits

Evidence is a CPU-only deterministic simulator with analytic latency and binary synthetic adequacy labels. It does not measure real transformer quality, GPU kernels, scheduler behavior, UMA memory, or production traces.

## Claim scope

Synthetic mixed-context serving traces show that routing sliding-window KV eviction only to window-tolerant long requests reduces peak KV tokens and over-budget exposure compared with full KV, while avoiding the large adequacy-proxy collapse caused by applying sliding windows to every request.

## Why it stopped

Proxy simulation supports the mechanism but is not direct model-serving validation and is insufficient for a paper.

## Recommended next action

Stop this run as no-paper proxy evidence; next run should implement the same policy comparison in a real local serving stack with a small model and measurable long-range correctness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Local-Serving Validation of Routed Sliding-Window KV
- Success threshold: Router reduces measured peak KV or memory pressure by at least 15% versus full KV, preserves at least 99% of long-range-sensitive correctness, and improves constrained-budget p95 latency or admission success without the correctness collapse of sliding-all.
- Stop condition: Stop if routed serving cannot preserve long-range correctness above 99%, if measured memory reduction is below 10%, or if implementation overhead erases constrained-budget latency/admission gains.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-kv-routing-for-mixed-context-local-serving-8b0cb754aee0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
