# Prefix-KV Shared Router for Local Model Cascades

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prefix-kv-shared-router-for-local-model-cascades-49d59582a1d9`
Run ID: `prefix-kv-shared-router-for-local-model-cascades-49d59582a1d9-20260521T232359679517+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4f687c69d27f

## What looked useful

The mechanism is useful only under a strict compatible-KV cascade design. Router lookup overhead is negligible in the proxy at about 0.27 to 0.28 microseconds per request, but broad heterogeneous local-model cascades cannot share KV directly and therefore get essentially zero incremental benefit beyond per-model prefix caching.

## Boundaries and scale limits

Synthetic CPU simulation only; no real transformer inference, no GPU serving benchmark, no generation-quality validation, no eviction policy, and analytical all-prefix KV retention estimates range from about 701,175 MiB for compatible shared caches to multiple TiB for per-model caches.

## Claim scope

In a 50,000-request synthetic local-cascade simulation, a shared prefix-KV router provides no meaningful incremental savings over ordinary per-model prefix caching for heterogeneous cascades, but provides 71.14% to 77.56% modeled prefill-cost reduction versus per-model caching when cross-model KV compatibility is assumed.

## Why it stopped

Closed as a no-paper useful signal because the current evidence is a proxy/cost-model result that falsifies broad heterogeneous sharing and only supports a constrained compatible-KV follow-up.

## Recommended next action

Run a bounded real-model serving benchmark with two deliberately KV-compatible cascade stages plus an eviction budget; stop if correctness diverges or if memory-bounded latency gain is below 15% versus per-model prefix caching.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model compatible-KV cascade benchmark with bounded eviction
- Success threshold: At least 15% time-to-first-token or prefill-latency reduction versus per-model prefix caching under a fixed memory budget, with no material generation-quality regression on shared-prefix requests.
- Stop condition: Stop if cross-model KV reuse is not semantically valid for the chosen models, if eviction erases the latency gain below 15%, or if cache memory exceeds the fixed local budget.

## Evidence references

- Artifact root: `<local-path>/projects/prefix-kv-shared-router-for-local-model-cascades-49d59582a1d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
