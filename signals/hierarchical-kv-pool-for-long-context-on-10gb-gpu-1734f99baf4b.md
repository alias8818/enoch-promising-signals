# Hierarchical KV pool for long-context on 10GB GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-kv-pool-for-long-context-on-10gb-gpu-1734f99baf4b`
Run ID: `hierarchical-kv-pool-for-long-context-on-10gb-gpu-1734f99baf4b-20260601T014326762942+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e56b47024e72

## What looked useful

Hierarchical KV routing is potentially useful for sparse/high-salience retrieval workloads under GPU memory pressure, but naive pooling and small routed active sets are poor drop-in approximations for broad full-context attention.

## Boundaries and scale limits

This was a one-layer synthetic attention probe on GB10, not a full transformer serving run. It did not implement real KV offload, real text prompts, trained routing, multi-layer cache behavior, or quality metrics on a language model.

## Claim scope

On synthetic single-query GPU attention at up to 65,536 tokens, a routed hierarchical active KV set can reduce active KV footprint by over 95% and preserve a constructed high-salience old-token needle, but it does not preserve general random full-context attention output at small top-k.

## Why it stopped

Proxy mechanism evidence is mixed: active memory reduction is strong and needle retrieval is preserved, but random attention fidelity is low and full serving quality was not directly validated.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is an end-to-end small-transformer retrieval benchmark with actual KV offload/indexing under a fixed 10GB memory budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-transformer routed KV offload benchmark
- Success threshold: At least 4x active-KV memory reduction at equal context length, less than 5% absolute retrieval accuracy loss versus exact KV, and no throughput collapse worse than 2x on GB10.
- Stop condition: Stop if routed KV loses 5% or more absolute retrieval accuracy at every memory-saving setting, or if offload/routing overhead makes throughput more than 2x slower before achieving at least 4x active-KV reduction.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-kv-pool-for-long-context-on-10gb-gpu-1734f99baf4b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
