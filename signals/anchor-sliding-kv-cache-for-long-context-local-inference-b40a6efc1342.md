# Anchor+Sliding KV Cache for Long-Context Local Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-sliding-kv-cache-for-long-context-local-inference-b40a6efc1342`
Run ID: `anchor-sliding-kv-cache-for-long-context-local-inference-b40a6efc1342-20260619T131920609937+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d2902e151206

## What looked useful

Anchor+sliding is useful for workloads whose old-token dependency is concentrated in stable prefix/system/prompt anchors plus recent dialogue. It is not a general replacement for full KV cache on arbitrary middle-document retrieval tasks.

## Boundaries and scale limits

Not a full LLM inference benchmark; no transformer integration, generation-quality evaluation, batching, paged-cache overhead measurement, or public long-context benchmark was tested. Middle-context retrieval outside retained anchors/window fails by construction.

## Claim scope

Synthetic single-step CUDA attention retrieval shows that an anchor+sliding KV policy preserves prefix-anchor and recent-token access while using 7.8% to 31.25% of full-cache tokens in the tested 65k and 8k configurations.

## Why it stopped

Synthetic evidence supports the bounded mechanism but also directly shows the failure mode for discarded middle context; this is not full validation or paper-ready evidence.

## Recommended next action

Stop this run as no-paper useful signal; next direct test should integrate the policy into a small transformer inference loop and measure task accuracy plus tokens/second against full and sliding baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer inference benchmark for anchor+sliding KV cache
- Success threshold: Anchor+sliding must recover at least 90% of full-cache prefix-instruction accuracy while using no more than 1.25x sliding-only KV tokens and must explicitly report middle-needle degradation.
- Stop condition: Stop if actual transformer integration shows prefix-instruction accuracy is not materially better than sliding-only, or if implementation overhead erases the memory/latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-sliding-kv-cache-for-long-context-local-inference-b40a6efc1342`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
