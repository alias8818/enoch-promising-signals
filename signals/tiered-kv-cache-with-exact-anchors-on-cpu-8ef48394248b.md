# Tiered KV Cache With Exact Anchors on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-kv-cache-with-exact-anchors-on-cpu-8ef48394248b`
Run ID: `tiered-kv-cache-with-exact-anchors-on-cpu-8ef48394248b-20260523T024154483356+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b356e38b90fa

## What looked useful

Periodic exact anchors are a coverage mechanism, not a general old-token retrieval solution. In the medium CPU benchmark, tiered cache used 8.08% of full entries and ran 16.4-17.7x faster, matched smooth attention with relative L2 about 0.0175, recovered anchored needles with relative L2 about 0.151, but failed unanchored needles with relative L2 about 1.000.

## Boundaries and scale limits

Evidence is synthetic and single-layer/proxy only; it does not measure LLM perplexity, generation quality, multi-layer error accumulation, fused inference kernels, quantized KV storage, or end-to-end CPU serving throughput.

## Claim scope

Synthetic CPU one-token attention benchmarks at 8192-token context show that local-window plus block-summary plus periodic exact-anchor KV caches can provide large attention-kernel speedups and preserve smooth or explicitly anchored old-token cases, but they fail arbitrary old-token retrieval when the target is not covered by an anchor.

## Why it stopped

Moderate synthetic evidence supports the speed and covered-anchor mechanism but falsifies periodic exact anchors as a general retrieval-preserving tiered KV cache; this is proxy evidence, not full LLM validation.

## Recommended next action

Stop this periodic-anchor variant as no-paper evidence; the concrete next bounded test is an importance-selected or query-adaptive exact-anchor cache at the same entry budget on GPT-2-small-class CPU decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Importance-Selected Exact Anchors for CPU Tiered KV Cache
- Success threshold: At equal represented-entry budget, importance-selected or adaptive anchors reduce old-token retrieval/logit error by at least 50% versus periodic anchors while keeping at least 10x attention-kernel speedup or a measured end-to-end CPU throughput gain.
- Stop condition: Stop if non-periodic anchor selection cannot beat periodic anchors on unanchored retrieval at the same budget, or if end-to-end CPU overhead removes the speed advantage.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-cache-with-exact-anchors-on-cpu-8ef48394248b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
